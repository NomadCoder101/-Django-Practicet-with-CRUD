from django.shortcuts import render ,redirect

from .models import Blog

from .forms import BlogCreateForm

# Create your views here.

def blogList(request):
    
    blog_list = Blog.objects.all()
    
    context = {
        'blog_list':blog_list
    }
    
    return render(request,'blog-list.html',context)
    
    
def blogdetail(request,pk):
    
    blog_detail = Blog.objects.get(id=pk)
    
    context = {
        'blog_detail':blog_detail
    }
    
    return render(request,'blog-detail.html',context)


def createBlogListing(request):
    
    form = BlogCreateForm()
    if request.method == 'POST':
        form = BlogCreateForm(request.POST,request.FILES)
        print(request.POST)
        if form.is_valid():
           form.save()
           return redirect('blogList')
        
    context ={
        'form':form
        }
    return render(request,'createblog.html', context)
    
    
def UpdateBLogListing(request,pk):
    
    blog_listing = Blog.objects.get(id = pk)
    
    form = BlogCreateForm(instance=blog_listing)
    if request.method == 'POST':
        form = BlogCreateForm(request.POST,instance=blog_listing,files=request.FILES)
        print(request.POST)
        if form.is_valid():
           form.save()
           return redirect('blogList')
        
    context ={
        'form':form
        }
    return render(request,'updateblog.html', context)


def BlogDelete(request,pk):
    blog_listing = Blog.objects.get(id = pk)
    blog_listing.delete()
    return redirect('blogList')
    