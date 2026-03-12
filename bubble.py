#bubblesort. IN-PLACE(SORTERAR INUTI LISTAN) DÄRFÖR ÄR SPACE COMLEXITY O(1).ÄR STABLE EFTERSOM VÄRDEN SOM INTE BEHÖVER BYTA PLATS BEHÅLLER SINA POSITIONER
#Bästa fall:Listan är redan sorterad. Endast en runda krävs och komplexiteten blir O(n).(INTE ALLA MED INRE LOOP BLIR N**2)
#Sämsta fall: Listan är omvänd sorterad. Fullt antal rundor krävs, och komplexiteten blir O(n²).

isSwapped=True # anta att någon i raden behöver byta plats
i=0
n=[9,8,1,2,3,4,5,6,7]
while isSwapped: #Så länge någon har bytt plats i raden, fortsätt!
    isSwapped=False
    for j in range(len(n)-1):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
            isSwapped=True #markera att vi har gjort platsbyte och vi fortsätter i inre loopen
    # När inget platsbyte sker, lämnas inre loopen,vi hamnar i yttre loppen där isSwapped=False och allt stannar
    i+=1 #antal rundor

