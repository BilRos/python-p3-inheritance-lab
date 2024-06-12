#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, last_name, first_name):
        super().__init__(last_name, first_name)
        self.knowledge =  [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

    def teach(self):
        pass
        new_knowledge = random.randint(0, len(self.knowledge)-1)   
        return self.knowledge[new_knowledge]
        