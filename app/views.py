
from django.shortcuts import render
from django.shortcuts import render, redirect

from app.models import User


def index(request):
    if not request.session.get("user_pk"):
        return redirect('login')
    return render(request, 'index.html')

def login_view(request):
    user = None
    if request.session.get("user_pk"):
        return redirect('index')

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = User.objects.get(email=email)
            if user.password == password:
                request.session["user_pk"] = user.pk
                return redirect('index')
        except User.DoesNotExist:
            user = User(email=email, password=password)
            user.save()
            request.session["user_pk"] = user.pk
            return redirect('index')
    return render(request, 'login.html')
