from django.http import HttpResponse

def index(request):
    return HttpResponse('<H2> Simple ..... :) </H2>')