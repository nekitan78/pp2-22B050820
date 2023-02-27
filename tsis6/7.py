def sToc(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(sToc('python_exercises'))