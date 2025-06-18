# 🧠 Detector de Estilos de Aprendizaje

Un sistema inteligente basado en **Django** que evalúa y analiza los estilos de aprendizaje de estudiantes, proporcionando recomendaciones personalizadas para docentes y estudiantes mediante inteligencia artificial.

## 🎯 Descripción del Proyecto

Este sistema educativo integral permite identificar los estilos de aprendizaje predominantes (visual, auditivo, kinestésico) de los estudiantes a través de un test interactivo. Utiliza **Google Gemini AI** y **machine learning** para generar recomendaciones personalizadas basadas en investigación académica, ayudando a docentes a planificar actividades más efectivas y a estudiantes a optimizar sus estrategias de estudio.

## ✨ Características Principales

### 🧪 Test de Estilos de Aprendizaje
- **Evaluación Interactiva**: Test dinámico que evalúa preferencias de aprendizaje
- **Validación Inteligente**: Verificación automática de respuestas completas
- **Análisis Gráfico**: Visualización de resultados con porcentajes por estilo
- **Almacenamiento Seguro**: Resultados cifrados en base de datos PostgreSQL

### 👨‍🏫 Panel de Docentes
- **Gestión de Grupos**: Crear y administrar grupos de estudiantes
- **Análisis Grupal**: Visualización de estadísticas de estilos por grupo
- **Recomendaciones IA**: Sugerencias personalizadas para planificar actividades
- **Gestión de Actividades**: Crear actividades alineadas con estilos de aprendizaje

### 👨‍🎓 Panel de Estudiantes
- **Dashboard Personalizado**: Visualización de resultados individuales
- **Recomendaciones Personalizadas**: Estrategias de estudio basadas en IA
- **Historial de Evaluaciones**: Seguimiento del progreso de aprendizaje

### 🤖 Inteligencia Artificial
- **Google Gemini AI**: Generación de recomendaciones contextuales
- **Análisis de Documentos**: Procesamiento de PDFs académicos con embeddings
- **Machine Learning**: Modelo de similitud semántica para búsqueda inteligente
- **Recomendaciones Dinámicas**: Sugerencias únicas y no repetitivas

## 🏗️ Arquitectura del Sistema

### Aplicaciones Django
- **`auth_app`**: Autenticación y dashboards principales
- **`Academico.Estudiantes`**: Gestión de perfiles estudiantiles
- **`Academico.Docentes`**: Administración de docentes
- **`Academico.Grupos`**: Gestión de grupos académicos
- **`Academico.Actividades`**: Creación y gestión de actividades
- **`Academico.Estudiantes_en_Grupos`**: Relaciones estudiante-grupo
- **`llm_api`**: API de inteligencia artificial y recomendaciones

### Base de Datos
- **PostgreSQL**: Base de datos principal
- **Modelos Relacionales**: Estructura normalizada para escalabilidad
- **Cifrado de Contraseñas**: Seguridad con Django hashers

## 🚀 Tecnologías Utilizadas

### Backend
- **Django 5.1.3**: Framework web principal
- **Django REST Framework**: API RESTful
- **PostgreSQL**: Base de datos relacional
- **django-environ**: Gestión de variables de entorno

### Inteligencia Artificial
- **Google Generative AI**: Generación de recomendaciones
- **Sentence Transformers**: Embeddings semánticos
- **Scikit-learn**: Análisis de similitud coseno
- **PDF Plumber**: Extracción de texto de documentos

### Frontend
- **HTML5/CSS3**: Interfaz responsiva
- **JavaScript**: Interactividad y validaciones
- **Bootstrap**: Framework CSS (implícito en templates)

### Herramientas de Desarrollo
- **Python 3.x**: Lenguaje de programación
- **Git**: Control de versiones
- **Django Admin**: Panel de administración

## 📋 Requisitos del Sistema

### Software Requerido
- Python 3.8 o superior
- PostgreSQL 12 o superior
- pip (gestor de paquetes de Python)

### Dependencias Principales
- Django 5.1.3
- google-generativeai 0.8.3
- sentence-transformers 3.3.1
- scikit-learn 1.6.0
- psycopg2 2.9.10

## ⚙️ Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone <url-del-repositorio>
cd Detector_Proyecto
```

### 2. Crear Entorno Virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno
Crear archivo `.env` en la raíz del proyecto:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
GOOGLE_API_KEY=your-google-api-key
```

### 5. Configurar Base de Datos
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear Superusuario (Opcional)
```bash
python manage.py createsuperuser
```

### 7. Ejecutar el Servidor
```bash
python manage.py runserver
```

## 🔧 Configuración de APIs

### Google Gemini AI
1. Obtener API key desde [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Agregar la clave al archivo `.env`
3. La API se utiliza para generar recomendaciones personalizadas

## 📊 Estructura de la Base de Datos

### Modelos Principales
- **Estudiante**: Perfiles con estilos de aprendizaje evaluados
- **Docente**: Información de profesores y asignaturas
- **Grupo**: Grupos académicos con estadísticas agregadas
- **Actividad**: Actividades educativas con estilos asociados
- **Estudiantes_en_Grupos**: Relación muchos a muchos

## 🔒 Seguridad

- **Cifrado de Contraseñas**: Uso de Django hashers
- **Validación de Sesiones**: Control de acceso por roles
- **Variables de Entorno**: Configuración sensible externalizada
- **CSRF Protection**: Protección contra ataques CSRF

## 📈 Funcionalidades Avanzadas

### Análisis de Documentos
El sistema procesa automáticamente documentos PDF académicos sobre estilos de aprendizaje para generar recomendaciones basadas en investigación científica.

### Machine Learning
- **Embeddings Semánticos**: Análisis de similitud de contenido
- **Búsqueda Inteligente**: Encuentra información relevante en documentos
- **Recomendaciones Contextuales**: Sugerencias basadas en patrones de aprendizaje

### Dashboard Analítico
- **Estadísticas Grupales**: Análisis de distribución de estilos
- **Tendencias Temporales**: Seguimiento de cambios en preferencias
- **Reportes Personalizados**: Generación de informes detallados

## 🤝 Contribución

### Autores
- **Moisés David González Bermúdez** - Desarrollador Principal
- **Carlos Andrés Jiménez Sarmiento** - [GitHub](https://github.com/CarlosCJ2306)

### Cómo Contribuir
1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Para soporte técnico o preguntas sobre el proyecto, contactar a los desarrolladores principales.

---

**Desarrollado con ❤️ para mejorar la educación mediante tecnología e inteligencia artificial.**

