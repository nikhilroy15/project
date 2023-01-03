from django.urls import path
from app1 import views


app_name = 'app1'



urlpatterns = [
    path('cousre',views.syllabus,name='syllabus'),
    path('admission',views.admission,name='admission'),
    path('info',views.information,name='info'),
    path('delete/<int:id>',views.delete,name='delete'),
]

