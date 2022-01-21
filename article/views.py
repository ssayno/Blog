from django.shortcuts import render, HttpResponse


# Create your views here.
def articles_list(request):
    print("查询所有文章")
    pass


def articles_author(request, author_id):
    print("查询指定作者的文章")
    pass


def articles_liked(request, author_id):
    print("查询指定作者的指定文章")
    pass


def articles_collected(request, author_id):
    print("查询指定作者的收藏")
    pass


def articles_year(request, year):
    print("指定年份")
    pass


def articles_month(request, month):
    print("指定月份")
    pass


def articles_detail(request, article_id):
    print("article_id")
    pass
