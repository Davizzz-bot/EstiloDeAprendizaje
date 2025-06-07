// Función para obtener el ID del estudiante desde el contenedor principal
function getStudentId() {
    const container = document.querySelector('.main-container');
    return container.getAttribute('data-student-id');
}

document.getElementById('generate-recommendations').addEventListener('click', async function () {
    const recommendationsPanel = document.getElementById('recommendations-panel');
    const recommendationsContent = document.getElementById('recommendations-content');
    const studentId = getStudentId();  // Obtener el ID del estudiante dinámicamente

    if (!studentId) {
        recommendationsContent.innerHTML = "<p class='error'>Error: No se encontró el ID del estudiante.</p>";
        recommendationsPanel.style.display = 'block';
        return;
    }

    recommendationsContent.innerHTML = "<p>Cargando recomendaciones...</p>";
    recommendationsPanel.style.display = 'block';

    try {
        const response = await fetch('/llm_api/api/student-recommendations/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
            body: JSON.stringify({ id_estudiante: studentId })
        });

        if (response.ok) {
            const data = await response.json();
            let formattedText = data.recomendaciones || "No se generaron recomendaciones.";

            // Reemplazar **texto** con <strong>texto</strong> y saltos de línea
            formattedText = formattedText.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
            formattedText = formattedText.split('\n')
                .filter(line => line.trim() !== '')
                .map(line => `<p>${line.trim()}</p>`)
                .join('');

            recommendationsContent.innerHTML = formattedText;
        } else {
            recommendationsContent.innerHTML = "<p class='error'>Hubo un problema al generar las recomendaciones.</p>";
        }
    } catch (error) {
        recommendationsContent.innerHTML = `<p class='error'>Error de conexión: ${error.message}</p>`;
    }
});

// Función para obtener el CSRF Token
function getCSRFToken() {
    let cookieValue = null;
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith('csrftoken=')) {
            cookieValue = cookie.substring('csrftoken='.length, cookie.length);
            break;
        }
    }
    return cookieValue;
}
