from django.http            import Http404
from django.shortcuts       import render, get_object_or_404
from django.core.paginator  import Paginator, InvalidPage
from myr.models             import Post, Event, AboutStatement


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


def calendar(request, pagenum=1):
    """Display all events in chronological order"""
    try:
        allEvents = Paginator(Event.objects.all().order_by('-date'), 25)
        eventlist = allEvents.page(int(pagenum))
    
    except:
        raise Http404

    return render(request, 'myr/calendar.html', {
        'events' : eventlist,
    })


def archive(request, pagenum=1):
    """Display archived posts using a paginator"""
    try:
        allPosts = Paginator(Post.objects.all().order_by('-date'), 25)
        postlist = allPosts.page(int(pagenum))

    except:
        raise Http404

    return render(request, 'myr/archive.html', {
        'posts'     : postlist,
    })
