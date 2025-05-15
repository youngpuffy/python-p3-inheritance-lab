#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name, subject= None):
        super().__init__(first_name, last_name)
        self.knowledge = [
             "OOP", "Inheritance", "Encapsulation", "Polymorphism", "Recursion"
        ]

    def teach(self):
        return random.choice(self.knowledge)
        pass