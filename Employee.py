class Employee:
    def work(self):
        print('work')

class Manager(Employee):
    def manage(self):
        print('manage')

m=Manager()
m.work()
m.manage()