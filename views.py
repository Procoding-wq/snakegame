from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def snake_game(request):
    return render(request, 'snakegame/snake.html')
