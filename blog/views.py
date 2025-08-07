from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q

def post_list(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    posts = Post.objects.all()
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
    if category:
        posts = posts.filter(category__iexact=category)
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/list.html', {
        'page_obj': page_obj,
        'query': query,
        'category': category,
    })
