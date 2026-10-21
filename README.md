# calculateur-dates

🔗 **Essayer en ligne, gratuitement : [momkdk.github.io/calculateur-dates](https://momkdk.github.io/calculateur-dates/)**

Âge exact, écart entre deux dates, ajout/soustraction de jours. Python pur (module `datetime`
standard), aucune dépendance, licence MIT.

## Ce qu'il fait

- **Âge exact** : années, mois et jours révolus entre une naissance et une date de référence.
- **Écart** : nombre de jours entre deux dates.
- **Décaler** : date obtenue en ajoutant ou soustrayant un nombre de jours.

## Utilisation

```
python -m calculateur_dates age 2000-06-15
python -m calculateur_dates ecart 2026-01-01 2026-06-15
python -m calculateur_dates decaler 2026-01-28 10
```

## Tests

```
python -m unittest discover -s tests -v
```

## Auteur

Mohamed Ali El Amri, développeur freelance Python et IA, Cluses (Haute-Savoie).

Licence MIT.
