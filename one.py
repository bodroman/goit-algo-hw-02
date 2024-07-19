import queue
import threading
import time
import random

# Ствоюємо чергу заявок
request_queue = queue.Queue()

# Лічильник для унікальних номерів заявок
request_counter = 0

def generate_request():
    global request_counter
    while True:
        # Імітація часу генерації нових заявок
        time.sleep(random.randint(1, 3))
        request_counter += 1
        request = f"Заявка #{request_counter}"
        request_queue.put(request)
        print(f"Нова заявка додана до черги: {request}")

def process_request():
    while True:
        if not request_queue.empty():
            request = request_queue.get()
            print(f"Обробка {request}")
            # Імітація часу обробки заявки
            time.sleep(random.randint(2, 5))
            print(f"{request} оброблено")
        else:
            print("Черга пуста, очікування нових заявок")
            time.sleep(1)

def main():
    # Створення окремих потоків для генерації та обробки заявок
    generator_thread = threading.Thread(target=generate_request)
    processor_thread = threading.Thread(target=process_request)

    # Запуск потоків
    generator_thread.start()
    processor_thread.start()

    # Чекаємо завершення роботи потоків (в цілому вони безкінечні)
    generator_thread.join()
    processor_thread.join()

if __name__ == "__main__":
    main()
