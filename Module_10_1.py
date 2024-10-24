import time
from time import sleep
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f'"Завершилась запись в файл {file_name}"')

start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()
res_time = end_time - start_time
print('Время выполнения функций и потоков:', res_time)

the_first = Thread(target=write_words, args=(10, 'example5.txt', ))
the_second = Thread(target=write_words, args=(30, 'example6.txt', ))
the_third = Thread(target=write_words, args=(200, 'example7.txt', ))
the_four = Thread(target=write_words, args=(100, 'example8.txt', ))

the_first.start()
the_second.start()
the_third.start()
the_four.start()

the_first.join()
the_second.join()
the_third.join()
the_four.join()

end_time_2 = time.time()
res_time_2 = end_time_2 - start_time
print('Время выполнения функций и потоков:', res_time_2)