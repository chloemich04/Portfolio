# Chloe Robinson's Portfolio

A personal portfolio built with Django, with an introduction, project collection, skills, and direct email / LinkedIn / GitHub contact links.

## Run locally (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/. Projects are at `/projects/` and contact information at `/contact/`.

## Make it yours

- `templates/main/index.html`: introduction, background, and skills. Confirm your current education and service details before publishing.
- `main/projects.py`: project descriptions, technology tags, repository links, and homepage selection. `templates/main/project_cards.html` renders the shared card layout.
- `templates/main/contact.html`: email and professional profiles. Email opens the visitor's mail application; this site does not collect or send form submissions.
- `templates/main/base.html`: shared navigation, metadata, and footer.
- `static/css/main.css`: colors, typography, and responsive layouts.
- `static/images/profile-placeholder.JPG`: existing profile photo used by the home page.

The Anime Tracker's original technology list was ambiguous, so its card describes features instead. Confirm the stack and your individual contributions before adding technical claims or performance results. Add a live demo only when a working URL is available.

## Check

```powershell
python manage.py check
python manage.py test
```

## Before publishing

Set a private `DJANGO_SECRET_KEY` and `DJANGO_DEBUG=0` in your hosting environment. Configure `ALLOWED_HOSTS` for your domain and static file serving for your host. The default settings are for local development. Confirm dependency versions in your deployment environment and review your bio, skills, project descriptions, and public contact details.

## Project collection

Edit `main/projects.py` to add or update projects. Each entry includes its title,
category, description, technology tags, repository URL, and artwork text/theme.
Set `featured` to `True` to include a project on the homepage. The Projects page
shows every entry using `templates/main/project_cards.html`.

The collection includes Atlas, the Cyber Threat Intelligence & Anomaly Platform,
SkillForge, Mini Shop, DeepCore, Scamming Codebook data analysis, Calculator,
Anime Tracker, and this portfolio. Descriptions are curated from the public
repositories; the website does not need a GitHub API connection to load.
