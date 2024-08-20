import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_exercise(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Puedes usar el modelo adecuado
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates programming exercises."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()