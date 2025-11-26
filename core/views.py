from django.utils import translation
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from firebase_admin import auth as firebase_auth
from .models import CustomUser
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import CustomUser


def set_language(request, lang_code):
    if lang_code in ['en', 'hi']:
        request.session[translation.LANGUAGE_SESSION_KEY] = lang_code
    return redirect(request.META.get('HTTP_REFERER', '/'))

def enter_mobile(request):
    return render(request, 'core/enter_mobile.html')  


@csrf_exempt
def verify_otp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        uid = data.get('uid')
        phone = data.get('phone')

        try:
            # 🔐 Verify UID from Firebase (security)
            decoded_token = firebase_auth.verify_id_token(uid)
            phone_number = decoded_token.get('phone_number')

            if not phone_number or phone_number != phone:
                return JsonResponse({'error': 'Invalid Firebase token'}, status=400)

            mobile = phone[-10:]  # Trim country code +91
            user, created = CustomUser.objects.get_or_create(mobile=mobile)

            login(request, user)

            if user.name and user.role:
                return JsonResponse({'redirect_url': f'/{user.role}/dashboard/'})
            else:
                return JsonResponse({'redirect_url': '/complete-profile/'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)



@login_required
def complete_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        role = request.POST.get('role')

        user = request.user
        user.name = name
        user.role = role
        user.save()

        return redirect(f'/{role}/dashboard/')

    return render(request, 'core/complete_profile.html')

