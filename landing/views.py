from django.shortcuts import render, redirect
from django.utils.translation import activate
from django.utils.translation import get_language

def landing_page(request):
    show_language_modal = not request.session.get('language_selected', False)
    return render(request, 'landing/landing.html',{
        'show_language_modal': show_language_modal,
    })
def select_language(request):
    lang = request.GET.get('lang')
    if lang in ['en', 'hi']:
        request.session['django_language'] = lang
        activate(lang)
    return redirect('core:enter_mobile')

def set_language(request, lang_code):
    from django.utils import translation
    request.session[translation.LANGUAGE_SESSION_KEY] = lang_code
    request.session['language_selected'] = True  # 🛑 Add this line
    translation.activate(lang_code)
    return JsonResponse({'status': 'ok'})
