#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import shutil
import urllib.parse
from pathlib import Path
from textwrap import dedent

from content import APPS, EFFECTIVE_DATE, PRIVACY_POLICIES, SUPPORT_EMAIL, TERMS_SECTIONS

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "docs"
STATIC = ROOT / "static"
BASE_PATH = "/asterline-labs"
SITE_URL = "https://brandonewade-debug.github.io/asterline-labs"
SOCIAL_IMAGE = f"{SITE_URL}/assets/og/asterline-social.png"

CONSOLE_BETA_BODY = """Device model and iOS version:
Relevant grandMA3 hardware/software:
How you plan to test:
"""
APP_SUPPORT_BODY = """App version/build:
Device and OS version:
What happened:
Steps to reproduce:
Expected result:

Do not include credentials, tokens, private URLs, or show files.
"""
MAIN_SUPPORT_BODY = """App and build:
Device and OS:
Steps to reproduce:
Expected result:
Actual result:

Do not include credentials, tokens, private URLs, pairing files, or show files.
"""
SECURITY_BODY = """Affected product/version:
Summary and impact:
Safe reproduction steps:
Suggested contact method:

Do not include live credentials or third-party data.
"""


def href(path: str = "") -> str:
    cleaned = path.strip("/")
    return f"{BASE_PATH}/" + (cleaned + "/" if cleaned else "")


def asset(path: str) -> str:
    return f"{BASE_PATH}/assets/{path.lstrip('/')}"


def canonical(path: str = "") -> str:
    cleaned = path.strip("/")
    return f"{SITE_URL}/" + (cleaned + "/" if cleaned else "")


def write(path: str, content: str | bytes) -> None:
    destination = OUT / path
    destination.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, bytes):
        destination.write_bytes(content)
    else:
        destination.write_text(content.rstrip() + "\n", encoding="utf-8")


def mailto(subject: str, body: str = "") -> str:
    query = urllib.parse.urlencode({"subject": subject, "body": body})
    return f"mailto:{SUPPORT_EMAIL}?{query}"


def icon_arrow() -> str:
    return '<svg aria-hidden="true" viewBox="0 0 20 20" fill="none"><path d="M4 10h11m-4-4 4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def icon_external() -> str:
    return '<svg aria-hidden="true" viewBox="0 0 20 20" fill="none"><path d="M8 4H4.8A1.8 1.8 0 0 0 3 5.8v9.4A1.8 1.8 0 0 0 4.8 17h9.4a1.8 1.8 0 0 0 1.8-1.8V12M11 3h6v6m0-6-8 8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def navigation(active: str) -> str:
    items = [
        ("apps", "Apps", href("#apps")),
        ("beta", "Betas", href("beta")),
        ("support", "Support", href("support")),
        ("privacy", "Privacy", href("privacy")),
    ]
    links = []
    for key, label, url in items:
        current = ' aria-current="page"' if active == key else ""
        links.append(f'<a href="{url}"{current}>{label}</a>')
    links.append(f'<a class="nav-cta" href="{href("beta")}">Join a beta</a>')
    return "".join(links)


def footer() -> str:
    product_links = "".join(
        f'<a href="{href("apps/" + app["slug"])}">{html.escape(app["name"])}</a>' for app in APPS
    )
    return f'''
<footer class="site-footer">
  <div class="shell footer-grid">
    <div class="footer-brand">
      <a class="brand-link" href="{href()}">
        <img class="brand-mark" src="{asset("brand/asterline-mark.svg")}" alt="">
        <span class="brand-name">Asterline Labs</span>
      </a>
      <p>Independent software for media, live production, and the systems around them.</p>
    </div>
    <div class="footer-col">
      <h2>Products</h2>
      {product_links}
    </div>
    <div class="footer-col">
      <h2>Resources</h2>
      <a href="{href("beta")}">Public betas</a>
      <a href="{href("support")}">Support</a>
      <a href="{href("privacy")}">Privacy center</a>
      <a href="{href("terms")}">Terms</a>
    </div>
    <div class="footer-col">
      <h2>Elsewhere</h2>
      <a href="https://github.com/brandonewade-debug" target="_blank" rel="noopener noreferrer">GitHub</a>
      <a href="{mailto("Asterline Labs inquiry")}">Email</a>
    </div>
  </div>
  <div class="shell footer-bottom">
    <p>© <span data-year>2026</span> Asterline Labs. Built by Brandon Wade.</p>
    <p>Apple, TestFlight, Plex, Google, YouTube, OpenAI, grandMA3, ONYX, Docker, Debian, and other names are marks of their respective owners. Asterline Labs is independent and is not endorsed by them.</p>
  </div>
</footer>
'''


