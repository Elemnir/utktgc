from django.http import Http404
from django.shortcuts import render, get_object_or_404

from myr.models import Post, Event, AboutStatement


def index(request):
    """Show the home page with all posts"""
    size = request.GET.get('size', 10)
    nextsize = int(size) * 2

    posts = Post.objects.all().order_by('-date')[:size]

    return render(request, 'myr/index.html', {
        'posts' : posts,
        'nextsize' : nextsize,
    })


def about(request):
    """Show the latest About Statement"""
    statement = AboutStatement.objects.order_by('updated').last()
        
    return render(request, 'myr/about.html', {
        'statement' : statement,
    })


def detail(request, rtype, val = None):
    """Show a requested post or event"""
    item = get_object_or_404(Post if rtype == 'post' else Event, pk=val)
    
    return render(request, 'myr/detail_'+str(rtype)+'.html', {
        rtype : item,
    })


def calendar(request):
    """Display all events in chronological order"""
    events = Event.objects.all().order_by('-date')

    return render(request, 'myr/calendar.html', {
        'events' : events,
    })


def archive(request):
    """Display all archived posts in reverse chronological order"""
    return render(request, 'myr/archive.html', {
        'posts' : Post.objects.all().order_by('date')
    })
