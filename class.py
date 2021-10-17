 import statistics
class Student:
    def __init__(self,name, score):
        self.name = name
        self.score = score
    def getData(self):
        print('{} get {} points'.format(self.name,self.score))

num = int(input("Input the number of students: "))
listStudent = []
for i in range(num):
    count = i + 1
    val = []
    for j in range(2):
        if j == 0:
           value = str(input('Enter the name of student{}:'.format(count)))
        else:
           value = float(input('Enter the score of student{}:'.format(count)))
        val.append(value)
    listStudent.append(val)
#listStudent = [['phu', 9], ['khanh', 10], ['dat', 4],['huy', 3],['minh', 5], ['hoa', 5], ['ty', 5]]

data_stu = [Student(name= i[0], score = i[1]) for i in listStudent]
print("list of student : ", [item.__dict__ for item in data_stu])


class Classroom:
    def __init__(self, Students):
        self.Students = Students
    def find_average(self):
        Sumscore = 0
        for item in self.Students:
            Sumscore += item.score
        avg = Sumscore/len(self.Students)
        return avg
    def find_mediance(self):
        lst_Score = []
        for item in self.Students:
            lst_Score.append(item.score)
        print(lst_Score)
        mediance = statistics.median(lst_Score)
        temp = 0
        for item in self.Students:
            if item.score == mediance:
                temp = temp + 1
                nameMe = item.name
            else:
                noOne = 'no one has got the median score'
        if temp != 0:
            noOne = nameMe
        return mediance, noOne

test = Classroom(Students = data_stu)
dtb = test.find_average()
print('Average score:', dtb)
med = test.find_mediance()
print('Median score and name of one of the students who has got the median score:', med)