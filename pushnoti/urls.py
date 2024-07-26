from django.contrib import admin
from django.urls import path
from home.views import index, send, showFirebaseJS
from notification.views import push, send_notification

urlpatterns = [
    path('', index, name='index'),
    path('send/', send, name='send'),
    path('firebase-messaging-sw.js', showFirebaseJS, name='show_firebase_js'),
    path('admin/', admin.site.urls),

    path('push/', push, name='push'),
    path('send_notification/', send_notification, name='send_notification'),
]
