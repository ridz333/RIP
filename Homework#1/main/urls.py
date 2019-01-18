from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.Main.as_view(), name='home'),
    path('delete_blog/<int:blog>',views.delete_blog, name='deleteblog'),
    path('edit_blog/<int:blog>',views.EditBlog.as_view(), name='editblog'),
    path('edit_blog/delete_image/<int:blog>/<int:image>', views.delete_image, name='deleteimage'),
]