import bcrypt


class UserBo:
    """
    Class for handling user data.
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        """
        Check encoded password from a given clear password.
        :param password:
        :return:
        """
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

    def __str__(self):
        return f"User: {self.username}"
