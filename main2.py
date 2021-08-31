from time import perf_counter_ns
import statistics
import matplotlib.pyplot as plt
import simples as sp
import mthread as mt

from concurrent.futures import ProcessPoolExecutor

data = []
with open("data.csv") as file:
    data = [line.strip() for line in file]

def speedupsf(x):
    global data
    print('ciclo: %d de %d' %((x+1),ciclos))
  
    start1 = perf_counter_ns()
    primo_sp = sp.resolve_simples(data)
    finish1 = perf_counter_ns()
    tempo1 = finish1-start1
    #print(start1)
    #print(finish1)

    start2 = perf_counter_ns()
    primo_mt = mt.resolve_thread(data)
    finish2 = perf_counter_ns()
    tempo2 = finish2-start2
    #print(start2)
    #print(finish2)

    speedup = (finish1-start1)/(finish2-start2)

    return (tempo1,tempo2,speedup)



data = list(map(int, data))

ciclos = 50

print('\n\nAnálise de %d valores\n\n'%(len(data)))
print('Início da execução dos ciclos')

speedups = []
tempo1 = []
tempo2 = []

execs = list(range(ciclos))
with ProcessPoolExecutor() as executor:
    results = executor.map(speedupsf,execs)

print("speedups: ", speedups)
print("tempo1: ", tempo1)
print("tempo2: ", tempo2)

tempo1 = []
tempo2 = []
speedups = []
for t1,t2,spdp in results:
    tempo1.append(t1)
    tempo2.append(t2)
    speedups.append(spdp)
  
mSpeedUps = statistics.mean(speedups)
print('\n\nMédia do SpeedUp: ', mSpeedUps)

plt.figure()
plt.plot(list(range(len(tempo1))),tempo1,label='Método Simples')
plt.plot(list(range(len(tempo2))),tempo2,label='Método Thread')
plt.legend()
plt.show()

plt.figure()
plt.plot(list(range(len(speedups))),speedups)
plt.title('Speed Ups')
plt.ylabel('SpeedUp(ms)')
plt.xlabel('Ciclos')
plt.grid()
plt.show()