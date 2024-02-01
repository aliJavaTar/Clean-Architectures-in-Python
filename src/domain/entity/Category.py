from src.domain import Id


class Category:
    category_id: Id
    title: str
    description: str

    def __init__(self, category_id: int, title: str, description: str):
        self.category_id = category_id
        self.title = title
        self.description = description
