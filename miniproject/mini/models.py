from django.db import models
from django.contrib.auth.models import User


class CarCategory(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='carcategory')

    def __str__(self):
        return self.name

class CarBrand(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='carbrand')

    def __str__(self):
        return self.name
    
class Car(models.Model):
    model = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='cars')
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE, related_name='cars')
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    fuel_type = models.CharField(max_length=100, null=True, blank=True)  
    engine = models.CharField(max_length=100, blank=True, null=True)
    transmission = models.CharField(max_length=100, blank=True, null=True)
    mileage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.brand.name} {self.model}"


class CarDetail(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name="detail")
    engine = models.CharField(max_length=100, blank=True, null=True)
    transmission = models.CharField(max_length=100, blank=True, null=True)
    mileage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    image1 = models.ImageField(upload_to='car_details', blank=True, null=True)
    image2 = models.ImageField(upload_to='car_details', blank=True, null=True)
    image3 = models.ImageField(upload_to='car_details', blank=True, null=True)
    image4 = models.ImageField(upload_to='car_details', blank=True, null=True)
    image5 = models.ImageField(upload_to='car_details', blank=True, null=True)
    image6 = models.ImageField(upload_to='car_details', blank=True, null=True)
    image7 = models.ImageField(upload_to='car_details', blank=True, null=True)
    image8 = models.ImageField(upload_to='car_details', blank=True, null=True)

    def __str__(self):
        return f"Details for {self.car}"
    


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.EmailField(null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to='profilepicture',null=True,blank=True)

    def __str__(self):
        return self.user.username  


class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Car, through='FavoriteItem')

    def __str__(self):
        return f"Favorites for {self.user.username}"

class FavoriteItem(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.car.model} in favorites"
    
class Posts(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    img1=models.ImageField(upload_to='post_images',blank=True,null=True)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)


# Create your models here.
