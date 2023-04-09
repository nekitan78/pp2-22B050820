import os
path = "\pp2 spring"
print("only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nonly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nall directories and files :")
print([ name for name in os.listdir(path)])