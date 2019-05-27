from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )
CATEGORIES = ['American', 'Mexican', 'Portuguese', 'Asian', 'Fish Land', 'South Indian', 'Coastal', 'Arabic', 'Healthy']

def validate_category(value):
    if not value in CATEGORIES:
        raise ValidationError(f"{value} not a valid category")
