# cyber_sec_blog/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse('Cyber Sec world!')