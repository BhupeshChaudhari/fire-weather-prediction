from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
from .models import Predict

# Create your views here.

def index(request):

    ridge_model=pickle.load(open('models/ridge.pkl','rb'))
    standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

    if request.method == "POST":
        Temperature = request.POST.get('Temperature', "")
        RH = float(request.POST.get('RH', ""))
        Ws = float(request.POST.get('Ws', ""))
        Rain = float(request.POST.get('Rain', ""))
        FFMC = float(request.POST.get('FFMC', ""))
        DMC = float(request.POST.get('DMC', ""))
        ISI = float(request.POST.get('ISI', ""))
        Classes = float(request.POST.get('Classes', ""))
        Region = float(request.POST.get('Region', ""))
        FWI = request.POST.get('FWI', "")

        
        new_data_scaled=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data_scaled)
        
        inputs = Predict(Temperature=Temperature, RH=RH, Ws=Ws, Rain=Rain, FFMC=FFMC, DMC=DMC, ISI=ISI, Classes=Classes, Region=Region, FWI=result[0])
        inputs.save()

        return render(request, 'myapp/index.html', {'result':result})
    else:
        return render(request, 'myapp/index.html')