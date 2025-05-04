from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import Carform,PostForm
from django.conf import settings

def home(request):
    categories = CarCategory.objects.all()
    brands = CarBrand.objects.all()
    cars = Car.objects.all()  
    return render(request, 'home/home.html', {'categories': categories, 'brands': brands, 'cars': cars})

def car_by_category(request, category_name):
    cars = Car.objects.filter(fuel_type=category_name)  
    return render(request, 'car_by_category.html', {'category_name': category_name, 'cars': cars})


def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    print(car.brand, car.image)
    return render(request, 'car_detailsall.html', {'car': car})


def car_by_brand(request, brand_name):
    brand = CarBrand.objects.get(name=brand_name)
    cars = Car.objects.filter(brand=brand)
    return render(request, 'car_by_brand.html', {'brand': brand, 'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    print(car.brand, car.image)
    return render(request, 'car_detailsall.html', {'car': car})

def all_cars(request):
    cars = Car.objects.all()
    return render(request, 'all_cars.html', {'cars': cars})

def car_detail_view(request, car_id):
    car = Car.objects.all().order_by('-id')[:20]
    car_detail = car.detail  

    return render(request, 'car_detail_page.html', {'car': car, 'car_detail': car_detail})



def homepage(request):
    return render(request,"home/home.html")


def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request, username=username, password=password)

        print(user)
        if user:
            login(request, user)
            if user.is_staff:
                print("admin logged in")
                return redirect(homepage)
            else:
                print("user has logged in")
                messages.success(request, 'login success')
                return redirect(homepage)
        else:
            print("no such user")
    return render(request, 'login.html')

def logoutpage(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

def creatuser(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            a = form.save()
            Profile.objects.create(user=a)
            return redirect(loginpage)
    else:
        form = RegisterUser()
    return render(request, 'register.html', {'form': form})



@login_required(login_url=reverse_lazy('login'))
def profilepage(request):
    usr = request.user
    pro = Profile.objects.get(user=usr)
    z=Posts.objects.filter(user=request.user)
    print(usr)
    print(z)
    return render(request, 'profile.html', {'pro': pro,'z':z})

def editpro(request, id):
    z = Profile.objects.get(id=id)
    
    if request.method == 'POST':
        form = profileForm(request.POST,request.FILES, instance=z)
        if form.is_valid():
            form.save()
            return redirect(profilepage)
    else:
        form = profileForm(instance=z)
    return render(request, 'addpro.html', {'form': form})

def brand_detail(request, brand_name):
    brand = CarBrand.objects.get(name=brand_name)
    return render(request, 'brand_detail.html', {'brand': brand})

@login_required
def add_to_favorites(request, car_id):
    car = Car.objects.get(id=car_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user)
    favorite.items.add(car)
    return redirect('car_detail', car_id=car.id)

@login_required
def favorites(request):
    favorite = request.user.favorite
    return render(request, 'favorites.html', {'favorite': favorite})


def remove_favorite(request, car_id):
    if request.user.is_authenticated:
        favorite = request.user.favorite
        car = Car.objects.get(id=car_id)
        favorite.items.remove(car)
        return redirect('favorites')
    else:
        return redirect('login')
    

def allcars(request):
    cars = Car.objects.all()

    if request.method == "POST":
        form = Carform(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('allcars')  
    else:
        form = Carform()  
    return render(request, 'allcars.html', {'cars': cars, 'form': form})

def cardetails(request, car_id):
    car = Car.objects.get(id=car_id) 
    return render(request, 'cardetails.html', {'car': car})

def updatecars(request, car_id):
    car = Car.objects.get( id=car_id)

    if request.method == 'POST':
        form = Carform(request.POST, request.FILES,instance=car) 
        if form.is_valid():
            form.save()
            return redirect('allcars')  
    else:
        form = Carform(instance=car)

    return render(request, 'updatecars.html', {'form': form})

def deletecars(request, car_id):
    car = Car.objects.get( id=car_id)
    if request.method == 'POST':
        car.delete() 
        return redirect('allcars')  
    return render(request, 'deletecars.html', {'car': car})


def add_car(request):
    if request.method == 'POST':
        form = Carform(request.POST,request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('home') 
    else:
        form = Carform()  

    return render(request, 'sell_your_car.html', {'form': form})

def about_us(request):
    return render(request,'about_us.html')

def addpost(request):
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            a= form.save(commit=False)
            a.user=request.user
            a.save()
            print(f"Image URL: {a.img1.url}") 
            return redirect('home')
    else:
        form=PostForm()
    return render(request,'addpost.html',{'form':form})

def timeline(request):
    posts=Posts.objects.all()
    return render(request,'timeline.html',{'posts':posts})


def user_posts(request, user_id):
    user = User.objects.get(id=user_id)
    posts = Posts.objects.filter(user=user)
    return render(request, 'user_posts.html', {'posts': posts, 'user': user})



   