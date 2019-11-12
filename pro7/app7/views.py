from django.shortcuts import render
from django.core.mail import send_mail
from pro7 import settings as se

# Create your views here.
def show(request):
    return render(request,"login.html")


def showIndex(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    message=request.POST.get("message")
    if username == "venky" and password =="venky" :
        sudject="check mail"
        message=" HELLO U HAVE BE HACKED BRO "
        send_mail(sudject,message,se.EMAIL_HOST_USER,["ravimaram012@gmail.com","saikumar8877@gmail.com"])
        return render(request,"welcome.html")
    else:
        return render(request,"login.html",{"message":"invalid user"})


def logout(request):
    return render(request,"login.html")