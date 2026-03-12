import time
import random

class MinHeap:
    def __init__(self):
        self.heap=[]

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        parent=(index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index=parent
            parent=(index - 1) // 2

    def delete_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val=self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_val

    def heapify_down(self, index):
        smallest=index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest !=index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

# Mätning av operationer med flera repetition
def measure_insertion(heap, value, repetitions):
    start_time=time.perf_counter()
    for _ in range(repetitions):
        heap.insert(value)
    end_time =time.perf_counter()
    return (end_time - start_time) / repetitions

def measure_deletion(heap, repetitions):
    start_time=time.perf_counter()
    for _ in range(repetitions):
        heap.delete_min()
    end_time=time.perf_counter()
    return (end_time - start_time) / repetitions

if __name__ == "__main__":
    # Skapa en heap och fyll den med slumpmässiga data
    initial_data = [random.randint(1, 1000000) for _ in range(1000000)]  # Ändra storlek här
    heap =MinHeap()
    for value in initial_data:
        heap.insert(value)

    # Antal repetitioner för mätning
    repetitions=10000

    # Mät genomsnittlig tid för infogning
    insertion_time=measure_insertion(heap, random.randint(1, 1000000), repetitions)

    # Mät genomsnittlig tid för borttagning av minsta elementet
    deletion_time=measure_deletion(heap, repetitions)

    # Presentera resultaten
    print("Genomsnittlig tid för infogning: {:.6f} sekunder".format(insertion_time))
    print("Genomsnittlig tid för borttagning av minsta element: {:.6f} sekunder".format(deletion_time))
