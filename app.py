import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Quantité vendue par région 
figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')
figure.write_html('ventes-par-region.html')
print('ventes-par-region.html généré avec succès !')

# Chiffre d'affaires par quantité
données['ca'] = données['prix'] * données['qte']

# Ventes par produit
ventes_par_produit = données.groupby('produit', as_index=False)['qte'].sum()
figure2 = px.bar(
    ventes_par_produit,
    x='qte',
    y='produit',
    orientation='h',
    text='qte',
    title='Quantité vendue par produit',
    color='produit',
)
figure2.update_traces(textposition='outside')
figure2.write_html('ventes-par-produit.html')
print('ventes-par-produit.html généré avec succès !')

# Chiffre d'affaires par produit
ca_par_produit = données.groupby('produit', as_index=False)['ca'].sum()
figure3 = px.bar(
    ca_par_produit,
    x='ca',
    y='produit',
    orientation='h',
    text='ca',
    title="Chiffre d'affaires par produit",
    color='produit',
)
figure3.update_traces(texttemplate='%{text:,.0f} €', textposition='outside')
figure3.write_html('ca-par-produit.html')
print("ca-par-produit.html généré avec succès !")