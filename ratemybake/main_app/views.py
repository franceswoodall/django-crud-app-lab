from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Bakery: 
    def __init__(self, name, pastry, description, price): 
        self.name = name
        self.pastry = pastry 
        self.description = description 
        self.price = price

bakeries = [
    Bakery('August', 'cronut', 'deliciously moist', 2), 
    Bakery('Ole & Steen', 'cinammon social', 'flavoursome and soft', 6), 
    Bakery('Buddys Deli', 'banana bread', 'filling and yum', 4) 
]

def bakery_index(request):
    return render(request, 'bakeries/index.html', {'bakeries' : bakeries})