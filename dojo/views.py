# dojo/views.py
import os
from django.conf import settings
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404,redirect, render
from django.views.generic import DetailView
from .forms import PostForm
from .models import Post



post_detail = DetailView.as_view(model=Post)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR'] # ip를 받아오기
            post.save()
            return redirect('/dojo/') #namespace:name <- url쓸때
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html',{
        'form':form,
    })

def post_edit(request,id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR'] # ip를 받아오기
            post.save()
            return redirect('/dojo/') #namespace:name <- url쓸때
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html',{
        'form':form,
    })

def mysum(request, numbers):
    # request: HttpResponse
    # numbers = "1/2/123/123/132/1215/123123"
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))

    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))

def post_list1(request):
    # 'FBV: 직접 문자열로 HTML형식 응답하기'
    name = '공유'
    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>여러분의 파이썬&장고 페이스메이커가 되겠습니다.</p>
    '''.format(name=name))

def post_list2(request):
    # 'FBV: 템플릿을 통해 HTML형식 응답하기'
    name = '공유'
    response = render(request, 'dojo/post_list.html', {'name': name})
    return response


def post_list3(request):
    # 'FBV: JSON 형식 응답하기'
    return JsonResponse({
    'message': '안녕, 파이썬&장고',
    'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params={'ensure_ascii': False})

def excel_download(request):
    # 'FBV: 엑셀 다운로드 응답하기'
    # filepath = '/Users/Wook/Desktop/test.xls' <- 내 바탕화면 경로
    filepath = os.path.join(settings.BASE_DIR, 'test.xls')
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) <- 경로
    # <- settings.py의 BASE_DIR 경로 즉 C:\Users\Wook\dev\askdjango에 있는 test.xis 경로
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        # 필요한 응답헤더 세팅
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
