from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from datetime import datetime
from .models import mppr

def InsertPageView(request):
    return render(request, "mpprinsert.html")

def InsertData(request):
    if request.method == 'POST':
        data = mppr()
        data.areaName = request.POST['areaName']
        data.areaSqm = request.POST['areaSqm']
        data.work = request.POST['work']
        data.manpower = request.POST['manpower']
        data.quantity = request.POST['quantity']
        data.startdate = request.POST['startdate']
        
        data.save()

        return render(request,"mpprinsert.html")

def GetData(request):
    data = mppr.objects.all()
    return render(request, "mpprget.html", {'data': data})


def Edit(request, pk):
    data = get_object_or_404(mppr, pk=pk)
    Data = mppr.objects.all()
    return render(request,"mpprupdate.html", {"data": data, "Data": Data})

def EditData(request, pk):
    if request.method == 'POST':
        data = mppr.objects.get(pk=pk)
        data.areaName = request.POST['areaName']
        data.areaSqm = request.POST['areaSqm']
        data.work = request.POST['work']
        data.manpower = request.POST['manpower']
        data.quantity = request.POST['quantity']
        data.startdate = request.POST['startdate']
        data.finishdate = request.POST['finishdate']

        startdate = datetime.strptime(data.startdate, '%Y-%m-%d').date()
        finishdate = datetime.strptime(data.finishdate, '%Y-%m-%d').date()

        data.duration = (finishdate - startdate).days
        data.rateHourPerSqm = (data.duration * 8) / float(data.areaSqm)

        data.save()

        return redirect('list')    
    return render(request, 'mpprget.html')   

def filterArea(request):
    if request.method == "POST":
        
        areaName = request.POST['areaName']
        mppr_filter = mppr.objects.filter(areaName__icontains=areaName)
        context = {'data':mppr_filter}

        return render(request, 'mpprget.html', context)

def filterWorks(request):
    if request.method == "POST":
        
        work = request.POST['work']
        mppr_filter = mppr.objects.filter(work__icontains=work)
        context = {'data':mppr_filter}

        return render(request, 'mpprget.html', context)
    

        


     


    
def DeleteData(request, pk):
    if request.method == 'POST':
        data = get_object_or_404(mppr, pk=pk)
        data.delete()
        return redirect('list')
    return render(request, 'mpprget.html')


    
    




