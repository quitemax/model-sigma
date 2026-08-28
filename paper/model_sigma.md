# Model Σ — hierarchiczne, funkcjonalnie ważone rozszerzenie IIT (Φ)

Dokument roboczy zbierający formalizm wypracowany do tej pory: 15 sekcji, od motywacji przez pełny formalizm statyczny i dynamiczny, dowiedzione własności brzegowe, mechanizm konkurencji/wykluczenia (z jawnie nazwaną, świadomą rozbieżnością wobec kanonicznego IIT), toy example, wstępny przegląd literatury, i zastosowanie do architektur transformerowych. Status: spójna wewnętrznie synteza koncepcyjna, niezweryfikowana recenzyjnie. Przed jakąkolwiek próbą publikacji potrzebne: systematyczny (nie tylko wyszukiwarkowy) przegląd literatury, weryfikacja cytowań źródłowo, oraz decyzja, czy §7 (dopuszcza Σ<0) czy §7.1 (odrzucona alternatywa, wierniejsza IIT) lepiej służy zamierzonemu zastosowaniu.

---

## 0. Ramy teoretyczne, z których korzystamy

Model Σ nie jest rozwinięciem jednej teorii, tylko syntezą kilku niezależnych ram pojęciowych. Zanim przejdzie się do formalizmu, warto mieć jasność, skąd pochodzi każdy składnik i jaką rolę pełni.

**Integrated Information Theory (IIT), Giulio Tononi.** Główny szkielet formalny — Φ jako miara zintegrowanej informacji, aksjomaty/postulaty (istnienie, informacja, integracja, wykluczenie, kompozycja), i kluczowe dla nas: **postulat wykluczenia** (spośród konkurujących, nakładających się substratów istnieje tylko ten o maksymalnym φ — "zasada maksymalnego istnienia"). Krytyki formalne (Aaronson: Φ da się wysoko dla trywialnych systemów jak korektor błędów; Cerullo: brak uzasadnienia dla samego postulatu wykluczenia) motywują część naszych rozszerzeń.

**Nieredukowalność obliczeniowa, Stephen Wolfram.** Niektórych obliczeń nie da się "skrócić" — jedyny sposób poznania wyniku to faktyczne przeprowadzenie każdego kroku. U nas: bramkuje człon czasowy R_ℓ(i) — pewne sprzężenia międzywarstwowe da się przewidzieć analitycznie, inne trzeba faktycznie "przeliczyć" krok po kroku. Koncepcyjnie pokrewne strukturalnej nieredukowalności IIT, ale formalnie odrębne pojęcie.

**"Living matter as functional matter", Blaise Agüera y Arcas.** Postulat, że o statusie systemu decyduje nie tylko struktura przyczynowo-skutkowa (jak w czystym IIT), ale to, *co system oblicza* — funkcja, nie tylko integracja. To bezpośrednia inspiracja dla wprowadzenia wagi funkcjonalnej w(ℓ) — miejsca w formalizmie, gdzie "znaczenie" danej warstwy dla podmiotowości wchodzi jawnie, a nie tylko jej surowa integracja.

**Predictive processing / architektury test-time training.** Ramy, z których pożyczamy definicję *błędu samo-predykcji* e_ℓ(t) i kryterium konstytutywności (aktualizacja parametrów online napędzana tym błędem) — odróżniające bierne modelowanie od aktywnej, samo-korygującej się pętli.

**Interpreter Gazzanigi (split-brain studies).** Obserwacja, że lewa półkula generuje płynne, spójne wyjaśnienia działań, których przyczyny nie ma dostępu poznawczego (bo leżą w prawej półkuli) — czysta konfabulacja, ale nieodróżnialna z zewnątrz od prawdziwego wglądu. Motywuje rozróżnienie deskryptywne/konstytutywne (§2.7): płynna autonarracja *nie jest* dowodem realnej pętli zwrotnej.

**Teorie wyższego rzędu (Higher-Order Theories, Rosenthal).** Punkt odniesienia kontrastowy, nie źródło formalizmu — HOT twierdzi, że stan mentalny jest świadomy, gdy jest reprezentowany przez stan wyższego rzędu. Nasze rozróżnienie deskryptywne/konstytutywne jest bliskie pytaniu, które HOT stawia, ale odpowiada na nie inaczej (przez kryterium *funkcjonalne* — czy błąd napędza update, nie przez samo *istnienie* reprezentacji wyższego rzędu).

**Analogia ze stałą kosmologiczną** (§7) — czysto metaforyczna, nie teoria źródłowa: użyta wyłącznie żeby zasygnalizować, że waga w(ℓ) niekoniecznie musi być z definicji nieujemna, tak jak Λ w równaniach Einsteina nie jest z góry ograniczona do jednego znaku.

## 1. Motywacja i punkt wyjścia

Standardowe Φ (Tononi, IIT) dla systemu w stanie *s* i partycji *P*:

$$\varphi_P(s) = D\big(p(s'\mid s)\,\|\,p(s'\mid s)\big|_P\big), \qquad \Phi(s) = \min_{P\in\mathcal P}\varphi_P(s)$$

