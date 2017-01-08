# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from . import models
import django.db.models


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        # image = forms.ImageField(
        #     required=True,
        # )

        fields = [
            'title',
        ]
