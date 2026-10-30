# Textový nástroj

Malý Python modul `textovy_nastroj.py` s tromi funkciami na prácu s textom: počet slov, skrátenie textu a najčastejšie slovo. Súčasťou sú testy napísané v `pytest`.

## Inštalácia

Testované na Pythone 3.14 (Windows). V priečinku projektu:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Príkaz na aktiváciu platí pre `cmd`. V PowerShelli je to `.venv\Scripts\Activate.ps1`.

## Spustenie testov

```
pytest
```

Všetky testy majú prejsť (`9 passed`).

## Príklady použitia

Spusti `python` v priečinku projektu a vyskúšaj:

```python
from textovy_nastroj import pocet_slov, skratit, najcastejsie_slovo

pocet_slov("ahoj svet ")           # 2
skratit("Dobrý deň", 5)            # "Dobr…"
najcastejsie_slovo("Ahoj svet ahoj")  # "ahoj"
```

## Funkcie

- `pocet_slov(text)` – počet slov, viac medzier za sebou sa neráta ako viac slov.
- `skratit(text, n)` – ak má text najviac `n` znakov, vráti ho nezmenený, inak ho skráti na presne `n` znakov vrátane `…` na konci.
- `najcastejsie_slovo(text)` – slovo s najviac výskytmi, veľké a malé písmená sa nerozlišujú, pri rovnosti vyhráva prvé v texte. Pre text bez slov vyhodí `ValueError`.