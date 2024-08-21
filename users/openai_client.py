import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_exercise(language, difficulty):
    prompt = f"Generate a {difficulty} {language} programming exercise. Ensure that the exercise does not require user input via `input()`."
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini-2024-07-18",  # Cambiamos al modelo mini
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates programming exercises."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

def generate_openai_feedback(user_code, expected_output, exercise_description):
    prompt = f"""
    You are a helpful programming mentor. Analyze the following exercise description and the user's code:
    
    ### Exercise Description:
    {exercise_description}
    
    ### User's Code:
    {user_code}
    
    Provide feedback to the user with the following structure:
    
    1. **Output Verification**: Start by acknowledging the user's efforts, then verify if the code produces the expected output based on the exercise.
    2. **Corrections**: If the code doesn't meet the exercise requirements, give the user clear, step-by-step instructions on what they should correct.
    3. **Improvements**: If the code is correct, offer suggestions on how the user can improve or optimize their code, or if no improvements are needed, praise them for their good work.
    4. **Encouragement**: End with a positive note, encouraging the user to keep practicing and refining their skills.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": "You are a programming expert that provides detailed feedback on coding exercises."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=300,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()