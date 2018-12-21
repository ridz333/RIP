from django.urls import path, re_path
from . import views
from django.shortcuts import HttpResponseRedirect

app_name = "main"

urlpatterns = [
    path('', views.main),
    re_path(r'(main/static/)', lambda request,arg: HttpResponseRedirect(request.path.replace("main/",""))),
    path('<int:id>/<slug:slug>/', views.item, name="model"),
   # path('reg',views.reg)
]
