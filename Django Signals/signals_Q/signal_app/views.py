from django.shortcuts import render
from .models import TestModel
from django.db import transaction
# Create your views here.
def home(request):
    return render(request,'home.html')

def save(request):
    if request.method == 'POST':
        with transaction.atomic():
            fname = request.POST.get('firstname')
            lname = request.POST.get('lastname')
            TestModel.objects.create(FirstName = fname , LastName = lname)
        return render(request, 'save.html')
    return render(request,'home.html')