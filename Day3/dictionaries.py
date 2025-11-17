students={}
subjects={"Calculus","Java","DSA","Instrumentation"}
while True:
  name=input("Enter name or 'q' to quit: ")
  if name.lower()=="q":
    break
  else:
    marks={}
    for subject in subjects:
      mark=int(input(f"Enter marks for {subject}: "))
      marks[subject]=mark
  students[name]=marks
print("\n Student records:")
for student,marks in students.items():
 print(f"{student}:")
 total=sum(marks.values())
 for subject,mark in marks.items():
   print(f"{subject}:{mark}")
 print(f"Total marks:{total}")
