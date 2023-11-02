from repository.user_repository import UserRepository
from bo.user_bo import UserBo

user_repository: UserRepository = UserRepository()


def check_username_and_password(username: str, password: str):
    """
    Check that given username and password are correct compared to saved user data.
    :param username: Username that will be checked with saved username.
    :param password: Password that will be checked with hashed password.
    :return: True, if correct. False otherwise.
    """

    user: UserBo = user_repository.find_by_username(username)
    if user is not None:

        success: bool = user.check_password(password)
        return success

    return False
