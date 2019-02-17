from django.shortcuts import render
# Create your views here.
from django_tables2 import RequestConfig
from .models import Person
from .tables import PersonTable

def people(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request).configure(table) #  automatically pulls values from request.GET
    return render(request, 'tabela/people.html', {'table': table})