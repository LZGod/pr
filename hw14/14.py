import os

def che(path):
    m = 0
    name = ''
    for roots, dirs, files in os.walk(path):
         if m <= len(files):
             m = len(files)
             name = roots
    print(m, name)
che('.')
