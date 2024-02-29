from django.shortcuts import render,redirect
from User.models import *
from Guest.models import UserRegistration,Worker
from Admin.models import *
from Landload.models import Plot,Plotbooking
from Worker.models import Work,Workbooking,WorkerBooking

# Create your views here.

def uhome(request):
    if 'uid' in request.session:
        us=UserRegistration.objects.get(id=request.session['uid'])
        return render(request,"User/UserHome.html",{'U':us})
    else:
        return redirect('guest:Userlogin')


def profile(request):
    if 'uid' in request.session:
        prf=UserRegistration.objects.get(id=request.session['uid'])
        return render(request,"User/MyProfile.html",{'PF':prf})
    else:
        return redirect('guest:Userlogin')


def editprf(request,eid):
    edit=UserRegistration.objects.get(id=eid)
    if request.method=="POST":
        edit.user_name=request.POST.get('txt_name')
        edit.user_contact=request.POST.get('txt_contact')
        edit.user_email=request.POST.get('txt_email')
        edit.user_address=request.POST.get('txt_address')
        edit.save()
        return redirect('User:myprofile')
    else:
        return render(request,"User/EditProfile.html",{'EDT':edit})

def cpswrd(request,cid):
    change=UserRegistration.objects.get(id=cid)
    if request.method=="POST":
        pwd=change.user_pswrd
        crrnt=request.POST.get('txt_pswd')
        if pwd == crrnt:
            change=UserRegistration.objects.get(id=cid)
            new=request.POST.get('txt_npswd')
            change.user_pswrd=new
            change.save()
            return redirect('guest:Userlogin')
        else:
            error="Password Incorrect!!"
            return render(request,"User/ChangePwd.html",{'ER':error})
    else:
        return render(request,"User/ChangePwd.html")
    


def Usrcomplaint(request):
    if 'uid' in request.session:
        com=Complainttype.objects.all()
        us=UserRegistration.objects.get(id=request.session['uid'])
        cmp=Complaint.objects.filter(user_id=us)
        if request.method=="POST":
            comid=request.POST.get("sel_coml")
            cmptype=Complainttype.objects.get(id=comid)
            Complaint.objects.create(Complaint_content=request.POST.get('txt_content'),user_id=us,Complainttype_id=cmptype)   
            return render(request,"User/UserComplaint.html",{'COM':com,'CMP':cmp})
        else:
            return render(request,"User/UserComplaint.html",{'COM':com,'CMP':cmp})
    else:
        return redirect('guest:Userlogin')
        

def del_com(request,uid):
    Complaint.objects.get(id=uid).delete()
    return redirect('User:complaint')
        

def feedback(request):
    if 'uid' in request.session:
        feedback=Feedback.objects.all()
        us=UserRegistration.objects.get(id=request.session['uid'])
        user=Feedback.objects.filter(user_id=us)
        if request.method=="POST":
            Feedback.objects.create(feedback_description=request.POST.get('txt_feedback'),user_id=us)
            return render(request,"User/Feedback.html",{'FEED':feedback,'USER':user})    
        else:
            return render(request,"User/Feedback.html",{'FEED':feedback,'USER':user})

    else:
        return redirect('guest:Userlogin')
        
def del_feed(request,uid):
    Feedback.objects.get(id=uid).delete()
    return redirect('User:Feedback') 

def search(request):
    if 'uid' in request.session:
        dis=District.objects.all()
        worker=Worker.objects.filter(worker_vstatus=1)
        return render(request,"User/SearchWorker.html",{'DS':dis,'WORKER':worker})  
    else:
        return redirect('guest:Userlogin')
         


def get_worker(request):
    if 'uid' in request.session:
        if request.GET.get('lid')!="":  
            loc=Location.objects.get(id=request.GET.get('lid'))
            wrkr=Worker.objects.filter(location_id=loc,worker_vstatus=1)
            return render(request,"User/GetWorker.html",{'WRKR':wrkr})
        elif request.GET.get('pid')!="":
            plc=Place.objects.get(id=request.GET.get('pid'))
            wrkr=Worker.objects.filter(location_id__place=plc,worker_vstatus=1)
            return render(request,"User/GetWorker.html",{'WRKR':wrkr})
        else:
            dis=District.objects.get(id=request.GET.get('did'))
            wrkr=Worker.objects.filter(location_id__place__district=dis,worker_vstatus=1)
            return render(request,"User/GetWorker.html",{'WRKR':wrkr})
    else:
        return redirect('guest:Userlogin')
             
                    


def land_search(request):
    if 'uid' in request.session:
        dis=District.objects.all()
        land=Landload.objects.filter(landload_vstatus=1)
        return render(request,"User/SearchLandload.html",{'DS':dis,'LAND':land})
    else:
        return redirect('guest:Userlogin')


