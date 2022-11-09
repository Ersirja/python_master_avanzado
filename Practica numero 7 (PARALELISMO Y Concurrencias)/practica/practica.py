import threading

from threading import Thread
from time import perf_counter, sleep

def ejemplo():
    sleep(2)


start_time=perf_counter()
ejemplo()
ejemplo()

end_time=perf_counter()
print(f"tiempo total secuencial {end_time-start_time:0.002f} segundos")



start_time=perf_counter()
threading_1 = Thread(target=ejemplo)
threading_2= Thread(target=ejemplo)
threading_3 = Thread(target=ejemplo)


threading_1.start()
threading_2.start()
threading_3.start()

threading_1.join()
threading_2.join()
threading_3.join()

end_time=perf_counter()

print(f"tiempo total secuencial {end_time-start_time:0.002f} segundos")