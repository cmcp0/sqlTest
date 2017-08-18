from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

import json
import logging
import hashlib

from django.apps import apps
from .models import *
from .forms import *

# Create your views here.
def index(request):
    request.session.clear_expired()
    if "pogU" not in request.session:
        # request.session['pogU'] = "asdf"
        # return HttpResponse(":(")
        return render_to_response("login.html")

    else:

        return render_to_response("index.html",{
            'request': request,
            'perfilUsuario': 'A',
            'modelList': apps.get_app_config('app').get_models()
        })

def logout(request):
    request.session.flush()
    return render_to_response("login.html")
    
def login(request):

    if "pogU" not in request.session:
        if request.method == 'POST':
            logging.error(request.POST.get('user', False))
            logging.error(request.body)
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            # body = json.loads(request.body)
            content = body['user']
            try:
                user = Usuario.objects.get(usuario=content)
                hash = hashlib.md5()
            except (KeyError, Usuario.DoesNotExist):
                return JsonResponse({'success': False, 'msg': 'Usuario no existe'})
            else:
                hash.update(bytes(body['pass'], encoding='utf-8'))
                h = hash.hexdigest()
                logging.error(h + " " + user.clave)
                if user.clave == h:
                    token = hashlib.md5()
                    token.update(bytes(str(user.id_usuario), encoding='utf-8'))
                    request.session['pogU'] = token.hexdigest()
                    request.session['UId'] = user.id_usuario
                    request.session.set_expiry(0)
                    # return HttpResponseRedirect('/app/index')
                    return JsonResponse({'success': True, 'msg': 'Validado'})

                else:
                    return JsonResponse({'success': False, 'msg': 'Usuario no existe'})

        else:
            return render_to_response("login.html")
    else:
        return HttpResponseRedirect('/app/index')

def brw(request, tabla):
    request.session.clear_expired()

    if "pogU" in request.session:
        # request.session['UId'] #TODO check permissions

        found = getModelo(tabla)
        if found['found']:
            return render_to_response("brw.html", {
                'request': request,
                'tabla': tabla,
                'perfilUsuario': 'A',
                'modelList': apps.get_app_config('app').get_models(),
                'registros': found['modelo'].objects.all(),
                'forms': found['form']
            })
        else:
            raise Http404("?")
    else:
        return render_to_response("login.html")

def guardar(request, tabla):
    if "pogU" not in request.session:
        # request.session['pogU'] = "asdf"
        # return HttpResponse(":(")
        return JsonResponse({'success': False, 'msg': 'Sesion ha finalizado'})

    else:
        if request.method == 'POST':
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            # logging.error('id_'+tabla[0].lower()+tabla[1:])
            modelo = getModelo(tabla)
            registro = modelo['modelo'](**body)

            # if ('id_'+tabla[0].lower()+tabla[1:]) in body:
            #     logging.error("actualizar")
            # else:
            #     logging.error("guardar")
            try:
                # keys = list(body.values())
                # logging.error(keys[0])
                if tabla == "Usuario":
                    hash = hashlib.md5()
                    hash.update(bytes(registro.clave, encoding='utf-8'))
                    registro.clave = hash.hexdigest()
                registro.save()
            except Exception as e:
                return JsonResponse({'success': False, 'msg': 'Error al guardar registro' })
            else:
                return JsonResponse({'success': True, 'msg': 'Guardado exitoso' })

        else:
            return JsonResponse({'success': False, 'msg': 'Metodo: ' + request.method + ' no permitido' })

def seleccionar(request, tabla):
    if "pogU" not in request.session:

        return JsonResponse({'success': False, 'msg': 'Sesion ha finalizado'})
    else:
        if request.method == 'POST':
            modelo = getModelo(tabla)
            registro = modelo['modelo']
            data = {}
            try:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                reg = registro.objects.get(pk = body['id'])
                if tabla == 'Usuario':
                    reg.clave = ''
                data = model_to_dict(reg)
            except Exception as e:
                logging.error(e)
                return JsonResponse({'success': False, 'msg': 'Error al buscar registro'})
            else:
                return JsonResponse({'success': True, 'msg': 'Registro encontrado', 'data': data })
        else:
            return JsonResponse({'success': False, 'msg': 'Metodo: ' + request.method + ' no permitido' })

def borrar(request, tabla):
    if "pogU" not in request.session:
        return JsonResponse({'success': False, 'msg': 'Sesion ha finalizado'})
    else:
        if request.method == 'POST':
            modelo = getModelo(tabla)
            registro = modelo['modelo']
            try:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                reg = registro.objects.get(pk = body['id'])
                reg.delete()
            except Exception as e:
                return JsonResponse({'success': False, 'msg': 'Error al borrar registro'})
            else:
                return JsonResponse({'success': True, 'msg': 'Borrado exitoso' })
# ---------------------------------------

def getModelo(tabla):

    found = False
    modelo = {}
    form = {}
    # logging.error(getForms())
    for model in apps.get_app_config('app').get_models():
        # logging.error(model.__name__)
        if model.__name__ == tabla:
            found = True
            modelo = model
            for item in getForms():
                if item['name'] == tabla+'Form':
                    form = item['form']()

    return {
        'found': found,
        'modelo': modelo,
        'form': form
    }
