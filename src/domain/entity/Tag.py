from src.domain import Id


class Tag:
    tag_id: Id
    title: str


def __init__(self, tag_id: int, title: str):
    self.tag_id = tag_id
    self.title = title
