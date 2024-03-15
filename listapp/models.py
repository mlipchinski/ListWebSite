from django.db import models

class User(models.Model):
    # Define fields for user profile
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
    # Define fields for user permissions
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    can_create_list = models.BooleanField(default=True)
    can_edit_list = models.BooleanField(default=True)
    can_delete_list = models.BooleanField(default=True)
    can_view_list = models.BooleanField(default=True)

class List(models.Model):
    # Define fields for list
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    