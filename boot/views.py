from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth


from boot.models import Inquiry

# Create your views here.
def test(request):
    return render(request, "base.html")

def blog(request):
    if not request.user.is_authenticated:
        return redirect("boot:login")
    return render(request, "boot/blog.html")

def about(request):
    return render(request, "boot/about.html")

def contact(request):
    if request.method == "GET":
        return render(request, "boot/contact.html")
    elif request.method == "POST":
        new = Inquiry()
        new.fullname = request.POST["fullname"]
        new.email = request.POST["email"]
        new.phone_number = request.POST["phone_number"]
        new.message = request.POST["message"]
        new.save()

        return redirect("boot:contact")


def home(request):
    print(request.user.is_authenticated)
    return render(request, "boot/index.html")

def redirect_home(request):
    return render(request, "boot:home")

def login(request):
    if request.user.is_authenticated:
        return redirect("boot:home")
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(
            request, 
            username=username, 
            password=password
            )
        if user is not None:
            auth.login(request, user)
            return redirect("boot:home")

    return render(request, "boot/login.html", context=context)

def sign_up(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_check = request.POST.get("password_check")
        if username and password and password == password_check:
            
            new_user = User.objects.create_user(
                username = username,
                password = password,
            )

            return redirect("boot:login")

    return render(request, "boot/sign-up.html")


def logout(request):
    print(request.user.is_authenticated)
    if request.method == "POST":
        auth.logout(request)

    return redirect("boot:home")