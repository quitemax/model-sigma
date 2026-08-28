# Citation verification — 2026-08-28

Review of every bibliography entry in `paper/sigma_model_en.tex` / `paper/sigma_model_pl.tex`
against primary sources. Placeholders (`[Author]`, `Autor(zy)`, "Journal TBD") were filled in
and wrong keys / metadata corrected.

## Corrected — wrong author / key / venue

| old key | problem | correct |
|---|---|---|
| `fink2024` | author "Fink, S. B." is wrong; not an author of the NOW paper | **`riddle2024`** — Riddle, J. & Schooler, J. W. (2024). *Hierarchical consciousness: the Nested Observer Windows model.* Neuroscience of Consciousness 2024(1), niae010. |
| `sarasso2013` | key implies Sarasso; the actual authors are Lee et al.; no year in the record | **`lee2013disruption`** — Lee, U., Ku, S., Noh, G., Baek, S., Choi, B. & Mashour, G. A. (2013). *Disruption of frontal–parietal communication by ketamine, propofol, and sevoflurane.* Anesthesiology 118(6), 1264–1275. |
| `vollenweider2022` | Vollenweider is not an author; "Frontiers/PMC" is wrong | **`ketaminemodel2022`** — Marguilho, M., Figueiredo, I. & Castro-Rodrigues, P. (2023). *A unified model of ketamine's dissociative and psychedelic properties.* Journal of Psychopharmacology 37(1), 14–32 (online Dec 2022). |
| `qela2025` | title "…deviations…: a systematic mapping" and "Journal TBD" — both wrong | Qela, B., Damiani, S., De Santis, S., et al. (2025). *Predictive coding in neuropsychiatric disorders: A systematic transdiagnostic review.* Neuroscience & Biobehavioral Reviews 169, 106020. |

## Author placeholders filled in (verified)

| key | resolved |
|---|---|
| `usk2026` | Tallam, K. (2026). arXiv:2605.13884. |
| `tsm2026` | Xie, Y. (2026). arXiv:2604.11914. ("Temporal Self-Model" is the name of a module from that paper.) |
| `interoceptive2026` | Candia-Rivera, D. (2026). arXiv:2604.24527. |
| `hotzone2021` | Ihalainen, R., Gosseries, O., Van de Steen, F., Raimondo, F., Panda, R., Bonhomme, V., Marinazzo, D., Bowman, H., Laureys, S. & Chennu, S. (2021). NeuroImage 231, 117841. |

## Added

- **`aaronson2014`** — Aaronson, S. (2014). *Why I am not an integrated information theorist
  (or, the unconscious expander).* Shtetl-Optimized (blog). Both language versions of the paper
  refer to "Aaronson's informal objection" but had no bibliography entry for it.
- `\cite{cerullo2015}` and `\cite{oswald2023}` — the entries were in the bibliography but never
  cited (an "unused bibitem" warning). Text references were added: Cerullo in the Introduction
  (critique of Φ), von Oswald in the transformer section (ICL as implicit gradient descent).

## Verified with no substantive change (volume/pages filled in)

`albantakis2023` (PLOS Comput Biol 19(10):e1011465) · `friston2010` (Nat Rev Neurosci
11(2):127–138) · `deane2021` (Neurosci Conscious 2021(2):niab024) · `rosenthal2005` ·
`behrouz2024` (arXiv:2501.00663) · `premakumar2026` (Phil Trans R Soc A 384(2320):20240531;
preprint arXiv:2407.10188) · `casali2013` (Sci Transl Med 5(198):198ra105) ·
`vandecruys2014` (Psychol Rev 121(4):649–675).

## Second batch — added 2026-08-28 (from the literature review)

Nine entries added from `literature.md`, cited in the paper: `bayne2016`, `safron2020`,
`hanson2023`, `barrett2019`, `mediano2019`, `phiid2019`, `oizumi2016`, `intrepid2026`,
`predmetacog2026`. Well-established ones (Bayne, Oizumi, Mediano/Barrett, Safron, Hanson) are
solid; still to confirm against the publisher record:
- `barrett2019` — whether it has a journal version beyond arXiv (JCS?).
- `phiid2019` — the *Entropy* volume/issue if it was published there.
- `intrepid2026` — the *Neurosci. Biobehav. Rev.* article number (106742) and DOI.
- `predmetacog2026` — volume / article number (only the DOI is confirmed).

## Local library

Full notes for each entry (details, link, abstract, "Role in Model Σ") live in `references/` —
one `.md` file per citation key, index in `references/README.md`.

## To check in later work

- `hotzone2021`: volume/page (231, 117841) from secondary records — confirm on the publisher's
  page.
- `qela2025`: full author list truncated to "et al." — fill in from the original.
- `premakumar2026`: article number 20240531 from the DOI; confirm the start page.
- `tsm2026` / `interoceptive2026` / `usk2026`: 2026 preprints with no peer-reviewed version —
  update once they appear.
