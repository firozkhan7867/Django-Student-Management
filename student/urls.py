
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from student import settings
from student_manage import views,HodView

urlpatterns = [
    path('demo',views.show),
    path('admin/', admin.site.urls),
    path('',views.ShowLoginPage),
    path('doLogin', views.doLogin, name="do_login"),
    path('get_user_details',views.GetUserDetails),
    path('logout_user',views.logout_user,name="logout"),
    path('admin_home',HodView.admin_home,name="admin_home"),
    path('add_staff', HodView.add_staff, name="add_staff"),
    path('add_staff_save', HodView.add_staff_save, name="add_staff_save"),
    path('add_course', HodView.add_course, name="add_course"),
    path('add_course_save', HodView.add_course_save, name="add_course_save"),
    path('add_student', HodView.add_student, name="add_student"),
    path('add_student_save', HodView.add_student_save, name="add_student_save"),
    path('add_subject', HodView.add_subject, name="add_subject"),
    path('add_subject_save', HodView.add_subject_save, name="add_subject_save"),
    path('manage_staff', HodView.manage_staff, name="manage_staff"),
    path('manage_student', HodView.manage_student, name="manage_student"),
    path('manage_course', HodView.manage_course, name="manage_course"),
    path('manage_subject', HodView.manage_subject, name="manage_subject"),
    path('edit_staff/<str:staff_id>', HodView.edit_staff,name="edit_staff"),
    path('edit_staff_save', HodView.edit_staff_save, name="edit_staff_save"),
    path('edit_student/<str:student_id>',
         HodView.edit_student, name="edit_student"),
    path('edit_student_save', HodView.edit_staff_save, name="edit_staff_save"),
    path('edit_subject/<str:subject_id>',
         HodView.edit_subject, name="edit_subject"),
    path('edit_course/<str:course_id>', HodView.edit_course, name="edit_course"),
    path('edit_subject_save', HodView.edit_subject_save, name="edit_subject_save"),
    path('edit_course_save', HodView.edit_course_save, name="edit_course_save"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
