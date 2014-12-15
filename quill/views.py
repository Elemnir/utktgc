from django.shortcuts               import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms      import PasswordChangeForm
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