def page(
    title: str,
    description: str,
    body: str,
    path: str = "",
    active: str = "",
    schema: dict | list | None = None,
    robots: str = "index,follow",
) -> str:
    full_title = "Asterline Labs" if not title else f"{title} — Asterline Labs"
    schema_markup = ""
    if schema is not None:
        schema_markup = '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False, separators=(",", ":")) + "</script>"
    return dedent(f'''\
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
      <meta name="description" content="{html.escape(description, quote=True)}">
      <meta name="robots" content="{robots}">
      <meta name="referrer" content="strict-origin-when-cross-origin">
      <meta name="theme-color" content="#05070d">
      <meta name="apple-mobile-web-app-title" content="Asterline Labs">
      <title>{html.escape(full_title)}</title>
      <link rel="canonical" href="{canonical(path)}">
      <link rel="icon" href="{asset("brand/asterline-mark.svg")}" type="image/svg+xml">
      <link rel="manifest" href="{asset("site.webmanifest")}">
      <link rel="stylesheet" href="{asset("styles.css")}">
      <meta property="og:type" content="website">
      <meta property="og:site_name" content="Asterline Labs">
      <meta property="og:title" content="{html.escape(full_title, quote=True)}">
      <meta property="og:description" content="{html.escape(description, quote=True)}">
      <meta property="og:url" content="{canonical(path)}">
      <meta property="og:image" content="{SOCIAL_IMAGE}">
      <meta property="og:image:width" content="1200">
      <meta property="og:image:height" content="630">
      <meta name="twitter:card" content="summary_large_image">
      {schema_markup}
      <script defer src="{asset("site.js")}"></script>
    </head>
    <body>
      <a class="skip-link" href="#main-content">Skip to content</a>
      <header class="site-header">
        <div class="shell header-inner">
          <a class="brand-link" href="{href()}">
            <img class="brand-mark" src="{asset("brand/asterline-mark.svg")}" alt="">
            <span class="brand-name">Asterline Labs</span>
          </a>
          <button class="nav-toggle" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="Open navigation"><span></span></button>
          <nav class="site-nav" id="site-nav" aria-label="Primary navigation">
            {navigation(active)}
          </nav>
        </div>
      </header>
      <main id="main-content">
        {body}
      </main>
      {footer()}
    </body>
    </html>
    ''')


def app_icon(app: dict) -> str:
    return asset("apps/" + app["icon"])


def status_badge(app: dict) -> str:
    return f'<span class="status {app["status_class"]}">{html.escape(app["status"])}</span>'


def platforms(app: dict) -> str:
    return "".join(f'<span class="platform">{html.escape(item)}</span>' for item in app["platforms"])


def beta_button(app: dict, label: str = "Join the beta") -> str:
    if app["testflight"]:
        return f'<a class="button button-primary" href="{app["testflight"]}" target="_blank" rel="noopener noreferrer">{label}{icon_external()}</a>'
    if app["slug"] == "console-bridge":
        return f'<a class="button button-primary" href="{mailto("Console Bridge beta access", CONSOLE_BETA_BODY)}">Request beta access{icon_arrow()}</a>'
    return f'<a class="button button-secondary" href="{mailto(app["name"] + " project inquiry")}">Ask about the project{icon_arrow()}</a>'


