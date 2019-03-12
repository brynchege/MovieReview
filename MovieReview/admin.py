# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import MovieInfo, MovieInfo_Test
# Register your models here.

admin.site.register(MovieInfo)
admin.site.register(MovieInfo_Test)