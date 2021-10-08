from django.shortcuts import render
from django.http import HttpResponse
from admissions.models import students
from admissions.forms import  studentsModelForm
from admissions.forms import VendorForm
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from admissions.models import Teacher
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required,permission_required


# Create your views here.

#function based views

@login_required
def homepage(request):
    return render(request,'index.html')

def logoutUser(request):
    return render(request,'logout.html')

@login_required
def addAdmission(request):
    #retrieve values from hidden variables

    form =  studentsModelForm
    studentsform = {'form':form}
    if request.method=='POST':
        form=studentsModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)


    return render(request,"admissionstemp/admission.html",studentsform)


@login_required
def AdmissionsReport(request):
    #get all the records from the table
    result = students.objects.all(); #select * from students
    #store it in dictionary students
    student = {"allstudents":result}
    return render(request,'admissionstemp/adreport.html',student)


@login_required
@permission_required('admissions.delete_student')
def deleteStudent(request,id):
    s=students.objects.get(id=id) #select * from admissions_student where id=idvalue
    s.delete()
    return AdmissionsReport(request)

@login_required
@permission_required('admissions.change_student') #add delete change view
def updateStudent(request,id):
    s=students.objects.get(id=id)
    form=studentsModelForm(instance=s)
    dict={'form':form}

    if request.method=='POST':
        form=studentsModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return homepage(request)
    return render(request,'admissionstemp/update-admission.html',dict)


@login_required
def addVendor(request):
    form =  VendorForm
    vform = {'form':form}
    if request.method=='POST':
        form=VendorForm(request.POST)
        if form.is_valid():
            n=form.cleaned_data['name']
            a=form.cleaned_data['address']
            c=form.cleaned_data['contact']
            i=form.cleaned_data['item']

            response = render(request,'index.html')
            response.set_cookie("name",n)
            response.set_cookie("address",a)
            response.set_cookie("contact",c)
            response.set_cookie("tem",i)

        return response
    return render(request,"admissionstemp/add-vendor.html",vform)



#class based views
class FirstClassBasedView(View):
    def get(self,request):
        return HttpResponse("<h1>Hello.... This is my first class based view</h1>")


class TeacherRead(ListView):
    model = Teacher


class GetTeacher(DetailView):
    model = Teacher


class AddTeacher(CreateView):
    model = Teacher
    fields = ('name','exp','subject','contact')


class UpdateTeacher(UpdateView):
    model = Teacher
    fields = ('name','contact')


class DeleteTeacher(DeleteView):
    model = Teacher
    success_url =  reverse_lazy('listteachers')
