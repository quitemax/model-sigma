# Model Σ

*[English](README.md) | Polski*

Hierarchiczne, funkcjonalnie ważone rozszerzenie zintegrowanej teorii informacji (IIT) —
robocza synteza koncepcyjna wypracowana w dialogu z Claude (Anthropic), sierpień 2026.

## Nawigacja

- **Praca:** [`paper/sigma_model_en.tex`](paper/sigma_model_en.tex) — leaner, argumentowana wersja (prowadzi trójką $(\Sigma,\Gamma,A)$ i argumentem o AI; warstwy konkurujące / $\Sigma<0$ to jeden akapit). PDF-y: [EN](paper/sigma_model_en.pdf) · [PL](paper/sigma_model_pl.pdf) (źródło PL: [`sigma_model_pl.tex`](paper/sigma_model_pl.tex))
- **Pełna wersja robocza** (wszystko, co rozważono): [`paper/model_sigma.md`](paper/model_sigma.md) · pol.: [`paper/model_sigma.pl.md`](paper/model_sigma.pl.md)
- Dlaczego tak, a nie inaczej: [`notes/decisions.md`](notes/decisions.md) · mapa literatury: [`notes/literature.md`](notes/literature.md)
- Bibliografia z abstraktami: [`references/`](references/) ([indeks](references/README.md)) · audyt cytowań: [`notes/citations.md`](notes/citations.md)
- Liczby z pracy, wykonywalne: [`examples/toy_example.py`](examples/toy_example.py)
- [Stan projektu](#stan-projektu) · [Otwarte wątki](#otwarte-wątki) · [Kompilacja PDF-ów](#kompilacja-pdf-ów-ze-źródeł) · [Uruchomienie przykładu](#uruchomienie-przykładu-numerycznego)

## Struktura repo

- [`paper/`](paper/)
  - [`sigma_model_en.tex`](paper/sigma_model_en.tex) / [`sigma_model_pl.tex`](paper/sigma_model_pl.tex) — **praca** (EN / PL): leaner, argumentowana wersja
  - [`model_sigma.md`](paper/model_sigma.md) — pełna wersja robocza, angielski (wszystko, co rozważono, w porządku narastania); przy rozbieżnościach obowiązują decyzje redakcyjne pracy
  - [`model_sigma.pl.md`](paper/model_sigma.pl.md) — tłumaczenie polskie wersji roboczej
  - [`sigma_model_en.pdf`](paper/sigma_model_en.pdf) / [`sigma_model_pl.pdf`](paper/sigma_model_pl.pdf) — skompilowane PDF-y, artefakty builda; **obecnie nieaktualne** (sprzed przebudowy) — regenerować przez `make` albo CI `build-paper`
  - [`Makefile`](paper/Makefile) — `make` buduje oba PDF-y, `make clean` czyści pliki pomocnicze
- [`notes/`](notes/)
  - [`decisions.md`](notes/decisions.md) — log kluczowych rozstrzygnięć (dlaczego, nie tylko co)
  - [`citations.md`](notes/citations.md) — audyt poprawności cytowań (co zweryfikowano / poprawiono)
  - [`literature.md`](notes/literature.md) — mapa literatury per-teza; co jest nowe, a co już zrobione
  - [`layer-decomposition.md`](notes/layer-decomposition.md) — jak wyprowadzać warstwy funkcjonalne, a nie przyjmować
  - [`related-theories.md`](notes/related-theories.md) — notatki o pokrewnych frameworkach (np. Grounded Duality Theory)
- [`references/`](references/) — jeden plik `.md` na pozycję bibliografii (dane, link, abstrakt, rola w Σ); [indeks](references/README.md)
- [`examples/`](examples/)
  - [`toy_example.py`](examples/toy_example.py) — wszystkie przeliczenia numeryczne z pracy, w jednym miejscu
- [`.github/workflows/build-paper.yml`](.github/workflows/build-paper.yml) — CI: kompiluje oba PDF-y i uruchamia `toy_example.py`

## Stan projektu

Spójna wewnętrznie synteza koncepcyjna. Rdzeń: trójka stanu **(Σ, Γ, A)** po małym, ustalonym
zbiorze warstw funkcjonalnych — zintegrowana informacja, aktywność konstytutywnej samo-korekty
(błąd samo-predykcji, który napędza aktualizację parametrów online, nie tylko raport) oraz ich
wyrównanie — zbudowane z rozłącznych zmiennych. Najostrzejsza konsekwencja: Γ ≡ 0 dla dowolnego
zamrożonego LLM przy inferencji, z definicji. Do tego kanał odczytu R_ℓ, przykład numeryczny,
przegląd literatury. Materiał o warstwach konkurujących / Σ<0 zostaje tylko jako szkicowany
kierunek. **Niezweryfikowana recenzyjnie; bez instancji empirycznej; dziedziczy problemy
fundamentalne IIT.**

## Otwarte wątki

- Systematyczny (nie tylko wyszukiwarkowy) przegląd literatury — PhilPapers / PhilSci-Archive
- Jedna przeliczona instancja empiryczna — np. (Σ,Γ,A) na realnych danych EEG/fMRI
  (propofol vs. ketamina), choć g_ℓ może nie być odtwarzalne z danych neuronalnych
- Zasadnicze uzasadnienie podziału na warstwy (obecnie przyjęty)

Zamknięte: praca (`sigma_model_en.tex`) prowadzi trójką + argumentem o AI i sprowadza warstwy
konkurujące do jednego akapitu; weryfikacja cytowań
([`notes/citations.md`](notes/citations.md)); usunięcie formy całkowej. Pełny log decyzji
i uzasadnień: [`notes/decisions.md`](notes/decisions.md).

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
