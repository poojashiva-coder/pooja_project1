from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import Predict
from .ML_ALGORITHM import you
import numpy 

def index(request):
    return render(request, 'autism/home.html')

def predict(request):
    return render(request, 'autism/predict.html')

def predicted(request):
    if request.method == "POST":  
        form = Predict(request.POST)  
        type1 = int(request.POST['type1'])
        type2 = int(request.POST['type2'])
        type3 = int(request.POST['type3'])
        type4 = int(request.POST['type4'])
        type5 = int(request.POST['type5'])
        type6 = float(request.POST['type6'])
        type7 = float(request.POST['type7'])
        type8 = int(request.POST['type8'])
        x= []
        new_list = []
        x.append(type1)
        x.append(type2)
        x.append(type3)
        x.append(type4)
        x.append(type5)
        x.append(type6)
        x.append(type7)
        x.append(type8)
        list = you.getPrediction(x)
        yes = list[0]
        no = 100-list[0]
        new_list.append(yes)
        new_list.append(no)
        label = ['yes','no']
        zipped_list = zip(list)
        context = {
        'zipped_list': zipped_list,
        'list': new_list,
        'label': label,
        }
        print(list)
        return render(request, 'autism/predicted.html',context)
        
        
    else:  
        form = Predict()  
    return render(request,'autism/predicted.html',{'form':form})

def restapi(request):
        type1 = request.GET.get('value1', -1)
        type2 = request.GET.get('value2', -1)
        type3 = request.GET.get('value3', -1)
        type4 = request.GET.get('value4', -1)
        type5 = request.GET.get('value5', -1)
        type6 = request.GET.get('value6', -1)
        type7 = request.GET.get('value7', -1)
        type8 = request.GET.get('value8', -1)
        x= []
        new_list = []
        x.append(type1)
        x.append(type2)
        x.append(type3)
        x.append(type4)
        x.append(type5)
        x.append(type6)
        x.append(type7)
        x.append(type8)
        list = you.getPrediction(x)
        yes = list[0]
        no = 100-list[0]
        new_list.append(yes)
        new_list.append(no)
        label = ['yes','no']
        zipped_list = zip(list)
        context = {
        'zipped_list': zipped_list,
        'list': new_list,
        'label': label,
        }
        print(list)
        return render(request, 'autism/predicted.html',context)