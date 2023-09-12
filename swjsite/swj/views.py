from django.shortcuts import render, get_object_or_404
from .models import Member
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm

def main_page(request):
    return render(request,
                 'swj/pages/mainpage.html',
                )


def post_detail(request, id):
    post = get_object_or_404(Member,
                             id=id,
                             status=Member.Status.PUBLISHED)
    return render(request,
                  'swj/member/detail.html',
                  {'member': post})

def homepage(request):
    return render(request,
                  'swj/pages/list.html')

def contributors(request):
    return render(request, 
                  'swj/pages/contributors.html')


def members(request):
    form = SearchForm()
    query = None
    results = []
    members = Member.published.all()

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Member.published.annotate(
                search=SearchVector('name', 'body'),
            ).filter(search=query)

    return render(request, 
                  'swj/pages/members.html',
                  {'members': members,
                   'form': form,
                   'query': query,
                   'results': results})

def references(request):
    return render(request, 
                  'swj/pages/references.html')