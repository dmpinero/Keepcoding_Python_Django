from django.core.exceptions import ValidationError


BADWORDS = ("Abollao", "Abrazafarolas", "Afilasables", "afinabanjos")


def badwords(description):
    """
    Valida que la descripción no contenga ninguna palabrota
    :return: diccionario con los datos limpios y validados
    """
    for badword in BADWORDS:
        if badword in description:
            raise ValidationError("La palabra {0} no está permitida".format(badword))

    return True