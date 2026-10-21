"""Calculs de dates : âge exact, écart entre deux dates, décalage de jours."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta


@dataclass(frozen=True)
class Age:
    annees: int
    mois: int
    jours: int
    jours_total: int


def age_exact(naissance: date, a_la_date: date | None = None) -> Age:
    """Âge en années/mois/jours révolus, et en nombre total de jours."""
    a_la_date = a_la_date or date.today()
    if naissance > a_la_date:
        raise ValueError("la date de naissance doit être antérieure ou égale à la date de référence")

    annees = a_la_date.year - naissance.year
    mois = a_la_date.month - naissance.month
    jours = a_la_date.day - naissance.day

    if jours < 0:
        mois -= 1
        mois_precedent = a_la_date.month - 1 or 12
        annee_mois_precedent = a_la_date.year if a_la_date.month > 1 else a_la_date.year - 1
        jours_dans_mois_precedent = _jours_dans_mois(annee_mois_precedent, mois_precedent)
        jours += jours_dans_mois_precedent
    if mois < 0:
        mois += 12
        annees -= 1

    return Age(annees, mois, jours, (a_la_date - naissance).days)


def _jours_dans_mois(annee: int, mois: int) -> int:
    if mois == 12:
        premier_jour_suivant = date(annee + 1, 1, 1)
    else:
        premier_jour_suivant = date(annee, mois + 1, 1)
    return (premier_jour_suivant - date(annee, mois, 1)).days


def jours_entre(date1: date, date2: date) -> int:
    """Nombre de jours entre deux dates (toujours positif ou nul)."""
    return abs((date2 - date1).days)


def decaler(depart: date, jours: int) -> date:
    """Date obtenue en ajoutant (ou soustrayant si négatif) un nombre de jours."""
    return depart + timedelta(days=jours)
