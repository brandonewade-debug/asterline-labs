EFFECTIVE_DATE = "September 21, 2026"
SUPPORT_EMAIL = "brandonewade+asterline@gmail.com"

APPS = [
    {
        "slug": "orbit",
        "name": "Orbit",
        "store_name": "Orbit Media",
        "tagline": "Your media universe, in one place.",
        "summary": "A cinematic home for personal media, authorized live TV, music, guide data, and connected discovery.",
        "description": "Orbit brings the services and sources you already control into one focused experience for iPhone, iPad, and Apple TV.",
        "platforms": ["iPhone", "iPad", "Apple TV"],
        "status": "External beta",
        "status_class": "beta",
        "accent": "violet",
        "icon": "orbit.png",
        "testflight": "https://testflight.apple.com/join/48K5A1fD",
        "privacy": "privacy/orbit/",
        "features": [
            ("Personal media first", "Browse and play Plex movies, television, music, profiles, artwork, and watch progress through your own server."),
            ("Live TV and guide", "Connect authorized M3U or Xtream-compatible sources and XMLTV guide data, with source-aware browsing and playback."),
            ("Connected discovery", "Use OrbiTube, a selected Invidious server, read-only YouTube subscriptions, and compatible request services from one app."),
        ],
        "connections": "Plex; user-authorized M3U, Xtream-compatible, and XMLTV sources; Invidious; optional read-only Google/YouTube access; and compatible request services such as Overseerr or Cantinarr.",
        "beta_note": "Orbit does not include media, television channels, provider credentials, or access to paid services. Test only with sources and accounts you are authorized to use.",
        "disclaimer": "Orbit is an independent client. It is not affiliated with or endorsed by Plex, Google, YouTube, Apple, or any television provider.",
    },
    {
        "slug": "nova-stream",
        "name": "Nova Stream",
        "store_name": "Nova Streams",
        "tagline": "Video, on your server and your terms.",
        "summary": "A native Invidious-powered experience for discovery, subscriptions, live streams, watch later, and local profiles.",
        "description": "Nova Stream pairs a clean native interface with the Invidious server you choose, while keeping library state and account tokens under your control.",
        "platforms": ["iPhone", "Apple TV"],
        "status": "External beta",
        "status_class": "beta",
        "accent": "red",
        "icon": "nova-stream.png",
        "testflight": "https://testflight.apple.com/join/5mVgdSed",
        "privacy": "privacy/nova-stream/",
        "features": [
            ("Bring your own server", "Connect a compatible HTTPS Invidious instance and, when supported, sign in with a scoped account token."),
            ("Native playback", "Use platform playback controls for regular videos and live sources supplied by the configured server or media host."),
            ("A personal library", "Keep subscriptions, local profiles, favorites, watch later, history, and saved items organized on your device."),
        ],
        "connections": "A user-selected Invidious instance and the media-delivery hosts returned by that server. Live playback may contact YouTube or Google video hosts directly without a Google account.",
        "beta_note": "Invidious deployments differ. Account endpoints, playback formats, region availability, and live streams can vary by server and can change independently of Nova Stream.",
        "disclaimer": "Nova Stream is an independent client. It is not affiliated with or endorsed by Invidious, Google, YouTube, or Apple, and it does not include any video catalog or media rights.",
    },
    {
        "slug": "console-bridge",
        "name": "Console Bridge",
        "store_name": "Console Bridge",
        "tagline": "A safer bridge from idea to console.",
        "summary": "A review-first bridge between iPhone, Raspberry Pi, and grandMA3 for diagnostics, drafting, and deliberately approved actions.",
        "description": "Console Bridge keeps the connection local, separates AI drafting from console control, and puts explicit review and approval in front of consequential actions.",
        "platforms": ["iPhone", "Raspberry Pi", "grandMA3"],
        "status": "Private beta",
        "status_class": "private",
        "accent": "mint",
        "icon": "console-bridge.png",
        "testflight": None,
        "privacy": "privacy/console-bridge/",
        "features": [
            ("Find and pair locally", "Discover a bridge on the same network, verify its identity, and connect over device-pinned HTTPS."),
            ("Draft, review, approve", "Create commands, macros, or Lua drafts, inspect the exact output, and decide what is allowed to proceed."),
            ("Console-aware workflow", "Manage network targets, run bounded connection checks, inspect selected diagnostics, and support controlled plugin transfer."),
        ],
        "connections": "A user-controlled Raspberry Pi, a grandMA3 console on a trusted local network, and—only when enabled by the user—an OpenAI or ChatGPT connection for drafting.",
        "beta_note": "This is not autonomous show control. Physical commissioning, version-specific validation, an isolated trusted network, and a qualified operator remain required before production use.",
        "disclaimer": "Console Bridge is independent and is not affiliated with or endorsed by MA Lighting, OpenAI, Apple, or Raspberry Pi. grandMA3 and other marks belong to their owners.",
    },
    {
        "slug": "cueforge",
        "name": "CueForge",
        "store_name": "CueForge",
        "tagline": "Shape ideas into reviewable lighting cues.",
        "summary": "A local-first lighting cue planning and review environment for inventory-aware ONYX workflows.",
        "description": "CueForge explores how local models, saved-show inspection, and strict review gates can assist a lighting programmer without pretending drafts are verified console actions.",
        "platforms": ["Linux", "Windows", "Local AI"],
        "status": "Development prototype",
        "status_class": "prototype",
        "accent": "amber",
        "icon": "cueforge.svg",
        "testflight": None,
        "privacy": "privacy/cueforge/",
        "features": [
            ("Inventory-aware planning", "Ground drafts in imported fixture and preset information instead of free-form guesses."),
            ("Local model workflow", "Run supported planning and review models on local hardware, with source material kept on the workstation."),
            ("Human approval boundary", "Present expected cues, validation results, and known uncertainty before any operator-controlled next step."),
        ],
        "connections": "Local model runtimes and saved ONYX show snapshots. Live console synchronization and native cue recording remain development work.",
        "beta_note": "CueForge is a prototype, not a production console adapter. Current validation does not establish safe autonomous programming or live-show reliability.",
        "disclaimer": "CueForge is independent and is not affiliated with or endorsed by ONYX, Obsidian Control Systems, or any console manufacturer.",
    },
    {
        "slug": "dockeros",
        "name": "DockerOS",
        "store_name": "DockerOS",
        "tagline": "Boot into a focused Docker workstation.",
        "summary": "A bootable Linux system concept centered on Docker Engine, Compose, and browser-based container operations.",
        "description": "DockerOS packages a minimal Debian base with a guided installer and a web-first operating model for a dedicated x86-64 Docker host.",
        "platforms": ["x86-64", "Linux", "Docker"],
        "status": "In development",
        "status_class": "building",
        "accent": "cyan",
        "icon": "dockeros.svg",
        "testflight": None,
        "privacy": "privacy/dockeros/",
        "features": [
            ("Purpose-built host", "Start with a minimal Linux environment designed around Docker Engine and Compose."),
            ("Web-managed operations", "Use a browser-accessible container manager while retaining normal command-line access."),
            ("Repeatable installation", "Build a bootable image and install to a selected disk with explicit destructive-action warnings."),
        ],
        "connections": "Container registries, package mirrors, local network services, and any third-party containers the operator chooses to install.",
        "beta_note": "The installer can erase a selected disk. Back up data, verify the target drive, and test on non-production hardware before relying on a development image.",
        "disclaimer": "DockerOS is an independent project and is not affiliated with or endorsed by Docker, Debian, or the maintainers of included third-party software.",
    },
]

