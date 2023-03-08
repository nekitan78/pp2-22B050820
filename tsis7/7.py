import os
print('Exist:', os.access('c:\\pp2 spring\\getfile.txt', os.F_OK))
print('Readable:', os.access('c:\\pp2 spring\\.gitignore', os.R_OK))
print('Writable:', os.access('c:\\pp2 spring\\getfile.txt', os.W_OK))
print('Executable:', os.access('c:\\pp2 spring\\tsis6', os.X_OK))