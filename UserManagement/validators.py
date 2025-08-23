from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re

class CustomPasswordValidator:
    def __init__(self):
        pass

    def validate(self,password,user=None):
        if not re.search(r"[A-Z]", password):
            raise ValidationError("Password should contain at least one uppercase letter")
        if not re.search(r"[a-z]",password):
            raise ValidationError("Password should contain at least one lowercase letter")
        if not re.search(r"[0-9]",password):
            raise ValidationError("Password should contain at least one number")
        if not re.search(r"[@$!%*?&]",password):
            raise ValidationError("Password should contain at least one special character")
        if " " in password:
            raise ValidationError("Password should not contain space")

    def get_help_text(self):
        return "Password should contain at least one uppercase letter, one lowercase letter, one number and one special character and no spaces."