def app_card(app: dict, featured: bool = False) -> str:
    card_classes = f'app-card {app["accent"]}' + (" featured" if featured else "")
    join = ""
    if app["testflight"]:
        join = f'<a class="text-link" href="{app["testflight"]}" target="_blank" rel="noopener noreferrer">Join beta</a>'
    return f'''
<article class="{card_classes}">
  <div class="app-card-head">
    <img class="app-icon" src="{app_icon(app)}" alt="{html.escape(app["name"])} app icon" width="168" height="168">
    {status_badge(app)}
  </div>
  <h3>{html.escape(app["name"])}</h3>
  <p>{html.escape(app["summary"])}</p>
  <div class="platforms">{platforms(app)}</div>
  <div class="app-card-actions">
    <a class="text-link" href="{href("apps/" + app["slug"])}">Explore {html.escape(app["name"])}</a>
    {join}
  </div>
</article>
'''


def home_page() -> str:
    cards = "\n".join(app_card(app, featured=(index == 0)) for index, app in enumerate(APPS))
    schema = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Asterline Labs",
        "url": canonical(),
        "logo": f"{SITE_URL}/assets/brand/asterline-mark.svg",
        "founder": {"@type": "Person", "name": "Brandon Wade"},
        "sameAs": ["https://github.com/brandonewade-debug"],
    }
    body = f'''
<section class="hero">
  <div class="shell hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">Independent software studio</p>
      <h1 class="display"><span class="gradient-text">Useful tools.</span><br>Built with intent.</h1>
      <p class="hero-lede">Asterline Labs creates focused apps for personal media, live production, and the systems that connect them.</p>
      <div class="actions">
        <a class="button button-primary" href="#apps">Explore the apps{icon_arrow()}</a>
        <a class="button button-secondary" href="{href("beta")}">Join a public beta</a>
      </div>
    </div>
    <div class="hero-emblem" aria-hidden="true">
      <img src="{asset("brand/asterline-mark.svg")}" alt="">
    </div>
  </div>
</section>
<div class="trust-strip" aria-label="Asterline Labs principles">
  <div class="trust-item"><strong>User-controlled connections</strong><span>Your services, servers, and hardware</span></div>
  <div class="trust-item"><strong>No Asterline ad tracking</strong><span>No behavioral analytics on this website</span></div>
  <div class="trust-item"><strong>Review before consequence</strong><span>Safety gates for production tools</span></div>
</div>
<section class="section" id="apps">
  <div class="shell">
    <div class="section-head">
      <div class="section-head-copy">
        <p class="eyebrow">The portfolio</p>
        <h2 class="section-title">One studio. Six distinct tools.</h2>
        <p class="section-lede">Each product gets its own purpose, platform, privacy policy, support path, and honest status.</p>
      </div>
    </div>
    <div class="app-grid">{cards}</div>
  </div>
</section>
<section class="section section-tight">
  <div class="shell">
    <div class="section-head">
      <div class="section-head-copy">
        <p class="eyebrow">How we build</p>
        <h2 class="section-title">Clear boundaries matter.</h2>
      </div>
    </div>
    <div class="values-grid">
      <article class="value-card"><div class="mini-icon">01</div><h3>Local where practical</h3><p>Connections and project data stay between the device and the services or hardware the user deliberately selects.</p></article>
      <article class="value-card"><div class="mini-icon">02</div><h3>Honest beta labels</h3><p>Public betas, private tests, and prototypes are described differently so a concept is never presented as production-ready.</p></article>
      <article class="value-card"><div class="mini-icon">03</div><h3>Privacy by explanation</h3><p>Every product policy describes what is stored, where requests go, how to delete data, and which providers apply their own terms.</p></article>
    </div>
  </div>
</section>
<section class="section">
  <div class="shell cta-panel">
    <p class="eyebrow">Help shape the next build</p>
    <h2>Orbit and Nova Stream are open to external testers.</h2>
    <p>Install through Apple’s TestFlight service, use your own authorized sources, and report issues without sharing credentials or private URLs.</p>
    <div class="actions"><a class="button button-primary" href="{href("beta")}">View beta access{icon_arrow()}</a><a class="button button-secondary" href="{href("support")}">Read support guidance</a></div>
  </div>
</section>
'''
    write("index.html", page("", "Independent apps for personal media, live production, and connected systems.", body, schema=schema))


