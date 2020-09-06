from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Meddata
import sweetify


def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=="POST":
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'register.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                #sweetify.success(request, '', timer=3000)
                sweetify.success(request, 'Registration Successful', persistent='Continue to login')
                return redirect('login')
        else:
            return render(request,'register.html',{'error':'password does not matched'})
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        else:
            return render(request, 'register.html',{'error':'Please fill the details correctly'})
    else:
        return render(request, 'register.html')

def addmed(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            m1=request.POST['medname']
            m2=request.POST['duration']
            m3=request.POST['start_time']
            m4=request.POST['ts']
            m5=request.POST['cdd']
            m6=request.POST['times']

            new=Meddata(Med_Name=m1,Med_Dur=m2,Mrg_med=m3,category=m4,course=m5,no_of_tabs=m6,user=request.user)
            new.save()
            return redirect('medicinelist')
        else:
            return render(request,'addmedicine.html')
    else:
        return render(request,'register.html',{'error':'Please Log In'})

def medlist(request):
    if request.user.is_authenticated:
        med_user=request.user
        med=Meddata.objects.filter(user=med_user)
        return render(request,'medicinelist.html',{'med':med})
    else:
        return render(request,'register.html',{'error':'Please Log In'})

def profile(request):
    if request.user.is_authenticated:
        #sweetify.sweetalert(request, 'Successfully Registered', text='Really... if you have the chance - watch it!', persistent='I agree!')
        #sweetify.info(request, 'Message sent', button='Ok', timer=3000)
        sweetify.warning(request, 'Westworld is awesome', text='Really... if you have the chance - watch it!', persistent='I agree!')
        return render(request,'profile.html',{'profile':profile})
    else:
        return render(request,'register.html',{'error':'Please Log In'})

def logout(request):
        auth.logout(request)
        return redirect(home)