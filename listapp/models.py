"""
This module defines the data models for the application. 

It includes the User model, which represents a registered user in the system, 
and the UserPermissions model, which represents the permissions a user has in the system.
"""

# Importing Django's database models module to define our data models
from django.db import models

class User(models.Model):
    """
    User model represents a registered user in the system.
    It contains fields for the user's first name, last name, email, password, 
    creation date, modification date, activity status, date of birth, and profile picture.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

class UserPermissions(models.Model):
    """
    UserPermissions model represents the permissions a user has in the system.
    It contains fields for the user it is associated with and boolean fields for 
    different permissions like creating, editing, deleting, and viewing a list.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    can_create_list = models.BooleanField(default=True)
    can_edit_list = models.BooleanField(default=True)
    can_delete_list = models.BooleanField(default=True)
    can_view_list = models.BooleanField(default=True)

class List(models.Model):
    """
    List model represents a list created by a user.
    It contains fields for the list's name, creation date, modification date, 
    activity status, and the user it is associated with.
    """
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
