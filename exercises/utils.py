# exercises/utils.py
import openai
import json
import re

def generate_exercise(language, difficulty):
    prompt = f"""
You are a helpful assistant that generates diverse and creative programming exercises. Please create a {difficulty} exercise in {language} following this format and respond **strictly as JSON**:

{{
    "title": "Exercise title",
    "objective": "Objective of the exercise",
    "instructions": ["Step 1", "Step 2", "Step 3"],
    "example_output": "Expected output example",
    "bonus_challenge": "Optional challenge for the exercise"
}}

Make sure to follow this JSON structure exactly without extra text.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates diverse and creative programming exercises."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1500,
        temperature=0.85
    )

    # Obtenemos la respuesta y limpiamos el espacio en blanco
    exercise_data = response['choices'][0]['message']['content'].strip()

    # Intentamos extraer el JSON usando una expresión regular
    json_match = re.search(r'\{.*\}', exercise_data, re.DOTALL)
    if json_match:
        json_data = json_match.group(0)  # Extraemos el JSON
        try:
            return json.loads(json_data)
        except json.JSONDecodeError:
            print("Error en JSON al intentar decodificar:", json_data)
            raise ValueError("La respuesta de OpenAI no es JSON válido.")
    else:
        print("No se encontró JSON en la respuesta:", exercise_data)
        raise ValueError("No se encontró JSON válido en la respuesta de OpenAI.")