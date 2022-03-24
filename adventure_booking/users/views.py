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
from django.core.files.storage import FileSystemStorage
from django.contrib import messages


# Create your views here.

def user_home(request):
    objects = ClientOffer.objects.all().order_by('-id')
    context = {'objects':objects}
    return render(request , "users/home.html",context)


def booking(request,user=None,pk=None):
    objects = ClientOffer.objects.filter(user=user,id=pk)
    print(objects[0].user)
    context = {'objects':objects}
    if request.method == 'POST':
        user = objects[0].user
        package_name = objects[0].trip_name
        full_name = request.POST["full_name"]
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        no_of_person = request.POST["no_of_person"]
        arraival_date = request.POST["arraival_date"]
        add_booking = ClientBooking(user=user,package_name=package_name,full_name=full_name,email=email,phone_number=phone_number,no_of_person=no_of_person,arraival_date=arraival_date)
        add_booking.save()
        messages.success(request, 'Your Booking has been recorded.')
    return render(request , "users/booking_page.html",context)



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
    return render(request , "users/register.html", context)





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
    return render(request , "users/login.html")





def logout_page(request):
    logout(request)
    return redirect('user_home')


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
        title = request.POST['title']
        content = request.POST['content']
        user = request.user
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name,image)
        add_detail = UserBlog(user=user,title=title,content=content,image=image)
        add_detail.save()
        return redirect('view_blog')
    return render(request , "users/blog_add.html",context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user','admin'])
def blog_delete(request,user=None,pk=None):
    object1 = UserBlog.objects.get(user=request.user,id=pk)
    object1.delete()
    return redirect('view_blog')




def view_blog(request):
    if request.user.is_authenticated:
        objects = UserBlog.objects.filter(user=request.user).order_by('-id')
        context = {'objects':objects}
        return render(request , "users/blog_page.html",context)
    else:
        return redirect('/user/login')


def view_all_blog(request):
    objects = UserBlog.objects.all().order_by('-id')
    context = {'objects':objects}
    return render(request , "users/all_blog_page.html",context)

def view_offer(request):
    objects = ClientOffer.objects.all().order_by('-id')
    context = {'objects':objects}
    return render(request , "users/offer.html",context)

def more_detail(request,user=None,pk=None):
    objects = ClientOffer.objects.filter(user=user,id=pk)
    context={'objects':objects}
    return render(request , "users/more_detail.html",context)



def offer_search(request):
    offers = ClientOffer.objects.all()
    query = request.GET['query']
    offers = offers.filter(trip_name__icontains=query)
    print(offers)
    context = {
            'offers': offers
            }
    return render(request,"users/offer_search.html", context)



def blog_search(request):
    offers = UserBlog.objects.all()
    query = request.GET['query']
    objects = offers.filter(title__icontains=query)
    print(offers)
    context = {
            'objects': objects
            }
    return render(request,"users/blog_search.html", context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['user','admin'])
def self_blog_search(request):
    offers = UserBlog.objects.filter(user=request.user)
    query = request.GET['query']
    objects = offers.filter(title__icontains=query)
    context = {
            'objects': objects
            }
    return render(request,"users/self_blog_search.html", context)
