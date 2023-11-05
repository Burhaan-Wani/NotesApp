"""
URL configuration for NotesApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Notes import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", views.Signup),
    path("otp/", views.SendOtp),
    path("", views.Login),
    path("login/", views.Login),
    path("logout/", views.Logout),
    path("delete/<int:id>", views.Delete),
    path("identify/", views.forgotPassword),
    path("resetotp/", views.resetOtp),
    path("NoteApp/", views.NoteApp),
    path("demo/", views.Demo),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
