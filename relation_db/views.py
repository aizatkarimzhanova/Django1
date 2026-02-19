from django.shortcuts import render
from . import models

def relation_db(request):
    if request.method == 'GET':
        number_car = models.NumberCar.objects.all()
        return render(
            request,
            'relation_db.html',
            {
                'number_car': number_car
            }
        )
