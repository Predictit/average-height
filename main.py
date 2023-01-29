
student_heights = [180, 124, 165, 173, 189, 169, 146]
#student_heights = input("Input a list of student heights ") #.split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum=0
for i in student_heights:
    sum = sum + i
print(sum)
mlen=0
for i in student_heights:
    mlen+=1
print(mlen)

print(round(sum/mlen))