def app_page(app: dict) -> None:
    feature_markup = "".join(
        f'<article class="feature-card"><div class="mini-icon">{index:02d}</div><h3>{html.escape(title)}</h3><p>{html.escape(text)}</p></article>'
        for index, (title, text) in enumerate(app["features"], start=1)
    )
    privacy_url = href(app["privacy"])
    beta_heading = "Join the external beta" if app["testflight"] else ("Private testing" if app["slug"] == "console-bridge" else "Development status")
    if app["testflight"]:
        beta_copy = "The public invitation opens in Apple’s TestFlight service. Availability depends on Apple processing, the active build, compatible devices, and remaining tester capacity."
    elif app["slug"] == "asteros":
        beta_copy = "AsterOS is installed through private TestFlight testing. External review is being prepared. Contact us about future access; there is no public invitation link yet."
    elif app["slug"] == "console-bridge":
        beta_copy = "Console Bridge is not using a public invitation link. Access is granted deliberately so hardware, software version, network setup, and safety expectations can be reviewed first."
    else:
        beta_copy = "This project does not have an iPhone or Apple TV TestFlight build. Its current status is shown here so development work is not confused with a public release."

    schema = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": app["name"],
        "applicationCategory": "MultimediaApplication" if app["slug"] in ("orbit", "nova-stream") else "DeveloperApplication",
        "operatingSystem": ", ".join(app["platforms"]),
        "description": app["summary"],
        "url": canonical("apps/" + app["slug"]),
        "author": {"@type": "Organization", "name": "Asterline Labs"},
    }
    body = f'''
<section class="page-hero">
  <div class="shell page-hero-grid">
    <div>
      <p class="eyebrow">Asterline Labs product</p>
      <h1 class="page-title">{html.escape(app["name"])}</h1>
      <p class="page-lede">{html.escape(app["tagline"])} {html.escape(app["description"])}</p>
      <div class="app-facts">{status_badge(app)}{platforms(app)}</div>
      <div class="actions">{beta_button(app)}<a class="button button-secondary" href="{privacy_url}">Read privacy details</a></div>
    </div>
    <div class="page-icon-wrap"><img class="page-icon" src="{app_icon(app)}" alt="{html.escape(app["name"])} icon" width="512" height="512"></div>
  </div>
</section>
<section class="section section-tight">
  <div class="shell">
    <div class="section-head"><div class="section-head-copy"><p class="eyebrow">Designed around the job</p><h2 class="section-title">What {html.escape(app["name"])} does</h2></div></div>
    <div class="feature-grid">{feature_markup}</div>
  </div>
</section>
<section class="section">
  <div class="shell split">
    <div class="sticky-copy"><p class="eyebrow">Connections and boundaries</p><h2>It works with what you choose.</h2><p>{html.escape(app["connections"])}</p></div>
    <div class="detail-list">
      <article class="detail-item"><h3>Nothing essential is bundled</h3><p>{html.escape(app["beta_note"])}</p></article>
      <article class="detail-item"><h3>Your data path is documented</h3><p>The product-specific privacy policy explains local storage, external services, retention, deletion, and the developer’s role.</p><p><a class="text-link" href="{privacy_url}">Open the {html.escape(app["name"])} privacy policy</a></p></article>
      <article class="detail-item"><h3>Independent interoperability</h3><p>{html.escape(app["disclaimer"])}</p></article>
    </div>
  </div>
</section>
<section class="section section-tight">
  <div class="shell cta-panel">
    <p class="eyebrow">{html.escape(app["status"])}</p>
    <h2>{beta_heading}</h2>
    <p>{html.escape(beta_copy)}</p>
    <div class="actions">{beta_button(app, "Open in TestFlight" if app["testflight"] else "Request beta access" if app["slug"] == "console-bridge" else "Contact Asterline Labs")}<a class="button button-secondary" href="{href("support")}">Support and testing notes</a></div>
  </div>
</section>
'''
    write(f'apps/{app["slug"]}/index.html', page(app["name"], app["summary"], body, f'apps/{app["slug"]}', active="apps", schema=schema))


