from django             import forms
from quill.models       import Member, Tag

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
