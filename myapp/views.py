from django.shortcuts import render
from .models import Warehouse
from datetime import date
import random

def generate_random_id():
    return f"CONT{random.randint(1, 20)}"

def index(request):
    container_id = generate_random_id()
    container_status = 'IN'
    container_location = random.choice([location[0] for location in Warehouse.CONTAINER_LOCATION])
    container_eta = date.today()
    return render(request, 'index.html', {})