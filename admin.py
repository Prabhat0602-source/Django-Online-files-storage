from django.contrib import admin

# Register your models here.
from .models import userdata
class ContactAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'phonenumber', 'email','enrollnment','branch','year','subject1','subject2','subject3','subject4','subject5','subject6','subject7','subject8') 

admin.site.register(userdata)
