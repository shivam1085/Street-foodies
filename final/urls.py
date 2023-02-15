"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from . import views
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 
urlpatterns = [
    path('product/',include('product.urls')),
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("visit",views.visit,name="visit"),
    path("qrvisit",views.qrvisit,name="qrvisit"),
    path("contact",views.contact,name="contact"),
    path("about",views.about_us,name="about_us"),
    path("blog",views.blog,name="blog"),
    path("query",views.query,name="query"),
    path("vendor",views.vendor,name="vendor"),
    path("vlogin",views.vlogin,name="vlogin"),
    path("appuser",views.appuser,name="appuser"),
    path("register",views.register,name="register"),
    path("signup",views.signup,name="signup"),
    path("ulogin",views.ulogin,name="ulogin"),
    # path("temp",views.temp,name="temp"),#for testing QR functionality
    # path("thqrcode",views.qrprofile,name="qrprofile"),#for testing QR functionality
     

] 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
