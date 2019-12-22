from django.db import models

# Create your models here.


class Blog(models.Model):
    title= models.CharField(max_length=200)
    date= models.DateTimeField()
    body= models.TextField()
    image= models.ImageField(upload_to='images/')

    def summary(self):   # function for getting rid of display full body details
        return self.body[:60] #For getting first 100 characters of body field

    def uploaded_date(self):
        return self.date.strftime(' %b %e %Y ')  # To display in the format Sep 19 2019 

    def __str__(self):  # This is used to display name as title in admin page  without this it will be looking like : Blog object (4)
        return self.title