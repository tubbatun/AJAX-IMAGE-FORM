# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.db import models


class Image(models.Model):

    title = models.CharField(
        max_length=240,
        verbose_name='Post title',
        unique=True,
        )
    # Attributes
    # image = models.ImageField(
    #     _('image'),
    #     upload_to='images/%Y/%m/%d'
    # )
    # Meta Data
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Meta
    class Meta:
        ordering = ['id']
        verbose_name = _('image')
        verbose_name_plural = _('images')

    # Functions
    def __str__(self):
        return "%s" % (self.id)

    def __unicode__(self):
        return "%s" % (self.id)
