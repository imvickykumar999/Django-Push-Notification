import json
import requests
from google.oauth2 import service_account
import google.auth.transport.requests

def get_access_token(secret):
    credentials = service_account.Credentials.from_service_account_file(
    	secret, scopes=['https://www.googleapis.com/auth/firebase.messaging']
    )
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)
    return credentials.token


def send_push_notification(token, title, body, image_url, ProjectID, secret):
    access_token = get_access_token(secret)
    url = f"https://fcm.googleapis.com/v1/projects/{ProjectID}/messages:send"
    
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
                "image": image_url
            },
            "android": {
                "notification": {
                    "sound": "default"
                }
            },
            "apns": {
                "payload": {
                    "aps": {
                        "sound": "default"
                    }
                }
            }
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

if __name__ == "__main__":
    fcm_token = 'cnrKLalKM68kqantC3MC4V:APA91bHlaQ9qdrcQc-RPc7s5OSxn7HB9w00-ZUJ6Ltb4juc9epOzneXSxyBrVZbcSYE_ugW4POj05PL5_uRi3aDyPQFyJ2bgHaRWPnb-7IzQlv5eqIYrdbg6KsU6xnDCc9RO5sr_7_62'
    
    ProjectID = 'fir-push-notification-85613'
    secret = 'serviceAccountKey.json'
    
    title = 'Hello'
    body = 'World'
    image_url = 'https://avatars.githubusercontent.com/u/67197854'
    
    response = send_push_notification(fcm_token, title, body, image_url, ProjectID, secret)
    print('Response:', response)
