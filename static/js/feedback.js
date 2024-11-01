document.addEventListener('DOMContentLoaded', function () {
    const startExerciseBtn = document.getElementById('start-exercise-btn');
    const exerciseContainer = document.getElementById('exercise-container');
    const runCodeBtn = document.getElementById('run-code-btn');
    const loadingSpinnerFeedback = document.getElementById('loading-spinner-feedback');
    const exerciseResult = document.getElementById('exercise-result');
    let editor;

    // Mostrar el editor de código al hacer clic en "Start Exercise"
    startExerciseBtn.addEventListener('click', function () {
        // Mostrar el contenedor del ejercicio
        exerciseContainer.classList.remove('d-none');
        
        // Inicializar CodeMirror solo una vez
        if (!editor) {
            editor = CodeMirror.fromTextArea(document.getElementById('code-editor'), {
                mode: 'python',  // Esto puede ser dinámico en función del lenguaje
                lineNumbers: true,
                theme: 'default',
                indentUnit: 4,
                tabSize: 4,
                matchBrackets: true,
            });
        }
    });

    // Lógica para el botón de "Run Code"
    runCodeBtn.addEventListener('click', function (event) {
        event.preventDefault();
        const code = editor.getValue();
        const exerciseDescription = "{{ exercise|escapejs }}";  // Descripción del ejercicio, pasada desde Django
        
        // Mostrar el spinner de carga mientras se obtiene feedback
        loadingSpinnerFeedback.classList.remove('d-none');
        runCodeBtn.disabled = true;

        fetch('/feedback/run-code/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}',
            },
            body: JSON.stringify({ code, exercise_description: exerciseDescription })
        })
        .then(response => {
            if (!response.ok) throw new Error('Network response was not ok');
            return response.json();
        })
        .then(data => {
            // Ocultar el spinner una vez que se recibe el feedback
            loadingSpinnerFeedback.classList.add('d-none');
            runCodeBtn.disabled = false;

            if (data.feedback) {
                const feedback = data.feedback;
                // Renderizar feedback en el DOM
                exerciseResult.innerHTML = `
                    <h4 class="font-weight-bold">Output Verification:</h4>
                    <p>${feedback.output_verification || "No verification provided."}</p>
                    
                    <h4 class="font-weight-bold">Corrections:</h4>
                    <p>${feedback.corrections || "No corrections needed."}</p>
                    
                    <h4 class="font-weight-bold">Improvements:</h4>
                    <p>${feedback.improvements || "No improvements suggested."}</p>
                    
                    <h4 class="font-weight-bold">Encouragement:</h4>
                    <p>${feedback.encouragement || "Keep up the great work!"}</p>
                `;
            } else {
                exerciseResult.innerHTML = `<p class="text-danger">No feedback available.</p>`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            exerciseResult.innerHTML = `<p class="text-danger">Error: ${error.message}</p>`;
            loadingSpinnerFeedback.classList.add('d-none');
            runCodeBtn.disabled = false;
        });
    });
});