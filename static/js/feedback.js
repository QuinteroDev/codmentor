// static/js/feedback.js

document.addEventListener('DOMContentLoaded', function () {
    const runCodeBtn = document.getElementById('run-code-btn');
    const exerciseResult = document.getElementById('exercise-result');
    const codeEditorElement = document.getElementById('code-editor');
    
    let editor;
    if (codeEditorElement) {
        editor = CodeMirror.fromTextArea(codeEditorElement, {
            mode: 'python',
            lineNumbers: true,
            theme: 'default',
            indentUnit: 4,
            tabSize: 4,
            matchBrackets: true,
        });
    }

    if (runCodeBtn) {
        runCodeBtn.addEventListener('click', function(event) {
            event.preventDefault();

            const code = editor.getValue();
            const exerciseDescription = "{{ exercise|escapejs }}"; // Esto se pasará desde Django

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
                exerciseResult.innerText = data.feedback || "No feedback available.";
            })
            .catch(error => {
                console.error('Error:', error);
                exerciseResult.innerText = `Error: ${error.message}`;
            });
        });
    }
});