from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request,"login.html")
def register_page(request):
    return render(request,"registration.html")
def home_page(request):
    return render(request,"index.html")
def client_page(request):
    return render(request,"client.html")
def clientform_page(request):
    return render(request,"clientform.html")
def booking_page(request):
    return render(request,"Booking.html")
def Description_page(request):
    return render(request,"Description.html")
def password_page(request):
    return render(request,"Password.html")
def userlogin_page(request):
    return render(request,"userlogin.html")