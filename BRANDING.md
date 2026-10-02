# Identité officielle Content Factory

Le symbole **CF**, blanc `#ffffff` sur fond anthracite `#11151d`, est un dessin géométrique sans police, dégradé ni ressource externe. Le C comporte deux angles coupés ; le F conserve une forme simple. Le fond carré opaque et les proportions sont identiques à toutes les tailles.

![Icône officielle](assets/branding/content-factory-icon-192.png)

## Source unique et fichiers créés

**Seul fichier à modifier pour changer le dessin :** `assets/branding/content-factory-icon.svg`.

Tous les fichiers de cette table sont dans `assets/branding/` :

| Fichier | Dimensions |
| --- | --- |
| `content-factory-icon.svg` | Vectoriel, viewBox 64 × 64, taille nominale 1024 × 1024 |
| `favicon.ico` | Trois images : 16 × 16, 32 × 32, 48 × 48 |
| `favicon-16x16.png` | 16 × 16 |
| `favicon-32x32.png` | 32 × 32 |
| `apple-touch-icon.png` | 180 × 180 |
| `content-factory-icon-192.png` | 192 × 192 |
| `content-factory-icon-512.png` | 512 × 512 |
| `content-factory-tiktok-app-icon.png` | 1024 × 1024, RGB opaque, 5 151 octets |

`favicon.ico` à la racine est une copie exacte du fichier du dossier branding. Le script `scripts/generate_branding.py` produit tous les formats depuis le SVG avec resvg et Pillow. Les dépendances de génération sont isolées par `uv` et ne sont pas ajoutées au moteur Content Factory.

```sh
uv run scripts/generate_branding.py
```

Pour synchroniser également l'interface locale depuis ce dossier :

```sh
uv run scripts/generate_branding.py \
  --app-static ../content_factory/content_factory/web/static
```

Les huit fichiers de `content_factory/content_factory/web/static/branding/` sont des copies générées, identiques octet par octet aux fichiers du site. Ne pas modifier ce second SVG directement.

Ce document et la section branding du `README.md` décrivent la procédure.

## Intégration HTML et favicon

Fichiers HTML modifiés : `index.html`, `privacy/index.html`, `terms/index.html`.

- Leur `<head>` déclare les icônes ICO, SVG, PNG 32/16 et Apple 180, ainsi que la couleur du thème.
- Leur lien `.brand`, dans le `<header>`, affiche le SVG maître avec une image de 40 × 40 et le nom Content Factory à côté.
- `assets/style.css` aligne le symbole et le nom et laisse la navigation passer à la ligne sur mobile.
- Les chemins utilisent `assets/...` à la racine et `../assets/...` dans les pages légales. Le favicon ICO utilise respectivement `favicon.ico` et `../favicon.ico`.
- Les URLs incluent la version stable `?v=cf-1`, également appliquée au CSS. Lors d'un futur changement de design, incrémenter cette version dans les trois pages publiques et le template local.

Dans le moteur, `content_factory/web/templates/base.html` déclare les mêmes icônes dans le `<head>` et remplace l'ancien logo typographique vert par le SVG dans la barre latérale. `content_factory/web/static/app.css` définit ses dimensions sans recoloration ni recadrage. `content_factory/web/app.py` sert `/favicon.ico` depuis le même jeu d'assets. Redémarrer un serveur local déjà lancé pour charger cette nouvelle route.

## Fichier à envoyer à TikTok

**TikTok Developer App Icon :**

```text
/Users/moi/code/money_printer/content-factory-site/assets/branding/content-factory-tiktok-app-icon.png
```

**Upload this file in TikTok Developer -> Basic Information -> App icon**

Dans ton portail : **Content Factory Bot → Production → Basic Information → App icon**.

Le [guide officiel Register Your App](https://developers.tiktok.com/docs/en/getting-started-create-an-app#basic-information), consulté le 2 octobre 2026, indique une icône de 1024 × 1024 pixels, JPEG/JPG/PNG, de 5 Mo maximum. Le fichier fourni respecte ces spécifications. Aucune configuration du portail, aucun credential et aucun paramètre OAuth n'ont été modifiés.

Avant une nouvelle soumission, déployer les fichiers modifiés de ce dépôt sur GitHub Pages et attendre la fin du déploiement, puis charger le PNG dans le portail. Vérifier sur l'URL publique utilisée par TikTok que la homepage, Privacy, Terms et l'onglet du navigateur montrent la nouvelle icône. Si un ancien favicon persiste, fermer puis rouvrir l'onglet ou vérifier dans une fenêtre privée. Le changement est préparé et vérifié localement ; aucun push GitHub ni déploiement public n'a été effectué pendant cette passe. La décision de review appartient à TikTok.

## Validation du 2 octobre 2026

- Serveur statique local lancé à la racine, puis sous `/content_factory_website/` pour simuler un site de projet GitHub Pages.
- Chromium : homepage, Privacy et Terms en HTTP 200 dans les deux configurations ; logo visible ; cinq déclarations d'icônes résolues par page ; tous les fichiers image et le favicon ICO en HTTP 200 avec un type MIME image.
- Application locale lancée sur un serveur de validation isolé : huit pages vérifiées (`/`, `/jobs/new`, `/jobs`, `/clips`, `/publishing`, `/tiktok`, `/settings`, `/docs`), même logo visible, icônes et route `/favicon.ico` en HTTP 200.
- Aucune image cassée ni erreur JavaScript sur les pages vérifiées. Pages publiques contrôlées à 1440 et 390 pixels de large, sans débordement horizontal sur mobile. Captures inspectées visuellement, ainsi que le favicon 16 × 16.
- Copies du site et de l'application identiques octet par octet ; images ICO 16/32 identiques pixel par pixel aux PNG correspondants ; dimensions et couleur du fond vérifiées.
- Suite existante du moteur : **384 passed, 1 warning in 10.87s** (`uv run pytest -q`). Avertissement de dépréciation Starlette/httpx déjà présent. Le site statique n'avait pas de suite de tests.
- Ruff sur le module Python modifié : vérification et formatage conformes ; `git diff --check` conforme dans les deux dépôts.
- Preuves locales et captures : `../content_factory/.smoke/branding/validation.json`, `root-desktop.png`, `root-mobile.png`, `subpath-desktop.png`, `subpath-mobile.png`, `app-desktop.png`, `app-mobile.png`.

Les contrôles ont porté sur les fichiers et les serveurs locaux. Aucun envoi de vidéo, changement TikTok ou test de review réelle n'a été effectué.
