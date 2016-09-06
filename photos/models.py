from django.db import models

class Photo(models.Model):

    LICENSES = (
        ('RIG', 'Copyright'),
        ('LEF', 'Copyleft'),
        ('CC', 'Creative commons')
    )

    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField()                   # Se diferencia del Charfield en que un TextField no tiene límite
    license = models.CharField(max_length=3, choices=LICENSES)
    created_at = models.DateTimeField(auto_now_add=True) # Sólo se actualiza cuando se crea
    modified_at = models.DateTimeField(auto_now=True)    # Se actualiza cuando se crea y cada vez que se actualiza

    def __str__(self):
        return self.name