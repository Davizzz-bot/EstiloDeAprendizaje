from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from Academico.Estudiantes.models import Estudiante
from Academico.Grupos.models import Grupo
import os
import pdfplumber
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
from django.conf import settings

# Configuración de la API de Google Gemini
genai.configure(api_key="")  # Coloca tu clave API válida aquí

# Inicialización del modelo de embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Ruta de los PDFs
PDF_FOLDER = os.path.join(settings.BASE_DIR, 'llm_api', 'static', 'pdf')

# Función para extraer texto de los PDFs
def extract_text_from_all_pdfs():
    text_data = []
    for file_name in os.listdir(PDF_FOLDER):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(PDF_FOLDER, file_name)
            try:
                with pdfplumber.open(file_path) as pdf:
                    for page in pdf.pages:
                        extracted_text = page.extract_text()
                        if extracted_text:
                            text_data.append(extracted_text)
            except Exception as e:
                print(f"Error al procesar {file_name}: {e}")
    return ' '.join(text_data)

# Función para encontrar fragmentos relevantes
def search_relevant_chunks(query, chunk_embeddings, chunks):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, chunk_embeddings)
    top_indexes = similarities[0].argsort()[-5:][::-1]  # Top 5 fragmentos más similares
    return [chunks[i] for i in top_indexes]

# Vista para recomendaciones de profesores
@csrf_exempt
@api_view(['POST'])
def teacher_recommendations(request):
    try:
        # Obtener el ID del grupo desde la solicitud
        data = request.data
        id_grupo = data.get('id_grupo')

        if not id_grupo:
            return Response({'error': 'ID del grupo es obligatorio.'}, status=400)

        # Buscar el grupo en la base de datos
        grupo = Grupo.objects.filter(id_grupo=id_grupo).first()
        if not grupo:
            return Response({'error': 'Grupo no encontrado.'}, status=404)

        # Obtener los porcentajes del grupo
        group_percentages = {
            "visual": grupo.visual or 0,
            "auditivo": grupo.auditivo or 0,
            "kinestesico": grupo.kinestesico or 0
        }

        # Extraer texto de los PDFs
        combined_text = extract_text_from_all_pdfs()
        if not combined_text:
            return Response({'error': 'No se pudo extraer texto de los documentos PDF.'}, status=500)

        # Dividir el texto en fragmentos
        chunks = combined_text.split('\n\n')
        chunk_embeddings = model.encode(chunks)

        # Generar los fragmentos relevantes
        query = f"Estrategias recomendadas para planificar actividades según los porcentajes: {group_percentages}"
        relevant_chunks = search_relevant_chunks(query, chunk_embeddings, chunks)
        relevant_text = ' '.join(relevant_chunks[:5])  # Limitar a 5 fragmentos relevantes

        # Crear el prompt para Google Gemini
        prompt = f"""
        Los porcentajes del grupo son los siguientes:
        Visual: {group_percentages['visual']}%, Auditivo: {group_percentages['auditivo']}%, Kinestésico: {group_percentages['kinestesico']}%.

        Basándote en los siguientes fragmentos de conocimiento extraídos de documentos académicos:

        {relevant_text}

        Genera recomendaciones concretas y específicas para que el profesor planifique actividades alineadas con estos porcentajes, trata de no repetir las mismas sugerencias y recomendar cada vez mas actividades, no solo las mismas.
        """

        # Generar respuesta utilizando Google Gemini
        gemini_model = genai.GenerativeModel("gemini-1.5-flash")
        response = gemini_model.generate_content(prompt)

        # Verificar la respuesta
        recommendations = response.text if hasattr(response, 'text') else "No se recibieron recomendaciones."

        return Response({
            "status": "success",
            "recommendations": recommendations
        }, status=200)

    except Exception as e:
        return Response({'error': f'Error interno: {str(e)}'}, status=500)

