from django.urls import path

from admissions.views import addAdmission
from admissions.views import AdmissionsReport
from admissions.views import addVendor
from admissions.views import deleteStudent
from admissions.views import updateStudent
from admissions.views import FirstClassBasedView
from admissions.views import TeacherRead
from admissions.views import GetTeacher
from admissions.views import AddTeacher
from admissions.views import UpdateTeacher
from admissions.views import DeleteTeacher
from django.contrib.auth.decorators import login_required



urlpatterns = [

    path('newadd/',addAdmission),
    path('addrep/',AdmissionsReport),
    path('newvendor/',addVendor),
    path('delete/<int:id>',deleteStudent),
    path('update/<int:id>',updateStudent),
    path('firstcbv/',login_required(FirstClassBasedView.as_view())),
    path('teacherslist/',login_required(TeacherRead.as_view()),name='listteacher'),
    path('getteacherdetails/<int:pk>/',login_required(GetTeacher.as_view()),name='getteacherinfo'),
    path('insertteacher/',login_required(AddTeacher.as_view())),
    path('updateteacher/<int:pk>/',login_required(UpdateTeacher.as_view())),
    path('deleteteacher/<int:pk>/',login_required(DeleteTeacher.as_view())),
]
