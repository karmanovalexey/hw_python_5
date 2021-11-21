import os
import random
import string
from tempfile import gettempdir

class File():
    def __init__(self, path):
        self.path = path
        if not os.path.exists(path):
            open(path, 'a').close()

    def __add__(self, another):
        filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        result = File(os.path.join(gettempdir(), filename))
        content = self.read() + another.read()
        result.write(content)
        return result

    def __str__(self):
        return self.path

    def __iter__(self):
        self.cur_iter = 0
        self.n_lines = sum(1 for line in open(self.path)) 
        self.f = open(self.path, 'r')
        return self
    
    def __next__(self):
        if self.cur_iter >= self.n_lines:
            self.f.close()
            raise StopIteration

        self.cur_iter+=1
        return self.f.readline()

    def read(self):
        content = ''
        with open(self.path, 'r') as f:
            content = f.read()
        return content

    def write(self, content):
        with open(self.path, 'w') as f:
            f.write(content)
        return len(content)

    