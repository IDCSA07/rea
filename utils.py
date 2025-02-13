import hashlib

def cifrar_contraseña(contraseña):
    """
    Cifra una contraseña utilizando SHA-256.
    :param contraseña: La contraseña en texto plano.
    :return: La contraseña cifrada en hexadecimal.
    """
    return hashlib.sha256(contraseña.encode()).hexdigest()

def verificar_contraseña(contraseña_ingresada, contraseña_cifrada):
    """
    Verifica si una contraseña ingresada coincide con su versión cifrada.
    :param contraseña_ingresada: La contraseña en texto plano.
    :param contraseña_cifrada: La contraseña previamente cifrada.
    :return: True si coinciden, False en caso contrario.
    """
    return cifrar_contraseña(contraseña_ingresada) == contraseña_cifrada
