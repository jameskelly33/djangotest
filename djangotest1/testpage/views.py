from django.shortcuts import render
from .models import Item

# Create your views here.
def home(request):
    items = Item.objects.all()
    return render(request,'testpage/index.html',context={
        'items':items
    })
    