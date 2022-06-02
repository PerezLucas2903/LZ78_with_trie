import numpy as np

class Node():
    def __init__(self, children = {}):
        self.children = children
        self.terminal = True


class trie():
    def __init__(self, text):
        self.text = text
        self.root = Node()