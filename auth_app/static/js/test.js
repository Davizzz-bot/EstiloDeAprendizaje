document.getElementById('learning-style-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const answers = {};

    for (const [key, value] of formData.entries()) {
        answers[value] = (answers[value] || 0) + 1;
    }

    const totalQuestions = Object.values(answers).reduce((a, b) => a + b, 0);
    const percentages = {
        visual: ((answers.visual || 0) / totalQuestions * 100).toFixed(2),
        auditivo: ((answers.auditivo || 0) / totalQuestions * 100).toFixed(2),
        kinestesico: ((answers.kinestesico || 0) / totalQuestions * 100).toFixed(2),
    };

    try {
        const response = await fetch('/llm_api/api/save-test-results/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
            body: JSON.stringify(percentages),
        });

        if (response.ok) {
            const data = await response.json();
            alert(`Resultados guardados correctamente. Estilo predominante: ${data.estilo_predominante}`);
            location.href = '/auth/student/';
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.error}`);
        }
    } catch (error) {
        console.error('Error al enviar los resultados:', error);
        alert('Error de conexión. Inténtalo de nuevo.');
    }
});

function getCSRFToken() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}