PRIVACY_POLICIES = {
    "website": {
        "title": "Website Privacy Policy",
        "summary": "How the Asterline Labs website handles visits, email, and links to external services.",
        "sections": [
            ("scope", "Scope", '''
<p>This policy covers the public Asterline Labs website. It does not replace the product-specific privacy policies linked below. Asterline Labs is an independent developer brand operated by Brandon Wade.</p>
<p>The site is designed as a static website. It does not create Asterline accounts, run advertising, use behavioral analytics, or place first-party tracking cookies.</p>
'''),
            ("information", "Information handled", '''
<h3>Ordinary website requests</h3>
<p>The hosting provider may receive standard request information such as an IP address, browser or device type, requested page, referring page, and request time. Asterline Labs does not add its own analytics scripts or advertising identifiers to the site.</p>
<h3>Email and support</h3>
<p>When you email support, the message may contain your address, the information you choose to provide, and technical details you include. Do not send passwords, API keys, access tokens, private playlist URLs, private server addresses, pairing files, show files, or other secrets.</p>
'''),
            ("use", "How information is used", '''
<p>Support messages are used to answer questions, investigate reports, improve documentation, protect product security, and maintain a record of the conversation when reasonably needed. Asterline Labs does not sell support information or use it for cross-context behavioral advertising.</p>
'''),
            ("services", "Hosting and external links", '''
<p>The website is hosted through GitHub Pages. GitHub may process request and security-log information under its own privacy terms. Links to TestFlight, Apple, GitHub, Google, OpenAI, Plex, Invidious servers, or other services leave this website; those services apply their own terms and privacy practices.</p>
'''),
            ("retention", "Retention and deletion", '''
<p>The static website does not maintain a user profile or first-party analytics database. Support email is retained only as long as reasonably necessary to handle the request, preserve security or business records, or meet legal obligations. You may request deletion of a support conversation, subject to records that must be kept for security, fraud prevention, or law.</p>
'''),
            ("choices", "Your choices", '''
<p>You can browse without an Asterline account and without accepting a first-party cookie banner because the site does not set tracking cookies. You may choose not to follow external links or send email. Browser privacy controls remain available for any storage or network behavior provided by your browser or hosting provider.</p>
'''),
            ("contact", "Contact", '''
<p>For a privacy question or deletion request, use the <a href="../../support/">support page</a> and include “Privacy” in the subject. Never include account credentials or private tokens.</p>
'''),
        ],
    },
    "orbit": {
        "title": "Orbit Privacy Policy",
        "summary": "How Orbit handles connected media services, local app data, account tokens, and optional synchronization.",
        "sections": [
            ("scope", "Scope and developer role", '''
<p>This policy applies to Orbit for iPhone, iPad, and Apple TV. Orbit is a client for services and sources selected by the user. Asterline Labs does not operate an Orbit account service, media catalog, streaming backend, advertising network, or analytics backend.</p>
<p>Information can be processed by the app and sent directly to a service you configure without being received by Asterline Labs. The distinction matters: app functionality may handle data even when the developer does not collect it on a developer-operated server.</p>
'''),
            ("data", "Data Orbit handles", '''
<h3>Connections and credentials</h3>
<ul>
<li>Plex server details, account or profile tokens, selected libraries, and playback state.</li>
<li>User-authorized M3U, Xtream-compatible, XMLTV, and guide-source URLs and credentials.</li>
<li>Selected Invidious server details and, when used, related account information.</li>
<li>Optional request-service endpoints and credentials, such as an Overseerr-compatible session or API key and a Cantinarr-compatible endpoint.</li>
<li>Optional Google OAuth access and refresh tokens for read-only YouTube subscription features.</li>
</ul>
<h3>Local library and preferences</h3>
<p>Orbit may store menu choices, profile selection, favorites, imported channel lists, guide data, searches, watch progress, playback preferences, artwork and metadata caches, downloaded or cached media created at the user’s direction, and diagnostic state needed to explain failures. Sensitive credentials are intended for Keychain or similarly protected local storage; ordinary preferences and caches use app storage.</p>
'''),
            ("use", "How the data is used", '''
<p>Orbit uses this information to connect to the service you selected, display your library or channels, resolve playback, keep progress and preferences, switch profiles, show guide information, and carry out actions you request. It is not used by Asterline Labs for advertising, user profiling, data brokerage, or sale.</p>
'''),
            ("sharing", "Where data goes", '''
<ul>
<li><strong>Your providers:</strong> Requests go directly to Plex, the media or guide provider, an Invidious instance, a request service, or another endpoint you entered.</li>
<li><strong>Google and YouTube:</strong> When you authorize read-only YouTube access, subscription and related API requests go to Google. Media playback can contact YouTube or Google video-delivery hosts.</li>
<li><strong>Apple:</strong> TestFlight and App Store distribution are handled by Apple. Keychain items marked for synchronization may be processed through iCloud when the user has iCloud Keychain enabled.</li>
<li><strong>No Asterline media relay:</strong> The current product does not route your Plex, IPTV, guide, or account traffic through an Asterline-operated backend.</li>
</ul>
'''),
            ("google", "Google API data", '''
<p>Orbit requests only the Google access needed for the described read-only YouTube subscription experience. Use and transfer of information received from Google APIs will adhere to the <a href="https://developers.google.com/terms/api-services-user-data-policy" rel="noopener noreferrer">Google API Services User Data Policy</a>, including its Limited Use requirements. Orbit does not use Google API data for advertising, credit decisions, or sale.</p>
'''),
            ("retention", "Retention and deletion", '''
<p>Data remains on the device, in Keychain, in optional iCloud Keychain synchronization, or with the external service according to that service’s settings. Within Orbit, disconnecting a service, removing an account, deleting an import, clearing history or downloads, or deleting the app removes the corresponding local data to the extent exposed by the build and platform. System backups or synchronized Keychain records may persist according to Apple settings.</p>
<p>Orbit does not create an Asterline account, so there is no Asterline account to delete. Deleting a Plex, Google, provider, or request-service account must be done with that provider. You can also revoke Orbit’s Google access from your Google account security settings.</p>
'''),
            ("tracking", "Tracking, advertising, and analytics", '''
<p>Orbit is not designed to include Asterline advertising, third-party behavioral analytics, or cross-app tracking. The external services you connect may log requests or apply their own analytics and privacy practices. Review each provider before connecting it.</p>
'''),
            ("security", "Security and user responsibilities", '''
<p>Orbit limits credential-bearing requests to the selected service and uses platform security features where implemented, but no software or network is perfectly secure. Use HTTPS endpoints where supported, protect your device, avoid untrusted playlists or servers, and never publish credentials in screenshots or support messages.</p>
'''),
            ("children", "Children", '''
<p>Orbit is not directed to children under 13 and does not knowingly operate a service that collects children’s personal information. Parents and guardians are responsible for the media services, sources, and accounts they configure.</p>
'''),
            ("contact", "Questions and changes", '''
<p>Material changes will be posted on this page with a revised effective date. For a privacy request, use the <a href="../../support/">support page</a>. Include the app name and do not send tokens, playlist URLs, passwords, or private server details.</p>
'''),
        ],
    },
    "nova-stream": {
        "title": "Nova Stream Privacy Policy",
        "summary": "How Nova Stream handles Invidious connections, local profiles, account tokens, history, and media requests.",
        "sections": [
            ("scope", "Scope and developer role", '''
<p>This policy applies to Nova Stream for iPhone and Apple TV. Nova Stream connects to an Invidious server chosen by the user and does not operate an Asterline account, video catalog, advertising system, analytics backend, or media relay.</p>
<p>The app processes information needed for features, but Asterline Labs generally does not receive that information because requests are made from the device to the configured server or media host.</p>
'''),
            ("data", "Data Nova Stream handles", '''
<ul>
<li>The HTTPS address of the Invidious server you select.</li>
<li>An optional scoped Invidious API token, normalized server identity, and local profile association. Password entry remains with the selected Invidious server.</li>
<li>Local profiles, subscriptions or imported channel lists, favorites, hidden channels, watch later or saved items, searches, playback preferences, watch history, and cached feed or artwork data.</li>
<li>Saved or locally downloaded media files created when the user invokes an available feature.</li>
<li>Video identifiers and playback metadata needed to request formats, thumbnails, captions, regular video, or live playback.</li>
</ul>
'''),
            ("use", "How the data is used", '''
<p>The data is used to authenticate to your chosen Invidious server, load feeds and search results, subscribe or unsubscribe when authorized, record history when the user granted that scope, resolve playback, and retain your on-device library. Nova Stream does not use it for Asterline advertising, cross-app tracking, data brokerage, or sale.</p>
'''),
            ("sharing", "Where data goes", '''
<ul>
<li><strong>Your Invidious server:</strong> Search, feed, account, subscription, history, metadata, and format requests go to the server you configure.</li>
<li><strong>Media hosts:</strong> Playback and images may be requested from hosts returned by Invidious. Live playback can contact YouTube or Google video-delivery endpoints directly without signing into a Google account.</li>
<li><strong>Optional self-hosted components:</strong> A compatible relay path, when configured by the server owner, is controlled by that operator rather than Asterline Labs.</li>
<li><strong>Apple:</strong> TestFlight and App Store distribution are handled by Apple.</li>
</ul>
<p>Server operators and media hosts may see ordinary request information such as IP address, user agent, requested video, and account activity. Choose an operator you trust and review its privacy practices.</p>
'''),
            ("retention", "Retention and deletion", '''
<p>Account tokens are intended for Keychain or protected app storage; library state and caches remain on the device. Use Nova Stream’s disconnect, profile, history, saved-item, import, or download controls where available, or delete the app to remove its local container. Device backups can retain data according to Apple settings.</p>
<p>Nova Stream does not create an Asterline account, so there is no Asterline account to delete. Delete an Invidious account with its server operator. Disconnecting Nova Stream removes the local token but does not by itself delete the remote account or all server logs.</p>
'''),
            ("tracking", "Tracking, advertising, and analytics", '''
<p>Nova Stream is not designed to include Asterline advertising, behavioral analytics, or cross-app tracking. Invidious operators, media hosts, Apple, and other external services apply their own logging and privacy practices.</p>
'''),
            ("rights", "Content and authorization", '''
<p>Users are responsible for using servers, downloads, streams, and content only when authorized. Nova Stream does not grant rights to third-party media, bypass provider permissions, or include a video catalog.</p>
'''),
            ("security", "Security", '''
<p>Nova Stream requires a normalized HTTPS server URL for current setup paths and rejects credential-bearing server URLs. No software can guarantee security. Keep the operating system current, use a trusted server, and never send account tokens or private URLs to support.</p>
'''),
            ("children", "Children", '''
<p>Nova Stream is not directed to children under 13, and Asterline Labs does not knowingly operate a service that collects children’s personal information. Parents and guardians control the server, media, and account access configured on a device.</p>
'''),
            ("contact", "Questions and changes", '''
<p>Material changes will be posted here with a new effective date. For a privacy request, use the <a href="../../support/">support page</a> and include “Nova Stream privacy” without including credentials.</p>
'''),
        ],
    },
    "console-bridge": {
        "title": "Console Bridge Privacy Policy",
        "summary": "How Console Bridge handles local-network pairing, bridge data, console diagnostics, saved drafts, and optional AI services.",
        "sections": [
            ("scope", "Scope and architecture", '''
<p>This policy covers the Console Bridge iPhone app and the companion software installed on a user-controlled Raspberry Pi. Daily app and browser traffic is intended to remain between the device, the Pi, and the selected console on the user’s network. Asterline Labs does not operate a Console Bridge cloud account or command relay.</p>
'''),
            ("data", "Data handled on the phone and Pi", '''
<h3>Pairing and local-network information</h3>
<ul>
<li>Bridge name and address, console target address, certificate identity or fingerprint, pairing or login state, and connection diagnostics.</li>
<li>A private setup file may contain bridge pairing details, recovery-network information, and a certificate fingerprint. It must be protected and deleted from Downloads after use.</li>
<li>On-device preferences and secure connection material needed to reconnect to the selected bridge.</li>
</ul>
<h3>Information stored on the Pi</h3>
<ul>
<li>Bridge login records, network settings, Wi-Fi profile information, console configuration, and local TLS material.</li>
<li>Saved chats, requests, AI drafts, macros, Lua drafts, a local library, confirmed console memory, and bounded diagnostic or audit records.</li>
<li>Optional OpenAI API configuration or a separate ChatGPT/Codex sign-in maintained by the isolated AI component on the Pi.</li>
</ul>
<p>Bridge passwords are designed to be stored as salted hashes. Wi-Fi passwords and optional provider credentials require protected local files. Operators remain responsible for securing the Pi, storage card, network, backups, and paired devices.</p>
'''),
            ("ai", "Optional AI processing", '''
<p>AI drafting is optional. When enabled, the Pi sends the user’s request, a bounded window of recent conversation messages, confirmed console memory, product instructions, and a limited diagnostic snapshot to the selected OpenAI service. The snapshot is designed to exclude credentials, raw OSC traffic, full fixture lists, and unrelated show data, but users should still avoid placing secrets in prompts or notes.</p>
<p>OpenAI processes the request under the account, plan, API terms, and privacy choices used by the operator. A requested provider setting such as <code>store:false</code> is not a guarantee of zero provider retention. ChatGPT or API credentials are not sent to Asterline Labs.</p>
'''),
            ("console", "Console and local-network data", '''
<p>The Pi can exchange bounded OSC, SFTP, HTTPS, discovery, or diagnostic traffic with the console and paired devices when a feature is deliberately used. Saved diagnostics can include configuration state, recent accepted feedback age, reachability results, and selected plugin error messages. Console feedback is not automatically treated as proof that an action executed successfully.</p>
'''),
            ("use", "How information is used", '''
<p>Information is used to authenticate paired devices, maintain the requested network connection, draft and save reviewable content, perform a user-approved transfer or command workflow, diagnose connectivity, and preserve a local audit trail. Asterline Labs does not receive it for advertising, behavioral profiling, sale, or cross-app tracking.</p>
'''),
            ("sharing", "Where data goes", '''
<ul>
<li><strong>Your equipment:</strong> The iPhone, Pi, and grandMA3 console communicate on networks you control.</li>
<li><strong>OpenAI, when enabled:</strong> Drafting requests go from the Pi to the selected OpenAI connection.</li>
<li><strong>Apple:</strong> TestFlight and App Store distribution are handled by Apple.</li>
<li><strong>No Asterline command cloud:</strong> Current product traffic is not routed through an Asterline-operated console or media backend.</li>
</ul>
'''),
            ("retention", "Retention and deletion", '''
<p>Phone data remains in the app container or secure storage until it is removed, replaced, or the app is deleted. Pi data remains until the operator deletes chats, memory, drafts, logs, credentials, or configuration; removes the application data; or reimages the device. Sign-out from OpenAI does not automatically erase local Console Bridge chats. Deleting local chats does not necessarily delete provider-side records governed by OpenAI’s terms.</p>
<p>Console Bridge does not create an Asterline account, so there is no Asterline account to delete. The operator controls the Pi and is responsible for deletion from backups and additional paired devices.</p>
'''),
            ("tracking", "Tracking and analytics", '''
<p>Console Bridge is not designed to include Asterline advertising, behavioral analytics, or cross-app tracking. Operating-system, Apple, OpenAI, router, console, or network logs remain subject to those systems’ practices.</p>
'''),
            ("security", "Security and safety boundary", '''
<p>The design uses local authentication, protected credentials, device-pinned HTTPS, isolated AI processing, expiring review plans, and explicit approval gates where implemented. These measures reduce risk but do not make a network or live show fail-safe. Use a dedicated trusted network, change default credentials, protect the setup file, verify certificates, keep backups, and qualify every supported console/software version before production use.</p>
'''),
            ("children", "Children", '''
<p>Console Bridge is a professional technical tool and is not directed to children under 13. Asterline Labs does not knowingly collect children’s personal information through a Console Bridge service.</p>
'''),
            ("contact", "Questions and changes", '''
<p>Material changes will be posted here with a revised effective date. For a privacy or security report, use the <a href="../../support/">support page</a>. Do not attach setup files, credentials, API keys, private IP plans, or show files unless a secure exchange has been arranged.</p>
'''),
        ],
    },
    "cueforge": {
        "title": "CueForge Privacy Policy",
        "summary": "How the CueForge development prototype handles local show snapshots, model prompts, drafts, and logs.",
        "sections": [
            ("scope", "Scope", '''
<p>This policy covers the CueForge development prototype. CueForge is currently a local-first planning and review environment, not a public cloud service or production console adapter. Asterline Labs does not operate a CueForge account, analytics backend, or hosted show-file service.</p>
'''),
            ("data", "Data handled locally", '''
<p>Depending on the development build, CueForge can handle imported fixture inventories, preset records, saved-show snapshots, user requests, generated drafts, review results, model configuration, reference documents, test results, and local audit or service logs. These items can contain production-sensitive information even when they do not contain conventional personal data.</p>
'''),
            ("ai", "Local model processing", '''
<p>Current documented workflows use local model runtimes on the operator’s workstation. Prompts, retrieved references, and drafts remain on that machine unless the operator separately exports, backs up, or configures an external provider. Any future external provider will require a policy update and will be governed by that provider’s terms.</p>
'''),
            ("use", "Use and disclosure", '''
<p>Local data is used to prepare inventory-grounded drafts, compare expected and saved results, display uncertainty, and support supervised testing. Asterline Labs does not receive it through a CueForge cloud backend, sell it, or use it for advertising or cross-context profiling.</p>
'''),
            ("retention", "Retention and deletion", '''
<p>The operator controls retention through local files, model stores, logs, exports, backups, and development checkpoints. Delete the relevant workspace, logs, model history, exports, and backups to remove the data. There is no Asterline account to delete.</p>
'''),
            ("security", "Security", '''
<p>Show files, patch information, and venue details can be confidential. Use encrypted storage where appropriate, restrict workstation access, keep the simulator and development services bound to trusted interfaces, and review exports before sharing. Do not treat the prototype as a hardened live-show system.</p>
'''),
            ("contact", "Questions and changes", '''
<p>Material changes will be posted here. Use the <a href="../../support/">support page</a> for privacy questions and do not send private show files or credentials in ordinary email.</p>
'''),
        ],
    },
    "dockeros": {
        "title": "DockerOS Privacy Policy",
        "summary": "How the DockerOS development project handles local configuration, logs, registries, and third-party containers.",
        "sections": [
            ("scope", "Scope", '''
<p>This policy covers the DockerOS development image and installer. DockerOS is software installed on hardware controlled by the operator. Asterline Labs does not operate a DockerOS cloud account, telemetry service, container registry, or hosted control plane.</p>
'''),
            ("data", "Data handled on the host", '''
<p>The system can store host and network configuration, administrator credentials, Docker settings, Compose files, container images, volumes, secrets, logs, and browser-management configuration. The exact information depends on the containers the operator installs.</p>
'''),
            ("network", "Network services and third-party containers", '''
<p>The base system may contact package mirrors, time services, and container registries for functions the operator invokes. Each installed image or container can have independent data practices, ports, credentials, and external services. Asterline Labs does not review or control every third-party container.</p>
'''),
            ("use", "Use and disclosure", '''
<p>Local information is used to install and operate the host and containers. The development image is not designed to send Asterline analytics, advertising identifiers, or host telemetry to Asterline Labs. Registry, package, DNS, router, and container operators may log ordinary requests under their own terms.</p>
'''),
            ("retention", "Retention and deletion", '''
<p>The operator controls local files, volumes, images, logs, backups, and secrets. Remove a container and its volumes, delete configuration, reset the manager, or securely erase/reinstall the host to remove data as appropriate. The installer is destructive to the selected disk; ordinary deletion does not guarantee forensic erasure.</p>
'''),
            ("security", "Security", '''
<p>A container host can expose powerful administrative functions. Change default credentials, restrict management ports, apply updates, protect secrets, use least privilege, review images and Compose files, and do not expose the manager directly to the public internet without a separately secured access design.</p>
'''),
            ("contact", "Questions and changes", '''
<p>Material changes will be posted here. Use the <a href="../../support/">support page</a> for privacy or security reports and redact credentials, tokens, public IP addresses, and private configuration before sending logs.</p>
'''),
        ],
    },
}

