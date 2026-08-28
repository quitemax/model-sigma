# Model Σ

Hierarchiczne, funkcjonalnie ważone rozszerzenie zintegrowanej teorii informacji (IIT) —
robocza synteza koncepcyjna wypracowana w dialogu z Claude (Anthropic), sierpień 2026.

## Struktura repo

```
paper/
  model_sigma.md        — pełna wersja robocza (19 sekcji), źródło prawdy
  sigma_model_en.tex    — źródło LaTeX, wersja angielska
  sigma_model_pl.tex    — źródło LaTeX, wersja polska
  sigma_model_en.pdf    — skompilowany PDF (EN), artefakt builda — regenerować przez `make`
  sigma_model_pl.pdf    — skompilowany PDF (PL), artefakt builda — regenerować przez `make`
  Makefile              — `make` buduje oba PDF-y, `make clean` czyści pliki pomocnicze
notes/
  decisions.md          — log kluczowych rozstrzygnięć (dlaczego, nie tylko co)
examples/
  toy_example.py        — wszystkie przeliczenia numeryczne z pracy, w jednym miejscu
.github/workflows/
  build-paper.yml       — CI: kompiluje oba PDF-y i uruchamia toy_example.py
```

## Stan projektu

Spójna wewnętrznie synteza koncepcyjna: pełny formalizm statyczny i dynamiczny (Σ, Γ, A) —
skończone sumy po warstwach, bez formy całkowej — dowiedzione własności brzegowe, mechanizm
konkurencji/wykluczenia (miękki w = w₊ − w₋, dopuszcza Σ<0 jako zamierzoną cechę), kanał odczytu
R_ℓ, wrażliwość kontekstowa bramki g_ℓ, przykład numeryczny, wstępny przegląd literatury,
zastosowanie do architektur transformerowych. **Niezweryfikowana recenzyjnie.**

## Otwarte wątki

- Systematyczny (nie tylko wyszukiwarkowy) przegląd literatury
- Empiryczna instancja poza toy example — np. przeliczenie (Σ,Γ,A) na realnych danych EEG/fMRI
  (propofol vs. ketamina, PCI pod znieczuleniem) — patrz hipoteza w §16 pracy

Zamknięte: §7 vs §7.1 (zachowano §7, Σ<0 jako cecha), weryfikacja cytowań (`notes/citations.md`),
usunięcie formy całkowej. Pełny log decyzji i uzasadnień: `notes/decisions.md`.

## Kompilacja PDF-ów ze źródeł

Wymaga dystrybucji TeX (TeX Live / MiKTeX):

```
cd paper
make            # buduje sigma_model_en.pdf i sigma_model_pl.pdf (po dwa przebiegi)
make clean      # usuwa pliki pomocnicze (.aux/.log/.out/.toc)
```

Bez `make` (np. czysty MiKTeX na Windows):

```
cd paper
pdflatex sigma_model_en.tex && pdflatex sigma_model_en.tex
pdflatex sigma_model_pl.tex && pdflatex sigma_model_pl.tex
```

Skompilowane PDF-y w repo to artefakty builda — po edycji źródeł trzeba je
przebudować (`make`) albo pobrać z artefaktów CI (workflow `build-paper`).

## Uruchomienie przykładu numerycznego

```
cd examples
python3 toy_example.py
```
