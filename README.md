# Systèmes de Fonctions Itérées (IFS) & Géométrie Fractale

Ce dépôt présente une étude théorique et appliquée de la géométrie fractale à travers la théorie des **Systèmes de Fonctions Itérées (IFS)**, le théorème du point fixe de Banach dans les espaces métriques complets et leur implémentation numérique en Python.

---

## 📄 Contenu du dépôt
- **Rapport PDF :** [`rapport_systemes_iteres_fractales.pdf`](./rapport_systemes_iteres_fractales.pdf) — *Mémoire complet d'analyse et de géométrie*
- **Source LaTeX :** [`main.tex`](./main.tex) — *Code source du document*
- **Simulations Python :** [`fractals_simulation.py`](./fractals_simulation.py) — *Script d'illustration des attracteurs fractals*

---

## Thématiques & Concepts clés
- **Analyse & Espaces Métriques :** Espaces métriques complets, compacité dans $\mathbb{R}^n$, théorème du point fixe et opérateurs contractants.
- **Théorème d'Attraction :** Construction d'attracteurs fractals déterministes comme ensembles invariants par une famille de contractions.
- **Transformations Géométriques & Affines :** Isométries (rotations, réflexions, translations), similitudes directes/indirectes et représentations matricielles.
- **Dimension de Hausdorff :** Calcul analytique de la dimension d'autosimilarité appliquée aux fractales classiques.

---

## Visualisations Python
Les fractales étudiées dans le rapport sont générées numériquement via `fractals_simulation.py` (utilisation de `numpy` et `matplotlib`) :

| Flocon de Von Koch | Triangle de Sierpinski | Fougère de Barnsley |
| :---: | :---: | :---: |
| ![Flocon de Von Koch](./koch_snowflake.png) | ![Triangle de Sierpinski](./sierpinski_triangle.png) | ![Fougère de Barnsley](./barnsley_fern.png) |
| *Dimension $d \approx 1{,}2618$* | *Dimension $d \approx 1{,}585$* | *Transformations affines* |

---

## Utilisation du script
Pour exécuter les simulations et générer les figures :
```bash
python fractals_simulation.py
```
