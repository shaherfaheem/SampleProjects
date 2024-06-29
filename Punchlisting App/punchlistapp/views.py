from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Punchlist

def InsertPageView(request):
    return render(request, "punchlistinsert.html")

def InsertData(request):
    if request.method == 'POST':
        item = Punchlist()
        item.description = request.POST['description']
        item.area = request.POST['area']
        item.status = request.POST['status']
        item.contractor = request.POST['contractor']
        item.action = request.POST['action']
        item.commitment = request.POST['commitment']
        
        if len(request.FILES) != 0:
            item.photo = (request.FILES)['photo']
        item.save()

    return render(request,"punchlistinsert.html")

def GetData(request):
    items = Punchlist.objects.all()
    return render(request, "punchlistget.html", {'items': items})

def Edit(request, pk):
    item = get_object_or_404(Punchlist, pk=pk)
    items = Punchlist.objects.all()
    return render(request,"punchlistupdate.html", {"item": item, "items": items})



def EditData(request, pk):
    if request.method == 'POST':
        item = Punchlist.objects.get(pk=pk)
        item.description = request.POST['description']
        item.status = request.POST['status']
        item.area = request.POST['area']
        item.contractor = request.POST['contractor']
        item.action = request.POST['action']
        item.commitment = request.POST['commitment']
        item.finishdate = request.POST['finishdate']

        if len(request.FILES) != 0:
            item.photo = (request.FILES)['photo']
        item.save()
        

        return redirect('list')    
    return render(request, 'punchlistget.html')  

def filterDescr(request):
    if request.method == "POST":
        
        description = request.POST['description']
        punchlist_filter = Punchlist.objects.filter(description__icontains=description)
        context = {'items':punchlist_filter}

        return render(request, 'punchlistget.html', context)

def filterArea(request):
    if request.method == "POST":
        
        area = request.POST['area']
        punchlist_filter = Punchlist.objects.filter(area__icontains=area)
        context = {'items':punchlist_filter}

        return render(request, 'punchlistget.html', context)  
    
def filterCont(request):
    if request.method == "POST":
        
        contractor = request.POST['contractor']
        punchlist_filter = Punchlist.objects.filter(contractor__icontains=contractor)
        context = {'items':punchlist_filter}

        return render(request, 'punchlistget.html', context) 
    
def DeleteData(request, pk):
    if request.method == 'POST':
        
        item = get_object_or_404(Punchlist, pk=pk)
        item.delete()
        return redirect('list')
    return render(request, 'punchlistget.html')



def Completed(request, pk):
    if request.method == 'POST':
        item = Punchlist.objects.get(pk=pk)

        item.status ='Completed'

        item.save()

        return redirect('list')    
    return render(request, 'punchlistget.html')  

    
    




