from django.shortcuts import render
from feedback.models import Feedback

# Create your views here.
def index(request):
    return render(request,'index.html')

def u_feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        text= request.POST['text']
        data = Feedback(name=name,text=text)
        data.save()

    data=Feedback.objects.all()
    dict = {
        'allfeedback': data
    }
    return render(request,'u_feedback.html',dict)
    

