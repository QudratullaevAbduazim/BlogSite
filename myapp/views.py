from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Project, Post, PostTag, CategoryTag, CategoryProject


class IndexView(View):
    def get(self, request):
        projects = Project.objects.all().order_by('-id')[:6]
        posts = Post.objects.all().order_by('-id')[:3]
        return render(request, 'index.html', {'projects': projects, 'posts': posts})


class PortfolioView(View):
    def get(self, request, category_id=None):
        categories = CategoryProject.objects.all()

        if category_id:
            category = get_object_or_404(CategoryProject, id=category_id)
            projects = Project.objects.filter(category=category).order_by('-id')
        else:
            projects = Project.objects.all().order_by('-id')

        return render(request, 'page-portfolio.html', {
            'projects': projects,
            'categories': categories,
            'current_category': category_id
        })

class PortfolioDetailView(View):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        categories = CategoryProject.objects.all()
        return render(request, 'portfolio-details.html', {
            'project': project,
            'categories': categories
        })

class PostListView(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-id')
        return render(request, 'blog-archive.html', {'posts': posts})

class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        categories = CategoryTag.objects.all()
        return render(request, 'single-sidebar.html', {
            'post': post,
            'categories': categories
        })

class TagPostsView(View):
    def get(self, request, tag_id):
        tag = get_object_or_404(CategoryTag, id=tag_id)
        posts = Post.objects.filter(posttag__tag=tag)
        return render(request, 'blog-archive.html', {'tag': tag, 'posts': posts})

class CategoryTagPostsView(View):
    def get(self, request, category_id):
        category = get_object_or_404(CategoryTag, id=category_id)
        posts = Post.objects.filter(category__id=category_id)
        return render(request, 'blog-archive.html', {'category': category, 'posts': posts})


class ContactView(View):
    def get(self, request):
        return render(request, 'page-contact.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'page-login.html')

class SignupView(View):
    def get(self, request):
        return render(request, 'page-signup.html')

class Page404View(View):
    def get(self, request, exception=None):
        return render(request, 'page-404.html')