from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, template_name='index.html')

def gallery(request):
    return  render(request, template_name='gallery.html')

def aboutus(request):
    return render(request,template_name='about.html')

def contactus(request):
    return render(request, template_name='contact.html')
