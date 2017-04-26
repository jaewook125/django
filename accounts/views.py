#accounts/views.py
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL) #회원가입에 성공하면 LOGIN 페이지로 이동 
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html',{
        'form': form
    })

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
#특정 뷰가 호출될때 로그아웃 상황이 아닌
#로그인상황에서만 호출이 되도록 강제시킬려면 장식자를 사용 @login_required
