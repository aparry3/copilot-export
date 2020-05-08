from connection import db

from .day import Day

class Week:
    @classmethod
    def get_week_by_id(cls, id):
        _week = db.weeks.find_one({'_id': id})
        return cls(**_week)

    def __init__(self, _id, days=None, **kwargs):
        self.id = _id
        self.days = map(lambda d: Day(**d), days or [])
