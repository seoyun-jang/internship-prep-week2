from django.contrib import admin
from .models import Author, Book
# Register your models here.

admin.site.register(Author)
admin.site.register(Book)

"""
python manage.py makemigrations # models.py에서 적용한 변경사항이나 추가된 혹은 삭제된 사항들을 감지하여 파일로 생성
python manage.py migrate # 적용되지 않은 migrations들을(설정값들을) 적용
python manage.py createsuperuser # admin 계정 생성
python manage.py runserver # 코드를 적용하여 서버 제공
"""

# http://127.0.0.1:8000/admin