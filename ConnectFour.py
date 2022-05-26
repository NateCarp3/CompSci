
""" Author: Nathan Carpenter
    Creater on May 1st, 2022
    I pledge my honor that I have abided by the Stevens Honor Code """

class Board:
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height

    def __str__(self):
        x = ""
        x *= width
        x *= height
        if len(x) > 7:
            x += "\n"

        return str()
