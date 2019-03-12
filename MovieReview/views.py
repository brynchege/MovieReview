# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import  MovieInfo

# Create your views here.

def index(request):
   all_movies = MovieInfo.objects.all()
   return render(request, "MovieReview/index.html", {"Movies": all_movies})

def AddMovie(request):
    return render(request, "MovieReview/add_movie.html")

def add_movie_form_submission(request):
   print ("Hello form is submitted.")
   movie_name = request.POST["movie_name"]
   movie_type = request.POST["movie_type"]
   movie_review = request.POST["movie_review"]
   movie_release_date = request.POST["movie_release_date"]
   movie_detail = request.POST["movie_details"]

   movie_info =  MovieInfo(movie_name=movie_name,movie_type=movie_type,movie_review=movie_review,movie_release_date=movie_release_date,movie_detail=movie_detail)

   movie_info.save()
   all_movies = MovieInfo.objects.all()
   return render(request, "MovieReview/index.html", {"Movies": all_movies})





