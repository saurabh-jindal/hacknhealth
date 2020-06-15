from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
from django.contrib import messages

# Create your views here.
from blog.models import Post, Comment, Contact, Newsletter, Category

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories' : categories
    }
    return render(request, 'blog/index.html', context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains= category
    ).order_by(
        '-created_on'
    )

    context = {
        'category': category,
        'posts':posts,
    }   
    return render(request, 'blog/category.html', context)

def blog_detail(request, slug):
    post = Post.objects.filter(slug= slug).first()
    context = {
        'post' : post, 
    }
    return render(request, 'blog/blog-post.html', context)


def contact(request):
    messages.success(request,'Your message has been recieved')
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        # some checks here
        contact = Contact(email =email, subject= subject, message= message)
        contact.save()
   
    return render(request, 'blog/contact.html')


def about(request):
    return render(request, 'blog/about.html')
def author(request):
    return render(request, 'blog/author.html')
def newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']
        news = Newsletter(email = email)
        # some check

        news.save()
    return redirect('/')
