# Codmentor

Codmentor is an interactive platform designed to help users learn programming through AI-generated exercises. Users can choose their programming language and difficulty level, solve coding challenges, and receive instant feedback.

## Features

- Choose programming language and difficulty level.
- Integrated code editor.
- Automated code evaluation and feedback.
- Track progress and scores.

## Requirements

- Python 3.x
- Django 4.x
- Django REST framework
- django-crispy-forms (Bootstrap 5)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/quinterodev/codmentor.git

2.	Navigate to the project directory:

   ```bash
   cd codmentor

3.	Create and activate a virtual environment:

   ```bash
   python -m venv codmentor-env
   source codmentor-env/bin/activate  # On Windows: codmentor-env\Scripts\activate

4.	Install the dependencies:

    ```bash
     pip install -r requirements.txt

5.	Apply the migrations and run the development server:

    ```bash
    python manage.py migrate
    python manage.py runserver

