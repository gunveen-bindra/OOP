# Method overriding


class employee:
    def add(self, salary, incentive):
        print('total salary in base class=', salary+incentive)


class department(employee):
    temp = 'i m member of dept cls'

    def add(self, salary, incentive):
        print(self.temp)
        print('total salary in derived class=', salary+incentive)
dept = department()
dept.add(45000, 5000)
