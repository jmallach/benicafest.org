# Benicafest — Lloc web oficial

Lloc web del **Benicafest**, festival de música a Gaianes, el Comtat.
Construït amb [Hugo](https://gohugo.io/) i allotjat a GitHub Pages.

---

## 🚀 Posada en marxa (primera vegada)

### 1. Instal·la Hugo
```bash
# macOS
brew install hugo

# Linux (Debian/Ubuntu)
sudo apt install hugo

# Windows — descarrega l'instal·lador a https://gohugo.io/installation/
```

### 2. Clona el repositori
```bash
git clone https://github.com/EL-TEU-USUARI/benicafest.git
cd benicafest
```

### 3. Arrenca el servidor local
```bash
hugo server -D
```
Obre `http://localhost:1313` al navegador. Els canvis es recarreguen automàticament.

---

## ✏️ Editar contingut

Tot el contingut editable és a la carpeta `content/` en format **Markdown**.

### Canviar dates, lloc, organitzadors
Edita el fitxer **`hugo.toml`** a l'arrel del projecte:
```toml
[params]
  date         = "13 de juny de 2026"
  doors        = "19:30"
  concertStart = "20:00"
  location     = "Gaianes, el Comtat"
  organiser    = "..."
```

### Editar una banda del lineup
Cada banda és un fitxer Markdown a `content/lineup/`:
```
content/lineup/
  marcel-el-marcia.md
  fardatxo.md
  the-sgraciats.md
  invers.md
  arre-ak.md
```

Exemple d'un fitxer de banda:
```markdown
---
title: "Invers"
genre: "Rock-metal alternatiu · En valencià"
time: "22:30"          ← hora d'actuació
order: 4               ← ordre al lineup (1 = primer)
familyFriendly: false
website: "https://..."
instagram: "https://www.instagram.com/..."
---

Bio de la banda en Markdown. Pots escriure **negreta**, *cursiva*, etc.
```

### Afegir una banda nova
```bash
hugo new lineup/nom-de-la-banda.md
```
Això crea el fitxer amb tots els camps buits a partir de l'arquetip.

### Eliminar una banda
Simplement esborra el fitxer corresponent de `content/lineup/`.

---

## 🌐 Publicar a GitHub Pages

### Primera vegada: configura GitHub Pages
1. Ves a **Settings → Pages** al teu repositori de GitHub.
2. A *Source*, selecciona **GitHub Actions**.
3. Edita `hugo.toml` i canvia `baseURL` per la teva URL real:
   ```toml
   baseURL = "https://EL-TEU-USUARI.github.io/benicafest/"
   # o si tens domini propi:
   baseURL = "https://benicafest.cat/"
   ```

### Publicar canvis
```bash
git add .
git commit -m "Actualitzo horaris del lineup"
git push
```
GitHub Actions construirà i publicarà el lloc automàticament en 1-2 minuts.
Pots veure el progrés a la pestanya **Actions** del teu repositori.

### Domini propi (opcional)
1. Afegeix el teu domini a **Settings → Pages → Custom domain**.
2. Al teu proveïdor DNS, crea un registre CNAME apuntant a `EL-TEU-USUARI.github.io`.
3. Actualitza `baseURL` a `hugo.toml`.

---

## 📁 Estructura del projecte

```
benicafest/
├── hugo.toml                  ← configuració i paràmetres globals
├── content/
│   ├── _index.md              ← pàgina d'inici
│   └── lineup/                ← un fitxer .md per banda
├── layouts/
│   ├── index.html             ← plantilla de la pàgina d'inici
│   ├── _default/baseof.html   ← estructura HTML base
│   └── partials/              ← components reutilitzables (nav, footer, logos)
├── static/
│   ├── css/main.css           ← tots els estils
│   └── js/main.js             ← JavaScript mínim
├── archetypes/lineup.md       ← plantilla per a noves bandes
└── .github/workflows/
    └── deploy.yml             ← desplegament automàtic a GitHub Pages
```

---

## 🛠 Eines útils

| Acció | Comanda |
|-------|---------|
| Servidor local | `hugo server` |
| Construir el lloc | `hugo --minify` |
| Nova banda | `hugo new lineup/nom-banda.md` |

---

*Benicafest · Organitzat per veïns i veïnes de Gaianes · el Comtat*
