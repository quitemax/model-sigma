# Log decyzji — model Σ

Chronologiczny zapis rozstrzygnięć, żeby nie trzeba było ich odtwarzać z pamięci przy każdym powrocie do projektu.

## Stan opisu systemu: dwuwymiarowy, potem trójwymiarowy
Rozważono w(ℓ,t) sprzężone z g·e (opcja 1, Σ i Γ tautologicznie skorelowane) vs. w(ℓ,t)=w₀(ℓ) statyczne
(opcja 2, Σ i Γ niezależne z konstrukcji). **Przyjęto opcję 2** — korelacja zmierzona w realnym systemie
jest wtedy odkryciem empirycznym, nie artefaktem definicji. Dodano trzecią wielkość A(t) (wyrównanie
przestrzenne) jako osobny, ortogonalny wymiar diagnostyczny.

## Mechanizm konkurencji/wykluczenia: §7 vs §7.1
Rozważono dwie wersje:
- **§7 (kanoniczna):** w = w₊ − w₋, ciągły indeks Jaccarda, w₋ = γ·overlap·Φ. Dopuszcza Σ<0
  ("netto fragmentacja"). Własny wynalazek inspirowany IIT, nie wyprowadzenie z niego.
- **§7.1 (rozważona, odrzucona):** binarna bramka overlap + tanh relaksacja różnicy Φ, uziemiona
  bezpośrednio w kanonicznym (binarnym) postulacie wykluczenia IIT. Dowodliwie wyklucza Σ<0.

**Decyzja:** zachować §7 jako kanoniczne. Zdolność modelu do wyrażenia netto fragmentacji uznano za
cenniejszą niż ścisła wierność binarnemu postulatowi IIT. To świadome, nazwane odejście od IIT — nie
nieporozumienie formalizmu. Do jawnego zaznaczenia w każdej przyszłej pracy.

## Self- vs. world-modeling (§4.1)
Dwa niezależne warunki dla genuine self-modelingu: (a) cel predykcji wewnętrzny (stan h_ℓ) vs.
zewnętrzny (token/zachowanie), (b) moment aktualizacji: online przy wdrożeniu vs. tylko trening.
Tylko przecięcie obu warunków spełnia pełną definicję e_ℓ, g_ℓ z §4. Titans ląduje w komórce
(zewnętrzny cel × online) — konstytutywne, ale world-modeling, nie self-modeling.

## Kanał odczytu R_ℓ (§17)
Dodany po dyskusji o różnych typach utraty przytomności (omdlenie, napad, sen REM, locked-in
syndrome). (Σ,Γ,A) opisuje stan wewnętrzny, ale nic nie mówi o obserwowalności z zewnątrz — stąd
R_ℓ(t) i nierówność Σ_obs(t) ≤ κ·R_L(t). Bezpośrednia inspiracja: Perturbational Complexity Index
(Casali i in. 2013), zaprojektowane dokładnie po to, żeby rozdzielić te dwa pytania klinicznie.

## Wrażliwość kontekstowa bramki g_ℓ (§18)
Dodana po natrafieniu na źródło łączące Fristona (2010) z Intense World Theory i "context
blindness" w autyzmie. g_ℓ(t) = h(e_ℓ(t), C(t)), χ_ℓ(t) = |∂g_ℓ/∂C| ≥ 0 jako nowy parametr
mierzący, jak silnie kontekst moduluje wagę błędu. Context blindness = χ_ℓ≈0.

## Status ogólny
Spójna wewnętrznie synteza koncepcyjna, niezweryfikowana recenzyjnie. Otwarte: systematyczny
przegląd literatury, weryfikacja cytowań źródłowo, rozstrzygnięcie §7 vs §7.1 przed jakąkolwiek
próbą publikacji, instancja empiryczna poza toy example.
