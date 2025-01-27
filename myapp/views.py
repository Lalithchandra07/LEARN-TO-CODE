from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm

# Create your views here.

def register_view(request):
    # Render the registration page with the registration card form
    return render(request, 'myapp/register.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register_submit(request):
    if request.method == 'POST':
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Basic validation checks
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register_view')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register_view')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register_view')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the home page after successful registration
        else:
            error = "Registration failed. Please correct the errors below."
    else:
        form = RegistrationForm()
        error = None
    
    context = {'form': form, 'error': error}
    return render(request, 'register.html', context)

def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def register(request):
    return render(request, 'myapp/register.html')

def course(request):
    return render(request, 'myapp/course.html')

def python(request):
    return render(request, 'myapp/python.html') #adding correct path to the video

def c(request):
    return render(request, 'myapp/c.html')

def cplus(request):
    return render(request, 'myapp/cplus.html')

def java(request):
    return render(request, 'myapp/java.html')

def javascript(request):
    return render(request, 'myapp/javascript.html')

def kotlin(request):
    return render(request, 'myapp/kotlin.html')

def p1(request):
    return render(request, 'myapp/python/p1.html')

def p2(request):
    return render(request, 'myapp/python/p2.html')

def p3(request):
    return render(request, 'myapp/python/p3.html')

def p4(request):
    return render(request, 'myapp/python/p4.html')

def p5(request):
    return render(request, 'myapp/python/p5.html')

def p6(request):
    return render(request, 'myapp/python/p6.html')

def p7(request):
    return render(request, 'myapp/python/p7.html')

def p8(request):
    return render(request, 'myapp/python/p8.html')

def p9(request):
    return render(request, 'myapp/python/p9.html')

def p10(request):
    return render(request, 'myapp/python/p10.html')

def j1(request):
    return render(request, 'myapp/java/java1.html')

def j2(request):
    return render(request, 'myapp/java/java2.html')

def j3(request):
    return render(request, 'myapp/java/java3.html')

def j4(request):
    return render(request, 'myapp/java/java4.html')

def j5(request):
    return render(request, 'myapp/java/java5.html')

def j6(request):
    return render(request, 'myapp/java/java6.html')

def j7(request):
    return render(request, 'myapp/java/java7.html')

def j8(request):
    return render(request, 'myapp/java/java8.html')

def j9(request):
    return render(request, 'myapp/java/java9.html')

def j10(request):
    return render(request, 'myapp/java/java10.html')

def c1(request):
    return render(request, 'myapp/c/c1.html')

def c2(request):
    return render(request, 'myapp/c/c2.html')

def c3(request):
    return render(request, 'myapp/c/c3.html')

def c4(request):
    return render(request, 'myapp/c/c4.html')

def c5(request):
    return render(request, 'myapp/c/c5.html')

def c6(request):
    return render(request, 'myapp/c/c6.html')

def c7(request):
    return render(request, 'myapp/c/c7.html')

def c8(request):
    return render(request, 'myapp/c/c8.html')

def c9(request):
    return render(request, 'myapp/c/c9.html')

def c10(request):
    return render(request, 'myapp/c/c10.html')

def k1(request):
    return render(request, 'myapp/kotlin/k1.html')

def k2(request):
    return render(request, 'myapp/kotlin/k2.html')

def k3(request):
    return render(request, 'myapp/kotlin/k3.html')

def k4(request):
    return render(request, 'myapp/kotlin/k4.html')

def k5(request):
    return render(request, 'myapp/kotlin/k5.html')

def k6(request):
    return render(request, 'myapp/kotlin/k6.html')

def k7(request):
    return render(request, 'myapp/kotlin/k7.html')

def k8(request):
    return render(request, 'myapp/kotlin/k8.html')

def k9(request):
    return render(request, 'myapp/kotlin/k9.html')

def k10(request):
    return render(request, 'myapp/kotlin/k10.html')

def js1(request):
    return render(request, 'myapp/js/js1.html')

def js2(request):
    return render(request, 'myapp/js/js2.html')

def js3(request):
    return render(request, 'myapp/js/js3.html')

def js4(request):
    return render(request, 'myapp/js/js4.html')

def js5(request):
    return render(request, 'myapp/js/js5.html')

def js6(request):
    return render(request, 'myapp/js/js6.html')

def js7(request):
    return render(request, 'myapp/js/js7.html')

def js8(request):
    return render(request, 'myapp/js/js8.html')

def js9(request):
    return render(request, 'myapp/js/js9.html')

def js10(request):
    return render(request, 'myapp/js/js10.html')

def cpp1(request):
    return render(request, 'myapp/cpp/cpp1.html')

def cpp2(request):
    return render(request, 'myapp/cpp/cpp2.html')

def cpp3(request):
    return render(request, 'myapp/cpp/cpp3.html')

def cpp4(request):
    return render(request, 'myapp/cpp/cpp4.html')

def cpp5(request):
    return render(request, 'myapp/cpp/cpp5.html')

def cpp6(request):
    return render(request, 'myapp/cpp/cpp6.html')

def cpp7(request):
    return render(request, 'myapp/cpp/cpp7.html')

def cpp8(request):
    return render(request, 'myapp/cpp/cpp8.html')

def cpp9(request):
    return render(request, 'myapp/cpp/cpp9.html')

def cpp10(request):
    return render(request, 'myapp/cpp/cpp10.html')








