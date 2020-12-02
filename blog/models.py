from django.db import models

# Create your models here.
GENERE_CATEGORY = (('', '------'), ('AT', 'Action'), ('ROM', 'Romantic'), ('SCI', 'Scipy'),('COM','Comedy'),('THR','Thriller'),
                    ('DOC','Documentry'),)
class Post(models.Model):
    movie_title=models.CharField(max_length=100)
    release_date=models.DateField(auto_now_add=True,null=True)
    genere=models.CharField(max_length=100,choices=GENERE_CATEGORY)
    plot=models.TextField(null=True)
    image=models.ImageField(upload_to='mve/')
    rating=models.IntegerField(default=1)
    def __str__(self):
        return self.movie_title