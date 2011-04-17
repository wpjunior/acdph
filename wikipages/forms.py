from django.forms import ModelForm
from wikipages.models import Page
# Create the form class.
class PageForm(ModelForm):
    class Meta:
        model = Page
        exclude = ('url', 'template_name')
