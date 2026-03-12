import time
import random
import pandas as pd #för output i tabellform
import matplotlib.pyplot as plt #skapa visualiseringar och grafer
#två funktioner men med olika inputstorlekar jämförs
#Algoritm 1 har insert(value), heapify_up(index) säkerställa heap-egenskapen, heapify_up(index)  Justerar heapen uppåt från ett givet index för att säkerställa att heap-egenskapen
#Algoritm 2 har build_heap(values), heapify_down(index) från toppen neråt, 
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def build_heap(self, values):
        self.heap = values[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def heapify_down(self, index):
        minst=index
        left=2 * index + 1
        right=2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[minst]: #Kontrollerar om vänstra barnet finns inom heapen.om vänster är <= har noden inte vänsterbarn
            minst=left                                                 # Jämför värdet på vänstra barnets värde är mindre än värdet i minst blir v-barn minst
        if right < len(self.heap) and self.heap[right] < self.heap[minst]:
            minst= right

        if minst !=index: #kontrollerar om det minsta inte finns i pisitionen index
            self.heap[index], self.heap[minst] = self.heap[minst], self.heap[index]#om sant byts värdena mellan den nuvarande noden och det minsta barnet
            self.heapify_down(minst) #ropar rekursivt för att fortsätta justeringen av heapen efter att ha bytt plats på noder

# Funktion för att mäta tiden för Algoritm 1 (Insert one at a time)
def measure_algorithm_1(input_data):
    heap=MinHeap()
    start_time= time.time()
    for value in input_data:
        heap.insert(value)
    end_time=time.time()
    return end_time - start_time

# Funktion för att mäta tiden för Algoritm 2 (Build heap from array)
def measure_algorithm_2(input_data):
    heap=MinHeap()
    start_time=time.time()
    heap.build_heap(input_data)
    end_time=time.time()
    return end_time - start_time

# Storlekar på input
input_sizes=[100, 1000, 10000, 50000, 100000]
results=[]

# Mät komplexiteten för båda algoritmerna
for size in input_sizes:
    input_data=[random.randint(1, 1000000) for _ in range(size)]#random nummer mellan 1-1000000.size är 5 element taget från listan input_sizes
    time_alg1=measure_algorithm_1(input_data)
    time_alg2=measure_algorithm_2(input_data)
    results.append({"Input Size": size, "Algorithm 1 Time (s)": time_alg1, "Algorithm 2 Time (s)": time_alg2})

# Skapa en tabell med resultaten
df_results=pd.DataFrame(results)
print(df_results)

# Rita diagram för resultaten
plt.figure(figsize=(10, 6))#storlek på 10 tum i bredd och 6 tum i höjd.
#X-axeln representeras av inputstorlekarna (100, 1000, 10000) från DataFrame df_results
#Y-axeln representerar tiden det tog att köra algoritm 1
#label1 lilla etiketten som beskriver vilken linja som respresenterar vilke
#marker="o" gör små cirklar på linjerna
plt.plot(df_results["Input Size"], df_results["Algorithm 1 Time (s)"], label="Algorithm 1 (Insert one at a time)", marker="o")
plt.plot(df_results["Input Size"], df_results["Algorithm 2 Time (s)"], label="Algorithm 2 (Build heap from array)", marker="o")
plt.title("Time Complexity of Algorithm 1 and Algorithm 2")
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.legend()#samlar alla etiketter och visar dem i ett litet fönster
plt.grid()
plt.show()#Visar grafen på skärmen
