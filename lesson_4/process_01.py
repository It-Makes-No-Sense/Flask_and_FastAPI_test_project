import multiprocessing
import time

# counter = 0
counter = multiprocessing.Value('i', 0)  # Создание общей переменной для всех процессоров


# def increment():
#     global counter
#     for _ in range(10_000):
#         counter += 1
#     print(f'Значение счетчика: {counter:_}')

def increment(cnt):
    for _ in range(10_000):
        with cnt.get_lock():
            cnt.value += 1
    print(f'Значение счетчика: {cnt.value:_}')


if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=increment, args=(counter,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # print(f'Значение счетчика: {counter:_}')
    print(f'Значение счетчика в финале: {counter.value:_}')