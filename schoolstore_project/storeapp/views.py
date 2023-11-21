from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import orders

def home(request):

    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('new')

        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['confirmpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"wrong password")
            return redirect('register')

        return redirect('/')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')



def new(request):

    return render(request,'new.html')

def order(request):
    if request.method == "POST":
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        sorders =orders(name=name,dob=dob,age=age,gender=gender,phone=phone,email=email,address=address,department=department,course=course,purpose=purpose)
        if sorders.save():
            messages.info(request, "order is placed")
            return redirect('new')
        else:
            messages.info(request, "order is not placed")
            return redirect('new')

        return redirect('new')

    return render(request,'order.html')