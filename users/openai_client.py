from django.conf import settings

import openai
openai.api_key = settings.OPENAI_API_KEY

def generate_exercise(language, difficulty):
    prompt = f"""
You are a helpful assistant that generates diverse and creative programming exercises. Please create a {difficulty} exercise in {language} following this format:

1. Title: Provide the title in a simple text format, without using hashtags or other markdown symbols. Ensure the title reflects a unique and varied topic.
2. Objective: Clearly describe the goal of the exercise in plain text. Aim to cover a wide range of programming concepts beyond simple calculations.
3. Instructions: List the steps the user must follow to complete the exercise. Use a numbered list without any special formatting. Ensure the instructions explore different areas such as data structures, algorithms, file handling, or real-world problem-solving. **Do not ask the user to provide input via functions like `input()` or other interactive methods. The exercise should be designed to run without requiring any user input during execution.**
4. Example Output: Provide a clear example of what the output should look like. Present the example as plain text, without code blocks or markdown.
5. Bonus Challenge: If applicable, add an optional challenge to extend the exercise, using plain text only.

Ensure that the exercises vary significantly and cover different programming concepts, avoiding repetition of similar tasks like calculators. The language should be natural, engaging, and free of any markdown or special formatting symbols.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates diverse and creative programming exercises."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=3000,
        temperature=0.85
    )
    return response['choices'][0]['message']['content'].strip()

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
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": "You are a programming expert that provides detailed feedback on coding exercises."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=3000,
        temperature=0.85
    )
    return response['choices'][0]['message']['content'].strip()