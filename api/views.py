from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from bookstore.models import Libro, Autor
from api.serializers import LibroSerializer
import json

# Create your views here.
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
    content = {"mensaje": "Hola Mundo!"}
    return JsonResponse(content)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_libros(request):
    user = request.user.id
    libros = Libro.objects.filter(creado_por=user)
    serializer = LibroSerializer(libros, many=True)
    return JsonResponse({'libros': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_libro(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        autor = Autor.objects.get(id=payload["autor"])
        libro = Libro.objects.create(
            titulo=payload["titulo"],
            descripcion=payload["descripcion"],
            creado_por=user,
            autor=autor
        )
        serializer = LibroSerializer(libro)
        return JsonResponse({'libros': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)},  safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Algo salió mal"},  safe=False, status=status.HTTP_404_NOT_FOUND)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_libro(request, libro_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        libro_item = Libro.objects.filter(creado_por=user, id=libro_id)
        libro_item.update(**payload)
        libro = Libro.objects.get(id=libro_id)
        serializer = LibroSerializer(libro)
        return JsonResponse({'libros': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)},  safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Algo salió mal"},  safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_libro(request, libro_id):
    user = request.user.id
    try:
        libro = Libro.objects.get(creado_por=user, id=libro_id)
        libro.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)},  safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Algo salió mal"},  safe=False, status=status.HTTP_404_NOT_FOUND)