def beta_page() -> None:
    public_apps = [app for app in APPS if app["testflight"]]
    rows = "".join(f'''
<article class="beta-row">
  <img src="{app_icon(app)}" alt="{html.escape(app["name"])} icon" width="136" height="136">
  <div><h3>{html.escape(app["name"])}</h3><p>{html.escape(app["summary"])}</p></div>
  <a class="button button-primary" href="{app["testflight"]}" target="_blank" rel="noopener noreferrer">Open in TestFlight{icon_external()}</a>
</article>
''' for app in public_apps)
    console = next(app for app in APPS if app["slug"] == "console-bridge")
    body = f'''
<section class="page-hero">
  <div class="shell">
    <p class="eyebrow">External testing</p>
    <h1 class="page-title">Join an Asterline beta.</h1>
    <p class="page-lede">Public links go directly to Apple’s TestFlight service. Beta software is unfinished, can change quickly, and should not be trusted as the only copy of important data.</p>
  </div>
</section>
<section class="section section-tight">
  <div class="shell">
    <div class="beta-list">{rows}
      <article class="beta-row">
        <img src="{app_icon(console)}" alt="Console Bridge icon" width="136" height="136">
        <div><h3>Console Bridge</h3><p>Private testing only. Hardware, software version, and safety expectations are reviewed before access.</p></div>
        <a class="button button-secondary" href="{mailto("Console Bridge beta access", CONSOLE_BETA_BODY)}">Request access</a>
      </article>
    </div>
  </div>
</section>
<section class="section">
  <div class="shell split">
    <div class="sticky-copy"><p class="eyebrow">Before installing</p><h2>Test deliberately.</h2><p>Use services, media, accounts, networks, and hardware you are authorized to access. Keep backups and avoid production-only environments.</p></div>
    <div class="detail-list">
      <article class="detail-item"><h3>1. Open the invitation</h3><p>Use the public link on a compatible Apple device. Apple may prompt you to install or open TestFlight.</p></article>
      <article class="detail-item"><h3>2. Read the testing notes</h3><p>Review the build description, supported platform, known limits, privacy policy, and any service or hardware requirements before installing.</p></article>
      <article class="detail-item"><h3>3. Report useful detail</h3><p>Include the app, build, device, operating-system version, steps, expected result, and actual result. Redact tokens, account details, playlist URLs, private server addresses, and show data.</p></article>
      <article class="detail-item"><h3>4. Expect change</h3><p>Builds can expire, be replaced, lose compatibility, or be removed from testing. A beta invitation does not promise a release date or continuing access.</p></article>
    </div>
  </div>
</section>
<section class="section section-tight">
  <div class="shell"><div class="notice info"><strong>Apple service:</strong> TestFlight distribution, invitations, diagnostics shared through TestFlight, and Apple account handling are governed by Apple’s terms and privacy practices. Asterline Labs does not control TestFlight availability.</div></div>
</section>
'''
    write("beta/index.html", page("Public Betas", "Join the Orbit or Nova Stream external beta through Apple TestFlight.", body, "beta", active="beta"))


