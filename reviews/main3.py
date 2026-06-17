#dictionary
student = {
  "mathematique": 0,
  "french": 0,
  "english": 0
}

def average_grade(student):
  average = sum(student.values()) / len(student)
  
  if average >= 10:
    return "Admis ✅"
  else:
    return "Recalé ❌"
result = average_grade(student)
print(result)