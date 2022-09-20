class User:
    def __init__(self, username,password,is_active=True,authenticated=False,is_anonymous=True) -> None:
        self.username=username
        self.password=password
        self.active=is_active
        self.authenticated=authenticated
        self.anonymous=is_anonymous

    def get_id(self)->str:
        return str(self.username)

    def is_active(self):
        """True, as all users are active."""
        return True

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
    
    # def __str__(self) -> str:
    #     return self.username