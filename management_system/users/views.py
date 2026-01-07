from django.shortcuts import render,redirect,get_object_or_404
from .models import User

# Create your views here.
def user_list(request):
    users = User.objects.all()
    return render(request, "users/list.html", {"users": users})


def add_user(request):
    if request.method == "POST":
        User.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            contact=request.POST["contact"]
        )
        return redirect("user_list")
    return render(request, "users/add.html")

def update_user(request, id):
    user = get_object_or_404(User, id=id)  

    if request.method == "POST":
        user.name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.contact = request.POST.get("contact")
        user.save()
        return redirect("user_list")

    return render(request, "users/update.html", {"user": user})


def delete_user(request, id):
    User.objects.filter(id=id).delete()
    return redirect("user_list")