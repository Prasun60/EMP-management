from django.http import HttpResponse
from django.shortcuts import render
def test(request):
    print("index file fired")
    #return HttpResponse("<h1>index page done</h1>")
    return render(request,"index.html",{})

def home(request):
    print("index file fired")
    if request.method=="POST":
        check = request.POST.get('check')
        print(check)
    isactive=True
    name="prasun"
    programs=[
        "wap to check odd even",
        "eap to print nth fibonacci",
        "wap to find sum of n digits"
    ]
    student={
        'student_name':"Rahul",
        'rollno':"2021bcs_055",
        'college':"abv iiitm",
    }
    #return HttpResponse("<h1>index page done</h1>")
    data={
        'isactive':isactive,
        'name':name,
        'programs':programs,
        'student':student
    }
    return render(request,"home.html",data)

def services(request):
    print("index file fired")
    #return HttpResponse("<h1>index page done</h1>")
    return render(request,"services.html",{})
