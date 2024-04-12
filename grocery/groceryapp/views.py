from django.shortcuts import render
from .models import registertable

# Create your views here.
def index(request):
    return render (request,"index.html")
def shop(request):
    return render (request,"shop.html")
def vegetable(request):
    return render(request,"vegetable.html")
def navbar(request):
    return render(request,"navbar.html")
def footer(request):
    return render(request,"footer.html")
def toy(request):
    return render(request,"toy.html")
def indexregister(request):
    a=request.POST['firstname']
    b=request.POST['lastname']
    c=request.POST['phoneno']
    d=request.POST['dob']
    e=request.POST['email']
    f=request.POST['password']
    ins=registertable(firstname=a,lastname=b,phoneno=c,dob=d,email=e,password=f)
    ins.save()
    return render(request,"index.html")