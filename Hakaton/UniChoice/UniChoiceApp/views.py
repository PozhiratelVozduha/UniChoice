from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def tech_universities(request):
    return render(request, 'technical.html')

def med_universities(request):
    return render(request, 'medical.html')

def human_universities(request):
    return render(request, 'human.html')

def art_universities(request):
    return render(request, 'creative.html')

