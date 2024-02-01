from datetime import datetime

from src.domain import Id


class Article:
    article_id: Id
    title: str
    content: str
    brief: str
    is_published: bool
    created_at: datetime
    updated_at: datetime

    def __init__(self, article_id: int, title: str, content: str, brief: str, is_published: bool):
        self.article_id = article_id
        self.title = title
        self.content = content
        self.brief = brief
        self.is_published = is_published
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


