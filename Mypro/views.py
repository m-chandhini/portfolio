from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def blog_single(request):
    return render(request,'blog_single.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index1.html')

def portfolio(request):
    return render(request,'portfolio.html')
