from django import forms # 폼 정의 모듈

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word') # 검색 키워드