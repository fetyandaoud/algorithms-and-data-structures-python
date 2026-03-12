class MinHeap:
    def __init__(self):
        self.heap=[]

    def insert(self, value):
        # Lägg till värdet i slutet av listan
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        #justera uppåt för att bibehålla heap-egenskapen
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index=parent
            parent=(index - 1) // 2

    def build_heap(self, values):
        #byygg heap från en lista (bottom-up)
        self.heap=values[:] #kopia av hela listan
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def heapify_down(self, index):
        #justera nedåt för att bibehålla heap-egenskapen
        smallest=index
        left=2 * index + 1
        right=2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    #när jag rekursivt anropar in_order för vänster och höger barn med hjälp av index i formeln, är index igentligen förälder underfrstått
    def in_order(self, index=0):#returnerar i ordningen vänster, rot, höger
        if index >= len(self.heap):#om index är utanför heapens gränser 
            return [] #så returnera tom lista för att avsluta rekursionen.
        left=self.in_order(2 * index + 1) #hämtar resultatet från vänstra barnet
        right =self.in_order(2 * index + 2) #hämtar resultatet från högra barnet
        return left + [self.heap[index]] + right #Listan returneras som vänsterdel, rotvärde, högerdel.index är föräldern för just detta träd
                      # [self.heap[index]] är lista med värdet från den aktuella roten

    def pre_order(self, index=0):
        if index >= len(self.heap):
            return []
        left= self.pre_order(2 * index + 1)
        right=self.pre_order(2 * index + 2)
        return [self.heap[index]] + left + right

    def post_order(self, index=0):
        if index >= len(self.heap):
            return []
        left = self.post_order(2 * index + 1)
        right = self.post_order(2 * index + 2)
        return left + right + [self.heap[index]]

    def level_order(self):
        return self.heap

if __name__ == "__main__":
    values = [10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2]

    # Algorithm 1: Insert one at a time
    print("Algorithm 1 (Insert one at a time):")
    heap1 = MinHeap()
    for value in values:
        heap1.insert(value)
    print("Heap:", heap1.level_order())

    # Algorithm 2: Build heap from array
    print("\nAlgorithm 2 (Build heap from array):")
    heap2 = MinHeap()
    heap2.build_heap(values)
    print("Heap:", heap2.level_order())

    # Traversals
    print("\nTraversals (Algorithm 2 Heap):")
    print("In-order:", heap2.in_order())
    print("Pre-order:", heap2.pre_order())
    print("Post-order:", heap2.post_order())
    print("Level-order:", heap2.level_order())
