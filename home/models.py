from django.db import models

class FirebaseConfig(models.Model):
    api_key = models.CharField(max_length=255)
    auth_domain = models.CharField(max_length=255)
    project_id = models.CharField(max_length=255)
    storage_bucket = models.CharField(max_length=255)
    messaging_sender_id = models.CharField(max_length=255)
    app_id = models.CharField(max_length=255)
    measurement_id = models.CharField(max_length=255)
    vapid_key = models.CharField(max_length=255)

    def __str__(self):
        return self.project_id


# python manage.py shell

'''
from home.models import FirebaseConfig

config = FirebaseConfig.objects.create(
    api_key="AIzaSyDEffV60DqptX5isXVzlhYp1JMKf7t2wlA",
    auth_domain="fir-push-notification-85613.firebaseapp.com",
    project_id="fir-push-notification-85613",
    storage_bucket="fir-push-notification-85613.appspot.com",
    messaging_sender_id="279392742552",
    app_id="1:279392742552:web:df183eb0e8c256fb7174ed",
    measurement_id="G-TZVKHMQSRE",
    vapid_key="BI_V_6JdbJ6jpCBSLqZHyhA6r96BG5qa3RbvNz5mq20MYSkFmzt5rDTtrZ6Z6PoaOrYp3REDVpIlu5uzNIxCqEk"
)
'''
