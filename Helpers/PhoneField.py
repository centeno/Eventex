# -*- coding: ascii -*-
from django import forms
from django.core.validators import EMPTY_VALUES

class PhoneWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (
                   forms.TextInput(attrs=attrs),
                   forms.TextInput(attrs=attrs))
        super(PhoneWidget, self).__init__(widgets, attrs)
        
    def decompress(self, value):
        if value:
            return value.split('-')
        return [None, None]


class PhoneField(forms.MultiValueField):
    widget = PhoneWidget
    
    def __init__(self, *args, **kwargs):
        fields = (
                  forms.IntegerField(),
                  forms.IntegerField())
        super(PhoneField, self).__init__(fields, *args, **kwargs)
        
    def compress(self, data_list):
        if data_list:
            if data_list[0] in EMPTY_VALUES:
                raise forms.ValidationError(u'DDD invalido.')
            if data_list[1] in EMPTY_VALUES:
                raise forms.ValidationError(u'Numero invalido.')
            return '%s-%s' % tuple(data_list)
        return None