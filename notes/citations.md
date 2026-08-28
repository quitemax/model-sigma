# Weryfikacja cytowań — 2026-08-28

Przegląd wszystkich pozycji bibliografii z `paper/sigma_model_en.tex` /
`paper/sigma_model_pl.tex` względem źródeł pierwotnych. Zastąpiono placeholdery
(`[Author]`, `Autor(zy)`, „Journal TBD"), poprawiono błędne klucze i metadane.

## Poprawione — błędny autor / klucz / miejsce publikacji

| stary klucz | problem | poprawnie |
|---|---|---|
| `fink2024` | autor „Fink, S. B." błędny; to nie jest autor pracy o NOW | **`riddle2024`** — Riddle, J. & Schooler, J. W. (2024). *Hierarchical consciousness: the Nested Observer Windows model.* Neuroscience of Consciousness 2024(1), niae010. |
| `sarasso2013` | klucz sugeruje Sarasso; faktyczni autorzy to Lee i in.; brak roku w rekordzie | **`lee2013disruption`** — Lee, U., Ku, S., Noh, G., Baek, S., Choi, B. & Mashour, G. A. (2013). *Disruption of frontal–parietal communication by ketamine, propofol, and sevoflurane.* Anesthesiology 118(6), 1264–1275. |
| `vollenweider2022` | Vollenweider nie jest autorem tej pracy; „Frontiers/PMC" błędne | **`ketaminemodel2022`** — Marguilho, M., Figueiredo, I. & Castro-Rodrigues, P. (2023). *A unified model of ketamine's dissociative and psychedelic properties.* Journal of Psychopharmacology 37(1), 14–32 (online XII 2022). |
| `qela2025` | tytuł „…deviations…: a systematic mapping" i „Journal TBD" — oba błędne | Qela, B., Damiani, S., De Santis, S., i in. (2025). *Predictive coding in neuropsychiatric disorders: A systematic transdiagnostic review.* Neuroscience & Biobehavioral Reviews 169, 106020. |

## Uzupełnione placeholdery autorów (zweryfikowane)

| klucz | ustalone |
|---|---|
| `usk2026` | Tallam, K. (2026). arXiv:2605.13884. |
| `tsm2026` | Xie, Y. (2026). arXiv:2604.11914. („Temporal Self-Model" to nazwa modułu z tej pracy.) |
| `interoceptive2026` | Candia-Rivera, D. (2026). arXiv:2604.24527. |
| `hotzone2021` | Ihalainen, R., Gosseries, O., Van de Steen, F., Raimondo, F., Panda, R., Bonhomme, V., Marinazzo, D., Bowman, H., Laureys, S. & Chennu, S. (2021). NeuroImage 231, 117841. |

## Dodane

- **`aaronson2014`** — Aaronson, S. (2014). *Why I am not an integrated information theorist
  (or, the unconscious expander).* Shtetl-Optimized (blog). Tekst obu wersji pracy
  powołuje się na „nieformalny zarzut Aaronsona", wcześniej bez pozycji w bibliografii.
- `\cite{cerullo2015}` i `\cite{oswald2023}` — pozycje były w bibliografii, ale nigdzie
  nie cytowane (ostrzeżenie „unused"). Dodano odwołania w tekście: Cerullo we Wstępie
  (krytyka Φ), von Oswald w sekcji o transformerach (ICL jako niejawny spadek gradientu).

## Zweryfikowane bez zmian merytorycznych (uzupełniono tom/strony)

`albantakis2023` (PLOS Comput Biol 19(10):e1011465) · `friston2010` (Nat Rev Neurosci
11(2):127–138) · `deane2021` (Neurosci Conscious 2021(2):niab024) · `rosenthal2005` ·
`behrouz2024` (arXiv:2501.00663) · `premakumar2026` (Phil Trans R Soc A 384(2320):20240531;
preprint arXiv:2407.10188) · `casali2013` (Sci Transl Med 5(198):198ra105) ·
`vandecruys2014` (Psychol Rev 121(4):649–675).

## Do sprawdzenia przy dalszej pracy

- `hotzone2021`: tom/strona (231, 117841) z rekordów wtórnych — potwierdzić na stronie
  wydawcy.
- `qela2025`: pełna lista autorów skrócona do „i in." — uzupełnić z oryginału.
- `premakumar2026`: numer artykułu 20240531 z DOI; potwierdzić stronę początkową.
- `tsm2026` / `interoceptive2026` / `usk2026`: preprinty z 2026 bez wersji recenzowanej —
  zaktualizować, gdy się ukażą.
