grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(sorted(students))
print(students)
avg_Aaron = sum(grades[0])/len(grades[0])
avg_Bilbo = sum(grades[1])/len(grades[1])
avg_Johnny = sum(grades[2])/len(grades[2])
avg_Khendrik = sum(grades[3])/len(grades[3])
avg_Steve = sum(grades[4])/len(grades[4])
avg_grades = dict(Aaron = avg_Aaron,Bilbo = avg_Bilbo,Johnny = avg_Johnny, Khendrik = avg_Khendrik, Steve = avg_Steve)
print(avg_grades)


