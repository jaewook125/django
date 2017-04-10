#blog/models
import re
from django.db import models
from django.forms import ValidationError
from django.conf import settings
from django.core.urlresolvers import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

def lnglat_validator(value):
     if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
         raise ValidationError('Invalid LngLat Type') # 발생을 시킨다 raise

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdraw'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100, verbose_name='제목',
        help_text='포스팅 제목을 입력해주세요. 최대 100자 내외로.') # 길이 제한이 있는 문자
    content = models.TextField(verbose_name='내용')             # 길이 제한이 없는 문자열

    photo = ProcessedImageField(blank=True, upload_to='blog/post/%Y/%m/%d',
            processors=[Thumbnail(300, 300)],
            format='JPEG',
            options={'quality': 50})


    tags = models.CharField(max_length=100, blank=True)        # blank <- 칸이 비여있어도 동작ok
    lnglat = models.CharField(max_length=50, blank=True,
        validators=[lnglat_validator],
        help_text='위도/경도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    #문자열로 클래스 지정해주면 현재 같은 앱 안에있는 태그 릴레이션과 연결
    #다른 앱과 연결하려면 'dojo.Tag'처럼 함
    created_at = models.DateTimeField(auto_now_add=True) #
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.id])

class Comment(models.Model):
        post = models.ForeignKey(Post)
        # 이 코멘트는 Post 모델에 대해서 1:N의 관계를 가진다
        # post_id 라는 필드가 생김 외래키의 영향
        author = models.CharField(max_length=20)
        message = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name #태그의 이름이 표시
