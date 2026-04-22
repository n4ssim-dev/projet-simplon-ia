# 📊 Analyse des ventes d'une PME

Projet de visualisation de données réalisé dans le cadre de la préparation à la journée de sélection pour le parcours **Développeur en Intelligence Artificielle** — [Simplon.co](https://simplon.co).

---

## 🎯 Objectifs

- Explorer un jeu de données et en comprendre les caractéristiques principales
- Requêter les données avec **SQL** (chiffre d'affaires, ventes par produit, ventes par région)
- Visualiser les résultats sous forme de graphiques interactifs avec **Python**

---

## 🛠️ Technologies utilisées

| Outil | Rôle |
|---|---|
| [pandas](https://pandas.pydata.org/about/) | Chargement et traitement des données CSV |
| [Plotly Express](https://plotly.com/python/plotly-express/) | Génération de graphiques interactifs exportés en HTML |
| Python 3 | Langage principal |
| GitHub Codespaces | Environnement de développement en ligne |

---

## 🚀 Démarrer le projet

### 1. Créer votre propre dépôt depuis ce modèle

Cliquez sur **"Use this template"** → **"Create a new repository"** en haut à droite de la page.  
[📖 Guide : créer un dépôt depuis un template](https://docs.github.com/fr/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template)

> Si vous n'avez pas encore de compte GitHub, il vous sera demandé d'en créer un.

### 2. Ouvrir dans GitHub Codespaces

Dans votre nouveau dépôt, cliquez sur **Code > Codespaces**, puis créez un nouveau Codespace sur votre branche principale.

<img alt="Créer un Codespace" src="https://github.com/user-attachments/assets/cb29a8da-d1ac-42f5-962c-7d43b8011324" width="400px"/>

> ⏳ L'environnement se construit automatiquement au premier lancement. Patientez quelques minutes sans intervenir.

L'environnement est prêt lorsque la barre d'outils en bas affiche :

```
💬 MESSAGE DE BIENVENUE   💻 TERMINAL   🔎 SPLIT   🏠 PREVIEW
```

---

## 📁 Structure du projet

```
.
├── app.py           # Script principal — génère les graphiques
├── README.md        # Ce fichier
├── ventes-par-region.html     # Graphique généré : répartition des ventes par région
├── ventes-par-produit.html    # Graphique généré : quantités vendues par produit
└── ca-par-produit.html        # Graphique généré : chiffre d'affaires par produit
```

---

## ▶️ Exécuter le projet

1. Cliquez sur le bouton **💻 TERMINAL** dans la barre d'outils en bas de page.
2. Saisissez la commande suivante et appuyez sur `Entrée` :

```bash
python3 app.py
```

Après quelques secondes, trois messages de succès apparaissent :

```
ventes-par-region.html généré avec succès !
ventes-par-produit.html généré avec succès !
ca-par-produit.html généré avec succès !
```

---

## 🔍 Visualiser les graphiques

Cliquez sur le bouton **🏠 PREVIEW** dans la barre d'outils, puis sélectionnez l'un des fichiers HTML générés :

- `ventes-par-region.html` — Camembert de la répartition des ventes par région
- `ventes-par-produit.html` — Barres horizontales des quantités vendues par produit
- `ca-par-produit.html` — Barres horizontales du chiffre d'affaires par produit

---

## 📈 Graphiques produits

### Quantité vendue par région
Diagramme circulaire (pie chart) représentant la part des ventes (`qte`) de chaque région.

### Quantité vendue par produit
Diagramme en barres horizontales représentant le total des quantités vendues, regroupées par produit.

### Chiffre d'affaires par produit
Diagramme en barres horizontales représentant le chiffre d'affaires (`prix × qte`) cumulé par produit, affiché en euros.

---

## 💾 Publier vos modifications

Une fois vos graphiques créés et validés, publiez vos modifications dans votre dépôt en suivant la section **"Validation (commit) de vos modifications"** de [ce guide GitHub](https://docs.github.com/fr/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace#validation-commit-de-vos-modifications).

---

## 📄 Livrables attendus

- ✅ Export SQL des requêtes (`file > save SQL` depuis sqliteonline.com)
- ✅ Fiche synthèse des résultats (CA total, ventes par produit, ventes par région)
- ✅ Lien vers ce dépôt GitHub complété

---

*Projet réalisé dans le cadre du processus de sélection Simplon — parcours Développeur en Intelligence Artificielle.*