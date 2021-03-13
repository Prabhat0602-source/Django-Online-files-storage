from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import userdata as userdat
from .forms import userdata ,clgdata , subdata , loginpage,GeeksForm,delete,change,ppchange
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from django.views.generic.edit import FormView
from django.core.files.storage import FileSystemStorage
import os
from .forms import GeeksForm
from django.core.mail import send_mail
from django.conf import settings

def handle_uploaded_file1(f):
    path="EndGemapp/media/%s/subject1/"%(p)
    with open(path+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def handle_uploaded_file2(f):
    path="EndGemapp/media/%s/subject2/"%(p)
    with open(path+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def handle_uploaded_file3(f):
    path="EndGemapp/media/%s/subject3/"%(p)
    with open(path+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def handle_uploaded_file4(f):
    path="EndGemapp/media/%s/subject4/"%(p)
    with open(path+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
# Create your views here.
def handle_uploaded_file5(f):
    path="EndGemapp/media/%s/subject5/"%(p)
    with open(path+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def handle_uploaded_file6(f):
    path="EndGemapp/media/%s/subject6/"%(p)
    with open(path+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def handle_uploaded_file7(f):
    path="EndGemapp/media/%s/subject7/"%(p)
    with open(path+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def handle_uploaded_file8(f):
    path="EndGemapp/media/%s/subject8/"%(p)
    with open(path+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
class SignUpView(TemplateView):
	template_name = "signup.html"
	form_class = "signup1.html"



	def get(self, request, *args, **kwargs):
		form = userdata()
		return render(request, self.template_name, {'form' : form})

	def post(self, request, *args, **kwargs):
		form = userdata(request.POST)

		if form.is_valid():
			global r
			r= form.cleaned_data['username']
			form.save()

		return HttpResponseRedirect( "/signup1/",{'form' : form})


class SignUpView1(TemplateView):
	template_name = "signup1.html"
	form_class = "signup2.html"



	def get(self, request, *args, **kwargs):
		form = clgdata()
		return render(request, self.template_name, {'form' : form})

	def post(self, request, *args, **kwargs):
		form = clgdata(request.POST)

		if form.is_valid():
		  userdat.objects.filter(pk=r).update(branch=form.cleaned_data['branch'],year=form.cleaned_data['year'],enrollnment=form.cleaned_data['enrollnment'])


		  return HttpResponseRedirect( "/signup2/",{'form' : form})

class SignUpView2(TemplateView):
	template_name = "signup2.html"




	def get(self, request, *args, **kwargs):
		form = subdata()
		return render(request, self.template_name, {'form' : form})

	def post(self, request, *args, **kwargs):
		form = subdata(request.POST)
		if form.is_valid():
		      userdat.objects.filter(pk=r).update(subject1=form.cleaned_data['subject1'],subject2=form.cleaned_data['subject2'],subject3=form.cleaned_data['subject3'],subject4=form.cleaned_data['subject4'],subject5=form.cleaned_data['subject5'],subject6=form.cleaned_data['subject6'],subject7=form.cleaned_data['subject7'],subject8=form.cleaned_data['subject8']);subject = 'Thank you for joining EndGem!';message = 'Thank you for trusting EndGem your files are completely safe with us!';email_from = settings.EMAIL_HOST_USER;recipient_list = userdat.objects.values_list('email', flat=True).get(pk=r);
		return HttpResponseRedirect( "/login/",{'form' : form})


class login(TemplateView):
	template_name = "login.html"



	def get(self, request, *args, **kwargs):
		form = loginpage()
		return render(request, self.template_name, {'form' : form})

	def post(self, request, *args, **kwargs):
	    form = loginpage(request.POST)
	    if form.is_valid():
		    try:userdat.objects.only('password').get(password=form.cleaned_data['pa']);userdat.objects.only('password').get(pk=form.cleaned_data['un']);
		    except userdat.DoesNotExist:return HttpResponseRedirect( "/login/",{'form' : form})
	    if (userdat.objects.only('password').get(password=form.cleaned_data['pa'])==userdat.objects.only('password').get(pk=form.cleaned_data['un'])):global p;p=form.cleaned_data['un'];return HttpResponseRedirect( "/home/")

	    else: return HttpResponseRedirect( "/login/",{'form' : form})

def loop(request,*args,**kwargs):

	s1=userdat.objects.values_list('subject1', flat=True).get(pk=p)
	en=userdat.objects.values_list('enrollnment', flat=True).get(pk=p)
	br=userdat.objects.values_list('branch', flat=True).get(pk=p)
	yr=userdat.objects.values_list('year', flat=True).get(pk=p);s2=userdat.objects.values_list('subject2', flat=True).get(pk=p)
	s3=userdat.objects.values_list('subject3', flat=True).get(pk=p)
	s4=userdat.objects.values_list('subject4', flat=True).get(pk=p)
	s5=userdat.objects.values_list('subject5', flat=True).get(pk=p)
	s6=userdat.objects.values_list('subject6', flat=True).get(pk=p)
	s7=userdat.objects.values_list('subject7', flat=True).get(pk=p)
	s8=userdat.objects.values_list('subject8', flat=True).get(pk=p);gn=userdat.objects.values_list('phonenumber', flat=True).get(pk=p);args={'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'en':en,'br':br,'yr':yr,'p':p,'gn':gn};return render(request, "afterlogin.html", args)

#def handle_uploaded_file(f):
    #if not os.path.exists('media/'):
        #os.mkdir('media/')
    #with open('media/' + f.name, 'wb+') as destination:
        #for chunk in f.chunks():
            #destination.write(chunk)
def home_view1(request,*args):
    s1=userdat.objects.values_list('subject1', flat=True).get(pk=p);en=userdat.objects.values_list('enrollnment', flat=True).get(pk=p);br=userdat.objects.values_list('branch', flat=True).get(pk=p);yr=userdat.objects.values_list('year', flat=True).get(pk=p);s2=userdat.objects.values_list('subject2', flat=True).get(pk=p);s3=userdat.objects.values_list('subject3', flat=True).get(pk=p);s4=userdat.objects.values_list('subject4', flat=True).get(pk=p);s5=userdat.objects.values_list('subject5', flat=True).get(pk=p);s6=userdat.objects.values_list('subject6', flat=True).get(pk=p);s7=userdat.objects.values_list('subject7', flat=True).get(pk=p);s8=userdat.objects.values_list('subject8', flat=True).get(pk=p);gn=userdat.objects.values_list('phonenumber', flat=True).get(pk=p)
    path="EndGemapp/media/%s/subject1"%(p)
    try:os.makedirs(path)
    except FileExistsError:pass
 # insert the path to your directory
    img_list =os.listdir(path)

    context = {}
    if request.POST:
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file1(request.FILES["Choose_File"])
            return HttpResponseRedirect('/subject1/')
    else:
        form = GeeksForm()
    context['form'] = form
    args={'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'en':en,'br':br,'yr':yr,'p':p,'form':form,'images': img_list,'gn':gn}
    return render(request, "subject1.html", args)

def home_view2(request,*args):
    s1=userdat.objects.values_list('subject1', flat=True).get(pk=p);en=userdat.objects.values_list('enrollnment', flat=True).get(pk=p);br=userdat.objects.values_list('branch', flat=True).get(pk=p);yr=userdat.objects.values_list('year', flat=True).get(pk=p);s2=userdat.objects.values_list('subject2', flat=True).get(pk=p);s3=userdat.objects.values_list('subject3', flat=True).get(pk=p);s4=userdat.objects.values_list('subject4', flat=True).get(pk=p);s5=userdat.objects.values_list('subject5', flat=True).get(pk=p);s6=userdat.objects.values_list('subject6', flat=True).get(pk=p);s7=userdat.objects.values_list('subject7', flat=True).get(pk=p);s8=userdat.objects.values_list('subject8', flat=True).get(pk=p);gn=userdat.objects.values_list('phonenumber', flat=True).get(pk=p)
    path="EndGemapp/media/%s/subject2"%(p)
    try:os.makedirs(path)
    except FileExistsError:pass
 # insert the path to your directory
    img_list =os.listdir(path)

    context = {}
    if request.POST:
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file2(request.FILES["Choose_File"])
            return HttpResponseRedirect('/subject2/')
    else:
        form = GeeksForm()
    context['form'] = form
    args={'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'en':en,'br':br,'yr':yr,'p':p,'form':form,'images': img_list,'gn':gn}
    return render(request, "subject2.html", args)

def home_view3(request,*args):
    s1=userdat.objects.values_list('subject1', flat=True).get(pk=p);en=userdat.objects.values_list('enrollnment', flat=True).get(pk=p);br=userdat.objects.values_list('branch', flat=True).get(pk=p);yr=userdat.objects.values_list('year', flat=True).get(pk=p);s2=userdat.objects.values_list('subject2', flat=True).get(pk=p);s3=userdat.objects.values_list('subject3', flat=True).get(pk=p);s4=userdat.objects.values_list('subject4', flat=True).get(pk=p);s5=userdat.objects.values_list('subject5', flat=True).get(pk=p);s6=userdat.objects.values_list('subject6', flat=True).get(pk=p);s7=userdat.objects.values_list('subject7', flat=True).get(pk=p);s8=userdat.objects.values_list('subject8', flat=True).get(pk=p);gn=userdat.objects.values_list('phonenumber', flat=True).get(pk=p)
    path="EndGemapp/media/%s/subject3"%(p)
    try:os.makedirs(path)
    except FileExistsError:pass
 # insert the path to your directory
    img_list =os.listdir(path)

    context = {}
    if request.POST:
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file3(request.FILES["Choose_File"])
            return HttpResponseRedirect('/subject3/')
    else:
        form = GeeksForm()
    context['form'] = form
    args={'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'en':en,'br':br,'yr':yr,'p':p,'form':form,'images': img_list,'gn':gn}
    return render(request, "subject3.html", args)

def home_view4(request,*args):
    s1=userdat.objects.values_list('subject1', flat=True).get(pk=p);en=userdat.objects.values_list('enrollnment', flat=True).get(pk=p);br=userdat.objects.values_list('branch', flat=True).get(pk=p);yr=userdat.objects.values_list('year', flat=True).get(pk=p);s2=userdat.objects.values_list('subject2', flat=True).get(pk=p);s3=userdat.objects.values_list('subject3', flat=True).get(pk=p);s4=userdat.objects.values_list('subject4', flat=True).get(pk=p);s5=userdat.objects.values_list('subject5', flat=True).get(pk=p);s6=userdat.objects.values_list('subject6', flat=True).get(pk=p);s7=userdat.objects.values_list('subject7', flat=True).get(pk=p);s8=userdat.objects.values_list('subject8', flat=True).get(pk=p);gn=userdat.objects.values_list('phonenumber', flat=True).get(pk=p)
    path="EndGemapp/media/%s/subject4"%(p)
    try:os.makedirs(path)
    except FileExistsError:pass
 # insert the path to your directory
    img_list =os.listdir(path)

    context = {}
    if request.POST:
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file4(request.FILES["Choose_File"])
            return HttpResponseRedirect('/subject4/')
    else:
        form = GeeksForm()
    context['form'] = form
    args={'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'en':en,'br':br,'yr':yr,'p':p,'form':form,'images': img_list,'gn':gn}
    return render(request, "subject4.html", args)

def home_view5(request,*args):
    s1=userdat.objects.values_list('subject1', flat=True).get(pk=p);en=userdat.objects.values_list('enrollnment', flat=True).get(pk=p);br=userdat.objects.values_list('branch', flat=True).get(pk=p);yr=userdat.objects.values_list('year', flat=True).get(pk=p);s2=userdat.objects.values_list('subject2', flat=True).get(pk=p);s3=userdat.objects.values_list('subject3', flat=True).get(pk=p);s4=userdat.objects.values_list('subject4', flat=True).get(pk=p);s5=userdat.objects.values_list('subject5', flat=True).get(pk=p);s6=userdat.objects.values_list('subject6', flat=True).get(pk=p);s7=userdat.objects.values_list('subject7', flat=True).get(pk=p);s8=userdat.objects.values_list('subject8', flat=True).get(pk=p);gn=userdat.objects.values_list('phonenumber', flat=True).get(pk=p)
    path="EndGemapp/media/%s/subject5"%(p)
    try:os.makedirs(path)
    except FileExistsError:pass
 # insert the path to your directory
    img_list =os.listdir(path)

    context = {}
    if request.POST:
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file5(request.FILES["Choose_File"])
            return HttpResponseRedirect('/subject5/')
    else:
        form = GeeksForm()
    context['form'] = form
    args={'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'en':en,'br':br,'yr':yr,'p':p,'form':form,'images': img_list,'gn':gn}
    return render(request, "subject5.html", args)

def home_view6(request,*args):
    s1=userdat.objects.values_list('subject1', flat=True).get(pk=p);en=userdat.objects.values_list('enrollnment', flat=True).get(pk=p);br=userdat.objects.values_list('branch', flat=True).get(pk=p);yr=userdat.objects.values_list('year', flat=True).get(pk=p);s2=userdat.objects.values_list('subject2', flat=True).get(pk=p);s3=userdat.objects.values_list('subject3', flat=True).get(pk=p);s4=userdat.objects.values_list('subject4', flat=True).get(pk=p);s5=userdat.objects.values_list('subject5', flat=True).get(pk=p);s6=userdat.objects.values_list('subject6', flat=True).get(pk=p);s7=userdat.objects.values_list('subject7', flat=True).get(pk=p);s8=userdat.objects.values_list('subject8', flat=True).get(pk=p);gn=userdat.objects.values_list('phonenumber', flat=True).get(pk=p)
    path="EndGemapp/media/%s/subject6"%(p)
    try:os.makedirs(path)
    except FileExistsError:pass
 # insert the path to your directory
    img_list =os.listdir(path)

    context = {}
    if request.POST:
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file6(request.FILES["Choose_File"])
            return HttpResponseRedirect('/subject6/')
    else:
        form = GeeksForm()
    context['form'] = form
    args={'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'en':en,'br':br,'yr':yr,'p':p,'form':form,'images': img_list,'gn':gn}
    return render(request, "subject6.html", args)

def home_view7(request,*args):
    s1=userdat.objects.values_list('subject1', flat=True).get(pk=p);en=userdat.objects.values_list('enrollnment', flat=True).get(pk=p);br=userdat.objects.values_list('branch', flat=True).get(pk=p);yr=userdat.objects.values_list('year', flat=True).get(pk=p);s2=userdat.objects.values_list('subject2', flat=True).get(pk=p);s3=userdat.objects.values_list('subject3', flat=True).get(pk=p);s4=userdat.objects.values_list('subject4', flat=True).get(pk=p);s5=userdat.objects.values_list('subject5', flat=True).get(pk=p);s6=userdat.objects.values_list('subject6', flat=True).get(pk=p);s7=userdat.objects.values_list('subject7', flat=True).get(pk=p);s8=userdat.objects.values_list('subject8', flat=True).get(pk=p);gn=userdat.objects.values_list('phonenumber', flat=True).get(pk=p)
    path="EndGemapp/media/%s/subject7"%(p)
    try:os.makedirs(path)
    except FileExistsError:pass
 # insert the path to your directory
    img_list =os.listdir(path)

    context = {}
    if request.POST:
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file7(request.FILES["Choose_File"])
            return HttpResponseRedirect('/subject7/')
    else:
        form = GeeksForm()
    context['form'] = form
    args={'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'en':en,'br':br,'yr':yr,'p':p,'form':form,'images': img_list,'gn':gn}
    return render(request, "subject7.html", args)

def home_view8(request,*args):
    s1=userdat.objects.values_list('subject1', flat=True).get(pk=p);en=userdat.objects.values_list('enrollnment', flat=True).get(pk=p);br=userdat.objects.values_list('branch', flat=True).get(pk=p);yr=userdat.objects.values_list('year', flat=True).get(pk=p);s2=userdat.objects.values_list('subject2', flat=True).get(pk=p);s3=userdat.objects.values_list('subject3', flat=True).get(pk=p);s4=userdat.objects.values_list('subject4', flat=True).get(pk=p);s5=userdat.objects.values_list('subject5', flat=True).get(pk=p);s6=userdat.objects.values_list('subject6', flat=True).get(pk=p);s7=userdat.objects.values_list('subject7', flat=True).get(pk=p);s8=userdat.objects.values_list('subject8', flat=True).get(pk=p);gn=userdat.objects.values_list('phonenumber', flat=True).get(pk=p)
    path="EndGemapp/media/%s/subject8"%(p)
    try:os.makedirs(path)
    except FileExistsError:pass
 # insert the path to your directory
    img_list =os.listdir(path)

    context = {}
    if request.POST:
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file8(request.FILES["Choose_File"])
            return HttpResponseRedirect('/subject8/')
    else:
        form = GeeksForm()
    context['form'] = form
    args={'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'en':en,'br':br,'yr':yr,'p':p,'form':form,'images': img_list,'gn':gn}
    return render(request, "subject8.html", args)

def loop1(request,*args,**kwargs):

	s1=userdat.objects.values_list('subject1', flat=True).get(pk=p)
	en=userdat.objects.values_list('enrollnment', flat=True).get(pk=p)
	br=userdat.objects.values_list('branch', flat=True).get(pk=p)
	yr=userdat.objects.values_list('year', flat=True).get(pk=p);s2=userdat.objects.values_list('subject2', flat=True).get(pk=p)
	s3=userdat.objects.values_list('subject3', flat=True).get(pk=p)
	s4=userdat.objects.values_list('subject4', flat=True).get(pk=p)
	s5=userdat.objects.values_list('subject5', flat=True).get(pk=p)
	s6=userdat.objects.values_list('subject6', flat=True).get(pk=p)
	s7=userdat.objects.values_list('subject7', flat=True).get(pk=p)
	s8=userdat.objects.values_list('subject8', flat=True).get(pk=p);gn=userdat.objects.values_list('phonenumber', flat=True).get(pk=p);args={'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'en':en,'br':br,'yr':yr,'p':p,'gn':gn};return render(request, "contact.html", args)

def deletefile1(request):
   form=delete(request.POST)
   if form.is_valid():
       string=form.cleaned_data['dele']
       os.remove(string)

   return HttpResponseRedirect('/subject1')
def deletefile2(request):
   form=delete(request.POST)
   if form.is_valid():
       string=form.cleaned_data['dele']
       os.remove(string)

   return HttpResponseRedirect('/subject2')
def deletefile3(request):
   form=delete(request.POST)
   if form.is_valid():
       string=form.cleaned_data['dele']
       os.remove(string)

   return HttpResponseRedirect('/subject3')
def deletefile4(request):
    form=delete(request.POST)
    if form.is_valid():
        string=form.cleaned_data['dele']
        os.remove(string)

    return HttpResponseRedirect('/subject4')
def deletefile5(request):
   form=delete(request.POST)
   if form.is_valid():
       string=form.cleaned_data['dele']
       os.remove(string)

   return HttpResponseRedirect('/subject5')
def deletefile6(request):
   form=delete(request.POST)
   if form.is_valid():
       string=form.cleaned_data['dele']
       os.remove(string)

   return HttpResponseRedirect('/subject6')
def deletefile7(request):
   form=delete(request.POST)
   if form.is_valid():
       string=form.cleaned_data['dele']
       os.remove(string)

   return HttpResponseRedirect('/subject7')
def deletefile8(request):
   form=delete(request.POST)
   if form.is_valid():
       string=form.cleaned_data['dele']
       os.remove(string)

   return HttpResponseRedirect('/subject8')

def email(request):
   form=change(request.POST)
   global ur
   if form.is_valid():
       ur=form.cleaned_data['pc']
       subject = 'Password Change Request'
       message = 'Please click on the link to http://127.0.0.1:8000/passwordchange/'
       email_from = settings.EMAIL_HOST_USER
       recipient_list = userdat.objects.values_list('email', flat=True).get(pk=ur)
       send_mail( subject, message, email_from,[recipient_list] )
   return render(request, "pcf.html")
def pchange(request):
    form= ppchange(request.POST)
    if form.is_valid():
        userdat.objects.filter(pk=ur).update(password=form.cleaned_data['passi'])
        return HttpResponseRedirect('/login/')


    return render(request,'password.html')
