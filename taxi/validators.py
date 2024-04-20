from django.core.validators import RegexValidator

license_number_validator = RegexValidator(
    regex=r"^[A-Z]{3}[0-9]{5}$",
    message="Invalid license number. Sample: 'AAA12345'."
)