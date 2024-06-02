from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

""" 
Item: This is the name of your model. In Django, each model represents a database table. In this case, 
the Item model will correspond to a table named yourappname_item in your database, 
where yourappname is the name of your Django app.

models.Model: This is the base class for all     Django models. By subclassing models.Model, 
your Item class inherits various features and functionalities provided by Django's ORM (Object-Relational Mapping) system.

name: This is a field of type CharField. It represents the name of the item. The max_length parameter specifies 
the maximum number of characters allowed for this field.

description: This is a field of type TextField. It represents the description of the item. Unlike CharField, 
TextField is suitable for longer pieces of text without a predefined maximum length.

created_at: This is a field of type DateTimeField. It represents the date and time when the item was created. 
The auto_now_add parameter is set to True, which means that the field will automatically be set to the current date and 
time when a new Item object is created.

By defining this model, you've created a blueprint for storing items in your database. Each Item object will have a name, description,
 and creation timestamp associated with it. You can perform various database operations such as creating, updating, deleting,
   and querying Item objects using Django's ORM.
"""