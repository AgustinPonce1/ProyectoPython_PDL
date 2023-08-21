# ARCHIVO SETUP CREACION DE PROGRAMA REDISTRIBUIBLE -- 22/08/23 --
# Comando de despliegue -> python setup.py sdist

from setuptools import setup

setup(
    name="paquete_agustin",
    version="1.0",
    description="Mi primer paquete para la entrega 2",
    author="Agustin Lucas Ponce de Leon",
    author_email="agustinlucaspdl@gmail.com",
    
    packages=["paquete_agustin"]
)