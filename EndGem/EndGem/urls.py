"""EndGem URL Configuration

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
from django.urls import path
from EndGemapp import views
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.SignUpView.as_view()),
    path('signup1/',views.SignUpView1.as_view()),
    path('signup2/',views.SignUpView2.as_view()),
    path('login/',views.login.as_view()),
    path('home/',views.loop),
    path('subject1/',views.home_view1),
    path('subject2/',views.home_view2),
    path('subject3/',views.home_view3),
    path('subject4/',views.home_view4),
    path('subject5/',views.home_view5),
    path('subject6/',views.home_view6),
    path('subject8/',views.home_view8),
    path('subject7/',views.home_view7),
    path('contact/',views.loop1),
    path('delete1/',views.deletefile1),
    path('delete2/',views.deletefile2),
    path('delete3/',views.deletefile3),
    path('delete4/',views.deletefile4),
    path('delete5/',views.deletefile5),
    path('delete6/',views.deletefile6),
    path('delete7/',views.deletefile7),
    path('delete8/',views.deletefile8),
    path('email/',views.email),
    path('passwordchange/',views.pchange)
]
