import qrcode
from django.shortcuts import render, get_object_or_404
from .models import FirebaseConfig
from django.http import HttpResponse
import requests
import json
from google.oauth2 import service_account
import google.auth.transport.requests
from io import BytesIO
import base64

def get_access_token():
    credentials = service_account.Credentials.from_service_account_file(
        'serviceAccountKey.json',
        scopes=['https://www.googleapis.com/auth/firebase.messaging']
    )
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)
    return credentials.token

def send_notification(registration_ids, message_title, message_desc):
    fcm_api = get_access_token()  # Get the OAuth 2.0 access token
    url = "https://fcm.googleapis.com/v1/projects/fir-push-notification-85613/messages:send"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": 'Bearer ' + fcm_api
    }

    payload = {
        "message": {
            "token": registration_ids,
            "notification": {
                "body": message_desc,
                "title": message_title,
            }
        }
    }

    result = requests.post(url, data=json.dumps(payload), headers=headers)
    data = result.json()

    print(data)
    return data

def index(request):
    firebase_config = get_object_or_404(FirebaseConfig, id=1)
    return render(request, 'index.html', {'firebase_config': firebase_config})

def send(request):
    if request.method == 'POST':
        registration_id = request.POST.get('registration_id')
        message_title = request.POST.get('title')
        message_desc = request.POST.get('body')
        
        result = send_notification(registration_id, message_title, message_desc)
        
        # Generate QR code
        base_url = "https://djangofcm.pythonanywhere.com/push/?send="
        full_url = base_url + registration_id
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=2,
        )
        qr.add_data(full_url)
        qr.make(fit=True)
        
        img = qr.make_image(fill='black', back_color='white')
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        response_string = json.dumps(result)
        return render(request, 'result.html', {
            'registration_id': registration_id,
            'message_title': message_title,
            'message_desc': message_desc,
            'response': response_string,
            'qr_code': img_str
        })
    else:
        return HttpResponse("Invalid request method", status=405)

def showFirebaseJS(request):
    firebase_config = get_object_or_404(FirebaseConfig, id=1)

    data = ('importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");'
            'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); '
            'var firebaseConfig = {'
            f'        apiKey: "{firebase_config.api_key}",'
            f'        authDomain: "{firebase_config.auth_domain}",'
            f'        projectId: "{firebase_config.project_id}",'
            f'        storageBucket: "{firebase_config.storage_bucket}",'
            f'        messagingSenderId: "{firebase_config.messaging_sender_id}",'
            f'        appId: "{firebase_config.app_id}",'
            f'        measurementId: "{firebase_config.measurement_id}"'
            '};'
            'firebase.initializeApp(firebaseConfig);'
            'const messaging=firebase.messaging();'
            'messaging.setBackgroundMessageHandler(function (payload) {'
            '    console.log(payload);'
            '    const notification=JSON.parse(payload);'
            '    const notificationOption={'
            '        body:notification.body,'
            '        icon:notification.icon'
            '    };'
            '    return self.registration.showNotification(payload.notification.title,notificationOption);'
            '});')

    return HttpResponse(data, content_type="text/javascript")
