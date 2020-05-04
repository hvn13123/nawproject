from django.shortcuts import render
from nawapp.models import Person

# Create your views here.

def pindex(request):
    al = Person.objects.order_by('name')
    my_dict = {'insert_me': "Jacky and Django",}
    return render(request, 'nawapp/index.html', context=my_dict)
