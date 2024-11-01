// static/js/codemirror.js

document.addEventListener('DOMContentLoaded', function () {
    const codeEditorElement = document.getElementById('code-editor');
    let editor;

    if (codeEditorElement) {
        editor = CodeMirror.fromTextArea(codeEditorElement, {
            mode: 'python',  // Puedes hacer esto dinámico según el lenguaje seleccionado
            lineNumbers: true,
            theme: 'default',
            indentUnit: 20,
            tabSize: 20,
            matchBrackets: true,
        });
    }
});