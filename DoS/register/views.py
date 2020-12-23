from django.shortcuts import render,redirect
from .forms import RegisterForm
from .models import Bulk,Individual,Industrial,Commercial,User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout
# Create your views here.



def login(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)

            if user.is_individual:
                return redirect('bulk_dashboard')
            elif user.is_bulk:
                return redirect('bulk_dashboard')
            elif user.is_commercial:
                return redirect('bulk_dashboard')
            elif user.is_industrial:
                return redirect('bulk_dashboard')     
        else:
            error = "Invalid credentials. Try again."
    return render(request , 'register/login.html',{'error':error})

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request,user_type):
    if request.method == "POST":
        form = RegisterForm(request.POST)
       
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data.get("username")    
            address = form.cleaned_data.get("address")
            phone = form.cleaned_data.get("phone")
            email = form.cleaned_data.get("email")
         
            user = User.objects.get(username = username)
            if user_type == 'Bulk':
                user.is_bulk = True
                user.is_individual  = False
                user.save()
                
                bulk_user = Bulk.objects.create(
                    user = user,
                    address = address,
                    phone_number = phone,
                    email = email
                )
                
                bulk_user.save()
            
            elif user_type == 'Industry':
                user.is_industrial = True
                user.is_individual  = False
                user.save()

                industry_user = Industrial.objects.create(
                    user = user,
                    address = address,
                    phone_number = phone,
                    email = email
                )
                industry_user.save()

            elif user_type == 'Commercial':
                user.is_commercial = True
                user.is_individual  = False
                user.save()
                
                commercial_user = Commercial.objects.create(
                    user = user,
                    address = address,
                    phone_number = phone,
                    email = email
                )  
                commercial_user.save()

            elif user_type == 'Individual':
                individual_user = Individual.objects.create(
                    user = user,
                    address = address,
                    phone_number = phone,
                    email = email
                )
                
                individual_user.save()

            return redirect('login')
        
    else:
        form = RegisterForm()
    context = {'form' : form ,"user_type" : user_type }
    return render(request,'register/register.html', context)