def get_land(request):
    if 'uid' in request.session:
        if request.GET.get('lid')!="":  
            loc=Location.objects.get(id=request.GET.get('lid'))
            landlord=Landload.objects.filter(location_id=loc,landload_vstatus=1)
            return render(request,"User/GetLandload.html",{'LAND':landlord})
        elif request.GET.get('pid')!="":
            plc=Place.objects.get(id=request.GET.get('pid'))
            landlord=Landload.objects.filter(location_id__place=plc,landload_vstatus=1)
            return render(request,"User/GetLandload.html",{'LAND':landlord})
        else:
            dis=District.objects.get(id=request.GET.get('did'))
            landlord=Landload.objects.filter(location_id__place__district=dis,landload_vstatus=1)
            return render(request,"User/GetLandload.html",{'LAND':landlord})
        
    else:
        return redirect('guest:Userlogin')
    

def view_plots(request,pid):
    land=Landload.objects.get(id=pid)
    plot=Plot.objects.filter(Landload_id=land)
    return render(request,"User/ViewPlots.html",{'PLOT':plot})

def plot_booking(request,bid):
    plot=Plot.objects.get(id=bid)
    usr=UserRegistration.objects.get(id=request.session['uid'])
    if request.method=="POST":
        Plotbooking.objects.create(user_id=usr,plot_id=plot)
        return redirect('User:Plotbookings')
    else:
        return render(request,"User/PlotBooking.html",{'PLOTS':plot})
    
def view_works(request,wid):
    worker=Worker.objects.get(id=wid) 
    work=Work.objects.filter(worker_id=worker) 
    return render(request,"User/ViewWorks.html",{'WRKR':work})


def work_booking(request,wbid):
    work=Work.objects.get(id=wbid)
    usr=UserRegistration.objects.get(id=request.session['uid'])
    if request.method=="POST":
        Workbooking.objects.create(user_id=usr,work_id=work,workbooking_fordate=request.POST.get('fordate'))
        return redirect('User:Workbookings')
    else:
        return render(request,"User/WorkBooking.html",{'WORK':work})

    
def worker_booking(request,wrid):
    worker=Worker.objects.get(id=wrid)
    usr=UserRegistration.objects.get(id=request.session['uid'])
    if request.method=="POST":
        WorkerBooking.objects.create(user_id=usr,worker_id=worker,wbooking_fordate=request.POST.get('fordate'),
                                     w_details=request.POST.get('txtdetails'))
        return redirect('User:Worker_bookings')
    else:
        return render(request,"User/WorkerBooking.html",{'WORKER':worker})

def Workbookings(request):
    if 'uid' in request.session:
        # worker=Worker.objects.get(id=request.session['wid'])
        # bookings=Workbooking.objects.filter(work_id__worker_id=worker)
        usr=UserRegistration.objects.get(id=request.session['uid'])
        bookings=Workbooking.objects.filter(user_id=usr)
        if request.method=="POST":
            return redirect("user:paywork")
        else:
            return render(request,"User/ViewWorkBookings.html",{'Bookings':bookings}) 
    else:
        return redirect('guest:Userlogin')
    

def Plotbookings(request):
    if 'uid' in request.session:
        usr=UserRegistration.objects.get(id=request.session['uid'])
        bookings=Plotbooking.objects.filter(user_id=usr)
        if request.method=="POST":
            return redirect("user:payment")
        else:
            return render(request,"User/ViewPlotBookings.html",{'Bookings':bookings})
    else:
        return redirect('guest:Userlogin')
 

def Worker_bookings(request):
    if 'uid' in request.session:
        usr=UserRegistration.objects.get(id=request.session['uid'])
        bookings=WorkerBooking.objects.filter(user_id=usr)
        if request.method=="POST":
            return redirect("user:payworker")
        else:
            return render(request,"User/ViewWorkerBookings.html",{'BOOKINGS':bookings}) 
    else:
        return redirect('guest:Userlogin')

     

def pay_now(request,pbid):
    pbooking=Plotbooking.objects.get(id=pbid)
    if request.method=="POST":
        pbooking.payment_status=1
        pbooking.save()
        return redirect('User:processingpayment')
    else:
        return render(request,"User/Payment.html")
    
def pay_work(request,wrid):
    workbooking=Workbooking.objects.get(id=wrid)
    if request.method=="POST":
        workbooking.payment_status=1
        workbooking.save()
        return redirect('User:processingpayment')
    else:
        return render(request,"User/Payment.html")
    
def pay_worker(request,wrkid):
    workerbooking=WorkerBooking.objects.get(id=wrkid)
    if request.method=="POST":
        workerbooking.p_status=1
        workerbooking.save()
        return redirect('User:processingpayment')
    else:
        return render(request,"User/Payment.html")


def processingpayment(request):
    if 'uid' in request.session:
        return render(request,"User/Loader.html")
    else:
        return redirect('guest:Userlogin')


def paysucess(request):
    if 'uid' in request.session:
        return render(request,"User/Success.html")
    else:
        return redirect('guest:Userlogin')



        
 
        


