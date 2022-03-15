from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from client.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login , logout
from django.contrib.auth.decorators import login_required
from client.decorators import unauthenticated_user,allowed_users
from client.models import ClientDetail,ClientOffer,ClientBooking
from django.http import HttpResponse
from client.models import ClientBooking,ClientOffer
from .models import UserBlog
from .forms import BlogForm


# Create your views here.

def user_home(request):
    objects = ClientOffer.objects.all()
    context = {'objects':objects}
    return render(request , "users/home.html",context)


def booking(request,user=None):
    if request.method == 'POST':
        full_name = request.POST["full_name"]
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        arrival_date = request.POST["arrival_date"]
        add_booking = ClientBooking(user=user,full_name=full_name,email=email,phone_number=phone_number,arrival_date=arrival_date)
        add_booking.save()
    return render(request , "users/booking_page.html")



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
            return redirect('user_home')
        else:
            messages.info(request, 'Username and password incorrect')
    return render(request , "clients/login.html")





def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['user','admin'])
def blog_edit(request,user=None,pk=None):
    object1 = UserBlog.objects.get(user=request.user,id=pk)
    form = BlogForm(instance=object1)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES,instance=object1)
        if form.is_valid():
            form.save()
            return redirect('view_blog')
    context = {'form':form}
    return render(request , "users/blog_edit.html",context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['user','admin'])
def blog_add(request):
    context = {'form':BlogForm}
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_blog')
    return render(request , "users/blog_add.html",context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user','admin'])
def blog_delete(request,user=None,pk=None):
    object1 = UserBlog.objects.get(user=request.user,id=pk)
    object1.delete()
    return redirect('view_blog')




def view_blog(request):
    objects = UserBlog.objects.filter(user=request.user)
    context = {'objects':objects}
    return render(request , "users/blog_page.html",context)


def view_all_blog(request):
    objects = UserBlog.objects.all()
    context = {'objects':objects}
    return render(request , "users/all_blog_page.html",context)
