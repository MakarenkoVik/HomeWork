from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):

    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        if rating < 0 or rating > 10:
            raise forms.ValidationError("Only positive ratings from 1 to 10 are allowed")
        return rating

    class Meta:
        model = Comment
        fields = ["rating", "text"]
        exclude = ["pub_date", "game"]
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        },
        labels = {
            'text': "Comment text",
        },
        help_texts = {
 	        'text': "Please, rate this game for better experience"
        }
