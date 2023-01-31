from django.shortcuts import render
from django.contrib.auth import login , logout, authenticate
from django.http import HttpResponse , HttpResponseRedirect
from student_manage.EmailBackEnd import EmailBackEnd
from django.contrib  import messages
# Create your views here.
def show(request):
    return render(request,"demo.htm")

def ShowLoginPage(request):
    return render(request,'login_page.htm')

def doLogin(request):
    if request.method != "POST":
        return HttpResponse('<h2> Method Not Allowed </h2>')
    else:
        user = EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type == '1':
                return HttpResponseRedirect('/admin_home')
            elif user.user_type == '2':
                return HttpResponse("Staff Login "+str(user.user_type))
            else:
                return HttpResponse("Student Login "+str(user.user_type))
            
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")
        
        
        
def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User: "+request.user.email + 'Usertpe : '+str(request.user.user_type))
    else:
        return HttpResponse("PLease Login FIrst")
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")



    
    
    
