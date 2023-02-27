import re
def insert(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(insert("Python"))
print(insert("PythonExercises"))
print(insert("PythonExercisesPracticeSolution"))