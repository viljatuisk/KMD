# KMD Projekt

## Ülevaade
KMD (Käibemaksudeklaratsioon) on Directo-stiilis veebirakendus KMD tehingupäeviku haldamiseks.

**GitHub:** `viljatuisk/KMD`
**Avalik URL:** https://viljatuisk.github.io/KMD/

## Failid

| Fail | Kirjeldus |
|------|-----------|
| `kmd_tehingupaevik_ver2.html` | Peamine fail — tehingupäevik, aktiivne arendusfail |
| `kmd_tehingupaevik_ver1.html` | Varasem versioon |
| `index.html` | Avalehe fail |
| `elsa_kallis.html` | Eraldiseisev leht |
| `serve.py` | Kohalik livereload server testimiseks (ainult arenduskeskkonnas) |

## kmd_tehingupaevik_ver2.html

### Kujundus
- Hele ja tume teema (toggle-nupp päises: `☀ Hele` / `☾ Tume`)
- Vaikimisi: **tume** Directo-stiilis kujundus
- Teema salvestub `localStorage`-i võtmega `kmd-theme`
- CSS muutujad `:root` ja `[data-theme="dark"]` blokkides

### Struktuur
- Vasak paneel: filtrid (periood, registrikood, KMD sektsioon, KMK kood)
- Peaala: kolm tab-i — Tehingupäevik, Lisa kirje, Koondvaade
- Päis: staatuse riba, kokkuvõttekaardid (M, S, O, tasumisele)

### Tehnoloogia
- Puhas HTML/CSS/JavaScript, ilma raamistikulta
- Kõik andmed on JS massiivina failis (ei kasuta backendi)

## Arendusvoog
- Tööharu: `claude/move-public-files-B5qn5`
- GitHub Pages serveerib `main` harust
- Muudatused nähtavad avalikul URL-il pärast PR merge-i `main`-i
