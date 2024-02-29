from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *

# Create your views here.
def UserReg(request):
    ds=District.objects.all()
    if request.method=="POST" and request.FILES:
        locid=request.POST.get('sel_loc')
        loc=Location.objects.get(id=locid)
        UserRegistration.objects.create(user_name=request.POST.get('txt_uname'),
            user_contact=request.POST.get('txt_contact'),user_email=request.POST.get('txt_email'),
            user_address=request.POST.get('txt_address'),user_photo=request.FILES.get('fil_img'),
             user_proof=request.FILES.get('fil_img'),user_pswrd=request.POST.get('txt_password'),user_location=loc)
        
        return render(request,"Guest/UserReg.html",{'DS':ds})   
    else:
        return render(request,"Guest/UserReg.html",{'DS':ds})   

        
    

def Ajaxlocation(request):
    plc=request.GET.get('PLC')
    loc=Location.objects.filter(place=plc)
    return render(request,"Guest/AjaxLocation.html",{'LOC':loc})       


def userlogin(request):
    if request.method=="POST":
        Email=request.POST.get('txt_email')
        Pwd=request.POST.get('txt_pswd')
        userlog=UserRegistration.objects.filter(user_email=Email,user_pswrd=Pwd).count()
        workerlog= Worker.objects.filter(worker_email=Email,worker_password=Pwd,worker_vstatus=1).count()
        landloadlog=Landload.objects.filter(landload_email=Email,landload_password=Pwd,landload_vstatus=1).count()
        adminlog=AdminReg.objects.filter(admin_email=Email,admin_password=Pwd).count()
        if userlog > 0:
            usr=UserRegistration.objects.get(user_email=Email,user_pswrd=Pwd)
            request.session['uid']=usr.id
            return redirect('User:userhome')
        elif workerlog> 0:
            worker=Worker.objects.get(worker_email=Email,worker_password=Pwd,worker_vstatus=1)
            request.session['wid']=worker.id
            return redirect('Worker:workerhome')
        elif landloadlog> 0:
            landload=Landload.objects.get(landload_email=Email,landload_password=Pwd,landload_vstatus=1)
            request.session['lid']=landload.id
            return redirect('landload:landloadhome')
        elif adminlog> 0 :
            admin=AdminReg.objects.get(admin_email=Email,admin_password=Pwd)
            request.session['aid']=admin.id
            return redirect('webadmin:adminhome')

        else:   
             error="Invalid Credentials!!"
             return render(request,"Guest/Userlog.html",{'ER':error})
    else:
        return render(request,"Guest/Userlog.html")


def worker(request):
    wtpe=Workertype.objects.all()
    ds=District.objects.all()
    if request.method=="POST" and request.FILES:
        locid=request.POST.get('sel_loc')
        loc=Location.objects.get(id=locid)
        Workertypeid=request.POST.get('sel_worker')
        wtype=Workertype.objects.get(id=Workertypeid)
        Worker.objects.create(worker_name=request.POST.get('txt_name'),
            worker_contact=request.POST.get('txt_contact'),worker_email=request.POST.get('txt_email'),
            worker_address=request.POST.get('txt_address'),worker_photo=request.FILES.get('fil_img'),
            worker_proof=request.FILES.get('fil_img'),worker_password=request.POST.get('txt_password'),location_id=loc,worker_typeid=wtype)
        
        return render(request,"Guest/Worker.html",{'DS':ds,'WT':wtpe})   
    else:
        return render(request,"Guest/Worker.html",{'DS':ds,'WT':wtpe})  

def Ajaxplace(request):
    dis=District.objects.get(id=request.GET.get('DIST'))
    pl=Place.objects.filter(district=dis)
    return render(request,"Admin/Ajaxplace.html",{'pl':pl})   

def landload(request):
    ds=District.objects.all()
    if request.method=="POST" and request.FILES:
        locid=request.POST.get('sel_loc')
        loc=Location.objects.get(id=locid)
        Landload.objects.create(landload_name=request.POST.get('txt_name'),
            landload_contact=request.POST.get('txt_contact'),landload_email=request.POST.get('txt_email'),
            landload_address=request.POST.get('txt_address'),landload_photo=request.FILES.get('fil_img'),
            landload_proof=request.FILES.get('fil_img'),landload_password=request.POST.get('txt_password'),location_id=loc)
        
        return render(request,"Guest/Landload.html",{'DS':ds})   
    else:
        return render(request,"Guest/Landload.html",{'DS':ds})
    
def home(request):
    return render(request,"Guest/Home.html")    
    
   