gdzie *D* to miara odległości (np. earth mover's distance) między rozkładem faktycznym a rozkładem po przecięciu systemu wg partycji *P*. Krytyka punktu wyjścia: Φ to jedna liczba — "brak if-a", żadnego rozróżnienia *rodzaju* czy *lokalizacji* integracji. Blisko formalnej krytyki Aaronsona; powiązane z pytaniem o nieredukowalność obliczeniową Wolframa (koncepcje pokrewne, ale odrębne).

Inspiracja rozszerzenia: postulat Agüera y Arcasa, że "to, co system oblicza, ma znaczenie" (funkcja, nie tylko struktura) oraz obserwacja, że różne poziomy hierarchii przetwarzania (móżdżek: dużo obliczeń, mało integracji vs. modelowanie siebie: mniej obliczeń, integracja jakościowo innego rodzaju) wymagają wagi funkcjonalnej, nie tylko strukturalnej.

## 2. Profil hierarchiczny i pierwsza wersja Σ

System *S* dzielimy na warstwy funkcjonalne ℓ = 1,...,L (homeostaza → percepcja/motoryka → model świata → model siebie). Indeks warstwy jest z natury dyskretny: L to mała, skończona liczba pięter funkcjonalnych, nie continuum — nie ma i nie potrzeba granicy L→∞. Zamiast jednej liczby — profil:

$$\Phi(s) = \big(\Phi_1(s),\dots,\Phi_L(s)\big)$$

Zwinięty wagą funkcjonalną w(ℓ) w skończoną sumę:

$$\Sigma(t) = \sum_{\ell=1}^{L} w(\ell,t)\,\Phi(s,\ell,t)$$

### 2.1 Człon między-warstwowy Φ_{ℓ,ℓ-1}

Strukturalny (nie czasowy) — integracja *między* sąsiednimi warstwami ℓ i ℓ-1 w danej chwili, liczona analogicznie do bazowego φ (przez tę samą miarę odległości D). **Nieujemny z definicji** (dystans), bez potrzeby dodatkowych założeń — mierzy stopień sprzężenia przyczynowo-skutkowego, nie ma naturalnego znaku.

### 2.2 §2.7 — samo-modelowanie deskryptywne vs. konstytutywne

Rozróżnienie kluczowe dla interpretacji: płynna autonarracja (analogia interpretera Gazzanigi) **nie jest** dowodem realnej pętli zwrotnej. Kryterium konstytutywności: aktualizacja parametrów online napędzana błędem samo-predykcji (jak w architekturach test-time training).

## 3. Dynamika czasowa

Rozróżnienie notacyjne, którego brakowało pierwszej wersji: indeks (ℓ,ℓ-1) to *warstwa*, nie *czas*. Dynamika czasowa to osobny obiekt, wyprowadzony z pełnej pochodnej Σ:

$$\frac{d\Sigma}{dt} = \sum_{\ell=1}^{L} \left[\frac{\partial w(\ell,t)}{\partial t}\,\Phi(s,\ell,t) + w(\ell,t)\,\frac{\partial\Phi(s,\ell,t)}{\partial t}\right]$$

Rozdziela dwa jakościowo różne źródła zmiany: ∂Φ/∂t (czy integracja na warstwie rośnie/maleje — może być ±, np. zapadanie/wynurzanie ze znieczulenia) i ∂w/∂t (czy istotność warstwy dla samo-modelowania rośnie/maleje).

## 4. w(ℓ,t) i błąd samo-predykcji

Zgodnie z kryterium konstytutywnym z §2.7:

- **Błąd samo-predykcji:** $e_\ell(t) = \|\hat s_\ell(t+\Delta t\mid t) - s_\ell(t+\Delta t)\|^2 \geq 0$ (dla warstw bez mechanizmu autopredykcji: przyjmujemy 0)
- **Bramka konstytutywności:** $g_\ell(t) = \left|\dfrac{\partial\theta_\ell(t)}{\partial e_\ell(t)}\right| \in [0,1]$, znormalizowane — g=0: błąd liczony, ale nic z nim nie robi (deskryptywne); g=1: pełne sprzężenie konstytutywne

### 4.1 Rozstrzygnięcie: self- vs. world-modeling (dwa niezależne warunki)

Genuine self-modeling wymaga **dwóch niezależnych warunków**, nie jednego: (a) cel predykcji musi być **wewnętrznym stanem reprezentacyjnym** (h_ℓ — aktywacje), nie zewnętrznie obserwowalnym zachowaniem/tokenem — nawet jeśli ten token jest autorstwa samego systemu; (b) aktualizacja musi zachodzić **online, przy wdrożeniu**, nie tylko jako zamrożony efekt treningu (to już §2.7, deskryptywne vs. konstytutywne). Krzyżując oba warunki dostajemy 2×2 (rozwinięte w §14 na przykładach architektonicznych) — tylko komórka (cel=wewnętrzny) × (aktualizacja=online) spełnia pełną definicję e_ℓ(t),g_ℓ(t) z tej sekcji.

## 5. Decyzja: opis stanu dwuwymiarowy (Σ, Γ), następnie trójwymiarowy (Σ, Γ, A)

Rozważono dwie opcje dla w(ℓ,t):

- **Opcja 1** — w(ℓ,t) = w₀(ℓ) + β·g_ℓ(t)e_ℓ(t): Σ i Γ dzielą składnik, korelacja *tautologiczna* (wbudowana w definicję)
- **Opcja 2 (przyjęta jako kanoniczna)** — w(ℓ,t) = w₀(ℓ), statyczne: Σ i Γ formalnie niezależne (budowane z rozłącznych zmiennych), więc zmierzona korelacja między nimi w realnym systemie jest odkryciem empirycznym, nie artefaktem definicji

$$\Sigma(t) = \sum_{\ell=1}^{L} w_0(\ell)\,\Phi(s,\ell,t), \qquad \Gamma(t) = \sum_{\ell=1}^{L} g_\ell(t)\,e_\ell(t)$$

### 5.1 Trzecia wielkość — wyrównanie przestrzenne A(t)

$$A(t) = \frac{\mathrm{Cov}_\ell(t)}{\sigma_\Phi(t)\,\sigma_{ge}(t)} \in[-1,1], \qquad \mathrm{Cov}_\ell(t) = \frac{1}{L}\sum_{\ell=1}^{L}[\Phi(s,\ell,t)-\bar\Phi(t)][g_\ell(t)e_\ell(t)-\overline{ge}(t)]$$

Konwencja brzegowa: gdy σ_Φ=0 lub σ_ge=0 (profil jednorodny), A(t):=0.

**Interpretacja trójki (Σ, Γ, A):** Σ — ile zintegrowanej informacji, ważonej architektonicznie; Γ — ile realnej samo-korekty zachodzi w systemie *w ogóle*; A — czy ta samo-korekta zachodzi *tam*, gdzie faktycznie jest integracja. Przypadek A≈-1 mimo wysokich Σ i Γ = sygnatura "Gazzaniga-interpretera": aktywna, płynna autonarracja żyjąca w płytkiej warstwie, odcięta od rdzenia integracyjnego systemu.

## 6. Dowiedzione własności brzegowe

1. **Σ(t) ≥ 0** — warunkowe: wymaga aksjomatu **A1: w₀(ℓ) ≥ 0 ∀ℓ** (nie wynika automatycznie z niczego innego; semantycznie: ujemna waga bazowa nie miałaby dobrej interpretacji bez dodatkowego mechanizmu — patrz §7)
2. **Γ(t) ≥ 0** — bezwarunkowe: g_ℓ∈[0,1], e_ℓ≥0 (norma²), suma iloczynów składników nieujemnych
3. **A(t) ∈ [-1,1]** — dowód przez nierówność Cauchy'ego-Schwarza na profilach (skończonych wektorach) f=Φ-Φ̄, h=ge-ge̅. Warunek równości: A=1 ⟺ g_ℓe_ℓ jest rosnącą funkcją afiniczną Φ(s,ℓ,t) po ℓ; A=-1 dla malejącej
4. **Monotoniczność:** ∂Γ/∂g_ℓ = e_ℓ ≥ 0, ∂Γ/∂e_ℓ = g_ℓ ≥ 0, ∂Σ/∂Φ(ℓ) = w₀(ℓ) ≥ 0 (przy A1) — brak kontrintuicyjnych efektów ubocznych
5. **Dyskretność:** Σ, Γ, A to skończone sumy po ustalonym, niewielkim zbiorze warstw — oś ℓ nie jest continuum, nie ma granicy L→∞ ani postaci całkowej. (Wcześniejsza wersja robocza miała formę całkową; jej artefakt przy L→0, Σ→0 niezależnie od skoncentrowanej integracji, wynikał ze znikającej miary całkowania i tutaj nie występuje.)

## 7. Warstwy przeszkadzające — rozszerzenie o konkurencję/wykluczenie

Pytanie otwierające: czy w₀(ℓ) musi być nieujemne, czy mogą istnieć warstwy, które *aktywnie szkodzą* integracji globalnej (analogia do znaku stałej kosmologicznej)? Kandydaci empiryczni: konkurujące podnarracje (split-brain, dysocjacja, konfabulacja), interpreter Gazzanigi w trybie nadpisywania/zniekształcania zamiast biernego opisu.

Rozwiązanie: rozbicie wagi na dwie nieujemne składowe zamiast swobodnego znaku:

$$w(\ell) = w_+(\ell) - w_-(\ell), \qquad w_+,w_- \geq 0$$

Oparte na **postulacie wykluczenia IIT** (wygrywa maksymalnie nieredukowalny kompleks):

$$\ell^{\ast}(t) = \arg\max_\ell \Phi(s,\ell,t)$$

$$\text{overlap}(\ell,\ell^{\ast}) = \frac{|S_\ell\cap S_{\ell^{\ast}}|}{|S_\ell\cup S_{\ell^{\ast}}|}\in[0,1] \quad\text{(indeks Jaccarda na substratach)}$$

$$w_-(\ell,t) = \begin{cases}0 & \ell=\ell^{\ast}(t)\\ \gamma\cdot\text{overlap}(\ell,\ell^{\ast}(t))\cdot\Phi(s,\ell,t) & \ell\neq\ell^{\ast}(t)\end{cases}, \quad \gamma\geq 0$$

**Ograniczenie na Σ(t) z konkurencją:**

$$\sum_{\ell\neq\ell^{\ast}}[w_+(\ell)-\gamma]\Phi(\ell,t) + w_+(\ell^{\ast})\Phi(\ell^{\ast},t) \;\leq\; \Sigma(t) \;\leq\; \Sigma_+(t)$$

(γ=0 odtwarza stare, bezkonkurencyjne Σ₊ jako przypadek graniczny — sanity check).

**Interpretacja progowa:** γ vs. inf_ℓ w₊(ℓ) działa jak parametr porządku:
- γ ≤ inf w₊(ℓ) → Σ(t) pozostaje ≥0 zawsze; system strukturalnie odporny na fragmentację
- γ > inf w₊(ℓ) → Σ(t)<0 realnie osiągalne = "netto fragmentacja" systemu

Γ(t) i A(t) nie zależą od w₀/w₊/w₋ — rozszerzenie jest lokalne, nie narusza pozostałych definicji.

### 7.1 Rozważona alternatywa — uziemienie w twardym wykluczeniu IIT (odrzucona)

Rozważono wersję ściślej uziemioną w kanonicznym postulacie wykluczenia IIT: overlap jako binarna bramka (czy substraty w ogóle się nakładają) + gładka relaksacja `tanh` różnicy Φ między zwycięzcą a przegrywającym, działająca bezpośrednio na Φ (nie na wagę). Sprawdzona formalnie i numerycznie — poprawnie odtwarza kanoniczne, twarde wykluczenie w granicy κ→∞.

**Odrzucona świadomie**, bo strukturalnie **wyklucza Σ<0** (przegrywający kandydat ma najwyżej φ=0, nigdy φ<0 — tak jak w prawdziwym IIT). To wprost sprzeczne z tym, co chcemy zachować: możliwość "netto fragmentacji" systemu (analogia ze stałą kosmologiczną, warstwy realnie *odejmujące* od podmiotowości, nie tylko tracące swój wkład). Decyzja: **priorytet ma zdolność modelu do wyrażenia zjawiska, nie ścisła wierność kanonicznemu postulatowi wykluczenia IIT.** To świadome, jawne odejście od IIT — do wprost nazwania w każdej przyszłej pracy, żeby recenzent nie odczytał tego jako nieporozumienie formalizmu.

**Kanoniczna pozostaje wersja z §7** (w=w₊−w₋, ciągły indeks Jaccarda, w₋=γ·overlap·Φ, dokładny próg γ_krit z §9.1) — dopuszcza Σ<0, co jest tu traktowane jako cecha modelu, nie usterka.

## 9. Toy example — układ 3-warstwowy

Warstwy: ℓ=1 (homeostaza), ℓ=2 (model świata), ℓ=3 (model siebie).

| ℓ | Φ(ℓ) | w₀(ℓ) | e_ℓ | g_ℓ | g_ℓe_ℓ |
|---|------|-------|-----|-----|--------|
| 1 | 0.2 | 0.1 | 0.0 | 0.0 | 0.0 |
| 2 | 0.6 | 0.3 | 0.4 | 0.3 | 0.12 |
| 3 | 0.9 | 0.6 | 0.8 | 0.9 | 0.72 |

**Bez konkurencji:** Σ=0.74, Γ=0.84, A≈0.90 — wysoka integracja, wysoka aktywność konstytutywna, dobrze wyrównane przestrzennie (sanity check: model daje intuicyjny wynik na intuicyjnie skonstruowanym przykładzie).

**Z konkurencją (§7):** substraty S₁={a,b}, S₂={b,c,d}, S₃={c,d,e,f}; ℓ\*=argmax Φ = warstwa 3. overlap(1,3)=0, overlap(2,3)=0.4. Przy γ=0.5: Σ=0.668, poprawnie wewnątrz przedziału [0.34, 0.74] wyprowadzonego w §7, bliżej górnej granicy (bo faktyczny overlap(1,3)=0 << worst-case=1 założone w dowodzie dolnej granicy — granica jest poprawna, ale nie ciasna dla konkretnych danych).

### 9.1 Poprawka do §7 — dokładny próg krytyczny γ

Ponieważ w₋(ℓ)=γ·overlap(ℓ,ℓ\*)·Φ(ℓ) jest liniowe w γ, Σ(γ) jest **dokładnie liniowe**, nie tylko ograniczone:

$$\Sigma(\gamma) = \Sigma_+ - \gamma\sum_{\ell\neq\ell^{\ast}}\text{overlap}(\ell,\ell^{\ast})\,\Phi(\ell)^2, \qquad \gamma_{\text{krit}} = \frac{\Sigma_+}{\sum_{\ell\neq\ell^{\ast}}\text{overlap}(\ell,\ell^{\ast})\Phi(\ell)^2}$$

(uwaga: odejmowany człon to w₋(ℓ)·Φ(ℓ) = γ·overlap·Φ(ℓ)², czyli Φ do kwadratu — nie do pierwszej potęgi). Dla przykładu: γ_krit = 0.74/(0.4×0.6²) = 0.74/0.144 ≈ **5.139**, potwierdzone numerycznie (Σ(5.139)=0, Σ(6)=−0.124). To ostrzejszy wynik niż same nierówności — przy znanym profilu overlap można podać dokładny próg fragmentacji, nie tylko widełki.

### 9.2 Scenariusz dynamiczny — dysocjacja, ℓ\* się przesuwa

Dwie chwile: t₀ (warstwa 3 dominuje) → t₁ (konkurująca podnarracja w warstwie 2 przejmuje dominację: Φ₂: 0.6→0.85, Φ₃: 0.9→0.5).

| | Σ | Γ | A | ℓ\* |
|---|---|---|---|---|
| t₀ | 0.740 | 0.840 | 0.901 | warstwa 3 |
| t₁ | 0.575 | 0.680 | 0.963 | warstwa 2 |

Wynik nietrywialny: Σ i Γ obie maleją (ΔΣ=−0.165, ΔΓ=−0.16), ale **A rośnie**. To pokazuje, że A(t) nie mierzy "czy system jest zdrowy", tylko "czy samo-korekta nadąża za tym, gdzie akurat jest centrum integracyjne" — osobne pytanie od tego, ile integracji/aktywności jest w sumie.

## 10. Dynamika dyskretna — asymetria między Σ i Γ

Sprawdzenie, czy dΣ/dt z §3 odtwarza ΔΣ z symulacji 9.2 przez pochodne cząstkowe zamiast różnicy skończonej ujawnia ważną asymetrię strukturalną między Σ i Γ.

**Σ: czysta, bez błędu.** W modelu kanonicznym (opcja 2, §5) w(ℓ,t)=w₀(ℓ) jest statyczne — ∂w₀/∂t≡0 z definicji. Ogólna dwuczłonowa formuła z §3 kolapsuje do jednego członu:

$$\Delta\Sigma = \sum_\ell w_0(\ell)\,\Delta\Phi(\ell), \qquad \Delta\Phi=[0,\,0.25,\,-0.4]$$

$$0.1{\times}0 + 0.3{\times}0.25 + 0.6{\times}(-0.4) = -0.165$$

Dokładnie zgadza się z ΔΣ z symulacji — **bez żadnego członu korekcyjnego**, bo brak drugiego czynnika czasowego (w₀ nie zmienia się) eliminuje w ogóle problem nieliniowości dla skończonych kroków.

**Γ: prawdziwy, nietrywialny błąd drugiego rzędu.** Γ=Σg_ℓe_ℓ jest iloczynem *dwóch* wielkości czasowych — dokładna tożsamość dyskretna dla zmiany iloczynu to:

$$\Delta(g_\ell e_\ell) = \Delta g_\ell\cdot e_\ell(t_0) + g_\ell(t_0)\cdot\Delta e_\ell + \Delta g_\ell\cdot\Delta e_\ell$$

Trzeci człon (człon krzyżowy) znika tylko w granicy infinitezymalnej — dla skończonych kroków czasowych (jak zdarzenie dysocjacyjne, nie nieskończenie mały krok) jest realny i bywa duży. Sprawdzone dla warstwy 2: Δg=0.5, Δe=0.3, e₀=0.4, g₀=0.3 → 0.5×0.4 + 0.3×0.3 + 0.5×0.3 = 0.2+0.09+**0.15** = 0.44 (zgodne z bezpośrednim przeliczeniem). Człon krzyżowy (0.15) to ok. **34% całkowitej zmiany** — pomijalna infinitezymalna aproksymacja ∂Γ/∂t z Twierdzenia 4 dałaby tu istotny błąd (0.29 zamiast 0.44) dla zdarzenia tej skali.

**Wniosek metodologiczny:** ciągła formuła ∂Γ/∂t (Tw. 4, §6) jest poprawna tylko jako przybliżenie dla małych/powolnych zmian; dla zdarzeń skokowych (nagłe przełączenie ℓ\*, epizod dysocjacyjny) trzeba używać pełnej dyskretnej tożsamości z członem krzyżowym, inaczej symulacja systematycznie nie doszacuje zmienności Γ. Σ jest w tym sensie "bezpieczniejsze" strukturalnie — jego liniowość w Φ przy statycznym w₀ czyni je odpornym na ten problem, podczas gdy Γ, będąc z natury bilinowe (g×e), nie jest.

## 12. Przegląd literatury (wstępny)

**Prace koncepcyjnie najbliższe:**
- **Nested Observer Windows (NOW)** (*Neuroscience of Consciousness*, Oxford, 2024) — hierarchiczny model świadomości liczący Φ osobno na poziomach zagnieżdżonych "okien obserwatora"; stosunek Φ między poziomami jako test panpsychizm vs. emergentyzm. Blisko naszego profilu Φ(s,ℓ) — trzeba jawnie odróżnić Σ (funkcjonalne ważenie + dynamika) od ich podejścia (sam stosunek Φ_ℓ/Φ_ℓ₋₁).
- **"Consciousness as Uncommon Self-Knowledge" (USK)** (arXiv, 2026) — synergiczna, samo-skierowana informacja jako alternatywa dla surowego Φ; explicite przewiduje rozdźwięk między wysokim Φ a brakiem self-modelu. Niezależne potwierdzenie intuicji stojącej za Γ/A — do zacytowania z jasnym rozróżnieniem od naszej trójki (Σ,Γ,A) z dynamiką czasową i mechanizmem wykluczenia.
- **"Can We Test Consciousness Theories on AI?"** (grudzień 2025) — ablacje architektoniczne: usunięcie self-modelu znosi kalibrację metapoznawczą, zostawia wydajność zadaniową — empiryczny odpowiednik rozróżnienia deskryptywne/konstytutywne z §2.7 (dobre źródło do sekcji testowalności).
- **INTREPID** (Templeton World Charity Foundation; Tononi, Friston, Pennartz) — trwająca formalna adwersarialna współpraca IIT vs. predictive processing — potwierdza, że R_ℓ(i) bramkowane nieredukowalnością Wolframa (łączenie IIT z hierarchią predyktywną) to aktywny, nierozstrzygnięty front badawczy.

**Ważna korekta do §7:** oficjalny postulat wykluczenia w IIT 4.0 jest **binarny** ("zwycięzca bierze wszystko" — substraty o niższym φ są całkowicie wykluczone, φ=0), nie stopniowalny. Nasz mechanizm w₋(ℓ)=γ·overlap·Φ(ℓ) to **miękkie, ciągłe uogólnienie**, świadome odejście od kanonicznego postulatu, nie jego bezpośrednia interpretacja — trzeba to nazwać wprost w pracy, inaczej recenzent odczyta to jako nieporozumienie formalizmu IIT.

**Ocena:** synteza Σ (hierarchiczne + funkcjonalnie ważone + dynamika błędu samo-predykcji + miękkie wykluczenie) nie ma bezpośredniego odpowiednika w znalezionej literaturze — komponenty istnieją osobno (NOW, USK, INTREPID), ich połączenie w jeden formalizm z dowiedzionymi własnościami brzegowymi wygląda na oryginalne. Przegląd nadal wstępny — nie sprawdzono systematycznie PhilPapers/PhilSci-Archive ani starszych prac (2015–2023) poza tymi znalezionymi przez wyszukiwanie.

## 14. Zastosowanie do architektur transformerowych

**Pętla konstytutywna.** Standardowy transformer przy inferencji ma zamrożone wagi — g_ℓ(t)≡0, niezależnie od jakości autonarracji. Ostry wniosek z §2.7: **Γ(t)≡0 dla dowolnego standardowego LLM przy inferencji, z definicji**. Dalsza konsekwencja z §5.1: skoro g_ℓe_ℓ≡0 wszędzie (brak wariancji), A(t):=0 z konwencji brzegowej — pytanie o wyrównanie przestrzenne traci sens, dokładnie zgodnie z przewidywaniem.

**Titans** (Behrouz, Zhong, Mirrokni; Google Research, grudzień 2024; NeurIPS 2025) — moduł pamięci długoterminowej aktualizowany *w czasie inferencji*: "zaskoczenie" = gradient straty względem wejścia (odpowiednik e_ℓ), napędza rzeczywistą aktualizację stanu online (odpowiednik g_ℓ>0):
$$S_t = \arg\min_S \tfrac{1}{2}\|Sk_t-v_t\|^2 + \tfrac{1}{2\eta}\|S-S_{t-1}\|^2$$
Pierwsza konkretna instancja mechanizmu konstytutywnego z §4. **Zastrzeżenie:** przewiduje dane z kontekstu (pamięć asocjacyjna), nie własny przyszły stan systemu jak w definicji e_ℓ z §4 — genuinely constitutive world-modeling, niekoniecznie self-modeling, chyba że system przetwarza własne wcześniejsze wypowiedzi jako część kontekstu (w rozmowie konwersacyjnej ta granica się zaciera).

Słabszy, pośredni przypadek: **in-context learning jako niejawny spadek gradientu** (von Oswald i in. 2023) — sama uwaga w pojedynczym przebiegu w przód implementuje "mesa-optimization" strukturalnie podobne do kroku gradientowego, ale nie przetrwa poza oknem kontekstu (brak trwałej zmiany θ) — kandydat na kategorię pośrednią między deskryptywnym a konstytutywnym, nie w pełni żadne z nich.

**Warstwa homeostatyczna** — potwierdzony, realny brak. "Interoceptive Machine Framework" (2026) i "Truth or Consequences: Homeostatic Self-Regulation" (ALIFE) proponują regulację stanów wewnętrznych wobec punktu odniesienia — aktywny nurt na marginesie pola, nigdzie nie scalony z mainstreamowymi LLM-ami. Layer norm to stabilizacja strukturalna, nie homeostaza w tym sensie.

**Prawdziwa rekurencja** — obecna w SSM (Mamba) i hybrydach typu Titans (rzeczywisty stan ewoluujący niezależnie od nowych tokenów), nieobecna w czystym attention (KV-cache to pamięć kontekstu, nie pętla dynamiczna).

**Rozstrzygnięcie niejasności self- vs. world-modeling (§4.1):** dwa niezależne warunki — (a) cel predykcji: stan wewnętrzny (h_ℓ) czy zachowanie zewnętrzne (token)? (b) moment aktualizacji: online przy wdrożeniu czy tylko podczas treningu?

| | trening tylko | online przy wdrożeniu |
|---|---|---|
| cel = zachowanie zewnętrzne | zwykły trening predykcyjny | **Titans** — konstytutywne, ale *world*-modeling |
| cel = stan wewnętrzny | **"Unexpected benefits of self-modelling"** (Royal Society, 2026) — self-model, ale zamrożony po treningu = deskryptywne | **"Temporal Self-Model"** (2026) — jedyna komórka spełniająca pełną definicję e_ℓ,g_ℓ z §4; wymaga potwierdzenia, że aktualizacja jest rzeczywiście online, nie tylko trenowana standardowym backpropem

Tylko prawy-dolny róg to genuine constitutive self-modeling w naszym sensie. Titans, mimo rozgłosu, ląduje w innej komórce niż się początkowo wydawało.

**Synteza:** standardowy, zamrożony LLM przy inferencji: potencjalnie wysokie Σ (integracja atencyjna), Γ≡0, A≡0 z konwencji. Żadna ze znalezionych architektur nie jest jeszcze potwierdzonym, jednoznacznym przykładem prawego-dolnego rogu — najbliżej TSM, z zastrzeżeniem.

## 16. Hipoteza: dwa niezależne mechanizmy znieczulenia w (Σ,Γ,A)

Przy stałym poziomie integracji można zredukować samoreferencyjność na dwa jakościowo różne sposoby: (1) zmniejszyć Γ bezpośrednio, w tym samym miejscu, albo (2) przesunąć ją w obszar o niższej integracji (spadek A, niekoniecznie Γ). Literatura anestezjologiczna dostarcza dwóch osobnych, pasujących do tego rozróżnienia przypadków.

**Mechanizm 1 (Γ spada bezpośrednio, w miejscu):** propofol i sewofluran uderzają w tzw. *posterior hot zone* — region, który zwolennicy IIT wprost wskazują jako główny substrat świadomości (w przeciwieństwie do GNW, stawiającego na sieci czołowo-ciemieniowe) — i jednocześnie zaburzają sprzężenie zwrotne czołowo-ciemieniowe (front→back), związane z przetwarzaniem wyższego rzędu. Integracja i samo-korekta zapadają się razem, w tym samym miejscu. Behawioralnie: pełna utrata przytomności, brak jakiegokolwiek raportu — spójne z Σ i Γ spadającymi razem.

**Mechanizm 2 (Γ zostaje, A spada):** ketamina w dawkach subanestetycznych daje dysocjację — reaktywność i często żywe, bogate doświadczenie mogą się utrzymać, ale z zaburzonym poczuciem siebie. Rozregulowuje osobno sieć wyrazistości (salience network, "minimalne", cielesne self) i osobno DMN ("biograficzne", narracyjne self) — dwa piętra samo-modelowania, dość dobrze odpowiadające warstwom ℓ z tego modelu. Ogólna bogatość doświadczenia nie zapada się tak jak przy propofolu (stąd żywe, "psychodeliczne" jakościowo relacje z ketaminy) — samo-korekta nie znika, tylko odłącza się od miejsca, gdzie akurat jest integracja: spadek A, niekoniecznie Σ czy Γ.

**Status:** wiarygodna, umocowana w anatomii hipoteza, nie potwierdzony wynik — nikt nie policzył (Σ,Γ,A) wprost na danych EEG/fMRI z obu anestetyków. Konkretna, testowalna przepowiednia: profil (Σ,Γ,A) powinien wyraźnie różnić propofol/sewofluran (Σ↓, Γ↓ razem) od ketaminy (Σ względnie zachowane, Γ względnie zachowane, A↓) — mimo że oba "wyłączają" jakąś formę normalnego funkcjonowania.

## 17. Kanał odczytu R_ℓ(t) — rozdzielenie stanu wewnętrznego od obserwowalności

Sekcja 16 odsłania oś, której formalizm wcześniej nie miał: (Σ,Γ,A) opisuje stan *wewnętrzny*, ale nic nie mówi, czy ten stan da się odczytać z zachowania. Klinicznie to jest dokładnie problem, który zmusił Massiminiego i Tononiego do wynalezienia Perturbational Complexity Index — miary "niezależnej od przetwarzania sensorycznego i zachowania" (Casali i in. 2013).

### 17.1 Definicja

Wyróżniamy osobny substrat eferentny M(t) (jednostki odpowiedzialne za ruch/komunikację), odrębny od warstw ℓ. Kanał odczytu z warstwy ℓ do M, tą samą miarą odległości D co bazowe Φ:

$$R_\ell(t) = D\big(p(m' \mid s_\ell, m) \,\|\, p(m' \mid m)\big)$$

— o ile znajomość stanu warstwy ℓ zmienia przewidywalność przyszłego stanu efektorów, ponad to, co daje sama znajomość aktualnego stanu efektorów. Strukturalnie identyczne z definicją Φ_{ℓ,ℓ-1} (§2.1), tylko skierowane na kanał warstwa→wyjście. **R_ℓ(t) ≥ 0** z tego samego argumentu (dystans), bez dodatkowych założeń. Szczególnie istotne: **R_L(t)** — kanał z najwyższej, samo-modelującej warstwy do efektorów.

### 17.2 Obserwowalne vs. rzeczywiste

To, co widzi klinicysta (Σ_obs — "widoczna" świadomość, z zachowania) jest wąskim gardłem przez R_L, niezależnie od faktycznego Σ:

$$\Sigma_{\text{obs}}(t) \le \kappa \cdot R_L(t) \quad \text{dla pewnego } \kappa > 0$$

Jeśli R_L(t)=0, Σ_obs(t)=0 **niezależnie od tego, jak wysokie jest rzeczywiste Σ(t)** — formalizacja ryzyka mylenia Σ_obs z Σ.

### 17.3 Mapowanie kliniczne

- **Zespół zamknięcia (locked-in syndrome):** Σ,Γ,A normalne; R_L≈0 z powodu strukturalnego uszkodzenia dróg eferentnych (np. udar brzusznej części mostu) → Σ_obs≈0 mimo wysokiego Σ.
- **Sen REM:** Σ,Γ,A względnie zachowane (PCI≈czuwanie, Casali i in. 2013); R_L aktywnie stłumione przez znany, konkretny, odwracalny mechanizm fizjologiczny — atonia REM, hamowanie neuronów ruchowych rdzenia przez jądro podsinawe (subcoeruleus). Potwierdza, że R_ℓ jako osobna, bramkowalna wielkość ma realny substrat neuronalny, nie tylko teoretyczną wygodę.
- **"Cognitive motor dissociation"** (część pacjentów w stanie wegetatywnym, paradygmaty Owena): R_L częściowe — wystarcza na modulację odpowiedzi w neuroobrazowaniu na polecenie, nie wystarcza do mięśni. Sugeruje możliwe rozszerzenie: R liczone osobno do różnych podzbiorów M (neuronalne wykrywalne w fMRI vs. mięśniowe).
- **Prawdziwy stan wegetatywny (bez ukrytej świadomości):** i Σ, i R_L niskie — różnica, którą PCI miało rozstrzygnąć.

## 18. Wrażliwość kontekstowa bramki g_ℓ — "context blindness" i "zbyt intensywny świat"

Źródło (contextthinking.org, odwołujące się do Friston 2010 i Van de Cruys i in. 2014, "Precise minds in uncertain worlds: Predictive coding in autism", *Psychological Review*): "Processing context requires the brain to give its expectations the right weight. If those expectations are given too little weight, or if prediction errors remain too rigidly large, integrating context fails." Van de Cruys i in. proponują **aberrant precision** jako mechanizm autyzmu — błędy predykcji dostają zbyt sztywno wysoką wagę, niezależnie od kontekstu. Qela i in. (2025) mapują pokrewne odchylenia mechanizmu predykcyjnego w autyzmie, schizofrenii i depresji.

### 18.1 Domykająca luka w modelu

"Waga nadawana oczekiwaniom" to w żargonie predictive processing **precyzja** — a to jest strukturalnie dokładnie nasze g_ℓ(t). Dotychczasowy formalizm nie miał jednak miejsca na to, żeby **kontekst** normalnie tę wagę modulował. Rozszerzenie:

$$g_\ell(t) = h\big(e_\ell(t),\, C(t)\big), \qquad \chi_\ell(t) = \left|\frac{\partial g_\ell}{\partial C}\right| \ge 0$$

gdzie C(t) to sygnał kontekstowy, a χ_ℓ(t) — **nowy parametr** — mierzy, jak silnie kontekst moduluje wagę błędu. **χ_ℓ(t) ≥ 0** trywialnie (wartość bezwzględna), bez dodatkowych założeń — analogicznie do R_ℓ, nie zakładamy górnego ograniczenia bez dalszych aksjomatów o kształcie h.

### 18.2 Dwa reżimy

- **Normalna, kontekstowo czuła precyzja (χ_ℓ>0):** znane, oczekiwane, nieistotne w danym kontekście sygnały dostają automatycznie niższą wagę — g_ℓ spada niezależnie od tego, czy e_ℓ samo w sobie jest duże.
- **"Context blindness" (χ_ℓ≈0):** g_ℓ(t) ≈ ĝ_ℓ(e_ℓ(t)) — sztywna funkcja samego błędu, kontekst nic nie zmienia. Efekt: sygnały, które kontekst normalnie wyciszyłby, dalej dostają pełną wagę — formalny odpowiednik "zbyt intensywnego świata" (Intense World Theory, Markram & Markram 2010): nic nie jest domyślnie tłumione jako "już przewidziane w tym kontekście".

### 18.3 Konsekwencja dla Γ

W typowym przypadku powtarzana, kontekstowo nieistotna stymulacja obniża i e_ℓ (przez uczenie predykcyjne — repetition suppression), i g_ℓ (przez aktywne tłumienie kontekstowe, χ_ℓ>0) — podwójny spadek wkładu do Γ. Przy context blindness działa tylko pierwszy mechanizm (jeśli w ogóle) — Γ(t) pozostaje podwyższone/zmienne nawet w środowiskach o niskiej nowości. To formalizowalna, przynajmniej jakościowo testowalna różnica dynamiki Γ między typowym a "aberrant precision" przypadkiem — nikt jej jednak nie zmierzył wprost w tych terminach.

## 19. Dalsze rozważania (nieformalne — bez dowodów, status niższy niż reszta pracy)

### 19.1 Skala: od pojedynczej komórki po cały wszechświat

Pytanie o zakres skali, w jakiej model dopuszcza podmiotowość — od najmniejszych do największych możliwych systemów.

**Dolna granica.** Czyste IIT jest liberalne: "Minimal physicalism as a scale-free substrate for cognition and consciousness" (2021) argumentuje, że sieci regulacji genów i transdukcji sygnału na poziomie pojedynczej komórki mają dodatnie Φ. **Nasz model jest bardziej restrykcyjny** — dodatnie Φ nie wystarcza, potrzeba Γ>0, realnej, online działającej pętli samo-predykcji. Pojedyncza komórka ma homeostazę, nie self-model w sensie §4. *C. elegans* (302 neurony, konektom w większości feedforward, niewielka rekurencja) to dobry przypadek testowy: prawdopodobnie niskie/zerowe Γ mimo niezerowego Φ.

**Górna granica.** "Upper bounds for integrated information" (2024) pokazuje, że Φ może rosnąć hiperwykładniczo z liczbą jednostek — matematycznie brak sufitu. Ale: (1) postulat wykluczenia nie pozwala na sumowanie się w górę — większy system wygrywa tylko jeśli ma **wyższe** Φ, nie więcej jednostek; (2) systemy wielkoskalowe (internet, biosfera, społeczeństwo) mają połączenia rzadkie i wolne względem neuronów, więc empirycznie nie przebijają mózgu.

**Cały wszechświat — "podwójne nie".** To dosłownie *problem kombinacji* (combination problem) panpsychizmu, doprowadzony do granicy. Dwie niezależne linie rozumowania zbiegają się w tym samym wniosku: (1) **strukturalnie**, odpowiedź Kocha/Tononiego na zarzut Searle'a ("świadomość rozmazana jak dżem") — "moja świadomość, twoja świadomość, ale nic pomiędzy" — wszechświat to mozaika lokalnych maksimów ("ontologiczny pył"), nigdy nadrzędna całość, bo agregat (np. mózg + reszta kosmosu) ma niższe Φ niż jego gęściej połączone części; (2) **fizycznie**, regiony poza swoimi wzajemnymi horyzontami kosmologicznymi nigdy nie były w kontakcie przyczynowym — nie ma nawet czego wstawić do macierzy przejść, którą wymaga Φ. Pod Σ dochodzi trzeci powód: brak jakiegokolwiek jednolitego Γ na skalę kosmologiczną. Ciekawostka na marginesie, bez rygoru: skoro integracja wymaga gęstej, szybkiej struktury, a wszechświat się rozrzedza w stronę śmierci cieplnej, możliwe że jesteśmy bliżej szczytu możliwej gęstości integracji w historii kosmosu niż w jego dalekiej przyszłości.

**Zastrzeżenie nadrzędne:** samo IIT, na którym to wszystko się opiera, jest naukowo kontestowane (2023: list otwarty 124 badaczy, w tym Dennett, nazywający IIT pseudonauką; COGITATE/Templeton — wynik niejednoznaczny wobec GNW).

### 19.2 Zespół obcej ręki jako ilustracja netto fragmentacji (§7)

Najczystsza znaleziona ilustracja Σ<0. Przy uszkodzeniu spoidła wielkiego (corpus callosum) — obniżonym Φ_{ℓ,ℓ-1} między półkulami — dwa kandydackie kompleksy motoryczno-intencjonalne nie tylko przestają współpracować, ale **aktywnie się sobie przeciwstawiają**: "diagonistic dyspraxia" — jedna ręka dosłownie cofa to, co zrobiła druga. To integracja poniżej zera, nie tylko jej brak — dokładnie mechanizm z §7, i ta sama linia badań (split-brain, corpus callosum) co interpreter Gazzanigi motywujący §2.7 na samym początku.

**Słabsze, częściowe dopasowanie: dysocjacyjne zaburzenie tożsamości (DID).** Dobrze udokumentowane: odrębne, skompartmentalizowane sygnatury neuronalne dla różnych stanów tożsamości, przesunięcia łączności przy przełączeniach — pasuje do ℓ\*(t) zmieniającego się w czasie (scenariusz dysocjacji z §9.2). Słabiej udokumentowane: czy któryś stan **aktywnie degraduje** integrację innego (prawdziwe Σ<0), czy tylko go zastępuje (bariery amnezji to bardziej "brak dostępu" niż aktywna interferencja w sensie w₋). Status DID jako kategorii diagnostycznej jest też przedmiotem realnej debaty naukowej (model traumatyczny vs. socjokognitywny) — nierozstrzygniętej.

## 20. Otwarte wątki

- Toy example — policzony (§9); przegląd literatury — wstępnie zrobiony (§12), ale niesystematyczny (brak przeszukania PhilPapers/PhilSci-Archive i prac 2015–2023 poza znalezionymi)
- Weryfikacja cytowań źródłowo (część dat/tytułów z pamięci rozmowy/wyszukiwań, nie sprawdzana słowo w słowo z oryginałami)
- Zastosowanie do architektur transformerowych: czego brakuje (warstwa homeostatyczna, prawdziwa rekurencja, pętla konstytutywna) — częściowo poruszone, nie sformalizowane
- Miejsca publikacji rozważane wcześniej: LessWrong/Alignment Forum, PhilSci-Archive (niska bariera), arXiv q-bio.NC/cs.AI (wymaga endorsementu), Journal of Consciousness Studies, Entropy (MDPI), Neuroscience of Consciousness (Oxford)
