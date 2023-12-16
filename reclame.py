from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    korting = prijs * (1-korting)
    return (f'Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro.')

input = aanbieding_1('aardbei', 4, 0.1)

print(input)


def inkomsten_totaal(inkomsten, btw):
     totaal = sum(inkomsten)
     bedrag = totaal * btw
     return (f'Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden.')
    
bedragen = inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09)

print(bedragen)


def laag_en_hoog(mijn_lijst):
    return min(mijn_lijst), max(mijn_lijst)
     
lijst = laag_en_hoog([220, 430, 125, 160, 205, 90, 345])

print(lijst)


def gemiddelde(mijn_lijst):
    bedrag = sum(mijn_lijst)/len(mijn_lijst)
    return (f'De gemiddelde inkomsten deze week zijn {bedrag} euro.')

getallen = gemiddelde([220, 430, 125, 160, 205, 90, 345])

print(getallen)

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

nieuw = meervoudig([10,5,3,2,1,2,9])
print(nieuw)

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2) 
    return mijn_functie_2(max(korte_lijst), min(korte_lijst))
      
uitkomst = combinatie([])
print(uitkomst)