def support_page() -> None:
    cards = "".join(f'''
<article class="support-card"><h3>{html.escape(app["name"])}</h3><p>{html.escape(app["summary"])}</p><a class="text-link" href="{mailto(app["name"] + " support", APP_SUPPORT_BODY)}">Email {html.escape(app["name"])} support</a></article>
''' for app in APPS)
    body = f'''
<section class="page-hero">
  <div class="shell">
    <p class="eyebrow">Support</p>
    <h1 class="page-title">Tell us what happened.</h1>
    <p class="page-lede">A useful report includes enough context to reproduce the problem and no credentials that create a new one.</p>
    <div class="actions"><a class="button button-primary" href="{mailto("Asterline Labs support", MAIN_SUPPORT_BODY)}">Email support{icon_arrow()}</a><a class="button button-secondary" href="{href("privacy")}">Privacy center</a></div>
  </div>
</section>
<section class="section section-tight">
  <div class="shell">
    <div class="section-head"><div class="section-head-copy"><p class="eyebrow">Product support</p><h2 class="section-title">Choose the app.</h2></div></div>
    <div class="support-grid">{cards}</div>
  </div>
</section>
<section class="section">
  <div class="shell split">
    <div class="sticky-copy"><p class="eyebrow">A strong bug report</p><h2>Include facts, not secrets.</h2><p>Screenshots are helpful after private information has been removed.</p></div>
    <div class="detail-list">
      <article class="detail-item"><h3>Build and environment</h3><p>App name, version and build; iPhone, iPad, Apple TV, Pi, console, or computer model; operating-system and relevant console/server version.</p></article>
      <article class="detail-item"><h3>Reproduction</h3><p>The smallest repeatable sequence, what you expected, what occurred, and whether it happens every time.</p></article>
      <article class="detail-item"><h3>Sanitized evidence</h3><p>Error wording, timestamp, and a redacted screenshot or log excerpt. Remove passwords, API keys, session cookies, account tokens, playlist links, signed media URLs, pairing files, public IP addresses, and customer show data.</p></article>
    </div>
  </div>
</section>
<section class="section section-tight">
  <div class="shell">
    <div class="section-head"><div class="section-head-copy"><p class="eyebrow">Privacy and deletion</p><h2 class="section-title">You control local data.</h2></div></div>
    <div class="legal-card-grid">
      <article class="legal-card"><h3>No Asterline account</h3><p>The current products do not create a hosted Asterline user account. External Plex, Google, Invidious, OpenAI, media-provider, or other accounts remain with those providers.</p></article>
      <article class="legal-card"><h3>Delete app data</h3><p>Use in-app disconnect, history, import, profile, saved-item, download, or chat controls where available. Deleting the app removes its local container; device backups and synchronized Keychain data follow Apple settings.</p></article>
      <article class="legal-card"><h3>Device projects</h3><p>Console Bridge, CueForge, and DockerOS also store data on the Pi, workstation, or host. Delete those local files, logs, credentials, volumes, and backups separately.</p></article>
    </div>
  </div>
</section>
<section class="section section-tight">
  <div class="shell cta-panel">
    <p class="eyebrow">Security reporting</p>
    <h2>Found a security issue?</h2>
    <p>Email a concise description, affected product and version, impact, and safe reproduction steps. Do not access data that is not yours, disrupt a production system, or send active credentials in ordinary email.</p>
    <div class="actions"><a class="button button-primary" href="{mailto("[Security] Asterline Labs report", SECURITY_BODY)}">Report securely{icon_arrow()}</a></div>
  </div>
</section>
'''
    write("support/index.html", page("Support", "Support, testing guidance, privacy requests, and security reporting for Asterline Labs products.", body, "support", active="support"))


def privacy_index() -> None:
    cards = [
        '<article class="legal-card"><h3>Website</h3><p>No first-party tracking cookies, advertising, or behavioral analytics. Hosting and email are described separately.</p><p><a class="text-link" href="' + href("privacy/website") + '">Website policy</a></p></article>'
    ]
    for app in APPS:
        cards.append(f'<article class="legal-card"><h3>{html.escape(app["name"])}</h3><p>{html.escape(PRIVACY_POLICIES[app["slug"]]["summary"])}</p><p><a class="text-link" href="{href("privacy/" + app["slug"])}">{html.escape(app["name"])} policy</a></p></article>')
    body = f'''
<section class="page-hero">
  <div class="shell">
    <p class="eyebrow">Privacy center</p>
    <h1 class="page-title">Specific policies, not vague promises.</h1>
    <p class="page-lede">Each product has a separate data path. These pages explain what the app handles, where requests go, who operates each service, how data is retained, and how to delete it.</p>
  </div>
</section>
<section class="section section-tight">
  <div class="shell">
    <div class="legal-card-grid">{"".join(cards)}</div>
  </div>
</section>
<section class="section section-tight">
  <div class="shell"><div class="notice good"><strong>Website design:</strong> this site does not run Asterline advertising, behavioral analytics, or first-party tracking cookies. GitHub Pages and external links apply their own privacy practices.</div></div>
</section>
'''
    write("privacy/index.html", page("Privacy Center", "Privacy policies for the Asterline Labs website and each product.", body, "privacy", active="privacy"))


