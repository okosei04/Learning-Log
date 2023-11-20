from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    #exp
    #The Meta class holds extra information for managing a model; here, it allows us to set a special attribute telling Django to use Entries when it needs to refer to more than
    # one entry. Without this, Django would refer to multiple entries as Entrys.
    class Meta:
        verbose_name_plural ='entries'

    def __str__(self):
        """Return a strimg representation of the model"""
        return f"{self.text[:50]}..."
        #explanation
        #The __str__() method tells Django which information to show when it
        #refers to individual entries. Because an entry can be a long body of text,
        #we tell Django to show just the first 50 characters of text