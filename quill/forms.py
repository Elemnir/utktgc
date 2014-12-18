from django             import forms
from django.utils.html  import escape
from quill.models       import Member, Tag, Thread, Post


class SendEmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    taglist = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.order_by('name'),
        widget=forms.CheckboxSelectMultiple
    )

    def process(self):
        cd = self.cleaned_data
        tags = self.cleaned_data.get('taglist',[])
        for mem in Member.objects.filter(interests__in=tags):
            mem.user.email_user(cd['subject'],cd['message'],'UTKTGC Robot')

class UpdateInterestsForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['interests']
    interests = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.order_by('name'),
        widget=forms.CheckboxSelectMultiple
    )

class CreateThreadForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea(
        attrs={'cols':'80','rows':'10'}
        )
    )

    def process(self, user=None):
        cd = self.cleaned_data
        mem = Member.objects.get(user=user)
        t = self.cleaned_data.get('title', '')
        b = self.cleaned_data.get('body', '')
        b = escape(b)
        
        thread = Thread(title=t, creator=mem)
        thread.save()
        Post(creator=mem, thread=thread, body=b).save()
        return thread

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)
    body = forms.CharField(
        widget=forms.Textarea(
        attrs={'width':'100%'}
        )
    )
    
    def clean(self):
        cd = super(CreatePostForm, self).clean()
        self.cleaned_data['body'] = escape(cd.get('body',''))
