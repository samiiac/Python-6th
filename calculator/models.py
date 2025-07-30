from django.db import models

# Create your models here.

class CalculatorHistory(models.Model):
    number_a = models.FloatField()
    number_b = models.FloatField()
    operation = models.CharField(max_length = 10)
    operation_status = models.CharField(max_length = 10)
    result = models.TextField()
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        auto_now = False
    )
    
    updated_at = models.DateTimeField(
        auto_now_add=True,
        auto_now = False
    )
    
    class Meta:
        db_table = 'calculator_history'
        
    def __str__(self):
        return self.result
    