import queue
import time
from threading import Thread
from time import sleep
from random import randint
from datetime import datetime


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = "None"


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.queue = queue.Queue()
        self.tables = args
        self.threads = []

    def guest_arrival(self, *guests):
        my_guests = list(guests)
        guest_number = 0

        for table in self.tables:
            if guest_number >= len(guests):
                break
            table.guest = guests[guest_number]
            my_guests.remove(guests[guest_number])
            guest_number += 1
            t = Guest(table.guest.name)
            t.start()
            self.threads.append(t)
            print(f"{datetime.now()}\t{table.guest.name} сел(-а) за стол номер {table.number}")

        for guest in my_guests:
            self.queue.put(guest)

    def discuss_guests(self):
        while not (self.queue.empty() and all(table.guest.name == "None" for table in self.tables)):
            for table in self.tables:
                alive = True
                for i in self.threads:
                    if i.name == table.guest.name:
                        alive = i.is_alive()
                        break

                if table.guest.name != "None" and not alive:
                    print(f"{datetime.now()}\t{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"{datetime.now()}\tСтол номер {table.number} свободен")
                    table.guest = Guest("None")
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f"{datetime.now()}\t{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}") # , {self.queue.queue}, {self.queue.empty()}
                        t = Guest(table.guest.name)
                        t.start()
                        self.threads.append(t)

        for t in self.threads:
            t.join()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
