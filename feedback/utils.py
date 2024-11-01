import openai
import json
import re

def generate_openai_feedback(user_code, expected_output, exercise_description):
    prompt = f"""
You are a helpful programming mentor. Please analyze the following exercise description and the code provided by the student.


Exercise Description:
{exercise_description}

User's Code:
{user_code}

Expected Output:
{expected_output if expected_output else "No specific output provided."}

Please provide feedback in the following format without HTML or markdown:
1. Output Verification: Start by acknowledging the user's efforts, then verify if the code produces the expected output based on the exercise.
2. Corrections: If the code doesn't meet the exercise requirements, give the user clear, step-by-step instructions on what they should correct;
3. Improvements: If the code is correct, offer suggestions on how the user can improve or optimize their code, or if no improvements are needed, praise them for their good work;
4. Encouragement: A positive message encouraging further practice.

Respond strictly as JSON using this format:
{{
    "output_verification": "Feedback on output correctness",
    "corrections": "Necessary corrections",
    "improvements": "Suggestions or praise",
    "encouragement": "Encouraging message"
}}

Only respond in JSON format without extra text.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a programming expert that provides structured feedback on coding exercises."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1500,
        temperature=0.85
    )

    feedback_content = response['choices'][0]['message']['content'].strip()

    # Usa expresiones regulares para extraer JSON de la respuesta
    json_match = re.search(r'\{.*\}', feedback_content, re.DOTALL)
    if json_match:
        json_data = json_match.group(0)
        try:
            feedback_json = json.loads(json_data)
            return feedback_json  # Devuelve el JSON como diccionario
        except json.JSONDecodeError:
            print("Error en JSON al intentar decodificar:", json_data)
            raise ValueError("La respuesta de OpenAI no es JSON válido.")
    else:
        print("No se encontró JSON en la respuesta:", feedback_content)
        raise ValueError("No se encontró JSON válido en la respuesta de OpenAI.")