from time import perf_counter_ns
import statistics
import matplotlib.pyplot as plt
import simples as sp
import mthread as mt

from concurrent.futures import ProcessPoolExecutor

with open("data.csv") as file:
    data = [line.strip() for line in file]

data = list(map(int, data))

ciclos = 50

print('\n\nAnálise de %d valores\n\n'%(len(data)))
print('Início da execução dos ciclos')

speedups = []
tempo1 = []
tempo2 = []

for i in range(ciclos):
  
  print('ciclo: %d de %d' %((i+1),ciclos))
  

  start1 = perf_counter_ns()
  primo_sp = sp.resolve_simples(data)
  finish1 = perf_counter_ns()
  tempo1.append(finish1-start1)
  #print(start1)
  #print(finish1)

  start2 = perf_counter_ns()
  primo_mt = mt.resolve_thread(data)
  finish2 = perf_counter_ns()
  tempo2.append(finish2-start2)
  #print(start2)
  #print(finish2)

  speedup = (finish1-start1)/(finish2-start2)
  speedups.append(speedup)

  print('Fim do ciclo: %d de %d' %((i+1),ciclos))
  print()
  print('Método Simples')
  print('Tempo Execução: %f ms'%((finish1-start1)/1000000))
  print('Números Primos Encontrados: %d'%(primo_sp))
  print()
  print('Método Threads')
  print('Tempo Execução: %f ms'%((finish2-start2)/1000000))
  print('Números Primos Encontrados: %d'%(primo_mt))
  print()
  print('SpeedUP = %f\n'%(speedup))

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