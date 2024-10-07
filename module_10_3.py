from random import randint
from threading import Thread, Lock
from time import sleep


class Bank:
    def __init__(self):
        self.lock = Lock()
        self.balance = 0

    def deposit(self):
        for i in range(100):
            value = randint(50, 500)
            self.balance += value
            print(f"Пополнение: {value}. Баланс: {self.balance}")

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            sleep(0.001)

    def take(self):
        for i in range(100):
            value = randint(50, 500)
            print(f"Запрос на {value}")
            
            if self.balance >= value:
                self.balance -= value
                print(f"Снятие: {value}. Баланс: {self.balance}")
            else:
                self.lock.acquire()
                print(f"Запрос отклонён, недостаточно средств")
            sleep(0.001)


client = Bank()

thread1 = Thread(target=Bank.deposit, args=(client,))
thread2 = Thread(target=Bank.take, args=(client,))

thread1.start()
thread2.start()

thread1.join()
thread1.join()

sleep(1)
print(f"Итоговый баланс: {client.balance}")
