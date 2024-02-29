from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *

# Create your views here.

def district(request):
    if 'aid' in request.session:
        if request.method=="POST":
            District.objects.create(district_name=request.POST.get('txt_district'))
            dis=District.objects.all()
            return render(request,"Admin/District.html",{'DIS':dis})
        else:
            dis=District.objects.all()
            return render(request,"Admin/District.html",{'DIS':dis}) 
    else:  
        return redirect('guest:Userlogin')
     

def workertype(request):
    if 'aid' in request.session:
        if request.method=="POST":
            Workertype.objects.create(workertype_name=request.POST.get('txt_workertype')) 
            wtype=Workertype.objects.all()
            return render(request,"Admin/Workertype.html",{'WTYPE':wtype})
        else:
            wtype=Workertype.objects.all()
            return render(request,"Admin/Workertype.html",{'WTYPE':wtype})
    else:  
        return redirect('guest:Userlogin')

def del_dis(request,did):
    District.objects.get(id=did).delete()
    return redirect('webadmin:district')

def up_dis(request,eid):
    seldis=District.objects.get(id=eid)
    if request.method=="POST":
        seldis.district_name=request.POST.get('txt_district')
        seldis.save()
        return redirect('webadmin:district')
    else:
        return render(request,"Admin/EditDistrict.html",{'SD':seldis})                

def plc(request):
    if 'aid' in request.session:
        dis =District.objects.all()
        plc=Place.objects.all()
        if request.method=="POST":
            disid=request.POST.get('sel_dis')
            dist=District.objects.get(id=disid)
            Place.objects.create(place_name=request.POST.get('txt_plc'),district=dist)
            return render(request,"Admin/Place.html",{'DS':dis,'PLC':plc})          
        else:
            return render(request,"Admin/Place.html",{'DS':dis,'PLC':plc})  
    else:  
        return redirect('guest:Userlogin')        
 
def del_plc(request,pid):
    Place.objects.get(id=pid).delete()
    return redirect('webadmin:place')         

def loc(request):
    if 'aid' in request.session:
        loc =Location.objects.all()
        dis =District.objects.all()
        if request.method=="POST":
            plcid=request.POST.get('sel_plc')
            plc=Place.objects.get(id=plcid)
            Location.objects.create(location_name=request.POST.get('txt_loc'),place=plc)
            return render(request,"Admin/Location.html",{'DS':dis,'LOC':loc})
        else:
            return render(request,"Admin/Location.html",{'DS':dis,'LOC':loc})
    else:  
        return redirect('guest:Userlogin')
    
def del_loc(request,lid):
    Location.objects.get(id=lid).delete()
    return redirect('webadmin:Location')     


def Ajaxplace(request):
    if 'aid' in request.session:
        dis=District.objects.get(id=request.GET.get('DIST'))
        pl=Place.objects.filter(district=dis)
        return render(request,"Admin/Ajaxplace.html",{'pl':pl})   
    else:  
        return redirect('guest:Userlogin')

def del_wtype(request,wid):
    Workertype.objects.get(id=wid).delete()
    return redirect('webadmin:workertype')    

def workerverification(request):
    if 'aid' in request.session:
        wrkr=Worker.objects.filter(worker_vstatus=0)
        return render(request,"Admin/Workerverification.html",{'WRKR':wrkr})
    else:  
        return redirect('guest:Userlogin')

def acceptworker(request):
    if 'aid' in request.session:
        wrkr=Worker.objects.filter(worker_vstatus=1)
        return render(request,"Admin/WorkerAccept.html",{'WRKR':wrkr})
    else:  
        return redirect('guest:Userlogin')

def rejectworker(request):
    if 'aid' in request.session:
        wrkr=Worker.objects.filter(worker_vstatus=2)
        return render(request,"Admin/WorkerReject.html",{'WRKR':wrkr})
    else:  
        return redirect('guest:Userlogin')



def accept_worker(request,wacid):
    accept=Worker.objects.get(id=wacid)
    accept.worker_vstatus=1
    accept.save()
    return redirect('webadmin:acceptworker')

def reject_worker(request,wrjid):
    reject=Worker.objects.get(id=wrjid)
    reject.worker_vstatus=2
    reject.save()
    return redirect('webadmin:rejectworker')

def landloadverification(request):
    if 'aid' in request.session:
        land=Landload.objects.filter(landload_vstatus=0)
        return render(request,"Admin/Landloadverification.html",{'LAND':land})
    else:  
        return redirect('guest:Userlogin')

def acceptlandload(request):
    if 'aid' in request.session:
        land=Landload.objects.filter(landload_vstatus=1)
        return render(request,"Admin/LandloadAccept.html",{'LAND':land})
    else:  
        return redirect('guest:Userlogin')

def rejectlandload(request):
    if 'aid' in request.session:
        land=Landload.objects.filter(landload_vstatus=2)
        return render(request,"Admin/LandloadReject.html",{'LAND':land})
    else:  
        return redirect('guest:Userlogin')

def accept_land(request,lacid):
    accept=Landload.objects.get(id=lacid)
    accept.landload_vstatus=1
    accept.save()
    return redirect('webadmin:acceptland')

def reject_land(request,lrjid):
    reject=Landload.objects.get(id=lrjid)
    reject.landload_vstatus=2
    reject.save()
    
    return redirect('webadmin:rejectland')

def adminhome(request):
    if 'aid' in request.session:
        admin=AdminReg.objects.get(id=request.session['aid'])
        return render(request,"Admin/AdminHome.html",{'ADMIN':admin})
    else:  
        return redirect('guest:Userlogin')

def viewuser(request):
    if 'aid' in request.session:
        user=UserRegistration.objects.filter()
        return render(request,"Admin/ViewUser.html",{'USER':user})
    else:  
        return redirect('guest:Userlogin')

def complaints(request):
    if 'aid' in request.session:
        usr=Complaint.objects.filter(user_id__gt=0)
        wrkr=Complaint.objects.filter(worker_id__gt=0)
        landload=Complaint.objects.filter(Landload_id__gt=0)
        return render(request,"Admin/ViewComplaints.html",{'USR':usr,'WRKR':wrkr,'LAND':landload})
    else:  
        return redirect('guest:Userlogin')


def reply(request,rid):
    cmp=Complaint.objects.get(id=rid)
    if request.method=="POST":
        cmp.Complaint_reply=request.POST.get('txt_reply')  
        cmp.Complaint_status=1
        cmp.save() 
        return redirect('webadmin:complaints')
    else:
        return render(request,"Admin/Reply.html")
    

def feedback(request):
    if 'aid' in request.session:
        usr=Feedback.objects.filter(user_id__gt=0)
        wrkr=Feedback.objects.filter(worker_id__gt=0)
        landload=Feedback.objects.filter(Landload_id__gt=0)
        return render(request,"Admin/ViewFeedback.html",{'USR':usr,'WRKR':wrkr,'LAND':landload})   
    else:  
        return redirect('guest:Userlogin')



def complainttype(request):
    if 'aid' in request.session:
        if request.method=="POST":
            Complainttype.objects.create(complainttype_name=request.POST.get('txt_complainttype'))    
            ctype=Complainttype.objects.all()
            return render(request,"Admin/Complainttype.html",{'CTYPE':ctype})
        else:
            ctype=Complainttype.objects.all()
            return render(request,"Admin/Complainttype.html",{'CTYPE':ctype})
    else:
        return redirect('guest:Userlogin')
    
def delcom(request,cid):
    Complainttype.objects.get(id=cid).delete()
    return redirect('webadmin:comtype')



        



    