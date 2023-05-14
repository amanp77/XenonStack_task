from codecs import getencoder
import http
from django.shortcuts import render,HttpResponse
from .models import student1,faculty1,subject1,guardian1,classroom1


# Create your views here.
def home(request):
    return render(request,'home.html')

def student(request):
    st=student1.objects.all() # Collect all records from table 
    return render(request,'student.html',{'st':st})

def faculty(request):
    st=faculty1.objects.all() # Collect all records from table 
    return render(request,'faculty.html',{'st':st})

def subject(request):
    st=subject1.objects.all() # Collect all records from table 
    return render(request,'subject.html',{'st':st})

def guardian(request):
    st=guardian1.objects.all() # Collect all records from table 
    return render(request,'guardian.html',{'st':st})

def classroom(request):
    st=classroom1.objects.all() # Collect all records from table 
    return render(request,'classroom.html',{'st':st})

def guardianform(request):
    if request.method == "POST":
        guardian_id = request.POST.get('guardian_id')
        guardian_name = request.POST.get('guardian_name')
        gender = request.POST.get('gender') 
        contact = request.POST.get('contact') 
        g1 = guardian1(guardian_id = guardian_id , guardian_name = guardian_name , 
                             gender = gender , contact = contact )

        g1.save()
    return render(request,'guardianform.html')

def classroomform(request):
    if request.method == "POST":
        standard = request.POST.get('standard')
        fid = request.POST.get('fid')
        CR = request.POST.get('CR') 
        c1 = classroom1(standard = standard , fid = fid , 
                             CR = CR )

        c1.save()
    return render(request,'classroomform.html')

def facultyform(request):
    if request.method == "POST":
        fid = request.POST.get('fid')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        doj = request.POST.get('doj')
        sub_id = request.POST.get('sub_id')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        M_no = request.POST.get('M_no') 
        f1 = faculty1(fid = fid , fname = fname , 
                             lname = lname, doj = doj , sub_id = sub_id , 
                              gender = gender, address = address , M_no = M_no )

        f1.save()
    return render(request,'facultyform.html')
    
def studentform(request):
    if request.method == "POST":
        prn_no = request.POST.get('prn_no')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        standard = request.POST.get('standard')
        guardian_id = request.POST.get('guardian_id') 

        s1 = student1(prn_no = prn_no , fname = fname , 
                             lname = lname, dob = dob , address = address , 
                              gender = gender, standard = standard , guardian_id = guardian_id )

        s1.save()
    return render(request,'studentform.html')


def subjectform(request):
    if request.method == "POST":
        sub_id = request.POST.get('sub_id')
        sub_name = request.POST.get('sub_name')

        
        sf1 = subject1(sub_id = sub_id , sub_name = sub_name)
        sf1.save()
    return render(request,'subjectform.html')


