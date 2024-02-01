from src.domain import Id
from src.domain.entity import Article


class User:
    user_id: Id
    username: str
    password: str
    national_code: int
    article: Article

    def __init__(self, user_id: Id, username: str, password: str, national_code: int):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.national_code = national_code

    def edit_information(self):
        pass
