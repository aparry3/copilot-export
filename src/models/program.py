from .week import Week

class Program:
    def __init__(self, name, weeks=None, **kwargs):
        self.name = name
        self.weeks = map(lambda w: Week.get_week_by_id(w), weeks or [])
