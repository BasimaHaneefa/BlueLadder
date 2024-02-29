from django.urls import path
from Admin import views
from Guest import *
app_name="webadmin"

urlpatterns = [
    path('district/',views.district,name="district"),
    path('deldis/<int:did>',views.del_dis,name="Del_dis"),
    path('updis/<int:eid>',views.up_dis,name="Up_dist"),
    
    path('plc/',views.plc,name="place"),
    path('delplc/<int:pid>',views.del_plc,name="Del_plc"),

    path('loc/',views.loc,name="Location"),
    path('del_loc/<int:lid>',views.del_loc,name="del_loc"),

    path('comtype/',views.complainttype,name="comtype"),
    path('delcom/<int:cid>',views.delcom,name='Del_com'),

    path('workertype/',views.workertype,name="workertype"),
    path('delwtype/<int:wid>',views.del_wtype,name="Del_wtype"),

    path('Ajxplace/',views.Ajaxplace,name="Ajax-Place"),

    path('workerverification/',views.workerverification,name="workerverification"),
    path('acceptworker/',views.acceptworker,name="acceptworker"),
    path('rejectworker/',views.rejectworker,name="rejectworker"),
    path('acceptwrkr/<int:wacid>',views.accept_worker,name="accept_wrkr"),
    path('rejectwrkr/<int:wrjid>',views.reject_worker,name="reject_wrkr"),

    path('landloadverification/',views.landloadverification,name="landloadverification"),
    path('acceptland/',views.acceptlandload,name="acceptland"),
    path('rejectland/',views.rejectlandload,name="rejectland"),
    path('acceptland/<int:lacid>',views.accept_land,name="accept_landload"),
    path('rejectland/<int:lrjid>',views.reject_land,name="reject_landload"),

    path('adminhome/',views.adminhome,name="adminhome"),

    path('viewuser/',views.viewuser,name="viewuser"),

    path('complaints/',views.complaints,name="complaints"),
    path('reply/<int:rid>',views.reply,name="reply"),
    
    path('feedback/',views.feedback,name="feedback"),
    
    

]