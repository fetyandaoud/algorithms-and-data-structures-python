#Börjar med en tom MinHeap och lägger till element ett i taget med insert.
#Efter varje insättning justeras det nya värdet uppåt med heapify-up.
#Varje insättning tar O(log n), så att bygga hela heapen från n element tar O(n log n).
class MinHeap:
    def __init__(self):
        self.heap=[]
    def insert(self,value):
        # Lägg till värdet i slutet av listan
        self.heap.append(value)#hamnar alltid sist i listan
        # Justera uppåt (heapify up) för att bibehålla heap-egenskapen
        self.heapify_up(len(self.heap) - 1) # Det sista elementet i listan får index len(self.heap) - 1

    def heapify_up(self,index): #funktion för swapping
        #hitta förälderns index
        parent_index=(index - 1) // 2 #för att hitta nåns förälders index=minska index för nya värdet med 1 dividera med 2=förälderindex
        # Fortsätt justera uppåt så länge barnet är mindre än föräldern
        while index > 0 and self.heap[index] < self.heap[parent_index]:#jämförelsen och swappingen sker i den här loopen
            #byt plats mellan barnet och föräldern
            self.swap(index, parent_index)
            index = parent_index 
            parent_index=(index - 1) // 2 #beräknar vem som är föräldern för nya 3 en nivå högre upp

    def swap(self, i, j):
        #byt plats mellan två element i heapen
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i] #heheheh hehu

    def print_heap(self):
        # Skriv ut hela heapen
        print(self.heap)


     #Huvudprogram
if __name__ == "__main__":
    min_heap = MinHeap()

    #värden att infoga
    values=[10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2]

    for value in values:
        min_heap.insert(value)

    # Skriv ut resultatet
    min_heap.print_heap()

#Förälder på index 𝑖:⌊(𝑖−1)//2⌋------Vänster barn:2i+1.-------Höger barn:2𝑖+2 