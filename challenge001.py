#   Students  |  Grades  |  Letters
# ------------|----------|----------
#   George    |  46      |  F
#   Michell   |  80      |  B
#   Josh      |  12      |  F
#   Chloe     |  68      |  D
#   Stanley   |  99      |  A
#   Annie     |  100     |  A+

my_class = [{"name": "Washington", "score": 96,},
  { "name": "Jordan", "score": 91,},
  { "name": "Brady", "score": 92,},
  { "name": "James", "score": 98,},
  { "name": "Pele", "score": 99,},
  { "name": "Messi", "score": 100,}]

def score_to_letter_grade(user):
  if user["score"] == 100:
    user["grade"] = "A+"
  elif user["score"] >= 90:
    user["grade"] = "A"
  elif user["score"] >= 80:
    user["grade"] = "B"
  elif user["score"] >= 70:
    user["grade"] = "C"
  elif user["score"] >= 60:
    user["grade"] = "D"
  elif user["score"] <= 60:
    user["grade"] = "F"

for student in my_class:
  score_to_letter_grade(student)
  print(f"name: {student['name']} score: {student['score']} grade: {student['grade']}.")