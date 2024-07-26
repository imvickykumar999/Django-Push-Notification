# `Generate FCM Token`

![image](https://github.com/user-attachments/assets/d35a4462-5813-45a1-ad77-6926e733da75)
![image](https://github.com/user-attachments/assets/10a54d8e-7540-473b-b124-0a318e3da9fa)

To obtain the service account JSON file required for `service_account.Credentials.from_service_account_file`, you need to create a service account in your Firebase project and download the key. Here are the steps to do so:

![image](https://github.com/user-attachments/assets/94caac48-3947-42ef-9696-80d5a0974201)

### Steps to Create a Service Account and Download the JSON Key

1. **Go to the Firebase Console**:
   - Open the [Firebase Console](https://console.firebase.google.com/u/0/project/fir-push-notification-85613/settings/serviceaccounts/adminsdk).
   - Select your project (e.g., `fir-push-notification-85613`).

2. **Navigate to Project Settings**:
   - Click on the gear icon next to "Project Overview" and select "Project settings".

3. **Service Accounts**:
   - In the settings page, click on the "Service accounts" tab.
   - Click on the "Generate new private key" button.
   - A JSON file will be automatically downloaded to your computer. This is your service account key.

4. **Store the JSON Key Securely**:
   - Save this JSON file in a secure location on your server or development machine. The file contains sensitive information that should not be exposed publicly.
