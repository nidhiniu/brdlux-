from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('home/', home, name='home'),  

    path('about_us/',about_us,name='about_us'),

    path('category/<str:category_name>/', car_by_category, name='car_by_category'),
    path('brand/<str:brand_name>/', car_by_brand, name='car_by_brand'),
    path('car/<int:car_id>/', car_detail, name='car_detail'),

    path('car/<int:car_id>/', car_detail_view, name='car_detail_view'),
    path('all_cars/', all_cars, name='all_cars'),
    path('brand/<str:brand_name>/', brand_detail, name='brand_detail'),

    


    path('login',loginpage,name='login'),
    path('logout',logoutpage,name='logout'),
    path('register',creatuser,name='register'),
    path('home/',homepage,name='homepage'),
    path('profile',profilepage,name='profile'),
    path('addpro/<int:id>', editpro,name='editpro'),
    path('addpost',addpost,name='addpost'),
    path('timeline',timeline,name='timeline'),



    path('car/<int:car_id>/add_to_favorites/', add_to_favorites, name='add_to_favorites'),    
    path('favorites/', favorites, name='favorites'),
    path('remove_favorite/<int:car_id>/', remove_favorite, name='remove_favorite'),

 
    path('allcars/', allcars, name='allcars'),
    path('cardetails/<int:car_id>/', cardetails, name='cardet'),
    path('updatecars/<int:car_id>/', updatecars, name='updatecars'),
    path('deletecars/<int:car_id>/', deletecars, name='deletecars'),
    path('sell_your_car/', add_car, name='sell_your_car'),


    path('user_posts/<int:user_id>/', user_posts, name='user_posts'),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)