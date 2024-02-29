from django.urls import path,include
from Landload import views
app_name="landload"

urlpatterns = [
    path('llhome/',views.landloadhome,name="landloadhome"),

    path('myprf/',views.profile,name="myprofile"),

    path('edprf/<int:eid>',views.editprf,name="editprofile"),
    
    path('chpswd/<int:cid>',views.cpswrd,name="changepassword"),

    path('landcmp/',views.landcmp,name="landcmp"),
    path('del_com/<int:lid>',views.del_com,name="del_com"),

    path('feedback/',views.feedback,name="feedback"),
    path('del_feed/<int:lid>',views.del_feed,name="del_feed"),

    path('addplot/',views.plotdetails,name="addplot"),
    path('delplot/<int:pid>',views.del_plot,name="Del_plot"), 

    path('mybookings/',views.mybookings,name="mybookings"),
    path('accept/<int:acid>',views.accept,name="accept"),
    path('reject/<int:reid>',views.reject,name="reject"),

    path('Plotbookings/',views.plotbookings,name="Plotbookings"),

]