class Boss:
    def __init__(self, name):
        self.name = name

    def assign_task(self, worker, task):
        print(f"{self.name}: {worker.name}, ти маєш виконати завдання - {task}")
        worker.do_task(task)

class Worker:
    def __init__(self, name):
        self.name = name

    def do_task(self, task):
        print(f"{self.name}: Виконав завдання - {task}")

boss = Boss("Босс")
worker1 = Worker("Робітник Біба")
worker2 = Worker("Робітник Боба")

boss.assign_task(worker1, "Створити Всесвіт")
boss.assign_task(worker2, "Створити телепорт")