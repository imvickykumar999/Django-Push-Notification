from django.shortcuts import render
from django.http import JsonResponse
from google.oauth2 import service_account
import google.auth.transport.requests
import requests
import json

def get_access_token():
    credentials = service_account.Credentials.from_service_account_file(
        'serviceAccountKey.json',
        scopes=['https://www.googleapis.com/auth/firebase.messaging']
    )
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)
    return credentials.token

def send_push_notification(token, title, body, image=None):
    access_token = get_access_token()
    url = "https://fcm.googleapis.com/v1/projects/fir-push-notification-85613/messages:send"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    payload = {
        "message": {
            "token": token,
            "notification": {
                "title": title,
                "body": body,
            }
        }
    }

    if image:
        payload["message"]["notification"]["image"] = image

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

def push(request):
    fcm_token = request.GET.get('send', '')
    return render(request, 'push.html', {'fcm_token': fcm_token,})

def send_notification(request):
    if request.method == 'POST':
        fcm_token = request.POST.get('fcm_token')
        title = request.POST.get('title')
        body = request.POST.get('body')
        image = request.POST.get('image')

        response = send_push_notification(fcm_token, title, body, image)
        return render(request, 'sent.html', {
            'registration_id': fcm_token,
            'message_title': title,
            'message_desc': body,
            'image': image,
            'response': response
        })
    return JsonResponse({'error': 'Invalid request method'}, status=400)
