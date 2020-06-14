from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from blog.models import Post, Comment, Contact, Newsletter

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts
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
        'posts':posts
    }   
    return render(request, 'blog/category.html', context)

def blog_detail(request, slug):
    post = Post.objects.filter(slug=slug).first()
    if request.method == 'POST':
        author = request.POST['author']
        body = request.POST['body']

        comment_obj=  Comment(author = author, body= body, post= post)
        # Some checking
        comment_obj.save()
    comments = Comment.objects.filter(post= post)
    context = {
        'post' : post, 
        'comments' : comments
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
