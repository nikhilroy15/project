from django.shortcuts import render
from app1.models import course,create
from app1.forms import courseForm
from django.http import HttpResponseRedirect

# Create your views here.



def index(request):
    return render(request,'app1/index.html',{'msg':'this is homepage'})




def syllabus(request):
    Course = course.objects.all
    b = {'msg':'Available courses','acer':Course}
    return render(request,'app1/course.html',b)


def admission(request):
    form = courseForm()
    if request.method == 'POST':
        form = courseForm(request.POST)
        if form.is_valid():
            form.save()
            form = courseForm()
        else:
            print('invalid course form data')
    a = {'msg':'insert course date','form':form}
    return render(request,'app1/admission.html',a)



def information(request):
    n = create.objects.all()
    display = {'msg':'this is student information','dell':n}
    return render(request,'app1/info.html',display)




def delete(request,id):
    n = create.objects.get(pk=id)
    n.delete()
    return HttpResponseRedirect('/app1/info')












