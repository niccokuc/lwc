from django import forms
#from django.forms import ModelForm
from joins.models import Join

class EmailForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(required=True)

class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = "__all__" # i had to get this from web search must include all fields.

#
# >>> from django.forms import ModelForm
# >>> from myapp.models import Article
#
# # Create the form class.
# >>> class ArticleForm(ModelForm):
# ...     class Meta:
# ...         model = Article
# ...         fields = ['pub_date', 'headline', 'content', 'reporter']