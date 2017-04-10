from django.contrib import admin
from django.utils.safestring import mark_safe #글자 강조
from .models import Post, Comment, Tag

# admin.site.register(Post, PostAdmin)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','content_size','status','created_at', 'updated_at']

    actions = ['make_published','make_draft']

    def content_size(self, post):
        return mark_safe('<strong>{}<strong>글자'.format(len(post.content)))

    def make_draft(self,request,qureyset): #모든 액션은 인자:리퀘스트,쿼리셋을 받는다
        updated_count = qureyset.update(status='d') # 쿼리셋 업데이트 함수
        self.message_user(request, '{}건의 포스팅을 Draft상태로 변경'.format(updated_count))
    make_draft.short_description = "지정 포스팅을 Draft상태로 변경"

    content_size.short_description = '글자수' #content_size의 이름 바꾸기

    def make_published(self,request,qureyset): #모든 액션은 인자:리퀘스트,쿼리셋을 받는다
        updated_count = qureyset.update(status='p') # 쿼리셋 업데이트 함수
        self.message_user(request, '{}건의 포스팅을 Published상태로 변경'.format(updated_count))
        #장고 메세지 프레임워크를 쓴것
    make_published.short_description = "지정 포스팅을 Published상태로 변경" #make_published의 이름 바꾸기

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
