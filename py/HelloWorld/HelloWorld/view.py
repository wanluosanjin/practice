from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime
def hello(request):
    template = get_template('index.html')
    now=datetime.now
    userlist = []
    html=template.render(locals())
    return HttpResponse(html)
def text(request):
    template = get_template('text.html')
    now=datetime.now
    userlist = []
    html=template.render(locals())
    return HttpResponse(html)
