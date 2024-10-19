from django.http import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def say_hello(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def main(request):
    template = loader.get_template("CUNAT.HTML")
    return HttpResponse(template.render())


def main1(request):
    template = loader.get_template("htnl.html")
    return HttpResponse(template.render())
