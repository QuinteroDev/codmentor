import openai
import json
import re



def generate_openai_feedback(user_code, expected_output, exercise_description):
    prompt = f"""
You are a helpful programming mentor. Analyze the following exercise description and the user's code:

Exercise Description:
{exercise_description}

User's Code:
{user_code}

Please provide feedback in plain text without using HTML tags or markdown formatting. Ensure the feedback is varied and avoids repeating common phrases.
Separate each section with a line break, and structure the feedback in the following format:

1. Output Verification: Start by acknowledging the user's efforts, then verify if the code produces the expected output based on the exercise;

2. Corrections: If the code doesn't meet the exercise requirements, give the user clear, step-by-step instructions on what they should correct;

3. Improvements: If the code is correct, offer suggestions on how the user can improve or optimize their code, or if no improvements are needed, praise them for their good work;

Encouragement: End with a positive note, encouraging the user to keep practicing and refining their skills without numbering this section.
Please ensure the feedback is unique and not repetitive.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Cambiado a un modelo más económico para pruebas
        messages=[
            {"role": "system", "content": "You are a programming expert that provides detailed feedback on coding exercises."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1500,
        temperature=0.85
    )
    return response['choices'][0]['message']['content'].strip()