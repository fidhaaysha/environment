from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'students/login.html')
    
def viewmarks(request):
    return render(request,'students/viewmarks.html')

def viewattendance(request):
    return render(request,'students/viewattendances.html')