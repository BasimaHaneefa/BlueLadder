from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Landload.models import *
from Admin.models import *

# Create your views here.

def landloadhome(request):
    if 'lid' in request.session:
        landload=Landload.objects.get(id=request.session['lid'])
        return render(request,"Landload/LandloadHome.html",{'LAND':landload})
    else:
        return redirect('guest:Userlogin')

def profile(request):
    if 'lid' in request.session:
        prf=Landload.objects.get(id=request.session['lid'])
        return render(request,"Landload/MyProfile.html",{'PR':prf})
    else:
        return redirect('guest:Userlogin')

def editprf(request,eid):
    edit=Landload.objects.get(id=eid)
    if request.method=="POST":
        edit.landload_name=request.POST.get('txt_name')
        edit.landload_contact=request.POST.get('txt_contact')
        edit.landload_email=request.POST.get('txt_email')
        edit.landload_address=request.POST.get('txt_address')
        edit.save()
        return redirect('landload:myprofile')
    else:
        return render(request,"Landload/EditProfile.html",{'EDT':edit})

def cpswrd(request,cid):
    change=Landload.objects.get(id=cid)
    if request.method=="POST":
        pwd=change.landload_password
        crrnt=request.POST.get('txt_pswd')
        if pwd == crrnt:
            change=Landload.objects.get(id=cid)
            new=request.POST.get('txt_npswd')
            change.landload_password=new
            change.save()
            return redirect('guest:Userlogin')
        else:
            error="Password Incorrect!!"
            return render(request,"User/ChangePwd.html",{'ER':error})
    else:
        return render(request,"User/ChangePwd.html")

def landcmp(request):
    if 'lid' in request.session:
        com=Complainttype.objects.all()
        landload=Landload.objects.get(id=request.session['lid'])
        cmp=Complaint.objects.filter(Landload_id=landload)
        if request.method=="POST":
            comid=request.POST.get("sel_coml")
            cmptype=Complainttype.objects.get(id=comid)
            Complaint.objects.create(Complaint_content=request.POST.get('txt_content'),Landload_id=landload,Complainttype_id=cmptype)   
            return render(request,"Landload/LandloadComplaints.html",{'COM':com,'CMP':cmp})
        else:
            return render(request,"Landload/LandloadComplaints.html",{'COM':com,'CMP':cmp})
    else:
        return redirect('guest:Userlogin')
    
def del_com(request,lid):
    Complaint.objects.get(id=lid).delete()
    return redirect('landload:landcmp')     


def feedback(request):
    if 'lid' in request.session:
        feed=Feedback.objects.all()
        landload=Landload.objects.get(id=request.session['lid'])
        land=Feedback.objects.filter(Landload_id=landload)
        if request.method=="POST":
            Feedback.objects.create(feedback_description=request.POST.get('txt_feedback'),Landload_id=landload)       
            return render(request,"Landload/Feedback.html",{'FEED':feed,'LAND':land}) 
        else:
            return render(request,"Landload/Feedback.html",{'FEED':feed,'LAND':land})
    else:
        return redirect('guest:Userlogin')
    
def del_feed(request,lid):
    Feedback.objects.get(id=lid).delete()
    return redirect('landload:feedback')

def plotdetails(request):
    if 'lid' in request.session:
        landload=Landload.objects.get(id=request.session['lid'])
        plot=Plot.objects.filter(Landload_id=landload)
        dist=District.objects.all()
        if request.method=="POST" and request.FILES:
            locid=request.POST.get('sel_loc')
            loc=Location.objects.get(id=locid)
            Plot.objects.create(plot_des=request.POST.get("txt_des"),plot_image=request.FILES.get("fil_img"),
                                plot_amount=request.POST.get("txt_rate"),Landload_id=landload,location_id=loc)
            return render(request,"Landload/AddPlots.html",{'DIST':dist,'LAND':plot})   
        else:
            return render(request,"Landload/AddPlots.html",{'DIST':dist,'LAND':plot})
    else:
        return redirect('guest:Userlogin')

def del_plot(request,pid):
    Plot.objects.get(id=pid).delete()
    return redirect('landload:addplot') 

def mybookings(request):
    if 'lid' in request.session:
        landload=Landload.objects.get(id=request.session['lid'])
        bookings=Plotbooking.objects.filter(plot_id__Landload_id=landload,plotbooking_status=0)
        return render(request,"Landload/ViewMyBookings.html",{'Bookings':bookings}) 
    else:
        return redirect('guest:Userlogin')

def accept(request,acid):
    accept=Plotbooking.objects.get(id=acid)
    accept.plotbooking_status=1
    accept.save()
    return redirect('landload:mybookings')

def reject(request,reid):
    reject=Plotbooking.objects.get(id=reid)
    reject.plotbooking_status=2
    reject.save()
    return redirect('landload:mybookings')

def plotbookings(request):
    if 'lid' in request.session:
        landload=Landload.objects.get(id=request.session['lid'])
        bookings=Plotbooking.objects.filter(plot_id__Landload_id=landload,plotbooking_status=1)
        return render(request,"Landload/ViewAcceptedPlotBookings.html",{'Bookings':bookings}) 
    else:
        return redirect('guest:Userlogin')
      
    


