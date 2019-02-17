from django.shortcuts import render
from .models import Person
# Create your views here.


def people(request):
    person = Person.objects.all()
    return render(request, 'tutorial/people.html', {'people': person})