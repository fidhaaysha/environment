from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'school_admin/login.html')
    
def viewstudents(request):
    return render(request,'school_admin/viewstudents.html')

def viewteachers(request):
    return render(request,'school_admin/viewteachers.html')