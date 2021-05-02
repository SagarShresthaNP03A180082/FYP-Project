from django.shortcuts import render, HttpResponse

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


# Create your views here.
#Login
# def index(request):
#     return render(request,'index.html',)

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'dashboard.html')
        else:
            messages.info(request,"invalid username")
            return redirect('login')
    else:
        return render(request,'login1.html')


#logout

def logout(request):
    auth.logout(request)
    return render(request,'index.html')



#forgot
def forgotpassword(request):
    return render(request,'forgot-password.html')




# Signup
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        # birthday = request.POST['birthday']
        # gender = request.POST['gender']
        email = request.POST['email']
        # phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username Error')
                return render(request,'registerForm.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email Error')
                return render(request,'registerForm.html')
            else:
             user =User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
             user.save()
             messages.info(request,'Successfully Register')
             return redirect('login')
             
        else:
            messages.info(request,'password not matching')
            return render(request,'registerForm.html')
        return render(request,'index.html')
    else:
        return render(request,'registerForm.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change-password.html', {
        'form': form
    })

