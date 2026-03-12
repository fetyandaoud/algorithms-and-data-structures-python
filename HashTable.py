class HashTable:
    def __init__(self, size):
        self.size=size
        self.table=[None] * size  #skapa en tom hash-tabell Storleken på listan är samma som värdet på size

    def separate_chaining(self, input_data):
        self.table=[[] for _ in range(self.size)] #länkade listor för separate chaining.[] for _ in range(self.size)skapar en lista för varje index i size
        print("Separate Chaining Hash Table:")
        for value in input_data:
            index=value % self.size #räknar var ett värde ska lagras
            self.table[index].append(value)#lägger värdet i den beräknade lagringsplatsen

        for i, chain in enumerate(self.table):#itererar över varje index (i) och dess värde (chain)
            print(f"Index {i}: {chain}")
        print()

    def linear_probing(self, input_data):
        self.table=[None] * self.size 
        print("Linear Probing Hash Table:")
        for value in input_data:
            index=value % self.size
            while self.table[index] is not None:#om indexet inte är tom(upptaget)
                index=(index + 1) % self.size  #om upptaget testa nästa

            self.table[index]=value #lagrar värdet i det lediga indexet.

        print(self.table)
        print()

    def quadratic_probing(self, input_data):
        self.table=[None] * self.size  #återställ tabellen
        print("Quadratic Probing Hash Table:")
        for value in input_data:
            index= value % self.size
            i = 1 #första försöket
            while self.table[index] is not None:
                index=(index + i**2) % self.size  #kvadratisk förskjutning
                i += 1 #nästa försök
            self.table[index]=value

        print(self.table)
        print()

    def rehash(self, ny_storlek):#möjliggör ändring av antal index i hashtabellen
        print("Rehashing Hash Table to size:", ny_storlek)
        old_table=self.table
        self.size=ny_storlek
        self.table=[None] * ny_storlek

        for item in old_table:#går igenom alla element i den gamla hash-tabellen och flyttar dem till nya hash-tabell efter storleken ändrats genom rehash
            if isinstance(item, list): #kontrollerar om ett element är en lista
                for sub_item in item:#går igenom alla värden i listan elementet (kedjan) och flyttar dem till den nya tabellen
                    self.insert(sub_item)#med insert() som separat värde för att sedan få ett beräknat index för lagring
            elif item is not None: #alla icke-listvärden från den gamla tabellen flyttas också till den nya tabellen
                self.insert(item)

        print(self.table)#kriver ut hela tabellen som en lista
        print()

    def insert(self, value):#infogar ett värde i hash-tabellen med hjälp av linear probing
        index = value % self.size
        while self.table[index] is not None:
            index = (index + 1) % self.size  # Linear probing for rehash
        self.table[index]=value

    def discuss_complexity(self):
        print("Complexity Discussion:")
        print("- Separate Chaining: O(1) in best case, O(n) in worst case (long chains).")
        print("- Linear Probing: O(1) in best case, O(n) in worst case (clustering).")
        print("- Quadratic Probing: O(1) in best case, but avoids clustering better than linear probing.")
        print()

    def discuss_other_rehashing_functions(self):
        print("Diskussion för andra reshashing-funktioner:")
        print("- Double Hashing: använder en andra hashing för att minska hopklumpning")
        print("- Exempel: h1(x) = x % size, h2(x) = 7 - (x % 7).")
        print()


# Huvudprogram
if __name__ == "__main__":
    input_data=[4371, 1323, 6173, 4199, 4344, 9679, 1989]
    hash_table=HashTable(size=10)
    
    # Kör varje del
    hash_table.separate_chaining(input_data)
    hash_table.linear_probing(input_data)
    hash_table.quadratic_probing(input_data)
    hash_table.rehash(ny_storlek=20)
    hash_table.discuss_complexity()
    hash_table.discuss_other_rehashing_functions()