@api_view(['POST'])
def student_recommendations(request):
    try:
        data = request.data
        estudiante_id = data.get('id_estudiante')

        if not estudiante_id:
            return Response({'error': 'ID del estudiante es obligatorio.'}, status=400)

        estudiante = Estudiante.objects.filter(id_estudiante=estudiante_id).first()
        if not estudiante:
            return Response({'error': 'Estudiante no encontrado.'}, status=404)

        # Obtener porcentajes del estudiante
        learning_styles = {
            "visual": estudiante.visual or 0,
            "auditivo": estudiante.auditivo or 0,
            "kinestesico": estudiante.kinestesico or 0
        }
        
        # Extraer texto de los PDFs
        combined_text = extract_text_from_all_pdfs()
        if not combined_text:
            return Response({'error': 'No se pudo extraer texto de los documentos PDF.'}, status=500)

        # Dividir el texto en fragmentos
        chunks = combined_text.split('\n\n')
        chunk_embeddings = model.encode(chunks)

        # Generar los fragmentos relevantes
        query = f"Estrategias recomendadas para planificar actividades según los porcentajes: {learning_styles}"
        relevant_chunks = search_relevant_chunks(query, chunk_embeddings, chunks)
        relevant_text = ' '.join(relevant_chunks[:5])  # Limitar a 5 fragmentos relevantes
        
        
        # Crear prompt para Gemini
        prompt = f"""
        Basándote en los resultados del test de estilos de aprendizaje:
        Visual: {learning_styles['visual']}%, 
        Auditivo: {learning_styles['auditivo']}%, 
        Kinestésico: {learning_styles['kinestesico']}%.

        Proporciona estrategias prácticas y útiles para mejorar el rendimiento académico basado en lo siguiente {relevant_text}.
        
        **Estrategias de estudio:**  
        Para aprovechar al máximo tu estilo de aprendizaje, prueba las siguientes estrategias:
        - Identifica recursos específicos alineados a tu estilo.
        - Practica con ejemplos y herramientas que refuercen tu comprensión.
        
        Recuerda que la clave para un aprendizaje efectivo es identificar tus fortalezas y debilidades, y adaptar tus estrategias para maximizar tu potencial.
        """

        # Llamada a Gemini API
        gemini_model = genai.GenerativeModel("gemini-1.5-flash")
        response = gemini_model.generate_content(prompt)

        return Response({
            "recomendaciones": response.text
        }, status=200)

    except Exception as e:
        return Response({'error': str(e)}, status=500)
    #########################################################
    #test
    ########################################################
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from Academico.Estudiantes.models import Estudiante
from Academico.Grupos.models import Grupo
from django.db.models import Avg
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def save_test_results(request):
    if request.method == 'POST':
        try:
            estudiante_id = request.session.get('user_id')
            if not estudiante_id:
                return JsonResponse({'error': 'No se encontró el ID del estudiante en la sesión'}, status=400)

            data = json.loads(request.body)
            estudiante = Estudiante.objects.get(pk=estudiante_id)

            # Guardar resultados del test solo si los valores no son nulos o vacíos
            visual = data.get('visual')
            auditivo = data.get('auditivo')
            kinestesico = data.get('kinestesico')

            # Validar y asignar solo valores no nulos ni vacíos
            if visual not in [None, ""]:
                estudiante.visual = float(visual)
            if auditivo not in [None, ""]:
                estudiante.auditivo = float(auditivo)
            if kinestesico not in [None, ""]:
                estudiante.kinestesico = float(kinestesico)

            # Determinar el estilo predominante solo si los tres valores están completos
            if estudiante.visual is not None and estudiante.auditivo is not None and estudiante.kinestesico is not None:
                estilos = {
                    'visual': estudiante.visual,
                    'auditivo': estudiante.auditivo,
                    'kinestesico': estudiante.kinestesico
                }
                estudiante.estilo_predominante = max(estilos, key=estilos.get)

            estudiante.save()

            # Calcular promedios del grupo
            if estudiante.grupo:
                calcular_promedio_por_grupo(estudiante.grupo.id_grupo)

            return JsonResponse({'message': 'Resultados guardados correctamente',
                                 'estilo_predominante': estudiante.estilo_predominante})
        except Estudiante.DoesNotExist:
            return JsonResponse({'error': 'Estudiante no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)





from django.db.models import Avg
from Academico.Estudiantes.models import Estudiante
from Academico.Grupos.models import Grupo

def calcular_promedio_por_grupo(grupo_id):
    """
    Calcula los promedios de estilos de aprendizaje (visual, auditivo, kinestésico)
    para todos los estudiantes de un grupo y excluye a los estudiantes sin valores definidos.
    """
    try:
        # Obtener el grupo específico
        grupo = Grupo.objects.get(pk=grupo_id)

        # Filtrar estudiantes que pertenecen al grupo y tienen porcentajes válidos
        estudiantes_validos = Estudiante.objects.filter(
            grupo=grupo,
            visual__isnull=False,
            auditivo__isnull=False,
            kinestesico__isnull=False
        )

        # Si no hay estudiantes válidos, asignar 0 como promedio
        if not estudiantes_validos.exists():
            grupo.visual = 0.0
            grupo.auditivo = 0.0
            grupo.kinestesico = 0.0
        else:
            # Calcular los promedios de los estilos de aprendizaje
            promedios = estudiantes_validos.aggregate(
                promedio_visual=Avg('visual'),
                promedio_auditivo=Avg('auditivo'),
                promedio_kinestesico=Avg('kinestesico')
            )

            # Actualizar los valores en el grupo
            grupo.visual = promedios['promedio_visual'] or 0.0
            grupo.auditivo = promedios['promedio_auditivo'] or 0.0
            grupo.kinestesico = promedios['promedio_kinestesico'] or 0.0

        grupo.save()
        print(f"Promedios actualizados en grupo {grupo.nombre_grupo}")
    except Grupo.DoesNotExist:
        print(f"Error: El grupo con ID {grupo_id} no existe.")
    except Exception as e:
        print(f"Error al calcular los promedios: {e}")
