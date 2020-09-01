from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from .models import Post, Sermon

class HomePageView(TemplateView):
    model = Post
    template_name = 'index.html'

class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'

def sermon(request):
    sermons = Sermon.objects.all()    
    return render(request, "sermon.html", {'sermons':sermons})

def about(request):
    context = {}

    return render(request, "about.html", context)

def bulletin(request):
    sermons = Sermon.objects.all()

    return render(request, "bulletin.html", {'sermons':sermons})

def ministries(request):
    context = {}

    return render(request, "ministries.html", context)

def choir(request):
    context = {}

    return render(request, "choir.html", context)