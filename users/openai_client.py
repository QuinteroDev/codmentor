from django.conf import settings

import openai
openai.api_key = settings.OPENAI_API_KEY

def generate_exercise(language, difficulty):
    prompt = f"""
    Generate a {difficulty} {language} programming exercise. 
    Please structure the exercise using plain text without markdown or special characters like hashtags, asterisks, or backticks.
    Format the output clearly and simply, using the following structure:

    1. Title of the Exercise
    2. Objective: Describe what the user is expected to accomplish.
    3. Instructions: Provide a step-by-step guide on how to complete the exercise.
    4. Example Output: Show a clear example of what the output should look like, without any unnecessary symbols or formatting.
    5. Bonus Challenge (optional): Offer additional challenges if relevant.
    Important: Ensure that the exercise does not require user input via `input()` or any other form of direct user interaction. The exercise should be fully solvable within a single code execution without needing input from the user.
    Please omit, "of the exercise" in bullet point 1, "(optional): offer additional challenges if relevant" 
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates programming exercises."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=3000,
        temperature=0.7
    )
    
    exercise_text = response['choices'][0]['message']['content'].strip()
    print(exercise_text)  # Verificar si el texto completo se genera
    return exercise_text

def generate_openai_feedback(user_code, expected_output, exercise_description):
    prompt = f"""
You are a helpful programming mentor. Analyze the following exercise description and the user's code:

Exercise Description:
{exercise_description}

User's Code:
{user_code}

Please provide feedback in plain text without using HTML tags or markdown formatting.
Separate each section with a line break, and structure the feedback in the following format:

1. Output Verification: Start by acknowledging the user's efforts, then verify if the code produces the expected output based on the exercise;

2. Corrections: If the code doesn't meet the exercise requirements, give the user clear, step-by-step instructions on what they should correct;

3. Improvements: If the code is correct, offer suggestions on how the user can improve or optimize their code, or if no improvements are needed, praise them for their good work;

Encouragement: End with a positive note, encouraging the user to keep practicing and refining their skills without numbering this section.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": "You are a programming expert that provides detailed feedback on coding exercises."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=3000,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()