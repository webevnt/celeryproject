from django.urls import path
from notification import views
app_name = 'notification'

urlpatterns = [
	path('',views.user_notification,name='user_notification'),
    path('api/users/register', views.RegistrationAPIView.as_view(), name="register"),
]