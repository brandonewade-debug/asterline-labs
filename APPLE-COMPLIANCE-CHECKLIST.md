# Apple distribution preflight

Reviewed against the current repositories and App Store Connect state on **September 21, 2026**. This is an engineering and publishing checklist, not legal advice or a guarantee of App Review approval. Apple’s current online guidelines were not live-verified while this site was built, so compare every item with the current App Review Guidelines, TestFlight requirements, and App Store Connect prompts before submission.

## Stable public URLs

Base: `https://brandonewade-debug.github.io/asterline-labs/`

| App | Marketing URL | Support URL | Privacy policy URL |
|---|---|---|---|
| Orbit | `/apps/orbit/` | `/support/` | `/privacy/orbit/` |
| Nova Stream | `/apps/nova-stream/` | `/support/` | `/privacy/nova-stream/` |
| Console Bridge | `/apps/console-bridge/` | `/support/` | `/privacy/console-bridge/` |

Use the complete absolute URL in App Store Connect. Keep these routes stable after they are entered in metadata.

## TestFlight state confirmed through App Store Connect API

| App Store Connect app | Bundle ID | Public group | Public link | Current public limit |
|---|---|---|---|---:|
| Orbit Media | `com.deathstar.orbit` | External Testers | `https://testflight.apple.com/join/48K5A1fD` | 75 |
| Nova Streams | `com.deathstar.video` | External TestFlight users | `https://testflight.apple.com/join/5mVgdSed` | 75 |
| Console Bridge | `com.brandonewade.consolebridge` | No public-link group found | None | — |

Do not invent or publish a Console Bridge public link until an external group, approved build, tester limit, and invitation policy have been deliberately configured.

## Website preflight completed

- Static HTML, CSS, JavaScript, SVG, and PNG only.
- No Asterline advertising, behavioral analytics, session replay, or first-party tracking cookies.
- Separate product pages, support page, privacy center, terms, beta instructions, and product-specific privacy policies.
- Visible support email route and security-report route.
- Semantic headings, skip navigation, keyboard focus treatment, alt text, reduced-motion support, and responsive layouts.
- No credentials, private URLs, App Store Connect keys, provisioning data, or private repository source included.
- Public TestFlight links return HTTP 200.
- Internal routes and local assets validated with no broken references or placeholder text.

## Required App Store Connect checks for every Apple app

1. **Metadata consistency** — app name, subtitle, screenshots, description, support URL, marketing URL, privacy URL, category, age rating, and platform availability must match the shipped binary and website.
2. **App Privacy answers** — answer from the final binary and actual production services, not from this website alone. Data processed by a user-selected provider can still require analysis under Apple’s definitions even when Asterline does not receive it.
3. **Privacy manifest** — include and validate `PrivacyInfo.xcprivacy`; declare required-reason APIs accurately; verify every embedded SDK and binary dependency.
4. **Account deletion** — these builds do not create an Asterline-hosted account. Make that clear in review notes. Provide in-app disconnect or revocation for external accounts and point users to the provider for deletion of the external account itself.
5. **Export compliance** — review the final binary’s TLS, cryptography, VPN, and secure-storage behavior. Do not rely only on an old `ITSAppUsesNonExemptEncryption` value.
6. **Review access** — provide a legal demo path, test server, sample data, hardware/video explanation, or reviewer instructions whenever the main experience otherwise appears empty or requires private infrastructure.
7. **Intellectual property** — provide only content, streams, downloads, logos, metadata, and integrations that are authorized. Never imply third-party endorsement.
8. **Support readiness** — monitor the published support address, retain a working build/version path, and never ask a reviewer or tester to email credentials.
9. **Beta notes** — explain setup requirements, known limits, data deletion, and how to report a problem without exposing private data.
10. **Final-device testing** — test signed builds on every declared platform and form factor, including launch, setup, playback or connection failure, sign-out/disconnect, deletion, network permission prompts, and VoiceOver/keyboard/focus behavior.

## Orbit-specific review

### Repository findings

- Connects to Plex, user-provided IPTV/live-TV sources, XMLTV, Invidious, request services, and optional Google/YouTube read-only subscription access.
- Uses Keychain and local app storage; selected Keychain items can synchronize through iCloud when enabled.
- Current privacy manifest declares no tracking or collected-data categories and declares the UserDefaults required-reason category `CA92.1`.

### Before submission

