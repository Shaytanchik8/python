class MathProblemTraine:
    task = 0
    def __init__(self, task, answer):
        MathProblemTraine.task += 1
        self.answer = answer

    def Task_2a(self):
        print("Task:" +str(MathProblemTraine.task))
        answerUser = float(input("Please input your answer :"))
        if answerUser == self.answer:
            self.status = True
        else:
            self.status = False
    def Task_2b(self):
        return self.status

obj1 = MathProblemTraine(1, 7*5)
obj1.Task_2a()
print(obj1.Task_2b())


obj2 = MathProblemTraine(1, 12+8)
obj2.Task_2a()
print(obj2.Task_2b())