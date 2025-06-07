document.getElementById('teacher-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const form = event.target;
    const selectedGroup = form.querySelector('input[name="grupo_id"]:checked');

    if (!selectedGroup) {
        alert("Por favor selecciona un grupo.");
        return;
    }

    const grupo_id = selectedGroup.value;

    try {
        const response = await fetch('/llm_api/api/teacher-recommendations/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}',
            },
            body: JSON.stringify({ id_grupo: grupo_id })
        });

        const recommendationsPanel = document.getElementById('recommendations-panel');
        const recommendationsContent = document.getElementById('recommendations-content');

        if (response.ok) {
            const data = await response.json();
            let formattedText = data.recommendations;

            // 1. Reemplazar **texto** con <strong>texto</strong> para negrillas
            formattedText = formattedText.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

            // 2. Reemplazar saltos de línea con <p> para párrafos
            formattedText = formattedText
                .split('\n') // Dividir el texto por saltos de línea
                .filter(line => line.trim() !== '') // Eliminar líneas vacías
                .map(line => `<p>${line.trim()}</p>`) // Encerrar cada línea en un <p>
                .join(''); // Unir todo nuevamente

            // 3. Insertar el contenido formateado
            recommendationsContent.innerHTML = formattedText;

            // 4. Mostrar el panel y desplazar suavemente
            recommendationsPanel.style.display = 'block';
            recommendationsPanel.scrollIntoView({ behavior: 'smooth' });

        } else {
            const errorData = await response.json();
            recommendationsContent.innerHTML = `
                <p class="error">Error: ${errorData.error}</p>
            `;
            recommendationsPanel.style.display = 'block';
        }
    } catch (error) {
        const recommendationsPanel = document.getElementById('recommendations-panel');
        recommendationsPanel.style.display = 'block';
        document.getElementById('recommendations-content').innerHTML = `
            <p class="error">Error de conexión: ${error.message}</p>
        `;
    }
});
