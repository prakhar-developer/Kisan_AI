from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('set-language/<str:lang_code>/', views.set_language, name='set_language'),
    path('enter-mobile/', views.enter_mobile, name='enter_mobile'),  # Example]
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),

]

