from django.urls import path,include
from Guest import views
app_name="guest"

urlpatterns = [
    path('gst/',views.UserReg,name="Userreg"),
    path('ajaxlocation/',views.Ajaxlocation,name="Ajax_Location"),
    path('ulog/',views.userlogin,name="Userlogin"),
    path('worker/',views.worker,name="Worker"),
    path('Ajxplace/',views.Ajaxplace,name="Ajax-Place"),
    path('landload/',views.landload,name="Lanload"),
    path('',views.home,name="home"),
    
    
]
