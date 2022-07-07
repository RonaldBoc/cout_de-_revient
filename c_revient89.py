import json

#test

data = {
    'produits': []
}


def nouveau_produit():
    product_name = input('Entrez le nom du produit: ')
    product_price = float(input('Entrez le prix: '))
    product_quantity = int(input('Entrez la quantité: '))
    prix_achat_pur_produit = product_price * product_quantity
    return [product_name, product_price, product_quantity, prix_achat_pur_produit]




compteur = len(data['produits'])
taux_conversion = input('Entrez le taux de conversion (n si aucun): ')
if taux_conversion == 'n':
    taux_conversion = 1
    print(taux_conversion)
else:
    taux_conversion = float(taux_conversion)
    print(taux_conversion)
transport = float(input('Entrez le coût du transport: \n'))
octroi = float(input('Entrez le coût octroi de mer: \n'))
cout_transport = transport + octroi
new_p = 'y'

print('Entrez le premier produit: ')
while new_p == 'y':
    if new_p == 'y':
        nouveau = nouveau_produit()
        data['produits'].append({'name': nouveau[0]})
        data['produits'][compteur]['prix'] = nouveau[1]
        data['produits'][compteur]['prix_convertit'] = round(
            nouveau[1] * taux_conversion, 3)
        data['produits'][compteur]['quantite'] = nouveau[2]
        data['produits'][compteur]['prix_achat_pur_produit'] = nouveau[3]
        data['produits'][compteur]['cout_revient'] = 0
        compteur += 1
        new_p = input('Voulez-vous entrer un nouveau produit? (y/n): ')

achat_pur_total = 0


for product in data['produits']:
    achat_pur_total += product['prix_achat_pur_produit']

cout_total = achat_pur_total + cout_transport

for product in data['produits']:
    product['cout_revient'] = round(product['prix_achat_pur_produit'] *
                                    cout_total / achat_pur_total / product['quantite'], 3)

data['infos'] = {'cout_total': cout_total, 'achat_pur_total': achat_pur_total, 'quantite_produits': compteur,
                 'transport': transport, 'octroi': octroi, 'cout_transport': cout_transport, 'taux_conversion': taux_conversion}

for product in data['produits']:
    print(
        f"\nLe produit {product['name']} a un coût de revient de {product['cout_revient']}\n")

json_data = json.dumps(data, indent=4)

print(json_data)

with open('json_data.json', 'w') as outfile:
    outfile.write(json_data)