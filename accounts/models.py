from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    CHOICES =(("male","male"),("female","female"),("others","others"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_Department = models.BooleanField(default=False)
    is_Teacher = models.BooleanField(default=False)
    is_Student = models.BooleanField(default=True)
    phone_no =models.IntegerField(null=True)
    image = models.ImageField(upload_to='accounts/usersimage')
    age=models.IntegerField(null=True)
    roll_no = models.IntegerField(null=True)
    semester = models.CharField(max_length = 225,default="N/a")
    join_date = models.DateTimeField(auto_now_add=True,null=True)
    subject = models.CharField(max_length = 255,null= True)
    gender =models.CharField(max_length=6,default="N/A",choices=CHOICES)
    address = models.CharField(max_length=225,default="N/A")
    

    def __str__(self):
        return f'{self.user.username} UserProfile'
    def Is_Teacher(self):
        return self.is_Teacher
    def Is_Department(self):
        return self.is_Department
    def Is_Student(self):
        return self.is_Student




def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user = kwargs['instance'])
post_save.connect(create_profile, sender=User)