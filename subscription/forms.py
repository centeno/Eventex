from django import forms
from subscription.models import Subscription
from django.utils.translation import ugettext_lazy as _
from subscription import validators
from Helpers.PhoneField import *

class SubscriptionForm(forms.ModelForm):
    name = forms.CharField(label=_('Nome'), max_length=100)
    cpf = forms.CharField(label=_('CPF'), max_length=11, min_length=11, validators=[validators.CpfValidator])
    email = forms.EmailField(label=_('Email'), required=False)
    phone = PhoneField()
    #phone = PhoneField(required=False)

    class Meta:
        model = Subscription
        exclude = ('created_at','paid',)
        
    def clean(self):
        super(SubscriptionForm, self).clean()
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise forms.ValidationError(_(u'Informe seu email ou telefone.'))
        return self.cleaned_data