from django.shortcuts               import render
from django.contrib.auth.decorators import login_required, user_passes_test
from quill.models                   import Member
from quill.forms                    import SendEmailForm, UpdateInterestsForm

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def mailman(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():
            form.process()
            return render(request, 'quill/mailman.html', {
                'msg' : 'Success! Emails sent.'
            })
    else:
        form = SendEmailForm()

    return render(request, 'quill/mailman.html', {
        'form': form,
    })

@login_required
def profile(request):
    mem = Member.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdateInterestsForm(request.POST, instance=mem)
        if form.is_valid():
            form.save()
            return render(request, 'quill/profile.html', {
                'msg' : 'Email lists successfully updated.',
                'form' : form,
            })
    else:
        form = UpdateInterestsForm(instance=mem)

    return render(request, 'quill/profile.html', {
        'form': form,
    })
