from django import forms
#from django.contrib.auth.models import User
from django.db.models import Count
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Submit
from .models import OfertyMiasto, OfertyTyp
from envelope.forms import ContactForm
from django.utils.translation import ugettext_lazy as _
from collections import OrderedDict
from django.conf import settings

RODZAJ = (('1', 'sprzedaż'), ('3','najem'))

class OfertySearchForm(forms.Form):

    rodzaj = forms.ChoiceField(
        widget=forms.Select(attrs = {'name': 'rodzaj'}), choices = RODZAJ,
        label = "")

    typ = forms.ModelChoiceField(queryset=OfertyTyp.objects.all(),
                                 empty_label=None, label="")

    miasto = forms.ModelChoiceField(OfertyMiasto.objects.filter(
        ofertyest__status = 0).annotate(num_est = Count('ofertyest')).order_by(
            'prior', 'nazwa'), empty_label = None, label = "")


class CategorizedContactForm(ContactForm):

    CATEGORY_CHOICES = (
        ('', _("Choose")),
        (1, _("Oferty: Ustroń, Brenna, Górki, Skoczów")),
        (2, _("Oferty: Wisła, Istebna, Jaworzynka, Koniaków, Cieszyn")),
        (10, _("A general question regarding the website")),
        # ... any other choices you can imagine
        (11, _("Other")),
    )
    category = forms.ChoiceField(label=_("Category"), choices=CATEGORY_CHOICES)

    def __init__(self, *args, **kwargs):
        """
        Category choice will be rendered above the subject field.
        """
        super(CategorizedContactForm, self).__init__(*args, **kwargs)
        keys = [ 'category', 'email', 'message', 'subject', 'sender' ]
        self.fields['subject'].widget = forms.HiddenInput()
        self.fields['sender'].widget = forms.HiddenInput()
        self.fields['subject'].initial = 'zapytanie'
        self.fields['sender'].initial = 'no name'
        self.fields = OrderedDict(sorted(self.fields.items(), key = lambda x: keys.index(x[0])))

    def get_email_recipients(self):
        category = int(self.cleaned_data['category'])
        if category not in (1,2):
            return settings.ENVELOPE_EMAIL_RECIPIENTS
        
        return settings.ENVELOPE_EMAIL_RECIPIENTS_MAP[category] 
    
    def get_context(self):
        """
        Adds full category description to template variables in order
        to display the category in email body.
        """
        context = super(CategorizedContactForm, self).get_context()
        context['category'] = self.get_category_display()
        return context

    def get_category_display(self):
        """
        Returns the displayed name of the selected category.
        """
        try:
            category = int(self.cleaned_data['category'])
        except (AttributeError, ValueError, KeyError):
            category = None
        return dict(self.CATEGORY_CHOICES).get(category)


class DetailContactForm(ContactForm):

    def __init__(self, *args, **kwargs):
        """
        Category choice will be rendered above the subject field.
        """
        super(DetailContactForm, self).__init__(*args, **kwargs)
        keys = [ 'email', 'message', 'subject', 'sender' ]
        self.fields['subject'].widget = forms.HiddenInput()
        self.fields['sender'].widget = forms.HiddenInput()
        self.fields['subject'].initial = 'oferta'

        self.fields = OrderedDict(sorted(self.fields.items(), key = lambda x: keys.index(x[0])))
