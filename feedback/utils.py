import openai
import json
import re

def generate_openai_feedback(user_code, expected_output, exercise_description):
    prompt = f"""
You are a helpful programming mentor. Analyze the following exercise description and the user's code.

Exercise Description:
{exercise_description}

User's Code:
{user_code}

Expected Output:
{expected_output if expected_output else "No specific output provided."}

Please provide feedback in the following format without HTML or markdown:
1. Output Verification: Verify if the output meets expectations and acknowledge efforts.
2. Corrections: Step-by-step corrections if needed.
3. Improvements: Suggestions or praise if no improvements are needed.
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