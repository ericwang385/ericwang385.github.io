# Eric Chengyuan Wang's personal website

Source for <https://psyduck.wang/>. Hugo builds the site. GitHub Pages serves the generated files from the `gh-pages` branch.

## Requirements

- Hugo **0.168.0** or later. Version 0.168.0 is tested and pinned in CI.
- Dart Sass **1.105.2**. The `sass` executable must be on `PATH`.
- Python 3.9 or later for the site checks.

The standard Hugo edition is sufficient. The site uses Dart Sass, not LibSass.

On macOS:

```sh
brew install hugo
brew install sass/sass/sass
```

If Hugo is already installed, use `brew upgrade hugo`. Check both versions:

```sh
hugo version
sass --version
```

## Preview

Run these commands from the repository directory:

```sh
hugo server --buildDrafts
```

Open <http://localhost:1313/> to view the profile. The About menu link returns to `/`. The Blog menu link opens `/posts/`. Both links stay visible on small screens. The old `/about/` URL redirects to the home page.

## Build and check

```sh
hugo --minify --panicOnWarning
python3 scripts/check_site.py public
```

The build stops on Hugo warnings. The check verifies the main routes, local links, assets, and XML feeds. Generated files in `public/` and `resources/` are ignored by Git.

## Edit the site

- `content/_index.md`: home page content. The front matter holds the profile, contact links, and section navigation. The Markdown body holds the biography, publications, research, and education.
- `layouts/home.html`: academic home page layout.
- `assets/scss/_about.scss`: academic home page styles and shared navigation colors.
- `content/posts/_index.md`: blog page title and description.
- `content/posts/`: blog posts.
- `static/cv/Resume.pdf`: CV.
- `static/images/Profile.jpg`: portrait.
- `config.toml`: navigation, social links, and site settings.
- `layouts/`: local templates, based on Hello Friend NG.
- `assets/scss/`: styles. These use Sass modules (`@use`).

Template paths follow the current Hugo layout system. Shared templates use `layouts/_partials/`. Markdown shortcodes use `layouts/_shortcodes/`. Optional custom head markup belongs in `layouts/_partials/extra-head.html`.

## Deployment

Pull requests run the build and site checks. A push to `main`, or a manual workflow run on `main`, also publishes to `gh-pages`.

Keep GitHub Pages configured to deploy from the root of the `gh-pages` branch. The workflow preserves the `psyduck.wang` custom domain. It does not require a change to the Pages source setting.

The workflow pins Hugo and Dart Sass versions. Update these versions after a local build and site check. Keep `DART_SASS_SHA256` in sync with the Linux x64 release archive. Build logs use GitHub's normal retention policy.
