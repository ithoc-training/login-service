import bcrypt

from bo.user_bo import UserBo


class UserRepository:
    """
    In-memory database as singleton for development purposes.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserRepository, cls).__new__(cls)
        return cls._instance

    users = []

    def __init__(self):
        """
        Set some example users.
        """
        salt = bcrypt.gensalt()
        self.users.append(UserBo("user1", bcrypt.hashpw("password1".encode('utf-8'), salt)))
        self.users.append(UserBo("user2", bcrypt.hashpw("password2".encode('utf-8'), salt)))

    def find_by_username(self, username: str):
        """
        Get the user by its username or None if not existent.
        :param username:
        :return:
        """
        for user in self.users:
            if user.username == username:
                return user

        return None
