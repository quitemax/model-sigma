# Model Σ

Hierarchiczne, funkcjonalnie ważone rozszerzenie zintegrowanej teorii informacji (IIT) —
robocza synteza koncepcyjna wypracowana w dialogu z Claude (Anthropic), sierpień 2026.

## Struktura repo

```
paper/
  model_sigma.md      — pełna wersja robocza (19 sekcji), źródło prawdy
  sigma_en.tex         — źródło LaTeX, wersja angielska
  sigma_pl.tex         — źródło LaTeX, wersja polska
  sigma_model_en.pdf   — skompilowany PDF (EN)
  sigma_model_pl.pdf   — skompilowany PDF (PL)
notes/
  decisions.md         — log kluczowych rozstrzygnięć (dlaczego, nie tylko co)
examples/
  toy_example.py       — wszystkie przeliczenia numeryczne z pracy, w jednym miejscu
```

## Stan projektu

Spójna wewnętrznie synteza koncepcyjna: pełny formalizm statyczny i dynamiczny (Σ, Γ, A),
dowiedzione własności brzegowe, mechanizm konkurencji/wykluczenia, kanał odczytu R_ℓ,
wrażliwość kontekstowa bramki g_ℓ, przykład numeryczny, wstępny przegląd literatury,
zastosowanie do architektur transformerowych. **Niezweryfikowana recenzyjnie.**

## Otwarte wątki

- Systematyczny (nie tylko wyszukiwarkowy) przegląd literatury
- Weryfikacja cytowań źródłowo — część dat/tytułów w bibliografii ma placeholder "Autor(zy)"
- Rozstrzygnięcie §7 vs §7.1 (mechanizm konkurencji) przed jakąkolwiek próbą publikacji
- Empiryczna instancja poza toy example — np. przeliczenie (Σ,Γ,A) na realnych danych EEG/fMRI
  (propofol vs. ketamina, PCI pod znieczuleniem) — patrz hipoteza w §16 pracy

Pełny log decyzji i uzasadnień: `notes/decisions.md`.

## Kompilacja PDF-ów ze źródeł

```
cd paper
pdflatex sigma_en.tex && pdflatex sigma_en.tex   # dwa przebiegi dla referencji
pdflatex sigma_pl.tex && pdflatex sigma_pl.tex
```

## Uruchomienie przykładu numerycznego

```
cd examples
python3 toy_example.py
```
