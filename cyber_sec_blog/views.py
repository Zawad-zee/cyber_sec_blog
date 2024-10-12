# cyber_sec_blog/views.py viewing the landing page

from django.http import HttpResponse


def index(request):
    return HttpResponse('Cyber Sec world!')