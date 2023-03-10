from django.http import HttpResponse
from django.template import Template,Context
import datetime

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
    

def saludo (request):
    doc_externo=open('C:/Users/JesusM/Desktop/ciclo 2022-2/repo1/django/backend/prueba1/prueba1/template/index.html')
    plt=Template(doc_externo.read())
    doc_externo.close()
    # nombre='numero'
    p1=Persona('uno','dos')
    dia=datetime.datetime.now()
    lista=['plantillas','modelos','formularios','vistas','despliegue']
    ctx=Context({'nombre':p1.nombre,'apellido':p1.apellido,'dia':dia,'temas':lista})
    documento=plt.render(ctx)
    return HttpResponse(documento)

def edades(request,edad):
    if edad < 18:
        return HttpResponse("Eres menor de edad")
    else:
        return HttpResponse("Eres mayor de edad")