TERMS_SECTIONS = [
    ("agreement", "Agreement and scope", '''
<p>These terms govern the Asterline Labs website, beta software, development previews, documentation, and related support material. By installing, testing, or using a product, you agree to these terms and any platform terms that also apply, including Apple’s TestFlight terms for TestFlight builds.</p>
<p>Asterline Labs is an independent developer brand operated by Brandon Wade. A product-specific license or written agreement controls if it conflicts with these general terms.</p>
'''),
    ("beta", "Beta and development software", '''
<p>Beta builds and prototypes are unfinished. Features can change, disappear, fail, lose compatibility, corrupt local state, or become unavailable without notice. Builds can expire or be replaced. Do not use a beta as the sole copy of important information or as an unqualified production system.</p>
<p>Back up data before testing. Use non-production hardware, accounts, networks, media libraries, and show files when practical. Participation can be limited or ended to protect security, capacity, or product quality.</p>
'''),
    ("license", "Limited license", '''
<p>Subject to these terms, Asterline Labs grants you a limited, revocable, non-exclusive, non-transferable license to use the software for personal evaluation or authorized business testing on devices you control. You may not sell access, defeat security controls, impersonate the developer, distribute private builds or credentials, or use the products to violate law or third-party rights.</p>
'''),
    ("accounts", "Your accounts, equipment, and authorization", '''
<p>You are responsible for the accounts, services, servers, networks, hardware, credentials, content, and permissions you connect. Use only media, streams, downloads, consoles, show files, providers, and APIs you are authorized to access. Asterline Labs does not supply media rights, television service, a Plex library, an Invidious server, paid AI access, or console authorization.</p>
<p>Protect API keys, account tokens, pairing files, server URLs, Wi-Fi credentials, and console information. Activity performed through your connected equipment or account is your responsibility unless applicable law provides otherwise.</p>
'''),
    ("safety", "Professional and safety-critical use", '''
<p>Console Bridge and CueForge produce diagnostics, drafts, or operator-controlled workflows; they do not replace a qualified lighting programmer, console operator, system engineer, or venue safety process. AI output can be incomplete, incorrect, unsafe, or incompatible with a specific software version.</p>
<p>Review exact commands and source, confirm the target and show state, maintain an emergency stop or equivalent operational control, and validate on isolated test systems before production. Never rely on an AI statement, connection check, feedback age, or generated draft as proof that a console action succeeded.</p>
'''),
    ("third-parties", "Third-party services", '''
<p>Products may interoperate with Apple, TestFlight, GitHub, Plex, Google, YouTube, Invidious, OpenAI, MA Lighting, ONYX, Docker, Debian, media providers, and user-selected servers or containers. Those services are independent, can change without notice, and apply their own terms, privacy policies, fees, limits, and availability rules. Asterline Labs is not responsible for a third party’s service, content, security, or policy decisions.</p>
'''),
    ("content", "Content and intellectual property", '''
<p>The Asterline Labs name, original branding, website design, product interfaces, and original code or documentation are protected by applicable intellectual-property laws. Third-party names and marks belong to their owners and are used only to identify interoperability.</p>
<p>You retain rights in the content and feedback you submit. By sending product feedback, you grant Asterline Labs permission to use it to evaluate and improve the products without an obligation to pay, provided that private credentials and confidential customer content are not intentionally published.</p>
'''),
    ("privacy", "Privacy", '''
<p>Product and website data practices are described in the <a href="../privacy/">privacy center</a>. External providers apply their own privacy terms. Do not send secrets or private production files through ordinary support email.</p>
'''),
    ("warranty", "Disclaimers", '''
<p>To the maximum extent permitted by law, the website, beta software, prototypes, and documentation are provided “as is” and “as available,” without warranties of merchantability, fitness for a particular purpose, non-infringement, uninterrupted operation, data preservation, accuracy, or compatibility. Nothing in these terms excludes a warranty or consumer right that cannot legally be excluded.</p>
'''),
    ("liability", "Limitation of liability", '''
<p>To the maximum extent permitted by law, Asterline Labs will not be liable for indirect, incidental, special, consequential, exemplary, or punitive damages; lost profits, revenue, data, media, show files, or business opportunity; service interruption; equipment or network changes; or third-party claims arising from use of a beta or prototype. Non-waivable rights and liability remain unaffected.</p>
'''),
    ("termination", "Suspension and termination", '''
<p>You may stop using a product at any time. Asterline Labs may suspend access to a beta, revoke a private invitation, or discontinue a build when reasonably needed for security, legal compliance, capacity, abuse prevention, or development. Sections that by their nature should survive—such as intellectual property, disclaimers, and liability limits—continue after use ends.</p>
'''),
    ("changes", "Changes and contact", '''
<p>These terms may be updated as products and distribution change. The effective date identifies the current version. Material changes will be posted on this site. Questions can be sent through the <a href="../support/">support page</a>.</p>
'''),
]

