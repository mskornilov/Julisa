from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from .models import Post, Category, Subcategory, Comment
from .forms import CommentForm

# Create your views here.

def index(request, slug=None):
    recent_posts = Post.published.all()[:3]
    context = {'recent_posts': recent_posts}
    return render(request, 'blog/index.html', context)

def post_list(request):
    posts = Post.published.all()
    context = {'posts': posts}
    return render(request, 'blog/post/list.html', context)

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year, publish__month=month,
                             publish__day=day)
    form = CommentForm()
    comments = post.comments.filter(published=True)
    context = {'post': post,
               'comments': comments,
               'form': form}
    return render(request, 'blog/post/detail.html', context)

def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        author = get_object_or_404(User, id=1)
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            body = cd['body']
            comment = Comment.objects.create(author=author, post=post,
                                             body=body)
            comment.save()
            return redirect('blog:post_detail', post.publish.year,
                                                post.publish.month,
                                                post.publish.day,
                                                post.slug,
                                                )
