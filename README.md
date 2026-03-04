# Benicafest — Lloc web oficial

Lloc web del **Benicafest**, festival de música a Gaianes, el Comtat.
Construït amb [Hugo](https://gohugo.io/) i allotjat a GitHub Pages a **[benicafest.org](https://benicafest.org)**.

Repositori: [github.com/jmallach/benicafest.org](https://github.com/jmallach/benicafest.org)

---

## 🚀 Posada en marxa (primera vegada)

### 1. Instal·la Hugo

```bash
# macOS
brew install hugo

# Linux (Debian/Ubuntu)
sudo apt install hugo

# Windows — descarrega l'instal·lador des de https://gohugo.io/installation/
```

### 2. Clona el repositori

```bash
git clone https://github.com/jmallach/benicafest.org.git
cd benicafest.org
```

### 3. Arrenca el servidor local

```bash
hugo server
```

Obre `http://localhost:1313` al navegador. Els canvis es recarreguen automàticament.

---

## ✏️ Editar contingut

### Canviar dates, lloc, organitzadors

Edita **`hugo.toml`** a l'arrel del projecte:

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

Exemple:

```markdown
---
title: "Invers"
genre: "Rock-metal alternatiu · En valencià"
time: "22:30"
order: 4               # ordre al lineup (1 = primer)
familyFriendly: false
website: "https://..."
instagram: "https://www.instagram.com/..."
---

Bio de la banda en Markdown.
```

### Afegir una banda nova

```bash
hugo new lineup/nom-de-la-banda.md
```

### Eliminar una banda

Esborra el fitxer corresponent de `content/lineup/`.

---

## 🌐 Publicar canvis

```bash
git add .
git commit -m "Actualitzo horaris del lineup"
git push
```

GitHub Actions construirà i publicarà el lloc automàticament en 1-2 minuts.
Segueix el progrés a la pestanya **Actions** del repositori.

---

## ⚙️ Configuració de GitHub Pages (primera vegada)

1. Ves a **Settings → Pages** al repositori.
2. A *Source*, selecciona **GitHub Actions**.
3. A *Custom domain*, escriu `benicafest.org` i clica **Save**.

El fitxer `static/CNAME` ja conté el domini, de manera que el desplegament
automàtic mai el perdrà.

---

## 🌍 DNS — benicafest.org

El domini ha d'apuntar als servidors de GitHub Pages. Comprova que el teu
proveïdor DNS té aquests registres:

| Tipus  | Nom  | Valor                   |
|--------|------|-------------------------|
| A      | @    | `185.199.108.153`       |
| A      | @    | `185.199.109.153`       |
| A      | @    | `185.199.110.153`       |
| A      | @    | `185.199.111.153`       |
| CNAME  | www  | `jmallach.github.io`    |

Per verificar que tot és correcte, executa des del terminal:

```bash
dig benicafest.org A +short
# Ha de mostrar les quatre IPs de GitHub Pages

dig www.benicafest.org CNAME +short
# Ha de mostrar jmallach.github.io
```

Si els registres ja estan configurats, el lloc hauria d'estar disponible a
`https://benicafest.org` poc després del primer desplegament.

---

## 📁 Estructura del projecte

```
benicafest.org/
├── hugo.toml                    ← configuració i paràmetres globals
├── content/
│   ├── _index.md                ← pàgina d'inici
│   └── lineup/                  ← un fitxer .md per banda
├── layouts/
│   ├── index.html               ← plantilla de la pàgina d'inici
│   ├── _default/baseof.html     ← estructura HTML base
│   └── partials/                ← components (nav, footer, logos SVG)
├── static/
│   ├── CNAME                    ← domini personalitzat per a GitHub Pages
│   ├── css/main.css             ← tots els estils
│   └── js/main.js               ← JavaScript mínim
├── archetypes/lineup.md         ← plantilla per a noves bandes
└── .github/workflows/
    └── deploy.yml               ← desplegament automàtic
```

---

## 🛠 Referència ràpida

| Acció | Comanda |
|-------|---------|
| Servidor local | `hugo server` |
| Construir el lloc | `hugo --minify` |
| Nova banda | `hugo new lineup/nom-banda.md` |

---

*Benicafest · Organitzat per veïns i veïnes de Gaianes · el Comtat*
