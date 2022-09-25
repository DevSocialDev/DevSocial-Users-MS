from fastapi import HTTPException, status
import re


class UserSignupHandler:
    def __init__(self, user):
        self.new_user = user

    def is_strong_password(self):
        if len(self.new_user.password) >= 8:
            return True
        return False

    def is_valid_email(self):
        email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if re.fullmatch(email_regex, self.new_user.email):
            return True
        return False

    def validate_input(self):
        if (
            not self.is_strong_password()
            or not self.new_user.username.isalnum()
            or not self.is_valid_email()
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"please enter valid details",
            )
        else:
            return True

    def user_exists(self):
        pass

    def add_user_to_db(self):
        pass


class UserLoginHandler:
    def __init__(self, user_login):
        self.user_login = user_login

    # check if detailes entered are consistent with DB
    def verify_credentials(self):
        pass

    # check if user is already logged in
    def is_active(self):
        pass

    # generate token after validation and verification
    def generate_token(self):
        pass

    def login_user(self):
        pass


class UserLogoutHandler:
    def __init__(self, current_user):
        self.current_user = current_user

    def update_status(self):
        pass

    def blacklist_token(self):
        pass

    def logout_user(self):
        pass
