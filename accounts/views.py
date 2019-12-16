from django.shortcuts import render, redirect,get_object_or_404
from django.conf import settings
from accounts.forms import SignUpForm
from django.core.mail import send_mail


# Create your views here.
class SignUpView(View):
    
    def get(self, request, *args, **kwargs):
        template_name='accounts/signup.html'
        form = SignUpForm()
        return render(request,template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        #value = {'username':"",'email':"",'first_name':"",'last_name':"",'password1':"Ashesh1234",'password2':"Ashesh1234"}
        form = SignUpForm(request.POST)
        template_name='accounts/success.html'
        if form.is_valid():
            user =form.save(commit=False)
            raw_password = form.cleaned_data['password1']
            #raw_password =  User.objects.make_random_password(length=8, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889!@#$%^&*")
            username = form.cleaned_data['username']
            user.set_password(raw_password)
            user.save()
            subject = "Congratulation you are Inside the Trashcan Board"
            from_email = settings.EMAIL_HOST_USER
            to_mail = [user.email]
            signup_message = """ Wellcome to TrashCan SmartWaste management system. To configure you profile please visit http://127.0.0.1:8080/login \nUsername:"""+username+"""\nPassword:"""+raw_password
            send_mail(subject = subject,from_email=from_email,recipient_list=to_mail,message=signup_message,fail_silently=False)


            return redirect('/success/')

        else:
            return render(request, 'accounts/signup.html', {'form':form})
