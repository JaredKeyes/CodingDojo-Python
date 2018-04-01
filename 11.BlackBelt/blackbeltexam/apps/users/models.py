# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def validate_login(self, post):
        user = User.objects.filter(email=post['email']).first()
        if user and bcrypt.checkpw(post['password'].encode(), user.password.encode()):
            return { 'status': True, 'user': user }
        else:
            return { 'status': False, 'error': 'Invalid Credentials' }


    def validate_registration(self, post):
        errors = []
        if post['name'] == '':
            errors.append('Name cannot be blank')
        if post['email'] == '':
            errors.append('Email cannot be blank')
        user = User.objects.filter(email=post['email']).first()
        if user:
            errors.append('Email already in use')
        if len(post['password']) < 4:
             errors.append('Password must be at least four characters')
        elif post['password'] != post['password_confirmation']:
            errors.append('Passwords do not match')

        if not errors:
            user = User.objects.create(
                name=post['name'],
                email=post['email'],
                password=bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt(10))
            )
            return { 'status': True, 'user': user }
        else:
            return { 'status': False, 'errors': errors }   

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trip(models.Model):
    user = models.ForeignKey(User, related_name='Owner')
    destination = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    plan = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Trip_Join(models.Model):
    trip = models.ForeignKey(Trip, related_name='trip')
    attendee = models.ForeignKey(User, related_name='attendee')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
