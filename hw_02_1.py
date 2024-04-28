from queue import Queue
import time
import random

# Створення черги заявок
request_queue = Queue()

def generate_request():
    """Генерація нової заявки і додавання її до черги."""
    request_id = random.randint(1000, 9999)  # Генерація унікального ID для заявки
    request_queue.put(request_id)
    print(f"Заявка {request_id} додана до черги.")

def process_request():
    """Обробка заявки, видалення її з черги."""
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Заявка {request_id} оброблена.")
    else:
        print("Черга пуста.")

def main():
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(1)  # Затримка для імітації реального часу обробки
    except KeyboardInterrupt:
        print("Програма завершена користувачем.")

if __name__ == "__main__":
    main()