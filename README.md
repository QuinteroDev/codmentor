# Codmentor

[![Live Application](https://img.shields.io/badge/Live-Application-brightgreen)](http://codmentor.quinterodev.com/codmentor)

CodMentor is an educational platform designed to help students and developers improve their programming skills by generating personalized exercises and providing detailed feedback using the OpenAI API. The application integrates an interactive code editor that allows users to write, execute, and evaluate their code in real-time.

## Main Features

	•	Dynamic Exercise Generation: Utilizes the OpenAI API to create personalized exercises based on the programming language and difficulty selected by the user.
	•	Interactive Code Editor: Integration with CodeMirror to allow code editing directly on the platform, with support for multiple programming languages.
	•	Evaluation and Feedback: Provides detailed feedback on the code written by the user, highlighting corrections and suggestions for improvement.
	•	Multilanguage Support: Code editor with support for different programming languages and theme selection.

## Requirements

	•	Python 3.10 or higher
	•	Django 5.1
	•	OpenAI API
	•	CodeMirror for code editing

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/quinterodev/codmentor.git
   cd codmentor
   ```

2. Create and activate a virtual environment:
   
   ```
   python -m venv codmentor-env
   source codmentor-env/bin/activate  # On Windows: codmentor-env\Scripts\activate
   ```

3.	Install the dependencies:

     ```
     pip install -r requirements.txt
     ```

4. Configure Environments Variables

```
SECRET_KEY=your_django_secret_key
DEBUG=True
OPENAI_API_KEY=your_openai_api_key
```

5.	Apply the migrations and run the development server:
    
    ```
    python manage.py migrate
    python manage.py runserver
    ````

6.	Collect Static Files:

```
python manage.py collectstatic
```

7. Start the Development Server

```
python manage.py runserver
```

## Production Deployment

The deployment was carried out on an Ubuntu server using Gunicorn as the application server and Nginx as a reverse proxy. Let’s Encrypt was used to enable HTTPS by generating and renewing SSL certificates.

**Key Deployment Steps**

1.	Gunicorn Setup:

	•	Creation of a systemd service to manage Gunicorn.
	•	Start and enable the Gunicorn service for the application.

2.	Nginx Configuration:

	•	Configuring Nginx as a reverse proxy for Gunicorn.
	•	Enabling HTTPS using Let’s Encrypt.

3.	SSL Certificates:

	•	Generating SSL certificates with Let’s Encrypt.
	•	Automatic renewal configuration for the certificates.

## Contribution

Contributions are welcome. If you wish to contribute, please fork the repository and submit a pull request with your changes.

## Credits

CodMentor was developed by QuinteroDev as an educational tool to enhance programming skills through interactive practice and automated feedback.