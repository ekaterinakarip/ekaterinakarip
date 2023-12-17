from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    

    if request.method =='POST':
        try:
            dictionary = request.POST
            Sentexpression = dictionary['SentCalculation']
            answer= eval(Sentexpression)
        except:
            answer = "Please Give Valid Input"
        return render(request, 'index.html', {"answer":answer,"Sentexpression":Sentexpression})
    else:
        return render(request, 'index.html',{})

