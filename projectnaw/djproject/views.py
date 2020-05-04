from django.shortcuts import render


# Create your views here.

def home(request):
    my_dict = {'insert_home': "This is home",}
    return render(request, 'home/indexhome.html', context=my_dict)
