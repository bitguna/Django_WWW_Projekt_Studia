from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .forms import PostForm,CommentForm
from .models import Comment, Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post_id = pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'comments':comments})

def post_create(request):
    if request.method == "POST":
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
                    post = form.instance
                    post.author = request.user
                    post.published_date = timezone.now()
                    post.save()
                    return redirect("post_detail",pk=post.pk)
    else:
            form = PostForm()
            return render(request,"blog/post_create.html",{"form":form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.instance
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def comment_add(request,id):
    if request.method == "POST":
            form = CommentForm(request.POST,request.FILES)
            if form.is_valid():
                    comment = form.instance
                    comment.author = request.user
                    comment.created_date = timezone.now()
                    comment.post_id = id
                    comment.save()
                    return redirect("post_detail",pk = id)
    else:
            form = CommentForm()
            return render(request,"blog/comment_add.html",{"form":form,"postId":id})