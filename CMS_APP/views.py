from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,categories
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
import logging
from django.contrib import messages
from USER_PROFILE.models import Profile
from django.http import HttpResponseForbidden,HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator
logger = logging.getLogger(__name__)
# Create your views here.
 
 
 



 
def home(request, category_id=None):
    Categories = categories.objects.all()
    
    # Get the selected category (if any)
    selected_category = None
    if category_id:
        selected_category = get_object_or_404(categories, pk=category_id)

    if request.user.is_authenticated:
         if 'q' in request.GET:
            q = request.GET['q']
            result = Q(
                Q(title__icontains=q) |
                Q(tag__name__icontains=q) |  # Assuming 'name' is the field in the 'categories' model
                Q(body__icontains=q)
            )
            posts = Post.objects.filter(result)
         else:
       
             p = Paginator(Post.objects.all(),5)
             page = request.GET.get('page')
             posts = p.get_page(page)
         if selected_category:
            posts = Post.objects.filter(tag=selected_category)
         
           

         context = {'posts': posts, 'Categories': Categories, 'selected_category': selected_category}
         return render(request, 'home.html', context)
    else:
        p = Paginator(Post.objects.all(),5)
        page = request.GET.get('page')
        posts = p.get_page(page)
        context = {'posts': posts, 'Categories': Categories}
        return render(request, 'landingpage.html', context)
         


def detail(request,slug):
     posts = get_object_or_404(Post, slug=slug)
     #this displays the most recent post excluding the one selected
     recent_posts = Post.objects.exclude(slug=slug).order_by('-created')[:5]
     total_likes = posts.total_likes()
    
     context = {'posts':posts, 'recent_posts':recent_posts,'total_likes':total_likes}
     return render(request,'detail.html',context)






@login_required 
def CreatePost(request):
  
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
        
            profile, created = Profile.objects.get_or_create(name=request.user)
            post.author = profile
            
            post.slug = slugify(post.title)
            
            post.save()
            #messages.info( request,"Post saved successfully.")
            return redirect('detail',slug = post.slug)
        else:
            messages.error(request,"Form is not valid.")
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'create-article.html', context)

@login_required
def updatePost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        
        # Access the user's profile through the one-to-one relationship
        profile = request.user.profile

        if profile == post.author:
            if request.method == 'POST':
                form = PostForm(request.POST, request.FILES, instance=post)
                if form.is_valid():
                    form.save()
                    # messages.info(request, "Post updated successfully ")
                    return redirect('detail', slug=post.slug)
            else:
                form = PostForm(instance=post)

            context = {'form': form, 'slug': post.slug, 'post': post}
            return render(request, 'update.html', context)
        else:
            return HttpResponseForbidden("You don't have permission to update this post.")
    except Post.DoesNotExist:
        # Handle the case where the post doesn't exist.
        logger.error(f"Post with slug '{slug}' does not exist.")
        # You can return an appropriate response here.

@login_required
def deletePost(request, slug):
    try:
        post = Post.objects.get(slug=slug)  # Get the post object first

        # Check if the user is the author of the post
        if request.user.profile == post.author:
            post.delete()
            return redirect('home')
        else:
            return HttpResponseForbidden("You don't have permission to delete this post.")
    except Post.DoesNotExist:
        logger.error(f"Post with slug '{slug}' does not exist.")
 
def LikeView(request, pk):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')  # Get the post_id from the request.POST dictionary
        print(f"Received post_id: {post_id}")
        post = get_object_or_404(Post, post_id=pk)  # Use 'pk' to filter the Post object
        post.likes.add(request.user)
        return HttpResponseRedirect(reverse('detail', args=[post.slug]))
    else:
        return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

