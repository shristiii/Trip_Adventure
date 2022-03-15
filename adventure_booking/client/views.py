from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login , logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users
from .models import ClientDetail,ClientOffer,ClientBooking

# Create your views here.
#admin views
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for'+user)
    context = {'form':form}
    return render(request , "admin/register.html", context)





#client views
@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('client_home')
        else:
            messages.info(request, 'Username and password incorrect')
    return render(request , "clients/login.html")





def logout_page(request):
    logout(request)
    return redirect('login')






@login_required(login_url='login')
@allowed_users(allowed_roles=['client','admin'])
def client_home(request):
    val = ClientOffer.objects.filter(user=request.user).exists()
    print(val)
    if val == True:
        objects = ClientOffer.objects.filter(user=request.user)
        context = {'objects':objects}
    else:
        context = {}
    return render(request , "clients/home.html",context)





@login_required(login_url='login')
@allowed_users(allowed_roles=['client','admin'])
def Client_Detail(request):
    val = ClientDetail.objects.filter(user=request.user).exists()
    if val == True:
        objects = ClientDetail.objects.filter(user=request.user)
        context = {'objects':objects}
    else:
        context = {}
    if request.method == 'POST':
        user = request.user
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        phone_number = request.POST["phone_number"]
        company_name = request.POST["company_name"]
        location = request.POST["location"]
        if val == True:
            ClientDetail.objects.filter(user=user).update(first_name=first_name,last_name=last_name,phone_number=phone_number,company_name=company_name,location=location)
        else:
            add_detail = ClientDetail(user=user,first_name=first_name,last_name=last_name,phone_number=phone_number,company_name=company_name,location=location)
            add_detail.save()
    return render(request , "clients/ClientDetail.html",context)





@login_required(login_url='login')
@allowed_users(allowed_roles=['client','admin'])
def trip(request,user=None,pk=None):
    val = ClientOffer.objects.filter(user=request.user,id=pk).exists()
    if val == True:
        objects = ClientOffer.objects.filter(user=request.user,id=pk)
        context = {'objects':objects}
    else:
        context = {}
    if request.method == 'POST':
        user = request.user
        trip_name = request.POST["trip_name"]
        trip_desc = request.POST["trip_desc"]
        price = request.POST["price"]
        if val == True:
            ClientOffer.objects.filter(user=request.user,id=pk).update(trip_name=trip_name,trip_desc=trip_desc,price=price)
        else:
            add_offer = ClientOffer(user=user,trip_name=trip_name,trip_desc=trip_desc,price=price)
            add_offer.save()
    return render(request , "clients/trip.html",context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['client','admin'])
def trip_delete(request,user,pk):
    ClientOffer.objects.filter(user=request.user,id=pk).delete()
    return redirect('home')




@login_required(login_url='login')
@allowed_users(allowed_roles=['client','admin'])
def view_booking(request):
    objects = ClientBooking.objects.filter(user=request.user)
    context = {'objects':objects}
    return render(request , "clients/view_booking.html",context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['client','admin'])
def booking_edit(request,user=None,pk=None):
    val = ClientOffer.objects.filter(user=request.user,id=pk).exists()
    if val == True:
        objects = ClientOffer.objects.filter(user=request.user,id=pk)
        context = {'objects':objects}
    else:
        context = {}
    if request.method == 'POST':
        user = request.user
        trip_name = request.POST["trip_name"]
        trip_desc = request.POST["trip_desc"]
        price = request.POST["price"]
        if val == True:
            ClientOffer.objects.filter(user=request.user,id=pk).update(trip_name=trip_name,trip_desc=trip_desc,price=price)
        else:
            add_offer = ClientOffer(user=user,trip_name=trip_name,trip_desc=trip_desc,price=price)
            add_offer.save()
    return render(request , "clients/trip.html",context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['client','admin'])
def booking_delete(request,user,pk):
    ClientOffer.objects.filter(user=request.user,id=pk).delete()
    return redirect('home')
