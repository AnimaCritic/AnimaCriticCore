from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
#from django.views import generic
from .models import Post
from django.http import HttpResponseRedirect
#from django import forms
from .forms import CommentForm
from django.shortcuts import render, redirect

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    
class AddPostView(CreateView):
    model = Post
    template_name = "blog/new_post.html"
    fields = ('title', 'slug', 'summary', 'author', 'preview', 'review', 'content')

class UpdatePostView(UpdateView):
    model = Post
    template_name = "blog/update_post.html"
    fields = ('title', 'summary', 'preview', 'author', 'review','slug', 'content')
    
class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy('home')

def faq(request):
    return render(request, 'blog/faq.html')

def about_us(request):
    return render(request, 'blog/about_us.html')

def home(request):
    return request("base.html")

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post.id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse("post_detail"), args=[str(pk)])

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})
