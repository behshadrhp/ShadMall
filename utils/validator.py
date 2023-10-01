from django.core.validators import RegexValidator

english_character_regex = RegexValidator(
    regex=r'^[a-zA-Z0-9\s\-_\.!@#\$%^&*()+=\[\]{};:,<>\?/\\]{2,200}$',
    message='Only English letters, numbers, and spaces are allowed, and the allowed characters are between 2 and 200',
)
