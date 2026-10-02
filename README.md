# Content Factory website

Static website ready for GitHub Pages.

## Official icon

The single master is `assets/branding/content-factory-icon.svg`. Website logos,
favicons and the TikTok app icon all use this design. See [BRANDING.md](BRANDING.md)
for the asset inventory, regeneration command, validation and TikTok upload steps.

Upload `assets/branding/content-factory-tiktok-app-icon.png` (1024 × 1024) in
**TikTok Developer → Content Factory Bot → Production → Basic Information → App icon**.
Deploy this website update before resubmitting the review so the public site and
browser favicon match the uploaded image.

## Deploy with GitHub Pages

1. Create a public GitHub repository, e.g. `content-factory-site`.
2. Upload the **contents** of this folder to the repository root.
3. In GitHub, open **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select `main` and `/ (root)`, then save.
6. GitHub will provide the public URL after deployment.

Useful TikTok URLs will then be:

- Home: `https://USERNAME.github.io/content-factory-site/`
- Privacy: `https://USERNAME.github.io/content-factory-site/privacy/`
- Terms: `https://USERNAME.github.io/content-factory-site/terms/`

## Before a real public launch

The included legal pages are a practical starter for the current product description, not individualized legal advice. Replace the placeholder contact wording with your actual support/privacy contact and, if the service becomes available to other users, review the policies for your actual data flows and business details.
