from django.shortcuts import render, redirect
from Academico import Estudiantes_en_Grupos
from Academico.Docentes.models import Docente
from Academico.Estudiantes.models import Estudiante
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password  # Para validar contraseñas cifradas
from Academico.Docentes.models import Docente
from Academico.Estudiantes.models import Estudiante
from Academico.Grupos.models import Grupo
from Academico.Estudiantes_en_Grupos.models import Estudiantes_en_Grupos


def login_view(request):
    error_message = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Intentar autenticar como Docente
        try:
            docente = Docente.objects.get(usuario=username)
            if check_password(password, docente.contrasena):
                request.session['user_id'] = docente.id_docente
                request.session['role'] = 'docente'
                return redirect('teacher_dashboard')
        except Docente.DoesNotExist:
            pass

        # Intentar autenticar como Estudiante
        try:
            estudiante = Estudiante.objects.get(usuario=username)
            if check_password(password, estudiante.contrasena):
                request.session['user_id'] = estudiante.id_estudiante
                request.session['role'] = 'estudiante'
                return redirect('student_dashboard')
        except Estudiante.DoesNotExist:
            pass

        # Si falla la autenticación
        error_message = "Usuario o contraseña incorrectos."

    return render(request, 'login.html', {"error": error_message})

def logout_view(request):
    request.session.flush()  # Limpiar la sesión
    return redirect('login')



def teacher_dashboard(request):
    if request.session.get('role') != 'docente':
        return redirect('login')

    docente_id = request.session.get('user_id')
    docente = Docente.objects.get(pk=docente_id)

    # Obtener los grupos asociados al docente
    grupos = Grupo.objects.filter(
        id_grupo__in=Estudiantes_en_Grupos.objects.filter(
            id_docente=docente
        ).values('id_grupo')
    )

    return render(request, 'teacher.html', {
        'docente': docente,
        'grupos': grupos
    })



def student_dashboard(request):
    # Verificar si el usuario tiene rol de estudiante
    if request.session.get('role') != 'estudiante':
        return redirect('login')

    # Obtener los datos del estudiante
    estudiante_id = request.session.get('user_id')
    try:
        estudiante = Estudiante.objects.get(pk=estudiante_id)
    except Estudiante.DoesNotExist:
        return redirect('login')  # Si no existe, redirigir al login

    # Verificar si faltan porcentajes (visual, auditivo, kinestésico)
    if estudiante.visual is None or estudiante.auditivo is None or estudiante.kinestesico is None:
        return redirect('test_page')  # Redirigir a la página del test si los datos faltan

    # Renderizar la página principal del estudiante
    return render(request, 'student.html', {'estudiante': estudiante})


def test_page(request):
    if request.session.get('role') != 'estudiante':
        return redirect('login')

    # Aquí puedes incluir lógica adicional si necesitas validar algo
    return render(request, 'test.html')


#####################################
from django.shortcuts import render

def index_view(request):
    # Simplemente renderiza la página principal sin validaciones de sesión
    return render(request, 'index.html')

