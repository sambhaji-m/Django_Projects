"""inquiry_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inquiries import views
from inquiries.forms import enquiry
from inquiries.views import delete_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LoginPage,name='login'),
    path('signup/',views.SignupPage,name='signup'),
    # path('home/',views.HomePage,name='home'),
    # path('home/', views.my_view, name='home'),  using this backend data show on dashbord also 
    path('logout/',views.LogoutPage,name='logout'),
    path('enquiry/', views.enquiry_view, name='enquiry'),
    # path('view_inq/', views.view_inq, name='view_inq'),
    path('blank/', views.view_inq1, name='blank'),




    path('index/', views.index, name='index'),
    path('blank/', views.blank, name='blank'),
    path('table/', views.table, name='table'),



    # delete data from database
    path('delete/<int:data_id>/', delete_data, name='delete_data'),
    
    
]
