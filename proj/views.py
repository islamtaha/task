# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, render_to_response
from proj.forms import RegForm, UploadFileForm, DistanceForm, EditProfileForm
from django.template import RequestContext
import googlemaps
#from django.contrib.gis.geos import Point, GEOSGeometry
from math import *
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
	return render(request, 'proj/loginsuccess.html')

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')
    else:
        form = RegForm()
        arg = {'form': form}
        return render(request, 'proj/reg_form.html',arg)


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'proj/profile.html', args)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/account/success/upload')
    else:
        form = UploadFileForm()
    return render(request, 'proj/upload.html', {
        'form': form
    })


def upload_success(request):
    return render(request, 'proj/successupload.html')


def greatCircleDistance((lat1, lon1), (lat2, lon2)):
  def haversin(x):
    return sin(x/2)**2 
  lat1 = radians(lat1)
  lon1 = radians(lon1)
  lat2 = radians(lat2)
  lon2 = radians(lon2)
  return 2 * asin(sqrt(
      haversin(lat2-lat1) +
      cos(lat1) * cos(lat2) * haversin(lon2-lon1)))


def distance(request):
    dist = 0
    if request.method == 'POST':
        form = DistanceForm(request.POST)
        if form.is_valid():
            gmaps = googlemaps.Client(key='AIzaSyD4TwlFcF3yeY9uNyX3o7B3cal1SjV6P7k')
            location1 = form.cleaned_data['location1']
            location2 = form.cleaned_data['location2']
            loc1 = gmaps.geocode(location1)[0]['geometry']['location']
            loc2 = geocode_result = gmaps.geocode(location2)[0]['geometry']['location']
            #point1 = GEOSGeometry('SRID=4326;POINT(%s %s)'% (loc1['lng'], loc1['lat']))
            #point2 = GEOSGeometry('SRID=4326;POINT(%s %s)'% (loc2['lng'], loc2['lat']))
            #dist = point1.distance(point2)
            dist = greatCircleDistance((loc1['lat'], loc1['lng']), (loc2['lat'], loc2['lng'])) * 6371

    form = DistanceForm()
    arg = {'form': form, 'dist': dist}
    return render(request, 'proj/distance.html',arg)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance = request.user)
        args = {'form':form}
        return render(request, 'proj/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change_password')
    else:
        form = PasswordChangeForm(user = request.user)
        args = {'form':form}
        return render(request, 'proj/change_password.html', args)