def legal_page(title: str, summary: str, sections: list, path: str, active: str = "privacy", effective_date: str = EFFECTIVE_DATE) -> None:
    nav = "".join(f'<a href="#{section_id}">{html.escape(heading)}</a>' for section_id, heading, _ in sections)
    article = "".join(f'<section id="{section_id}"><h2>{html.escape(heading)}</h2>{content}</section>' for section_id, heading, content in sections)
    body = f'''
<section class="legal-hero">
  <div class="shell">
    <p class="eyebrow">Legal and privacy</p>
    <h1 class="page-title">{html.escape(title)}</h1>
    <p class="page-lede">{html.escape(summary)}</p>
    <p class="effective">Effective {effective_date}</p>
  </div>
</section>
<div class="shell legal-wrap">
  <nav class="legal-nav" aria-label="On this page"><strong>On this page</strong>{nav}</nav>
  <article class="legal">{article}</article>
</div>
'''
    write(path.strip("/") + "/index.html", page(title, summary, body, path, active=active))


def generate_legal_pages() -> None:
    for slug, policy in PRIVACY_POLICIES.items():
        legal_page(policy["title"], policy["summary"], policy["sections"], f"privacy/{slug}", effective_date=policy.get("effective_date", EFFECTIVE_DATE))
    legal_page("Terms of Use", "Terms for the Asterline Labs website, TestFlight builds, private betas, and development prototypes.", TERMS_SECTIONS, "terms")


def custom_icons() -> None:
    cueforge = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><defs><linearGradient id="b" x1="80" y1="440" x2="422" y2="80" gradientUnits="userSpaceOnUse"><stop stop-color="#ff8a3d"/><stop offset="1" stop-color="#ffd36a"/></linearGradient><radialGradient id="g" cx="0" cy="0" r="1" gradientTransform="translate(256 164) rotate(90) scale(250)"><stop stop-color="#47301b"/><stop offset="1" stop-color="#0b0d13"/></radialGradient></defs><rect width="512" height="512" rx="112" fill="url(#g)"/><path d="M256 83 369 332H143L256 83Z" fill="url(#b)" opacity=".28"/><path d="m164 299 92 80 92-80" fill="none" stroke="url(#b)" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/><path d="M125 392h262" stroke="#ffe3a6" stroke-width="18" stroke-linecap="round"/><circle cx="256" cy="125" r="22" fill="#fff3ce"/></svg>'''
    dockeros = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><defs><linearGradient id="b" x1="85" y1="420" x2="430" y2="88" gradientUnits="userSpaceOnUse"><stop stop-color="#2bcbff"/><stop offset="1" stop-color="#69f0ff"/></linearGradient><radialGradient id="g" cx="0" cy="0" r="1" gradientTransform="translate(340 120) rotate(135) scale(390)"><stop stop-color="#123b61"/><stop offset="1" stop-color="#07101d"/></radialGradient></defs><rect width="512" height="512" rx="112" fill="url(#g)"/><g fill="none" stroke="url(#b)" stroke-width="18"><rect x="106" y="128" width="300" height="72" rx="18"/><rect x="106" y="220" width="300" height="72" rx="18"/><rect x="106" y="312" width="300" height="72" rx="18"/></g><g fill="#8bf3ff"><circle cx="147" cy="164" r="10"/><circle cx="147" cy="256" r="10"/><circle cx="147" cy="348" r="10"/></g><path d="M205 155h151M205 247h151M205 339h151" stroke="#d8fbff" stroke-width="14" stroke-linecap="round" opacity=".85"/></svg>'''
    write("assets/apps/cueforge.svg", cueforge)
    write("assets/apps/dockeros.svg", dockeros)


