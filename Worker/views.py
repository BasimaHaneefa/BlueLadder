from django.shortcuts import render,redirect
from Guest.models import *
from Worker.models import Workbooking,WorkerBooking,Work
from User.models import *

# Create your views here.

def whome(request):
    if 'wid' in request.session:
        wr=Worker.objects.get(id=request.session['wid'])
        return render(request,"Worker/WorkerHome.html",{'W':wr})
    else:
        return redirect('guest:Userlogin')

def profile(request):
    if 'wid' in request.session:
        prf=Worker.objects.get(id=request.session['wid'])
        return render(request,"Worker/MyProfile.html",{'P':prf})
    else:
        return redirect('guest:Userlogin')

def editprf(request,eid):
    edit=Worker.objects.get(id=eid)
    if request.method=="POST":
        edit.worker_name=request.POST.get('txt_name')
        edit.worker_contact=request.POST.get('txt_contact')
        edit.worker_email=request.POST.get('txt_email')
        edit.worker_address=request.POST.get('txt_address')
        edit.save()
        return redirect('Worker:myprofile')
    else:
        return render(request,"Worker/EditProfile.html",{'EDT':edit})

def cpswrd(request,cid):
    change=Worker.objects.get(id=cid)
    if request.method=="POST":
        pwd=change.worker_password
        crrnt=request.POST.get('txt_pswd')
        if pwd == crrnt:
            change=Worker.objects.get(id=cid)
            new=request.POST.get('txt_npswd')
            change.worker_password=new
            change.save()
            return redirect('guest:Userlogin')
        else:
            error="Password Incorrect!!"
            return render(request,"User/ChangePwd.html",{'ER':error})
    else:
        return render(request,"User/ChangePwd.html")
    

def workdetails(request):
    if 'wid' in request.session:
        wrkr=Worker.objects.get(id=request.session['wid'])
        work=Work.objects.filter(worker_id=wrkr)
        if request.method=="POST" and request.FILES:
            Work.objects.create(work_details=request.POST.get("txt_details"),work_image=request.FILES.get("fil_img"),
                                work_amount=request.POST.get("txt_rate"),worker_id=wrkr)
            return render(request,"Worker/WorkDetails.html",{'WR':work})   
        else: 
            return render(request,"Worker/WorkDetails.html",{'WR':work})   
    else:
        return redirect('guest:Userlogin')
    
def del_work(request,wid):
    Work.objects.get(id=wid).delete()
    return redirect('Worker:workdetails') 

def wrkrcomp(request):
    if 'wid' in request.session:
        wrkr=Worker.objects.get(id=request.session['wid'])
        com=Complainttype.objects.all()
        cmp=Complaint.objects.filter(worker_id=wrkr)
        if request.method=="POST":
            comid=request.POST.get("sel_coml")
            cmptype=Complainttype.objects.get(id=comid)
            Complaint.objects.create(Complaint_content=request.POST.get('txt_content'),worker_id=wrkr,Complainttype_id=cmptype)   
            return render(request,"Worker/WorkerComplaints.html",{'COM':com,'CMP':cmp})
        else:
            return render(request,"Worker/WorkerComplaints.html",{'COM':com,'CMP':cmp})
    else:
        return redirect('guest:Userlogin')
    
def del_com(request,wid):
    Complaint.objects.get(id=wid).delete()
    return redirect('Worker:wrkrcom')
            

def feedback(request):
    if 'wid' in request.session:
        wrkr=Worker.objects.get(id=request.session['wid'])
        worker=Feedback.objects.filter(worker_id=wrkr)
        if request.method=="POST":
            Feedback.objects.create(feedback_description=request.POST.get('txt_feedback'),worker_id=wrkr)       
            return render(request,"Worker/Feedback.html",{'WORKER':worker}) 
        else:
            return render(request,"Worker/Feedback.html",{'WORKER':worker})
    else:
        return redirect('guest:Userlogin')
    
def del_feed(request,wid):
    Feedback.objects.get(id=wid).delete()
    return redirect('Worker:feedback')     

def Mybookings(request):
    if 'wid' in request.session:
        worker=Worker.objects.get(id=request.session['wid'])
        bookings=Workbooking.objects.filter(work_id__worker_id=worker,workbooking_status=0)
        return render(request,"Worker/ViewMyBookings.html",{'Bookings':bookings}) 
    else:
        return redirect('guest:Userlogin')

def Accept(request,acid):
    accept=Workbooking.objects.get(id=acid)
    accept.workbooking_status=1
    accept.save()
    return redirect('Worker:Mybookings')

def Reject(request,reid):
    reject=Workbooking.objects.get(id=reid)
    reject.workbooking_status=2
    reject.save()
    return redirect('Worker:Mybookings')

def Worker_bookings(request):
    if 'wid' in request.session:
        worker=Worker.objects.get(id=request.session['wid'])
        bookings=WorkerBooking.objects.filter(worker_id=worker,w_bstatus=0)
        return render(request,"Worker/ViewWorkerBookings.html",{'BOOKINGS':bookings}) 
    else:
        return redirect('guest:Userlogin')

def Accept_worker(request,aid):
    accept=WorkerBooking.objects.get(id=aid)
    accept.w_bstatus=1
    accept.save()
    return redirect('Worker:workerbooking')

def Reject_worker(request,rid):
    reject=WorkerBooking.objects.get(id=rid)
    reject.w_bstatus=2
    reject.save()
    return redirect('Worker:workerbooking')

def Accepted_Workbookings(request):
    if 'wid' in request.session:
        worker=Worker.objects.get(id=request.session['wid'])
        bookings=Workbooking.objects.filter(work_id__worker_id=worker,workbooking_status=1)
        return render(request,"Worker/ViewAcceptedWorkBookings.html",{'Bookings':bookings}) 
    else:
        return redirect('guest:Userlogin')

def AcceptedWorker_bookings(request):
    if 'wid' in request.session:
        worker=Worker.objects.get(id=request.session['wid'])
        bookings=WorkerBooking.objects.filter(worker_id=worker,w_bstatus=1)
        return render(request,"Worker/ViewAcceptedWorkerBookings.html",{'BOOKINGS':bookings})
    else:
        return redirect('guest:Userlogin')
      







