'''
Created on Mar 13, 2012

@author: thacdu
'''
from flashcardapp.models import FlashCard
from django import forms
import settings

GRADE_CHOICES = (
    ('first', '1st Grade'),
    ('second', '2nd Grade'),
    ('third', '3rd Grade'),
    ('fourth', '4th Grade'),
    ('fifth', '5th Grade'),
    ('sixth', '6th Grade'),
    ('seventh', '7th Grade'),
    ('eighth', '8th Grade'),
    ('ninth', '9th Grade'),
    ('tenth', '10th Grade'),
    ('eleventh', '11th Grade'),
    ('twelfth', '12th Grade'),
    ('college', 'College'),
    ('other', 'Other'),
)

SUBJECT_CHOICES = (
    ('art', 'Art'),
    ('bae', 'Business & Economics'),
    ('cos', 'Computer Science'),
    ('geo', 'Geography'),
    ('gov', 'Government & Politics'),
    ('his', 'History'),
    ('mat', 'Math'),
    ('mus', 'Music'),
    ('fol', 'Foreign Language'),
    ('sci', 'Science'),
    ('peh', 'PE & Health'),
    ('rel', 'Religion'),
)

class FlashCardForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=200)
    description = forms.CharField(
        widget = forms.Textarea(attrs = {'cols': 100, 'rows': 2}),
        required = True,
        min_length=10,
    )
    grade = forms.ChoiceField(
        choices = GRADE_CHOICES)
    subject = forms.ChoiceField(
        choices = SUBJECT_CHOICES)
    
    class Meta:
        model = FlashCard
        exclude = ('user', 'vote', 'uservote')

    def save(self):
        new_flashcard = FlashCard()
        new_flashcard.title = self.cleaned_data['title']
        new_flashcard.description = self.cleaned_data['description']
        new_flashcard.grade = self.cleaned_data['grade']
        new_flashcard.subject = self.cleaned_data['subject']
        return new_flashcard

class PromptForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PromptForm, self).__init__(*args, **kwargs)
        for i in xrange(settings.QuestNumber):
            if i < 9:
                self.fields['Prompt_%d' % (i+1)] = forms.CharField(label='Prompt 0%d' % (i+1), required=False)
                #self.fields['Prompt_%d' % (i+1)].widget.attrs = {'name': 'q%s' % i}
                self.fields['Answer_%d' % (i+1)] = forms.CharField(label='Answer 0%d' % (i+1), required=False)
                #self.fields['Answer_%d' % (i+1)].widget.attrs = {'name': 'a%s' % i}
            else:
                self.fields['Prompt_%d' % (i+1)] = forms.CharField(required=False)
                #self.fields['Prompt_%d' % (i+1)].widget.attrs = {'name': 'q%s' % i}
                self.fields['Answer_%d' % (i+1)] = forms.CharField(required=False)
                #self.fields['Answer_%d' % (i+1)].widget.attrs = {'name': 'a%s' % i}


class UploadFileForm(forms.Form):
    file  = forms.FileField()


    