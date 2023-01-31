from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from student_manage.models import CustomUser, Staffs, Courses,Students,Subjects
import datetime
def admin_home(request):
    return render(request,'hod_template/home_content.htm')

def add_staff(request):
    return render(request,'hod_template/add_staff_template.htm')

def add_staff_save(request):
    if request.method != "POST":
        return HttpResponse("NOT ALLOWED HERE")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(username = username,password=password,email=email , last_name = last_name , first_name = first_name ,user_type = 2)
            user.staffs.address=address
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect("/add_staff")
            
        except:
            messages.error(request,'Failed to create User')
            return HttpResponseRedirect("/add_staff")
            

def add_course(request):
    return render(request, 'hod_template/add_course_template.htm')


def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("NOT ALLOWED HERE")
    else:
        course = request.POST.get("course")
        
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request,"Successfully Added Course")
            return HttpResponseRedirect("/add_course")

        except:
            messages.error(request, 'Failed to create User')
            return HttpResponseRedirect("/add_course")

             
def add_student(request):
    courses = Courses.objects.all()
    return render(request, 'hod_template/add_student_template.htm',{"courses": courses})


def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("NOT ALLOWED HERE")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        course_id = request.POST.get("course")
        sex = request.POST.get('sex')
        # profile_pic = request.FILES['profile_pic']
        
        # fs = FileSystemStorage()
        # filename = fs.save(profile_pic.name,profile_pic)
        # profile_pic_url = fs.url(filename)
        
        if request.FILES.get('profile_pic',False):
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None
        
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=3)
            user.students.address = address
            course_obj = Courses.objects.get(id=course_id)
            user.students.course_id = course_obj
            user.students.session_start_year = session_start
            user.students.session_end_year  = session_end
            user.students.gender = sex
            # user.students.profile_pic = profile_pic_url
            if profile_pic_url != None:
                student_model.profile_pic = profile_pic_url
            user.save()
            messages.success(request, "Successfully Added Student")
            return HttpResponseRedirect("/add_student")

        except:
            messages.error(request, 'Failed to create Student')
            return HttpResponseRedirect("/add_student")


def add_subject(request):
    staffs  = CustomUser.objects.filter(user_type=2)
    courses = Courses.objects.all()
    return render(request, 'hod_template/add_subject_template.htm',{'staffs':staffs,'courses':courses})


def add_subject_save(request):
    if request.method != "POST":
        return HttpResponse("NOT ALLOWED HERE")
    else:
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get('course')
        staff_id = request.POST.get("staff")
        course = Courses.objects.get(id=course_id)
        staff = CustomUser.objects.get(id=staff_id)

        try:
            subject = Subjects(subjects_name=subject_name,course_id =course,staff_id=staff)
            subject.save()
            messages.success(request, "Successfully Added Subject")
            return HttpResponseRedirect("/add_subject")

        except:
            messages.error(request, 'Failed to create User')
            return HttpResponseRedirect("/add_subject")



def manage_staff(request):
    staffs = Staffs.objects.all()
    return render(request,'hod_template/manage_staff_template.htm',{'staffs':staffs})


def manage_student(request):
    students = Students.objects.all()
    return render(request, 'hod_template/manage_student_template.htm', {'students': students})


def manage_course(request):
    courses= Courses.objects.all()
    return render(request,'hod_template/manage_course_template.htm',{'courses':courses})


def manage_subject(request):
    subjects = Subjects.objects.all()
    return render(request, 'hod_template/manage_subject_template.htm', {'subjects': subjects})


def edit_staff(request,staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    return render(request,"hod_template/edit_staff_template.htm",{'staff':staff,"id":staff_id})


def edit_staff_save(request):
    if request.method != 'POST':
        return HttpResponse("Not allowed here")
    else:
        staff_id = request.POST.get("staff_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        address = request.POST.get("address")
        
        try:
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            staff_model = Staffs.objects.get(admin=staff_id)
            
            staff_model.address = address
            staff_model.save()
            
            messages.success(request,"SuccessFully Saved Changes")
            return HttpResponseRedirect("/edit_staff/"+staff_id)

        except:
            messages.error(request, 'Failed to Edit Staff')
            return HttpResponseRedirect("/edit_staff/"+staff_id)
        

def edit_student(request, student_id):
    students = Students.objects.get(admin=student_id)
    courses = Courses.objects.all()
    return render(request, "hod_template/edit_student_template.htm", {'students': students,'courses':courses,"id":student_id})


def edit_staff_save(request):
    if request.method != 'POST':
        return HttpResponse("Not allowed here")
    else:
        email = request.POST.get("email")
        student_id = request.POST.get("id")
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        address = request.POST.get("address")
        course_id = request.POST.get("course")
        gender = request.POST.get("gender")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        
        if request.FILES.get('profile_pic',False):
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None
        
        try:
            user = CustomUser.objects.get(id=student_id)
            user.email = email
            user.first_name = first_name
            user.username = username
            user.last_name = last_name
            user.save()
            
            student_model = Students.objects.get(admin=student_id)
            student_model.address = address
            student_model.gender = gender
            student_model.session_start_year = session_start
            student_model.session_end_year = session_end
            
            course = Courses.objects.get(id=course_id)
            student_model.course_id = course
            if profile_pic_url != None:
                student_model.profile_pic = profile_pic_url
            
            student_model.save()
            messages.success(request, "SuccessFully Saved Changes")
            return HttpResponseRedirect("/edit_student/"+student_id)

        except:
            messages.error(request, 'Failed to Edit Student')
            return HttpResponseRedirect("/edit_student/"+student_id)
        






def edit_subject(request,subject_id):
    subjects = Subjects.objects.get(id = subject_id)
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    return render(request,'hod_template/edit_subject_template.htm',{'subjects':subjects,'courses':courses,'staffs':staffs,'id':subject_id})

def edit_subject_save(request):
    if request.method != 'POST':
            return HttpResponse("<h2>Not allowed here</h2>")
    else:
        subject_name = request.POST.get("subject_name")
        subject_id = request.POST.get("id")
        course_id = request.POST.get("course")
        staff= request.POST.get("staff")
        
        try:
            subject_model  = Subjects.objects.get(id=subject_id)
            subject_model.subjects_name = subject_name
            course = Courses.objects.get(id=course_id)
            staff_model = CustomUser.objects.get(id=staff)
            subject_model.staff_id = staff_model
            subject_model.course_id = course
            subject_model.save()
            messages.success(request, "SuccessFully Saved Changes")
            return HttpResponseRedirect("/edit_subject/"+subject_id)

        except:
            messages.error(request, 'Failed to Edit Student')
            return HttpResponseRedirect("/edit_subject/"+subject_id)
        
            
        
        

def edit_course(request,course_id):
    courses = Courses.objects.get(id=course_id)
    return render(request,'hod_template/edit_course_template.htm',{'courses':courses,"id":course_id})


def edit_course_save(request):
    if request.method != 'POST':
            return HttpResponse("<h2>Not allowed here</h2>")
    else:
        course_name = request.POST.get("course")
        course_id = request.POST.get("id")
        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name
            course.save()
            messages.success(request, "SuccessFully Saved Changes")
            return HttpResponseRedirect("/edit_course/"+course_id)

        except:
            messages.error(request, 'Failed to Edit Course')
            return HttpResponseRedirect("/edit_course/"+course_id)
        
        
