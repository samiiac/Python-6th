from django.db import models

# Create your models here.
# similar to ORM


class Blog(models.Model):
    class Meta:
        db_table = "blogs"

    # id = models.UUIDField()
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog-images',null=True)
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    
    class Meta:
        db_table = 'comments'
            
    review = models.CharField(max_length = 200)
    blog = models.ForeignKey(Blog,on_delete = models.CASCADE)
    
   
    
    

