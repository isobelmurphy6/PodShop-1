from django.db import models
from django.urls import path
from . import views
from . import *
from .forms import *

urlpatterns = [
   path('', views.all_products, name="homepage"),
   path('products/', views.all_products, name="products"),
   path('products/<int:prodid>', views.product_individual, name="indvidual_product"),
   path('register/', views.UserSignupView.as_view(), name="register"),
   path('login/',views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm)),
   path('logout/', views.logout_user, name="logout"),
   path('addbasket/<int:prodid>/', views.add_to_basket, name="add_basket"),
   path('basket/', views.show_basket, name="show_basket"),
   path('removeitem/<int:sbi>', views.remove_item, name="remove_basket"),
   path('order/', views.order, name='order'),
   path('orderhistory/', views.previous_orders, name="order_history"),
] 
