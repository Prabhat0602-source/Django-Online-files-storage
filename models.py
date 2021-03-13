from django.db import models

# Create your modelsclass Dreamreal(models.Model):
class userdata(models.Model):
   username = models.CharField(primary_key=True, max_length = 50)
   password = models.CharField(max_length = 50)
   email= models.CharField(max_length = 50)
   phonenumber = models.CharField(max_length = 50)
   branch = models.CharField(max_length = 30,blank=True)
   year = models.CharField(max_length = 30,blank=True)
   enrollnment= models.CharField(max_length = 30,blank=True)
   subject1 = models.CharField(max_length = 30,blank=True)
   subject2 = models.CharField(max_length = 30,blank=True)
   subject3 = models.CharField(max_length = 30,blank=True)
   subject4 = models.CharField(max_length = 30,blank=True)
   subject5 = models.CharField(max_length = 30,blank=True)
   subject6 = models.CharField(max_length = 30,blank=True)
   subject7 = models.CharField(max_length = 30,blank=True)
   subject8 = models.CharField(max_length = 30,blank=True)
   #clgdata = models.ForeignKey('clgdata', on_delete=models.CASCADE,null=True)
   #subdata = models.ForeignKey('subdata', on_delete=models.CASCADE,null=True)

class Meta:
      db_table = "userdata"

#class clgdata(models.Model)  :
   #branch = models.CharField(max_length = 30,blank=True)
   #year = models.CharField(max_length = 30,blank=True)
   #enrollnment= models.CharField(max_length = 30,blank=True)
#class Meta:
     #db_table="clgdata"

#class subdata(models.Model):

   #subject1 = models.CharField(max_length = 30,blank=True)
   #subject2 = models.CharField(max_length = 30,blank=True)
   #subject3 = models.CharField(max_length = 30,blank=True)
   #subject4 = models.CharField(max_length = 30,blank=True)
   #subject5 = models.CharField(max_length = 30,blank=True)
   #subject6 = models.CharField(max_length = 30,blank=True)
   #subject7 = models.CharField(max_length = 30,blank=True)
   #subject8 = models.CharField(max_length = 30,blank=True)

#class Meta:
     # db_table = "clgdata
