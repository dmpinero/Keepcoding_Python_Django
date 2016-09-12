from django.core.exceptions import ValidationError

from photos.models import Photo
from django.forms import ModelForm

BADWORDS = ("Abollao", "Abrazafarolas", "Afilasables", "afinabanjos")

class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        exclude = ['owner']

    def clean(self):
        """
        Valida que la descripción no contenga ninguna palabrota
        :return: diccionario con los datos limpios y validados
        """
        cleaned_data = super().clean()
        description = cleaned_data.get('description', '')
        for badword in BADWORDS:
            if badword in description:
                raise ValidationError("La palabra {0} no está permitida".format(badword))

        return cleaned_data
