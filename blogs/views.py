from django.shortcuts import get_object_or_404, render, redirect
from .models import Post

# Create your views here.
def index(request):
  posts = Post.objects.all().order_by('-created_at')
  return render(request, 'index.html', {'posts': posts})

def create(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    body = request.POST.get('body')
    Post.objects.create(title=title, body=body)
    return redirect('/')
  return render(request, 'create.html')

def edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.body = request.POST.get('body')
        post.save()
        return redirect('/')
    
    return render(request, 'edit.html', {'post': post})

def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('/')