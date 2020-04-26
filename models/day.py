from connection import db

from .block import Block

class Day:

    def __init__(self, name, workout_blocks=None, **kwargs):
        self.name = name
        self.blocks = [Block(**b) for b in (workout_blocks or [])]
