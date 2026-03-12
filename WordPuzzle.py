def build_prefix_hash_table(words): #returnerar successivt ökande bkostäver
    prefix_table = set()#set lagrar unika värden om samma ord förekommer lagras det bara en gång
    for word in words:
        for i in range(1, len(word) + 1):#iterera i från 1 till ordlängden
            prefix_table.add(word[:i])#varje bokstav av ordet lägga i set
    return prefix_table #returnerar {"c", "ca", "cat"}

def find_words_in_puzzle(puzzle, words):#definiera dimensionerna av pusslet:
    rows, cols = len(puzzle), len(puzzle[0])# 1 rad har 4 kolumner
    directions = [
        (-1, 0), (1, 0),  # Vertikal från -1,0 till 1,0 är en riktning upp/(-1,0 uppåt)(-1,0 neråt)(0,-1 vänster)(0,1 höger) 
        (0, -1), (0, 1),  # Horisontell 0,-1 till 0,1 är en riktning i bredd
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonal
    ]

    # Bygg hash-tabellen med prefix
    prefix_table = build_prefix_hash_table(words)
    word_set = set(words)  
    found_words = []

    def is_valid_position(x, y):
    
        return 0 <= x < rows and 0 <= y < cols #0 <= x < rows Kontrollerar om (x)rader ligger mellan 0 och  totala antalet rader 
                                               #0 <= y < cols kontrollerar om (y) kolumner liger mellan 0 och totala antalet kolumner

    def search_from_position(x, y):
        for dx, dy in directions:# varje dx och dy kommer att anta v,v
            word = "" #Nollställer ordet som ska byggas för varje ny riktning.
            nx, ny = x, y
            ##Syfte:Bygger upp ord genom att successivt lägga till bokstäver från pusslet medan man rör sig i en riktning nx,ny
            while is_valid_position(nx, ny):#fortsätt loopen så länge som positionen nx,ny ligger inom pusslets gränser
                word += puzzle[nx][ny]#Lägg till bokstaven på position nx,ny i det akutella word     
                if word not in prefix_table:#Kollar om det nuvarande ordet (eller dess prefix) inte finns i prefix_table
                    break  # Avsluta tidigt om prefixet inte finns
                if word in word_set:#Kontrollerar om det aktuella ordet word finns i listan över giltiga ord word_set
                    found_words.append((word, (x, y), (nx, ny)))#Lägger till det funna ordet och dess koordinater i listan
                nx, ny = nx + dx, ny + dy#Uppdaterar positionerna nx,ny genom att flytta ett steg i riktningen dx,dy
                # nx+dx flyttar till nästa rad baserat på riktningen dx--ny + dy Flyttar till nästa kolumn baserat på riktningen dy

    # Syfte:Gå igenom varje cell i pusslet som en potentiell startpunkt och sök efter ord i alla riktningar från varje position
    for i in range(rows):# Itererar över varje rad i pusslet.
        for j in range(cols):#Itererar över varje kolumn i den aktuella raden
            search_from_position(i, j)#Startar sökningen från positionen i,j i pusslet

    return found_words


# Testa algoritmen
puzzle = [
    ['t', 'h', 'i', 's'],
    ['w', 'a', 't', 's'],
    ['o', 'a', 'h', 'g'],
    ['f', 'g', 'd', 't']
]
words = ["this", "two", "fat", "that"]#Dessa används av algoritmen för att jämföra mot bokstavskombinationer i pusslet och identifiera om de finns.

results = find_words_in_puzzle(puzzle, words)#Anropar funktionen med argumenten puzzle och words
for word, start, end in results:#Itererar över results som är en lista av tuples som returneras av find_words_in_puzzle
    print(f"Word: {word}, Start: {start}, End: {end}")#skriver ut hittade ordet word, start=Startpositionen för ordet som(x,y), och end
