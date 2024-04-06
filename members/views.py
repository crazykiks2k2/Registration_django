from django.shortcuts import render

# Create your views here.
def say_hello(request):
    return render(request,'home.html')

def say_hi(request):
    return render(request,'hi.html')

def print_txt(request):
    name=request.GET['name']
    return render(request,'bye.html',{ "name":name, "age":age })

