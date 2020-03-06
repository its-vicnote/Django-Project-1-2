from django.shortcuts import render, HttpResponse 
from time import strftime, gmtime, localtime

def index(request):
    context = {
        "date": strftime("%B %y, %Y", gmtime()),
        "time": strftime("%I:%M %p", localtime())
    }
    return render(request, "index.html", context)

def vic(request):
    return HttpResponse("Hello Vic Wagwan!")
def vic2(request):
    return HttpResponse('Dem man helped out with this one still. I do not feel like i am making progress sometimes')
# Create your views here.


