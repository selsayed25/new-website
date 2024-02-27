from django.shortcuts import render
from .models import Category, Post, Comment

# Create your views here.

def blogIndex(request):
    """
    View function for the blog index page. This view function retrieves all blog posts from the database and renders them using the "index.html" template.

    `@param request` The HTTP request. This parameter is required by Django for all view functions.
    
    `@type request` django.http.HttpRequest

    `@return` The HTTP response. This view function renders a template to generate the HTTP response. The template displays all blog posts.
    """
    posts = Post.objects.all().order_by("-created_on")
    
    context = {
        "posts": posts,
    }

    return render(request, "blog/index.html", context)

def blogCategory(request, category):
    """
    View function for the blog category page. This view function retrieves all blog posts in a specific category from the database and renders them using the "category.html" template.

    `@param` request: The HTTP request. This parameter is required by Django for all view functions.

    `@param` category: The category name. This parameter is passed from the URL pattern in the URL configuration.

    `@type request` django.http.HttpRequest

    `@type category` str

    `@return` The HTTP response. This view function renders a template to generate the HTTP response. The template displays all blog posts in a specific category.
    """
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        "-created_on"
    )
    
    context = {
        "category": category,
        "posts": posts,
    }

    return render(request, "blog/category.html", context)

def blogDetail(request, pk):
    """
    View function for the blog detail page. This view function retrieves a specific blog post from the database and renders it using the "detail.html" template.

    `@param request` The HTTP request. This parameter is required by Django for all view functions.

    `@param pk` The primary key of the blog post. This parameter is passed from the URL pattern in the URL configuration.

    `@type request` django.http.HttpRequest

    `@type pk` int

    `@return` The HTTP response. This view function renders a template to generate the HTTP response. The template displays a specific blog post.
    """
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog/detail.html", context)