- Confirm the final build’s App Privacy answers against every enabled integration and any crash/diagnostic tooling added later.
- Keep the Google API Limited Use disclosure in the published privacy policy and verify OAuth scopes, consent screen, redirect URIs, verification status, and token-revocation flow.
- Review whether iCloud/Keychain synchronization changes disclosure or entitlement requirements.
- Include review notes explaining that no media or television service is bundled and provide legal sample content or reviewer-accessible setup.
- Verify all playlist/provider credentials are stored securely and that logs and screenshots redact them.
- Verify Plex, IPTV, and guide failure states do not trap the reviewer on a blank setup page.
- Confirm the iOS and tvOS targets each include the correct privacy manifest and usage descriptions.

## Nova Stream-specific review

### Repository findings

- Connects to a user-selected Invidious server and media hosts returned by that server; live playback can contact YouTube/Google delivery hosts directly without a Google login.
- Stores optional Invidious tokens in Keychain and local profiles, subscriptions, history, saved items, and related state on device.
- Current privacy manifest declares no tracking or collected-data categories and declares the UserDefaults required-reason category `CA92.1`.
- Repository documentation still references iPhone download/offline paths.

### Critical media-download issue

A previous App Review response cited **Guideline 5.2.3** for unauthorized audio/video downloading. A privacy policy does not cure that issue. Before App Store submission, do one of the following:

- remove or disable third-party media downloading from the App Store build; or
- establish and document the authorization or licensing that permits each downloadable source and make the reviewer path unambiguous.

Do not hide an active download feature from metadata or review notes. TestFlight availability does not establish App Store compliance.

### Additional checks

- Explain that users supply the Invidious server and that servers differ in account endpoints, formats, regions, and availability.
- Confirm the final build does not use private APIs, spoof account identity, or imply official YouTube affiliation.
- Provide a stable reviewer-accessible HTTPS server and known legal test videos/live sources.
- Verify local and remote history behavior, token scopes, disconnect, token invalidation, local data deletion, and offline-file deletion.
- Ensure all direct-media host behavior is accurately reflected in privacy disclosures and review notes.

## Console Bridge-specific review

### Repository findings

- Uses local-network discovery and access, HTTPS with device identity/pinning, Raspberry Pi pairing, console networking, and optional OpenAI/ChatGPT drafting.
- `Info.plist` includes a local-network usage description and Bonjour service entries.
- No public TestFlight invitation link currently exists.
- A project-level `PrivacyInfo.xcprivacy` was not found during this review.

### Before submission

- Add and validate a privacy manifest for the iOS target, including any required-reason APIs used by the final binary.
- Make local-network and Bonjour purpose strings specific, readable, and consistent with the feature shown at first prompt.
- Document exactly what prompt/context is sent to OpenAI, where credentials live, provider retention limitations, and how to sign out/delete local chats.
- Confirm whether any login experience triggers Sign in with Apple requirements; a device-local bridge login or service-specific external account can be materially different from an Asterline consumer account, but the final implementation and current rule must be reviewed.
- Keep consequential console actions behind explicit review, target confirmation, short-lived approval, and qualified operator control.
- Include review notes and a video showing the Pi, pairing, safe test console or simulator, network permission, drafting, review, approval boundary, and deletion/sign-out paths.
- Do not open a public tester link until the build is externally approved and the hardware/support burden is intentional.

## Website/privacy-policy change triggers

Update the site and effective date before shipping any of the following:

- Asterline-hosted account creation, cloud sync, command relay, media proxy, analytics, advertising, or crash reporting.
- A new SDK, third-party API, OAuth scope, payment system, subscription, or data broker.
- Collection of contact, diagnostics, precise location, contacts, photos, audio, identifiers, purchases, or health/financial data.
- Remote storage of chats, show data, media history, console diagnostics, or credentials.
- Materially different data retention, deletion, export, or user-consent behavior.
- A public Console Bridge beta or a change in public TestFlight capacity/link.

## Final sign-off

Before pressing Submit for Review, record:

- final commit and build number;
- privacy-manifest validation result;
- App Privacy answers reviewed against final traffic and storage;
- reviewer test path and credentials handled through App Store Connect review notes, never this repository;
- current Apple guideline/version checked online;
- support and privacy URLs opened from a logged-out browser;
- TestFlight/App Store screenshots and descriptions matched to the same build;
- legal/IP authorization confirmed for media and third-party marks.
