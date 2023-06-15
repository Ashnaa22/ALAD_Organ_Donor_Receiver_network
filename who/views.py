from django.shortcuts import render

def whoselect(request): # new
    return render(request, 'who.html')