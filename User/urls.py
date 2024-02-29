from django.urls import path,include
from User import views
app_name="User"

urlpatterns = [
    path('uhome/',views.uhome,name="userhome"),

    path('myprf/',views.profile,name="myprofile"),
    path('edprf/<int:eid>',views.editprf,name="editprofile"),
    path('chpswd/<int:cid>',views.cpswrd,name="changepassword"),

    path('comp/',views.Usrcomplaint,name="complaint"),
    path('del_com/<int:uid>',views.del_com,name="del_com"),

    path('feedback/',views.feedback,name="Feedback"),
    path('del_feed/<int:uid>',views.del_feed,name="del_feed"),

    path('search/',views.search,name="search"),
    path('getworker/',views.get_worker,name="getworker"),

    path('landsearch/',views.land_search,name="landsearch"),
    path('getland/',views.get_land,name="getland"),

    path('viewplots/<int:pid>',views.view_plots,name="viewplots"),
    path('plotbooking/<int:bid>',views.plot_booking,name="plotbooking"),
    
    path('viewwork/<int:wid>',views.view_works,name="viewwork"),

    path('workbooking/<int:wbid>',views.work_booking,name="workbooking"),   
    path('workerbooking/<int:wrid>',views.worker_booking,name="workerbooking"),

    path('Workbookings/',views.Workbookings,name="Workbookings"),

    path('plotbookings/',views.Plotbookings,name="Plotbookings"),

    path('Worker_bookings/',views.Worker_bookings,name="Worker_bookings"),

    path('paynow/<int:pbid>',views.pay_now,name="payment"),

    path('paywork/<int:wrid>',views.pay_work,name="paywork"),
    
    path('paywoker/<int:wrkid>',views.pay_worker,name="payworker"),

    path('processingpayment/',views.processingpayment,name="processingpayment"),
    
    path('patmentsucessful/',views.paysucess,name="patmentsucessful"),
 

]