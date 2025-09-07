from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'application' : 'Football Shop',
        'npm' : '2406410235',
        'name' : 'Roselia Evanny Sucipto',
        'class' : 'PBP B'
    }

    return render(request, "main.html", context)