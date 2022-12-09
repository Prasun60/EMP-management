from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import emp,Testimonial

# Create your views here.
def emphome(request):
    emps=emp.objects.all()
    return render(request,"emp/home.html",{'emps':emps})

def addemp(request):
    if request.method=="POST":
        print("data is coming")

        #data fetch
        empname=request.POST.get("empname")
        empid=request.POST.get("empid")
        empphone=request.POST.get("empphone")
        empaddress=request.POST.get("empaddress")
        empworking=request.POST.get("empworking")
        empdept=request.POST.get("empdept")

        #create model object and set the data

        e=emp()
        e.name=empname
        e.empid=empid
        e.phone=empphone
        e.address=empaddress
        e.dept=empdept
        if empworking is None:
            e.working=False
        else:
            e.working=True
        e.save()


        return redirect("/emp/home/")
    return render(request,"emp/addemp.html",{})

def deleteemp(request,empid):
    e=emp.objects.get(pk=empid)
    e.delete()
    return redirect("/emp/home/")
def updateemp(request,empid):
    e=emp.objects.get(pk=empid)
    return render(request,"emp/update.html",{"emp":e})
def do_update_emp(request,emp_id):
    if request.method=='POST':
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=emp.objects.get(pk=emp_id)
        e.name=emp_name
        e.empid=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.dept=emp_department  

        if emp_working is None:
            e.working=False
        else:
            e.working=True

        e.save()
    return redirect("/emp/home/")

def testimonials(request):
    testi=Testimonial.objects.all()

    return render(request, "emp/testimonials.html",{
        'testi':testi
    })