def social_svg() -> str:
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"><defs><radialGradient id="bg" cx="0" cy="0" r="1" gradientTransform="translate(880 100) rotate(140) scale(900 650)"><stop stop-color="#211553"/><stop offset=".45" stop-color="#0c1830"/><stop offset="1" stop-color="#05070d"/></radialGradient><linearGradient id="t" x1="110" y1="430" x2="830" y2="160" gradientUnits="userSpaceOnUse"><stop stop-color="#fff"/><stop offset=".55" stop-color="#a8f1ff"/><stop offset="1" stop-color="#a784ff"/></linearGradient><filter id="glow"><feGaussianBlur stdDeviation="10" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="1200" height="630" fill="url(#bg)"/><ellipse cx="885" cy="320" rx="255" ry="87" transform="rotate(-13 885 320)" fill="none" stroke="#89eaff" stroke-opacity=".26" stroke-width="9"/><g transform="translate(700 84) scale(.74)"><path fill="#8ccfff" fill-rule="evenodd" d="M256 55 442 448h-82l-40-89H192l-40 89H70L256 55Zm0 125-68 151h136L256 180Z"/><path d="M169 311h174l24 52H145l24-52Z" fill="#987dff"/><path d="M410 78c4 28 9 34 35 43-26 8-31 15-35 43-4-28-9-35-35-43 26-9 31-15 35-43Z" fill="#fff" filter="url(#glow)"/></g><text x="92" y="225" fill="#76eaff" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="27" font-weight="700" letter-spacing="5">INDEPENDENT SOFTWARE STUDIO</text><text x="86" y="335" fill="url(#t)" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="88" font-weight="800" letter-spacing="-5">Asterline Labs</text><text x="92" y="405" fill="#b7c1d8" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="31">Media. Live production. Connected systems.</text><text x="92" y="526" fill="#7f8ba4" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="22">Orbit · Nova Stream · Console Bridge · CueForge · DockerOS</text></svg>'''


def copy_assets() -> None:
    target = OUT / "assets"
    target.mkdir(parents=True, exist_ok=True)
    shutil.copy2(STATIC / "styles.css", target / "styles.css")
    shutil.copy2(STATIC / "site.js", target / "site.js")
    shutil.copytree(STATIC / "brand", target / "brand", dirs_exist_ok=True)
    if (STATIC / "og").exists():
        shutil.copytree(STATIC / "og", target / "og", dirs_exist_ok=True)
    icon_sources = {
        "asteros.png": STATIC / "apps/asteros.png",
        "orbit.png": STATIC / "apps/orbit.png",
        "nova-stream.png": STATIC / "apps/nova-stream.png",
        "console-bridge.png": STATIC / "apps/console-bridge.png",
    }
    (target / "apps").mkdir(parents=True, exist_ok=True)
    for name, source in icon_sources.items():
        if not source.exists():
            raise FileNotFoundError(source)
        shutil.copy2(source, target / "apps" / name)
    custom_icons()
    write("assets/og/asterline-social.svg", social_svg())
    manifest = {
        "name": "Asterline Labs",
        "short_name": "Asterline",
        "start_url": href(),
        "display": "standalone",
        "background_color": "#05070d",
        "theme_color": "#05070d",
        "icons": [{"src": asset("brand/asterline-mark.svg"), "sizes": "any", "type": "image/svg+xml", "purpose": "any"}],
    }
    write("assets/site.webmanifest", json.dumps(manifest, indent=2))


def misc_pages() -> None:
    not_found_body = f'''
<section class="page-hero"><div class="shell"><p class="eyebrow">404</p><h1 class="page-title">That page drifted out of orbit.</h1><p class="page-lede">The address may have changed, or the page may not exist.</p><div class="actions"><a class="button button-primary" href="{href()}">Return home{icon_arrow()}</a><a class="button button-secondary" href="{href("support")}">Support</a></div></div></section>
'''
    write("404.html", page("Page Not Found", "The requested Asterline Labs page was not found.", not_found_body, "404", robots="noindex,follow"))
    paths = ["", "beta", "support", "privacy", "terms"]
    paths += [f'apps/{app["slug"]}' for app in APPS]
    paths += [f"privacy/{slug}" for slug in PRIVACY_POLICIES]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path in paths:
        sitemap.append(f"  <url><loc>{canonical(path)}</loc><lastmod>2026-09-21</lastmod></url>")
    sitemap.append("</urlset>")
    write("sitemap.xml", "\n".join(sitemap))
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml")
    write(".nojekyll", "")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    copy_assets()
    home_page()
    for app in APPS:
        app_page(app)
    beta_page()
    support_page()
    privacy_index()
    generate_legal_pages()
    misc_pages()
    print(f"Built {sum(1 for _ in OUT.rglob('*') if _.is_file())} files in {OUT}")


if __name__ == "__main__":
    main()
