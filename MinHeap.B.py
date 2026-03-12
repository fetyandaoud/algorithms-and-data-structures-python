#Tar en färdig lista med element och omvandlar den till en MinHeap.
#Börjar från den sista föräldern (beräknad som (n - 2) // 2) och justerar varje nod nedåt med heapify-down.
class MinHeap:
    def __init__(self, elements):
        # Starta med alla element i en array
        self.heap = elements
        # Bygg heapen med bottom-up-algoritmen
        self.build_heap()

    def build_heap(self):
        # Börja från den sista icke-lövnoden och heapify neråt
        for i in range((len(self.heap) // 2) - 1, -1, -1):#sista föräldern, dvs föräldern till löv
            self.heapify_down(i)

    def heapify_down(self, index):
        minst=index 
        left= 2 * index + 1  # Vänster barn
        right= 2 * index + 2  # Höger barn

        # Jämför minst (föräldern) med vänster barn
        if left < len(self.heap) and self.heap[left] < self.heap[minst]:#Kontrollerar om det vänstra barnet existerar inom heapen and om värdet i det vänstra barnet  är mindre än värdet i den nuvarande minsta noden
            minst = left #då blir left minst (föräldern)
        # Jämför med höger barn
        if right < len(self.heap) and self.heap[right] < self.heap[minst]:#högerbarn jämförs med förälder/nya föräldern
            minst = right #blir nya föräldern

        # Om en av barnen är mindre, byt plats och fortsätt heapify
        # i förra byter de variabel och i denna byter de plats
        if minst != index: #kontrollerar om den nuvarande noden inte är den minsta
            self.swap(index, minst)
            self.heapify_down(minst) #anropar metoden (rekursivt) för att fortsätta heapify-processen från det nya indexet (minst)

    def swap(self, i, j):
        # Byt plats mellan två element i heapen
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def print_heap(self):
        # Skriv ut hela heapen
        print(self.heap)


# Huvudprogram
if __name__ == "__main__":
    # Värden att använda
    values = [10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2]

    # Bygg heapen med linjärtidsalgoritmen
    min_heap = MinHeap(values) #skapar en instans av MinHea

    # Skriv ut resultatet
    min_heap.print_heap()


#Sista föräldern = (n-2)/2