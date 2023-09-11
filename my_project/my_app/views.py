from django.shortcuts import render , redirect
from .models import Students
from .models import Department
from .forms import StudentForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,'index.html')


def add_student(request):
        submitted = False
        if request.method == "POST":
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('add_student?submitted=True')
        else:
            form = StudentForm
            if 'submitted' in request.GET:
                submitted = True

        return render(request,'add_students.html',{'form':form , 'submitted':submitted})


def list_student(request):
     student_list = Students.objects.all()
     return render(request,'student_list.html',{'student_list':student_list})        


def show_student(request,student_id):
     student = Students.objects.get(pk=student_id)
     return render(request,'show_students.html',{'students': student})


def update_student(request,student_id):
     student=Students.objects.get(pk=student_id)
     form = StudentForm(request.POST or None , instance=student)
     if form.is_valid():
          form.save()
          return redirect('student-list')
     return render(request,'update_students.html',{'student':student,'form':form})


def delete_student(request,student_id):
     student = Students.objects.get(pk=student_id)
     student.delete()
     return redirect('student-list')


def show_Dep(request):
     deps=Department.objects.all()
     return render(request,'show_departments.html',{'departments':deps})


def search_student(request):
    if request.method == "POST":
        searched=request.POST['searched']
        #name = Students.f_name + Students.l_name
        student = Students.objects.filter(index__contains=searched) 
        

        return render(request,'search_student.html',{'searched':searched , 'student':student})
    
    else:
        return render(request,'search_student.html',{})