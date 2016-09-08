from django.db import models
from django.contrib.auth.models import User

LICENSE_COPYRIGHT = 'RIG'
LICENSE_COPYLEFT = 'LEF'
LICENSE_CC = 'CC'

LICENSES = (
    (LICENSE_COPYRIGHT, 'Copyright'),
    (LICENSE_COPYLEFT, 'Copyleft'),
    (LICENSE_CC, 'Creative commons')
)

VISIBILITY_PUBLIC = 'PUB'
VISIBILITY_PRIVATE = 'PRI'

VISIBILITY = (
    (VISIBILITY_PUBLIC, 'Pública'),
    (VISIBILITY_PRIVATE, 'Privada')
)

class Photo(models.Model):

    owner = models.ForeignKey(User)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(null=True, blank=True) # Se diferencia del Charfield en que un TextField no tiene límite
    license = models.CharField(max_length=3, choices=LICENSES, default=LICENSE_CC)
    created_at = models.DateTimeField(auto_now_add=True) # Sólo se actualiza cuando se crea
    modified_at = models.DateTimeField(auto_now=True)    # Se actualiza cuando se crea y cada vez que se actualiza
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=VISIBILITY_PUBLIC)

    def __str__(self):
        return self.name