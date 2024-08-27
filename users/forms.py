from django import forms

class ExerciseForm(forms.Form):
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('java', 'Java'),
        ('csharp', 'C#'),
        ('cpp', 'C++'),
        ('ruby', 'Ruby'),
        ('go', 'Go'),
        ('php', 'PHP'),
        ('swift', 'Swift'),
        ('typescript', 'TypeScript'),
        ('kotlin', 'Kotlin'),
    ]
    
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        error_messages={'required': 'Please select a programming language.'}
    )
    difficulty = forms.ChoiceField(
        choices=DIFFICULTY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        error_messages={'required': 'Please select a difficulty level.'}
    )

    def clean_language(self):
        language = self.cleaned_data.get('language')
        if language not in dict(self.LANGUAGE_CHOICES):
            raise forms.ValidationError("Invalid language selected.")
        return language

    def clean_difficulty(self):
        difficulty = self.cleaned_data.get('difficulty')
        if difficulty not in dict(self.DIFFICULTY_CHOICES):
            raise forms.ValidationError("Invalid difficulty level selected.")
        return difficulty