# AsterOS: current private TestFlight beta, September 27, 2026.
APPS.append({
    "slug": "asteros", "name": "AsterOS", "store_name": "AsterOS",
    "tagline": "Your server. Within reach.",
    "summary": "A native Unraid companion for server monitoring, Docker apps, files, and photo backups.",
    "description": "Keep your own server close with a rounded, glass-inspired interface for iPhone and iPad. Explore an offline demo before connecting.",
    "platforms": ["iPhone", "iPad", "Unraid"],
    "status": "Private TestFlight beta", "status_class": "private", "accent": "mint",
    "icon": "asteros.png", "testflight": None, "privacy": "privacy/asteros/",
    "features": [
        ("Know your server", "See CPU, memory, network, storage and supported GPU statistics. Hardware and server plugins determine available readings."),
        ("Make apps your own", "Arrange Docker apps in folders, choose custom icons, browse Community Applications, and review basic or advanced container settings."),
        ("Keep files and memories close", "Browse your network shares and explicitly back up photos, videos and Live Photos to a chosen folder, with year/month organization and resumable progress.")
    ],
    "connections": "Your Unraid server over HTTPS, SMB shares using your share account, and optional app-scoped Tailscale connectivity. The current direct connection workflow does not require an AsterOS Docker companion.",
    "beta_note": "AsterOS is in private TestFlight testing. External beta review is being prepared; no public invitation is available yet. Photo backup currently runs in the foreground after you start it. Use disposable files and containers for beta testing.",
    "disclaimer": "AsterOS is independent and is not affiliated with or endorsed by Unraid, Tailscale, Docker, Desktop Commander or Apple. Container software and Desktop Commander run on your server, not on iOS."
})

