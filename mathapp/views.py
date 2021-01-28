from django.shortcuts import render

# Create your views here.

def  mathadd(request):
    context = {}
    return render(request, 'mathapp/mathadd.html', context)

def cylindervolume(request):
    context = {}
    if request.method == 'POST':
        radius = int(request.POST.get('value_radius', 0))
        height = int(request.POST.get('value_height', 0))
        print("radius=", radius)
        print("height=", height)
        V = 3.14*radius*radius*height
        context['result'] = V
        context['radius'] = radius
        context['height'] = height

    if request.method == 'GET':
        context['radius'] = 0
        context['height'] = 0

    return render(request, 'mathapp/cylindervolume.html', context)

def rectanglearea(request):
    context = {}
    return render(request,'mathapp/rectanglearea.html',context)
