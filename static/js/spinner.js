// static/js/generate_exercise.js

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('exercise-form');
    const generateButton = document.getElementById('generate-button');
    const loadingSpinner = document.getElementById('loading-spinner');

    form.addEventListener('submit', function () {
        // Mostrar el spinner y deshabilitar el botón
        loadingSpinner.classList.remove('d-none');
        generateButton.disabled = true;
    });
});