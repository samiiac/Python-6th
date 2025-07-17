from django.db import models

# Create your models here.
# similar to ORM


class Blog(models.Model):
    class Meta:
        db_table = "blogs"

    # id = models.UUIDField()
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    body = models.TextField()
    
class Comment(models.Model):
    
    class Meta:
        db_table = 'comments'
            
    review = models.CharField(max_length = 200)
    blog = models.ForeignKey(Blog,on_delete = models.CASCADE)
    
   
    
    