PRIVACY_POLICIES["asteros"] = {
    "title": "AsterOS Privacy Policy",
    "effective_date": "September 27, 2026",
    "summary": "How AsterOS handles server access, network shares, photo backups, private connectivity and support information.",
    "sections": [
        ("scope", "Scope and developer role", """
<p>This policy covers AsterOS for iPhone and iPad, developed by Brandon Wade under Asterline Labs. AsterOS connects to servers and services you choose. It does not require an Asterline account, and Asterline Labs does not operate a backend that receives or relays your server files, photo backups or server credentials.</p>
<p>The app processes data on your device and through your configured services. This is distinct from information you deliberately send to Asterline Labs through support or Apple's beta feedback tools.</p>
"""),
        ("local", "Information stored on your device", """
<ul>
<li>Saved server names and addresses, app shortcuts, app order and folders, selected icons, display preferences and backup destination settings.</li>
<li>Server API credentials, share credentials and remembered server session cookies, stored using the device Keychain.</li>
<li>Local caches, selected file or photo resources needed for a transfer, backup progress information and technical state used to explain connection failures.</li>
<li>Optional Tailscale device identity and connection state in the app's protected storage.</li>
<li>App-lock settings and PIN verification material when enabled. Face ID and Touch ID authentication are handled by Apple's system APIs; AsterOS does not receive your face or fingerprint data.</li>
</ul>
<p>The offline demo uses fictional data and in-memory changes. It does not read your photo library, connect to your server or perform actual container installations.</p>
"""),
        ("servers", "Your server, files and apps", """
<p>API requests, monitoring data, container configuration and terminal traffic pass between your device and the server you configure. File browsing and backups use the share account and destination you select. Your server, reverse proxy and installed applications may keep their own access or activity logs.</p>
<p>App icons, catalog information and websites can be supplied by your server or by third-party hosts. Opening an app website or fetching its icon can send normal request information, such as your IP address, to that host. Website sessions may use cookies in their browser storage.</p>
<p>Optional Desktop Commander pairing and remote access involve the Desktop Commander service and any client you authorize. The integration runs on your server. Review its access and privacy practices before enabling it.</p>
"""),
        ("photos", "Photos, videos and backups", """
<p>When you enable a real backup, AsterOS requests photo-library access through iOS. Depending on your permission, it can read authorized photos, videos, Live Photo resources and associated metadata needed to identify, organize and upload originals. Originals may contain capture dates, location metadata and other information already present in the file.</p>
<p>After you explicitly start a backup, files are sent to your chosen server folder. They are not uploaded to Asterline Labs. Backup receipts and destination state help avoid repeating verified uploads. Photo resources stored in iCloud may be retrieved through Apple's Photos services when needed and permitted. The current backup workflow runs in the foreground.</p>
<p>You control Photos access in iOS Settings. Removing access does not delete originals already backed up to your server. Manage those files and backup receipts on your server.</p>
"""),
        ("tailscale", "Optional Tailscale connectivity", """
<p>If you choose private connectivity, the embedded Tailscale component connects to your Tailscale account and tailnet. Tailscale may process account and device information, public keys, network addresses and connection metadata to authenticate and coordinate connections. Connections may use Tailscale relay infrastructure when necessary.</p>
<p>This connection is scoped to the app's private-server traffic rather than a system-wide VPN. Tailscale and your chosen identity provider apply their own practices. See <a href="https://tailscale.com/legal/privacy-policy" rel="noopener noreferrer">Tailscale's Privacy Policy</a>. Signing out in AsterOS and removing the device in your Tailscale administration controls are separate from removing an Unraid server profile.</p>
"""),
        ("support", "Support and Apple diagnostics", """
<p>If you contact support, Asterline Labs receives your email address and the message, attachments or reports you choose to send. We use these to answer questions, investigate defects and improve the app. Review reports before sharing and do not include passwords, API keys, private server URLs or sensitive photos.</p>
<p>Apple handles App Store and TestFlight distribution. TestFlight can provide the developer with crash reports, usage information and feedback, including submitted screenshots. See <a href="https://www.apple.com/legal/privacy/data/en/test-flight/" rel="noopener noreferrer">TestFlight and Privacy</a>. AsterOS does not add an advertising SDK or a behavioral analytics account.</p>
"""),
        ("retention", "Retention and your controls", """
<p>Local preferences and caches remain until removed through available app controls, replaced or cleared, or the app is deleted. Keychain records and system backups can persist according to platform behavior and your Apple settings. Remove saved connections and revoke server-issued credentials when you no longer want access. Removing a server profile does not revoke its API key on the server.</p>
<p>Backups and other files on your server remain until you delete them there; deleting AsterOS does not delete server files or containers. Manage third-party accounts, sessions and devices with those providers. AsterOS does not create an Asterline account requiring deletion.</p>
<p>Support correspondence is retained as reasonably needed to resolve your request and maintain necessary security or business records. You may request access, correction or deletion of information you sent us, subject to information we must retain. Requests to external providers must be directed to them.</p>
"""),
        ("choices", "Choices and security", """
<p>You can use the demo without a server account, choose whether to enable Tailscale, limit photo access and enable an optional app lock. Server access should use only accounts and permissions you need. Asterline Labs does not sell personal information or use it for cross-app advertising. External services have their own logging, retention and privacy practices.</p>
<p>No software or network can guarantee complete security. Keep your device and server updated, protect credentials, and review sensitive actions before confirming them.</p>
"""),
        ("contact", "Contact and changes", """
<p>For AsterOS support or privacy questions, email <a href="mailto:brandonewade+asterline@gmail.com">brandonewade+asterline@gmail.com</a> or visit the <a href="../../support/">support page</a>. Include AsterOS in the subject. This policy will be updated as the app's data handling changes, with a revised effective date.</p>
""")
    ]
}
