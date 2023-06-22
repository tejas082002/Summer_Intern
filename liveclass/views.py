from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import Student_records
from .forms import SignUpForm
from django.contrib.auth.models import Group
from django.contrib import messages




# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def login_user(request):
    if request.method == 'POST':
        Fname = request.POST.get('fname')
        password = request.POST.get('password')
        user = authenticate(request, username=Fname, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('login')
    return render(request, 'login.html')


def create_room(request):
    group=request.user.groups.all()[0].name
    return render(request, 'create_room.html',{'group':group})


def join_room(request):
    if request.user.is_authenticated:
      return render(request,'join_room.html')
    else:
        return render(request,'error.html')

def Stud_record(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        Locality=request.POST.get('Locality')
        standard=request.POST.get('standard')
        state=request.POST.get('State')
        Zip=request.POST.get('Zip')
        country=request.POST.get('Country')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        
        
        stud=Student_records(Fname=fname,Lname=lname,email=email,address=Locality,standard=standard,state=state,
                         postalpcode=Zip,country=country,DOB=dob,gender=gender,phone=phone
                         )
        stud.save()
        return redirect('home')
    return render(request, 'stud_details.html')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            person=form.save()
            group=Group.objects.get(name='candidate')
            person.groups.add(group)
			# Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('stud_record')
    else:
        form = SignUpForm()
        return render(request, 'registration.html', {'form':form})
    return render(request, 'registration.html', {'form':form})

def room(request):
    return render(request, 'room.html')

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')


def join_candidate(request):
    pass