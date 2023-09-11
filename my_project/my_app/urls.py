from django.urls import path , include
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add_student',views.add_student,name="add-student"),
    path('student_list',views.list_student,name="student-list"),
    path('show_student/<student_id>',views.show_student,name="show-student"),
    path('update_student/<student_id>',views.update_student,name="update-student"),
    path('delete_student/<student_id>',views.delete_student,name="delete-student"),
    path('show_departments',views.show_Dep,name="show-dep"),
    path('search_student',views.search_student,name="search-student")

]