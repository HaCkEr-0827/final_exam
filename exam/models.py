from django.db import models


class randomMadal(models.Model):
    
    full_name = models.CharField(max_length=200)
    famous_saying = models.CharField(max_length=1000)
    complite = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = "Random"
        verbose_name = "Random"
        verbose_name_plural = "Randoms"