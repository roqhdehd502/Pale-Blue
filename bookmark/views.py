from django.shortcuts import render

from django.views.generic import ListView, DetailView # 클래스형 제네릭 뷰를 사용하기 위해 ListView, DetailView 클래스 임포트
from bookmark.models import Bookmark # 테이블 조회를 위해 모델 클래스를 임포트

# Create your views here.
class BookmarkLV(ListView): # Bookmark 테이블의 레코드 리스트를 보여주기 위한 뷰
    model = Bookmark

class BookmarkDV(DetailView): # Bookmark 테이블의 특정 레코드에 대한 상세 정보를 보여주기 위한 뷰
    model = Bookmark