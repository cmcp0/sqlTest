from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):

    if "pogU" not in request.session:
        # request.session['pogU'] = "asdf"
        return HttpResponse(":(")
    else:
        return HttpResponse(request.session['pogU'] + " :D")

def login(request):
    if "pogU" not in request.session:
        # request.session['pogU'] = "asdf"
        return render_to_response("Login.html", )
    else:
        return HttpResponse(request.session['pogU'] + " :D")
