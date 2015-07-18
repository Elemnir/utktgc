from difflib                        import ndiff
from django.http                    import (Http404, HttpResponseRedirect,
                                            HttpResponseForbidden)
from django.shortcuts               import render, redirect, get_object_or_404
from django.core.paginator          import Paginator, InvalidPage
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms      import PasswordChangeForm
from quill.models                   import Member, Tag, Thread, Post, PostDiff
from quill.forms                    import (UpdateInterestsForm, CreatePostForm, 
                                            CreateThreadForm)
from HTMLParser                     import HTMLParser

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def mailman(request):
    """Allow admins to access the group email lists"""
    allmem = ", ".join([m.user.email for m in Member.objects.all()])
    
    tags = Tag.objects.order_by('name')
    lists = {}
    for tag in tags:
        lists[tag.name] = [m.user.email for m in Member.objects.filter(interests=tag)]
    
    for key in lists:
        lists[key] = ", ".join(lists[key])

    return render(request, 'quill/mailman.html', {
        'allmem': allmem,
        'lists': lists,
    })

@login_required
def profile(request):
    """Allow users to modify their preferences and change their password"""
    mem = get_object_or_404(Member, user=request.user)
    msg = None
    if request.method == 'POST':
        if 'updateinterests' in request.POST:
            interestform = UpdateInterestsForm(request.POST, instance=mem)
            passwordform = PasswordChangeForm(mem.user)
            if interestform.is_valid():
                interestform.save()
                msg = 'Email lists successfully updated.'

        elif 'updatepassword' in request.POST:
            interestform = UpdateInterestsForm(instance=mem)
            passwordform = PasswordChangeForm(mem.user, request.POST)
            if passwordform.is_valid():
                passwordform.save()
                msg = 'Password successfully updated.'
    else:
        interestform = UpdateInterestsForm(instance=mem)
        passwordform = PasswordChangeForm(mem.user)

    return render(request, 'quill/profile.html', {
        'msg' : msg,
        'interestform': interestform,
        'passwordform': passwordform,
    })

def forum(request, pagenum=1):
    """Display all threads in chronological order"""
    try:
        threadlist = Paginator(Thread.objects.order_by('-sticky', '-created'), 25)
        threadlist = threadlist.page(int(pagenum))

    except:
        raise Http404

    return render(request, 'quill/forum.html', {
        'threads' : threadlist,
    })

@login_required
def add_thread(request):
    """Add a new thread"""
    if request.method == 'POST':
        form = CreateThreadForm(request.POST)
        if form.is_valid():
            thread = form.process(request.user)
            return redirect('thread', thread.pk)
    else:
        form = CreateThreadForm()
        
    return render(request, 'quill/add_thread.html', {
        'form' : form,
    })

def thread(request, val=None, pagenum=1):
    """Display all Posts for a particular thread"""
    thread = get_object_or_404(Thread, pk=val)

    # Get the posts for the requested page
    try:
        postlist = Paginator(thread.post_set.order_by('created'), 25)
        postlist = postlist.page(int(pagenum))
    
    except:
        raise Http404

    # Handle Post Submission
    if request.method == 'POST':
        mem = get_object_or_404(Member, user=request.user)
        form = CreatePostForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.thread = thread
            p.creator = mem
            p.save()
            return HttpResponseRedirect('/forum/thread/{}/{}/'.format(thread.pk, postlist.paginator.num_pages))
    else:
        form = CreatePostForm()

    return render(request, 'quill/thread.html', {
        'thread'    : thread,
        'posts'     : postlist,
        'form'      : form,
    })

def edit_post(request, val=None):
    post = get_object_or_404(Post, pk=val)
    if post.creator.user != request.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        oldbody = unicode(post.body)
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            diff = ndiff(unicode(oldbody).splitlines(), 
                unicode(form.cleaned_data.get('body','')).splitlines()
            )
            out = ''
            for line in diff:
                if line and line[0] != ' ' and line[0] != '?':
                    out = out + line.rstrip() + '\n'
            
            if out:
                PostDiff(post=post, history=out).save()
            
            form.save()
            return redirect('thread', val=post.thread.pk)
    else:
        post.body = HTMLParser().unescape(post.body)
        form = CreatePostForm(instance=post)

    return render(request, 'quill/edit_post.html', {
        'form'  : form,
    })
