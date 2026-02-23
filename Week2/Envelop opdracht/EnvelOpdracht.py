def lees_enveloppen(path):
    with open(path)as file: #opent mijn envelopes.txt bestand (en with sluit het ook automatisch)
        return[tuple(map(int, line.strip("()\n").split(","))) for line in file] 
        #verwijderd () en , en zet de getallen om in integers (en zet deze in een tuple)

def past_in(hoogte, breedte):
    return hoogte[0] < breedte[0] and hoogte[1] < breedte[1] #kijkt of de hoogte en breedte van de nieuwe envelop past in de huidige envelop

def grootste_stapel_hoogte(enveloppen):
    enveloppen.sort() #sorteert de gegeven tuple
    grootste_stapel_hoogte = [1] * len(enveloppen) #maakt een lijst van de lengte van enveloppen (50) met alle waarden 1 (deze worden overwritten als het hoger is)

    for i in range(len(enveloppen)):
        for j in range(i):
            if past_in(enveloppen[j], enveloppen[i]):
                grootste_stapel_hoogte[i] = max(grootste_stapel_hoogte[i], grootste_stapel_hoogte[j] + 1)

    return max(grootste_stapel_hoogte) #returned de grootste stapel mogelijk

def grootste_stapel(enveloppen):
    enveloppen.sort()
    
    lengte = len(enveloppen)
    grootste_stapel = [1] * lengte
    parent = [-1] * lengte 

    for i in range(lengte):
        for j in range(i):
            if past_in(enveloppen[j], enveloppen[i]):
                if grootste_stapel[j] + 1 > grootste_stapel[i]:
                    grootste_stapel[i] = grootste_stapel[j] + 1
                    parent[i] = j

    max_index = grootste_stapel.index(max(grootste_stapel))
    
    stapel = []
    while max_index != -1:
        stapel.append(enveloppen[max_index])
        max_index = parent[max_index]

    return stapel

enveloppen = lees_enveloppen("Week2\\DEAI - WC Source Data Model Design\\envelopes.txt") # pad naar mn evelopes.txt bestand
print("Grootste stapel:", grootste_stapel(enveloppen))