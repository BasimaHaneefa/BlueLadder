from django.urls import path,include
from Worker import views
app_name="Worker"

urlpatterns = [
    path('whome/',views.whome,name="workerhome"),

    path('myprf/',views.profile,name="myprofile"),

    path('edprf/<int:eid>',views.editprf,name="editprofile"),

    path('chpswd/<int:cid>',views.cpswrd,name="changepassword"),

    path('workdetails/',views.workdetails,name="workdetails"),

    path('delwork/<int:wid>',views.del_work,name="Del_work"),

    path('wrcom/',views.wrkrcomp,name="wrkrcom"),
    path('del_com/<int:wid>',views.del_com,name="del_com"),

    path('feedback/',views.feedback,name="feedback"),
    path('del_feed/<int:wid>',views.del_feed,name="delete"),

    path('workbookings/',views.Mybookings,name="Mybookings"),
    path('accept/<int:acid>',views.Accept,name="accept"),
    path('reject/<int:reid>',views.Reject,name="reject"),

    path('workerbooking/',views.Worker_bookings,name="workerbooking"),
    path('acceptworker/<int:aid>',views.Accept_worker,name="acceptworker"),
    path('rejectworker/<int:rid>',views.Reject_worker,name="rejectworker"),

    path('Accepted_Workbookings/',views.Accepted_Workbookings,name="Accepted_Workbookings"),

    path('AcceptedWorker_bookings/',views.AcceptedWorker_bookings,name="AcceptedWorker_bookings"),

]