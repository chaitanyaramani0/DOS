from django.shortcuts import render,redirect
from register.models import Bulk,Industrial,Individual,Commercial,PickUp,User
from register.forms import PickUpForm,PickUpedForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Sum
# Create your views here.



@login_required(login_url='login')
def pickup(request):
  
    user = request.user
    
    if user.is_authenticated:
        if request.method == 'POST':
            pickup_form = PickUpForm(request.POST)
            if pickup_form.is_valid():
                instance =  pickup_form.save(commit=False)
                instance.user =  request.user
                instance.save()
                return redirect('bulk_dashboard')
        else:
            pickup_form = PickUpForm()
    return render(request,'dashboard/pickup.html',{'form':pickup_form})



@login_required(login_url='login')
def bulk_dashboard(request):
    print("request user",request.user)
    user = User.objects.filter(username=request.user).first()
    data =  user.pickup_set.all()
    category_weight  =  user.pickup_set.values( 
        'bin_type'
    ).annotate(
        total_weight = Sum('weight')
    )
    is_pickedup = user.pickup_set.filter(is_pickedup = "yes").values('bin_type').annotate(total_count=Count('is_pickedup'))
    pickup_done  = user.pickup_set.filter(is_pickedup = "yes")
    print(is_pickedup)
    print(category_weight)
    print(data)
    contex = {
            'data' :data,
            'category_weight':category_weight,
            'total_pickup' : is_pickedup,
            'pickup_done':pickup_done
            }
    return render(request,'dashboard/bulk_dashboard.html',contex)


def dos_pickup(request,id):
    record =  get_object_or_404(PickUp,pk=id)
    if request.method =='POST':
        form  = PickUpedForm(request.POST,instance= record)
        if form.is_valid():
            form.save()
            return redirect('dos_dashboard')                                                            
    else:
        form = PickUpedForm(instance=record)
    return render(request,'dashboard/dos_pickup.html',{'form':form})
   

def dos_dashboard(request):
    data = PickUp.objects.all()
    # bulk = PickUp.objects.filter(user__is_bulk = True)
    # individual = PickUp.objects.filter(user__is_individual = True)
    # industrial = PickUp.objects.filter(user__is_industrial = True)
    # commercial = PickUp.objects.filter(user__is_commercial = True)
    
    total_weight =  PickUp.objects.aggregate(Sum('weight'))
    contex = {
        'data' : data,
        # 'total_weight' : total_weight,
        # 'bulk' : bulk,
        # 'individual' : individual,
        # 'industrial' :industrial,
        # 'commercial' :commercial
    }
    return render(request,'dashboard/dos_dashboard.html',contex)



