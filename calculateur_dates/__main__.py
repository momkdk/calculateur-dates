"""CLI : python -m calculateur_dates <age|ecart|decaler> ..."""

from __future__ import annotations

import argparse
import sys
from datetime import date

from . import __version__
from .dates import age_exact, decaler, jours_entre


def _parse_date(texte: str) -> date:
    try:
        return date.fromisoformat(texte)
    except ValueError as e:
        raise ValueError(f"date invalide '{texte}' (attendu AAAA-MM-JJ)") from e


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="calculateur_dates", description=__doc__)
    p.add_argument("--version", action="version", version=__version__)
    sous = p.add_subparsers(dest="commande", required=True)

    a = sous.add_parser("age", help="âge exact à une date donnée (aujourd'hui par défaut)")
    a.add_argument("naissance")
    a.add_argument("--a-la-date", default=None)

    e = sous.add_parser("ecart", help="nombre de jours entre deux dates")
    e.add_argument("date1")
    e.add_argument("date2")

    d = sous.add_parser("decaler", help="ajoute (ou soustrait) un nombre de jours à une date")
    d.add_argument("depart")
    d.add_argument("jours", type=int)

    args = p.parse_args(argv)

    try:
        if args.commande == "age":
            naissance = _parse_date(args.naissance)
            ref = _parse_date(args.a_la_date) if args.a_la_date else None
            r = age_exact(naissance, ref)
            print(f"{r.annees} an(s), {r.mois} mois, {r.jours} jour(s)  ({r.jours_total} jours au total)")
        elif args.commande == "ecart":
            print(f"{jours_entre(_parse_date(args.date1), _parse_date(args.date2))} jour(s)")
        else:
            print(decaler(_parse_date(args.depart), args.jours).isoformat())
    except ValueError as e:
        print(f"Erreur : {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
