def presenteer(dict, totaal):
    for k, v in dict.items():
        print(k,':', v, 'euro')
    print(26*'=')
    print('totaal :', totaal, 'euro')


mijn_dict = {
    'vis' : 10, 
    'vlees': 25, 
    'overig' : 15
    }

totaal = 50


