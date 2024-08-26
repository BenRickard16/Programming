from matplotlib import pyplot as plt
students = [
    [187.96, 185.42, 185.42, 182.88, 182.88, 167.64, 172.72, 175.26, 189.23, 165.1, 170.18, 162.56, 171.45, 193.04, 193.04, 165.1, 172.72, 157.48, 190.5, 170.18, 167.64, 167.64, 185.42, 167.64, 168.91, 180.34, 177.8, 167.64, 182.88, 172.72, 185.42, 172.72, 181.61, 170.18, 190.5, 172.72, 149.86, 172.72, 185.42, 167.64, 167.64, 187.96, 157.48],
    [82.628, 88.076, 59.02, 76.272, 66.738, 52.21, 64.922, 66.284, 79.904, 61.29, 63.56, 63.56, 60.382, 79.904, 88.984, 54.934, 69.916, 47.67, 97.156, 59.928, 54.026, 53.572, 76.272, 57.204, 57.204, 72.186, 63.56, 49.032, 70.824, 73.094, 88.984, 69.916, 68.554, 59.928, 77.18, 68.1, 43.13, 53.572, 69.916, 69.916, 60.382, 70.37, 51.302],
    [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 2]
]

lst1 = []
lst2 = []
lst3 = []
lst4 = []
for i in range(len(students[0])):
    if students[2][i] == 1:
        lst1.append(students[0][i])
        lst2.append(students[1][i])
    else:
        lst3.append(students[0][i])
        lst4.append(students[1][i])
    
    
    






plt.plot(lst1, lst2, 'o')
plt.plot(lst3, lst4, 'ro')
plt.xlabel("Student's Height")
plt.ylabel("Student's Weight")
plt.show()