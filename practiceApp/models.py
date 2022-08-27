from django.db import models

# Create your models here.


class PostModel(models.Model):

    title = models.CharField(
        choices=(('choose a title', 'Choose A Title'), ('mr', 'MR'),
                 ('mrs', 'MRS'),
                 ('miss', 'MISS')), max_length=14, default='choose a title'
    )
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.firstname} | {self.lastname}"
