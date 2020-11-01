from django.urls import path, include

from . import views 

urlpatterns = [
    path('', views.homepageRender, name='startUpHomePage'),
    path('Funder/', views.funderRegisterView, name="FunderRegister"),
    path('Company/', views.startupRegisterView, name="startupRegister"),
    path('signinRole/', views.roleSelectViewSignin, name="signinRole"),
    path('signupRole/', views.roleSelectViewSingup, name="signupRole"),
    path('sigupFunder/', views.funderSignup, name="signupFunder"),
    path('FunderDashBoard/', views.funderDashBoard, name="funderDashboard"),
    path('FunderOTP/', views.confirmOTPFunder, name="Funderotp"),
    path('FunderLogin/', views.funderLogin, name="funderLogin"),
    path('CompanySignup/', views.companySigup, name="companySingup"), 
    path('CompanyDashBoard/', views.companyDashBoard, name="companyDashBoard"),
    path('CompanyOTP/', views.confirmOTPCompnay, name="Companytop"),
    path('CompanyLogin/', views.companyLogin, name="companyLogin"),
    path('logoutUser/', views.logoutuser, name = "Logout"),
    path('productDesc/<str:productId>/', views.productView, name = 'productDesc')
]  