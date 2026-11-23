#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
index = (PUBLIC / "index.html").read_text()
header = re.search(r"<header class=\"site-header\">.*?</header>", index, re.S).group(0)
footer = re.search(r"<footer class=\"site-footer\">.*?</footer>", index, re.S).group(0)

def page(path, title, description, body, *, canonical=None, body_class=""):
    clean = path[:-5] if path.endswith(".html") else path
    if clean == "index": clean = ""
    canonical = canonical or f"https://mycelium.fpl.dev/{clean}"
    body_class_attr = f' class="{body_class}"' if body_class else ""
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="https://mycelium.fpl.dev/assets/og.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#f8f5ff">
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/assets/site.css">
  <script defer src="/assets/site.js"></script>
</head>
<body{body_class_attr}>
<a class="skip" href="#main">Skip to content</a>
{header}
<main id="main">
{body}
</main>
{footer}
</body>
</html>
'''
    out = PUBLIC / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)

PLANS = '''
<div class="pricing-grid reveal">
  <article class="plan">
    <div class="plan-label"><h3>Starter</h3></div>
    <div class="price"><strong data-monthly="$15" data-annual="$150">$15</strong><span>/ month</span></div>
    <div class="annual" data-annual-note>billed monthly</div>
    <p class="plan-copy">For one operator who wants the hosted workspace without the server.</p>
    <ul><li>1 human · 3 agents</li><li>1 hosted computer</li><li>10 GB workspace storage</li><li>BYO model keys or credits</li><li>Community + email support</li></ul>
    <a class="btn" href="/signup">Start free</a>
  </article>
  <article class="plan featured">
    <div class="plan-label"><h3>Team</h3><span class="badge">Most popular</span></div>
    <div class="price"><strong data-monthly="$49" data-annual="$490">$49</strong><span>/ month</span></div>
    <div class="annual" data-annual-note>billed monthly</div>
    <p class="plan-copy">For a small team that wants the business to run on one shared surface.</p>
    <ul><li>5 humans · 15 agents</li><li>3 hosted computers</li><li>50 GB workspace storage</li><li>Shared routines and approvals</li><li>Passkeys, roles, and invites</li><li>Priority email support</li></ul>
    <a class="btn primary" href="/signup">Start free</a>
  </article>
  <article class="plan">
    <div class="plan-label"><h3>Business</h3></div>
    <div class="price"><strong data-monthly="$99" data-annual="$990">$99</strong><span>/ month</span></div>
    <div class="annual" data-annual-note>billed monthly</div>
    <p class="plan-copy">For teams where the workspace is the operating picture, not a side project.</p>
    <ul><li>15 humans · 50 agents</li><li>10 hosted computers</li><li>200 GB workspace storage</li><li>Audit log and advanced roles</li><li>SSO · 99.9% uptime target</li><li>Priority support</li></ul>
    <a class="btn" href="/signup">Start free</a>
  </article>
</div>
'''

page("pricing.html", "Pricing — Mycelium", "Open source forever. Hosted plans from $15/month for a managed Mycelium workspace, with teams, agents, hosted computers, and enterprise SLA.", f'''
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Pricing</p>
    <h1>Open source forever. Hosted when you need it.</h1>
    <p class="lede">The core is free to run anywhere. Paid plans sell the boring, important parts: a workspace that stays up, shared computers, team controls, and someone to call when it matters.</p>
    <div style="display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin-top:24px">
      <div class="billing-toggle" role="group" aria-label="Billing period"><button type="button" data-billing="monthly" class="is-active">Monthly</button><button type="button" data-billing="annual">Annual · 2 months free</button></div>
      <span class="mono" style="font-size:10px;color:var(--muted)">7-day trial · no setup fee · cancel anytime</span>
    </div>
  </div>
</section>
<section class="section" style="padding-top:28px">
  <div class="wrap">
    {PLANS}
    <div class="pricing-note"><span>Annual billing: 2 months free</span><span>Extra humans, agents, and computers available</span><span>Enterprise from $1,000/mo</span></div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Compare</p><h2>What each plan includes.</h2></div><p class="lede">Start smaller than you think you need. Upgrade when the workspace becomes the place the team actually works.</p></div>
    <div class="plan-table-wrap reveal">
      <table class="plan-table">
        <thead><tr><th>Included</th><th>Starter</th><th>Team</th><th>Business</th><th>Enterprise</th></tr></thead>
        <tbody>
          <tr><td>Price</td><td>$15/mo</td><td>$49/mo</td><td>$99/mo</td><td>from $1,000/mo</td></tr>
          <tr><td>Humans</td><td>1</td><td>5</td><td>15</td><td>Custom</td></tr>
          <tr><td>Agents</td><td>3</td><td>15</td><td>50</td><td>Custom</td></tr>
          <tr><td>Hosted computers</td><td>1</td><td>3</td><td>10</td><td>Dedicated</td></tr>
          <tr><td>Workspace storage</td><td>10 GB</td><td>50 GB</td><td>200 GB</td><td>Custom</td></tr>
          <tr><td>Passkeys</td><td>✓</td><td>✓</td><td>✓</td><td>✓ + SSO / SCIM</td></tr>
          <tr><td>Audit log</td><td>—</td><td>—</td><td>✓</td><td>✓ + export</td></tr>
          <tr><td>Uptime commitment</td><td>Best effort</td><td>Best effort</td><td>99.9% target</td><td>99.95% SLA</td></tr>
          <tr><td>Support</td><td>Email</td><td>Priority email</td><td>Priority + onboarding</td><td>Named support path</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Billing, without the fog</p><h2>Four things make up a bill.</h2></div><p class="lede">Models are yours or ours. Hardware is yours or ours. You pay for the workspace, the people, the agents, and the compute that keeps it alive.</p></div>
    <div class="three reveal">
      <article class="feature"><span class="num">01</span><h3>Workspace</h3><p>One shared operating surface: apps, files, memory, routines, approvals, and the agents that connect them.</p></article>
      <article class="feature"><span class="num">02</span><h3>People &amp; agents</h3><p>Each plan includes a base team. Add humans and agents as the work grows. You can always bring your own model keys.</p></article>
      <article class="feature"><span class="num">03</span><h3>Compute</h3><p>Hosted computers run the agents and apps. Bring your own hardware, or use our managed compute with included hours.</p></article>
    </div>
    <p class="note reveal" style="margin-top:18px">Need a model-credit invoice instead of BYO keys? We sell credits at transparent rates. Need a private deployment? Enterprise includes dedicated infrastructure and a data processing agreement.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">FAQ</p><h2>Before you buy.</h2></div><p class="lede">The short version: the open source project is free; the hosted plan is for teams that want someone else to own the pager.</p></div>
    <div class="faq reveal">
      <details><summary>Do I need a credit card for the trial?</summary><p>No card for the 7-day hosted trial. We ask for payment details when you choose a plan. Self-hosting never requires payment.</p></details>
      <details><summary>Can I move from hosted to self-hosted?</summary><p>Yes. Export your workspace and follow the self-hosting guide. The open-source install does not require a license key.</p></details>
      <details><summary>What counts as an agent?</summary><p>An agent is a persistent worker with a job, memory, permissions, and a place in the workspace. You can create, pause, and delete them at any time.</p></details>
      <details><summary>What happens when I hit my limit?</summary><p>We warn you before the cap. You can upgrade, add a pack, or pause new agent runs. We do not want to surprise you with an overage bill.</p></details>
      <details><summary>Is there an enterprise SLA?</summary><p>Yes. Enterprise includes a 99.95% uptime SLA, a named support path, private deployment options, and security review support.</p></details>
    </div>
  </div>
</section>
''')

page("download.html", "Self-host Mycelium", "Install Mycelium on macOS, Linux, a server, or your own cloud. Open source under MIT OR Apache-2.0. Bring your own models and hardware.", f'''
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Self-host</p>
    <h1>Run it yourself. Keep the keys.</h1>
    <p class="lede">Mycelium is open source. Install it on a laptop, a server, or your own cloud. There is no license key, no phone-home requirement, and no feature held back for the hosted plan.</p>
    <div class="hero-actions"><a class="btn primary" href="/docs/self-hosting">Read the install guide <span class="arrow" aria-hidden="true">→</span></a><a class="btn" href="https://github.com/mycelium-linux/mycelium">View the repository</a></div>
  </div>
</section>
<section class="section" style="padding-top:20px">
  <div class="wrap page-grid">
    <article class="panel dark">
      <p class="eyebrow light">Fast path</p>
      <h2>One command.</h2>
      <p>The installer builds the core binaries, enrolls the host, and prompts for the optional pieces. It is safe to re-run.</p>
      <div class="terminal" style="margin-top:18px"><div class="terminal-top"><i></i><i></i><i></i><span>bash</span></div><pre><span class="prompt">$</span> curl --proto '=https' --tlsv1.2 -fsS \\
  https://raw.githubusercontent.com/mycelium-linux/mycelium/master/install.sh | bash</pre></div>
      <div class="copy-line"><code>curl --proto '=https' --tlsv1.2 -fsS https://raw.githubusercontent.com/mycelium-linux/mycelium/master/install.sh | bash</code><button type="button" data-copy="curl --proto '=https' --tlsv1.2 -fsS https://raw.githubusercontent.com/mycelium-linux/mycelium/master/install.sh | bash">Copy</button></div>
    </article>
    <article class="panel">
      <p class="eyebrow">What you need</p>
      <h2>A machine and a little patience.</h2>
      <ul class="checklist">
        <li>macOS or a systemd-based Linux distribution</li>
        <li>4 vCPU, 8 GB RAM, 100 GB free disk for a comfortable server</li>
        <li>A domain name if you want remote access and TLS</li>
        <li>Optional: a model provider key, or a local OpenAI-compatible endpoint</li>
        <li>Optional: object storage for larger file workspaces</li>
      </ul>
      <p class="note" style="margin-top:18px">For production, use the server guide. It covers TLS, reverse proxy, backups, and upgrades.</p>
    </article>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Pick your shape</p><h2>Laptop, server, or image.</h2></div><p class="lede">The same core. Different amounts of uptime and isolation.</p></div>
    <div class="three reveal">
      <article class="feature"><span class="num">01</span><h3>On your machine</h3><p>Try the workspace, connect a model, and keep everything local. Good for evaluation and personal use.</p><div style="margin-top:14px"><a class="btn small" href="/docs/self-hosting#laptop">Laptop guide</a></div></article>
      <article class="feature"><span class="num">02</span><h3>On a server</h3><p>Run a persistent workspace for a team with TLS, backups, and a reverse proxy. This is the recommended self-host path.</p><div style="margin-top:14px"><a class="btn small" href="/docs/self-hosting#server">Server guide</a></div></article>
      <article class="feature"><span class="num">03</span><h3>fungOS image</h3><p>Want the whole operating environment? Start with the fungOS distribution and bring Mycelium up as the control plane.</p><div style="margin-top:14px"><a class="btn small" href="https://fungos.dev/">Explore fungOS</a></div></article>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="enterprise reveal">
      <div><p class="eyebrow">Rather not run the pager?</p><h2>We can host it for you.</h2><p class="lede" style="margin-bottom:20px">Hosted Mycelium gives you the same workspace with managed uptime, shared computers, passkeys, and a team that gets paged before you do.</p><div class="hero-actions"><a class="btn primary" href="/pricing">See hosted plans <span class="arrow" aria-hidden="true">→</span></a><a class="btn" href="/enterprise">Talk to us</a></div></div>
      <ul class="enterprise-list"><li>Managed workspace on FPL Cloud</li><li>Passkeys and team invitations</li><li>Included hosted computers and storage</li><li>Export and leave whenever you want</li></ul>
    </div>
  </div>
</section>
''')

INTEGRATIONS = [
    "Beeper", "Gmail", "Google Drive", "Slack", "Notion", "GitHub", "Linear", "Stripe",
    "HubSpot", "Salesforce", "Postgres", "Figma", "Google Calendar", "Microsoft Teams",
    "WhatsApp", "Telegram", "Dropbox", "Airtable", "Jira", "Discord", "Twilio", "Shopify",
    "QuickBooks", "Snowflake", "BigQuery", "S3", "MCP", "Custom HTTP",
]
integration_cards = "\n".join(f'<div class="integration"><i></i>{name}</div>' for name in INTEGRATIONS)

page("integrations.html", "Integrations — Mycelium", "Connect Gmail, Slack, Notion, GitHub, Stripe, HubSpot, Postgres, Beeper, and 1,700+ apps through Composio — plus any MCP server.", f'''
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Integrations</p>
    <h1>Bring your stack. Keep your stack.</h1>
    <p class="lede">The best operating system is the one that already knows where your work lives. Connect the tools you pay for, keep your own MCP servers, and let the agents do the translation.</p>
    <div class="hero-actions"><a class="btn primary" href="/signup">Connect your stack <span class="arrow" aria-hidden="true">→</span></a><a class="btn" href="https://composio.dev/toolkits">Browse the Composio catalog</a></div>
  </div>
</section>
<section class="section" style="padding-top:20px">
  <div class="wrap">
    <div class="logo-band-head"><p>Representative integrations</p><span>1,700+ apps through Composio, plus any MCP server.</span></div>
    <div class="integration-grid reveal">{integration_cards}</div>
    <p class="note reveal" style="margin-top:18px">Logos and product names belong to their owners. “Works with” means a supported connection, not a partnership or endorsement.</p>
  </div>
</section>
<section class="section">
  <div class="wrap page-grid">
    <article class="panel"><p class="eyebrow">MCP first</p><h2>If it speaks MCP, it belongs.</h2><p>Mycelium uses MCP to connect tools, resources, and prompts. Point it at a local server, a hosted endpoint, or your own internal service. Scope access per agent and keep the credentials in the workspace boundary.</p><div class="code-block"><span class="c"># example</span><br><span class="g">mycelium</span> mcp add internal-crm \\<br>&nbsp;&nbsp;--url https://mcp.internal.example/sse \\<br>&nbsp;&nbsp;--scope crm.read</div></article>
    <article class="panel"><p class="eyebrow">Composio</p><h2>1,700+ apps without 1,700 integrations.</h2><p>Composio gives Mycelium a broad catalog of authenticated app actions. Connect Gmail, Slack, HubSpot, Salesforce, Notion, GitHub, and more without waiting for us to build each connector from scratch.</p><p><a class="text-link" style="color:var(--violet-2)" href="https://composio.dev/">Learn about Composio →</a></p></article>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Need something else?</p><h2>The long tail is the point.</h2></div><p class="lede">If your business runs on a tool nobody has heard of, that is exactly the kind of tool we want to connect.</p></div>
    <div class="three reveal">
      <article class="feature"><span class="num">01</span><h3>Custom MCP</h3><p>Wrap your internal API in an MCP server and bring it into the workspace. Your auth, your scopes, your data.</p></article>
      <article class="feature"><span class="num">02</span><h3>Bring your own keys</h3><p>Use your model provider, your cloud, and your storage. Mycelium coordinates; it does not have to own the account.</p></article>
      <article class="feature"><span class="num">03</span><h3>Request a connector</h3><p>Tell us what is missing. If it has an API or an MCP server, there is a path.</p><div style="margin-top:14px"><a class="btn small" href="mailto:hello@fpl.dev?subject=Mycelium%20integration%20request">Request an integration</a></div></article>
    </div>
  </div>
</section>
''')

page("security.html", "Security & trust — Mycelium", "Open source, exportable, and built around explicit access. Learn how Mycelium handles data, credentials, permissions, hosting, and security disclosures.", '''
<section class="page-hero"><div class="wrap"><p class="eyebrow">Security &amp; trust</p><h1>Open by default. Yours by design.</h1><p class="lede">You should not have to trust a marketing page with your business. Read the source, run it yourself, scope the access, and leave with your data whenever you want.</p></div></section>
<section class="section" style="padding-top:20px"><div class="wrap page-grid">
  <article class="panel"><p class="eyebrow">Source</p><h2>Inspect it.</h2><p>The core is open source under MIT OR Apache-2.0. The build, the access model, and the update path are visible. Security through obscurity is not a strategy.</p><p><a class="text-link" style="color:var(--violet-2)" href="https://github.com/mycelium-linux/mycelium">github.com/mycelium-linux/mycelium →</a></p></article>
  <article class="panel"><p class="eyebrow">Data</p><h2>Keep it.</h2><p>Your workspace data is yours. Export it. Delete it. Self-host it. We do not train models on customer workspace data, and enterprise deployments can keep the data boundary entirely inside your infrastructure.</p></article>
  <article class="panel"><p class="eyebrow">Access</p><h2>Scope it.</h2><p>Passkeys for people, scoped credentials for agents, explicit approvals for mutations, and an audit trail for the actions that matter. Credentials are leased at the moment of use, not baked into configuration.</p></article>
  <article class="panel"><p class="eyebrow">Hosting</p><h2>Isolate it.</h2><p>Hosted workspaces run on FPL Cloud with per-tenant isolation and encrypted storage. Enterprise customers can choose a dedicated deployment with a private network boundary.</p></article>
</div></section>
<section class="section"><div class="wrap">
  <div class="section-head reveal"><div><p class="eyebrow">The honest status</p><h2>What we claim. What we do not.</h2></div><p class="lede">Trust is easier when the claims are specific.</p></div>
  <div class="three reveal">
    <article class="feature"><span class="num">✓</span><h3>We claim</h3><p>Open-source core, exportable data, scoped access, approval gates, encrypted transport, and a private-deployment path for enterprise.</p></article>
    <article class="feature"><span class="num">→</span><h3>In progress</h3><p>SOC 2 readiness, a public trust center, third-party penetration testing, and formal uptime reporting. We will publish evidence as it exists.</p></article>
    <article class="feature"><span class="num">—</span><h3>We do not claim</h3><p>Certifications we have not earned, customers we do not have, or integrations that are not live. Ask for specifics and we will show our work.</p></article>
  </div>
  <p class="note reveal" style="margin-top:18px">Security disclosure: email <a href="mailto:security@fpl.dev" style="color:var(--violet-2)">security@fpl.dev</a>. Please include reproduction steps and give us a reasonable window to fix the issue before public disclosure.</p>
</div></section>
<section class="section"><div class="wrap"><div class="enterprise reveal"><div><p class="eyebrow">Enterprise</p><h2>Need a security review?</h2><p class="lede" style="margin-bottom:20px">We can provide architecture details, a DPA, subprocessor information, and a private deployment plan.</p><div class="hero-actions"><a class="btn primary" href="/enterprise">Talk to us <span class="arrow" aria-hidden="true">→</span></a><a class="btn" href="mailto:security@fpl.dev">security@fpl.dev</a></div></div><ul class="enterprise-list"><li>Private deployment and network isolation</li><li>SSO / SCIM and audit export</li><li>Data processing agreement</li><li>Named security contact</li></ul></div></div></section>
''')

page("enterprise.html", "Enterprise — Mycelium", "Private deployment, dedicated infrastructure, SSO, audit trails, and a named support path for teams that cannot wait for uptime.", '''
<section class="page-hero"><div class="wrap"><p class="eyebrow">Enterprise</p><h1>When the business cannot wait.</h1><p class="lede">Mycelium Enterprise is for teams that want the agent-native workspace without outsourcing the trust boundary. Private deployment, dedicated infrastructure, and a support path with names on it.</p><div class="hero-actions"><a class="btn primary" href="mailto:hello@fpl.dev?subject=Mycelium%20Enterprise">Talk to us <span class="arrow" aria-hidden="true">→</span></a><a class="btn" href="/security">Security &amp; trust</a></div></div></section>
<section class="section" style="padding-top:20px"><div class="wrap"><div class="three reveal">
  <article class="feature"><span class="num">01</span><h3>Private by default</h3><p>Single-tenant deployment on FPL Cloud or your own infrastructure. Your network boundary, your keys, your data.</p></article>
  <article class="feature"><span class="num">02</span><h3>Operational trust</h3><p>99.95% uptime SLA, incident response, audit export, SSO / SCIM, and a named support path.</p></article>
  <article class="feature"><span class="num">03</span><h3>Real migration</h3><p>We help map the first workflows, connect the important tools, and get the team onto the workspace without a six-month program.</p></article>
</div></div></section>
<section class="section"><div class="wrap"><div class="section-head reveal"><div><p class="eyebrow">What you get</p><h2>The boring parts, handled.</h2></div><p class="lede">Enterprise is less about a bigger plan card and more about a defined operating relationship.</p></div>
  <div class="plan-table-wrap reveal"><table class="plan-table"><thead><tr><th>Area</th><th>Enterprise</th></tr></thead><tbody>
    <tr><td>Deployment</td><td>Dedicated or private-cloud Mycelium workspace</td></tr>
    <tr><td>Identity</td><td>SSO, SCIM, role mapping, audit export</td></tr>
    <tr><td>Uptime</td><td>99.95% SLA with service credits</td></tr>
    <tr><td>Support</td><td>Named support path, incident response, architecture review</td></tr>
    <tr><td>Security</td><td>DPA, subprocessor review, security questionnaire support</td></tr>
    <tr><td>Commercial</td><td>Annual agreement, invoicing, procurement support</td></tr>
  </tbody></table></div>
  <p class="note reveal" style="margin-top:18px">Pricing starts at $1,000/month for a dedicated deployment. Final pricing depends on infrastructure, seats, and support scope. We will quote before you commit.</p>
</div></section>
<section class="section"><div class="wrap"><div class="enterprise reveal"><div><p class="eyebrow">Start the conversation</p><h2>Tell us what has to stay up.</h2><p class="lede" style="margin-bottom:20px">Send a sentence about the business, the team size, and the systems that cannot go down. We will reply with a real plan.</p><div class="hero-actions"><a class="btn primary" href="mailto:hello@fpl.dev?subject=Mycelium%20Enterprise">hello@fpl.dev <span class="arrow" aria-hidden="true">→</span></a><a class="btn" href="https://fpl.dev/cloud/contact/">FPL Cloud contact</a></div></div><ul class="enterprise-list"><li>Response within one business day</li><li>Architecture and security review</li><li>Pilot scope before contract</li><li>Procurement and DPA support</li></ul></div></div></section>
''')

page("login.html", "Sign in — Mycelium", "Sign in to a hosted Mycelium workspace with a passkey. Hosted access is opening in phases.", '''
<section class="auth-shell">
  <div class="auth-side">
    <div><p class="eyebrow light">Hosted Mycelium</p><h2>Welcome back to the operating picture.</h2><p>Passkeys are the fast path. Magic links are the recovery path. Your workspace stays yours.</p></div>
    <p class="mono" style="font-size:10px;color:rgba(255,255,255,.42)">MYCELIUM.FPL.DEV / SIGN IN</p>
  </div>
  <div class="auth-main">
    <div class="auth-card">
      <p class="eyebrow">Sign in</p>
      <h1>Open your workspace.</h1>
      <p class="lede">Hosted workspaces are opening in phases. If your workspace is ready, use the passkey link in your invitation.</p>
      <form action="mailto:hello@fpl.dev?subject=Mycelium%20workspace%20access" method="post" enctype="text/plain">
        <div class="field"><label for="login-email">Work email</label><input id="login-email" name="email" type="email" autocomplete="email" placeholder="you@company.com" required></div>
        <div class="auth-actions"><button class="btn primary" type="submit">Request an access link <span class="arrow" aria-hidden="true">→</span></button><a class="btn" href="/download">Self-host instead</a></div>
      </form>
      <div class="passkey-note" style="margin-top:18px"><span aria-hidden="true">✦</span><div><b>Passkey-first.</b> When your workspace is provisioned, sign-in happens on this device. No password to rotate, no shared secret to leak.</div></div>
      <p class="auth-small">Need a new workspace? <a href="/signup">Start here</a>. Trouble signing in? <a href="mailto:hello@fpl.dev">hello@fpl.dev</a>.</p>
    </div>
  </div>
</section>
''')

page("signup.html", "Start free — Mycelium", "Start with the open-source project, or join the hosted early access for a managed Mycelium workspace.", '''
<section class="page-hero"><div class="wrap"><p class="eyebrow">Start free</p><h1>Start with what you have.</h1><p class="lede">The open-source project is ready now. Hosted workspaces are opening in phases, with passkeys and Stripe billing rolling out to the first teams.</p></div></section>
<section class="section" style="padding-top:20px"><div class="wrap page-grid">
  <article class="panel dark"><p class="eyebrow light">Self-hosted</p><h2>Free, forever.</h2><p>Run Mycelium on your laptop or server. Bring your own model keys, your own storage, and your own domain. No license key, no seat count, no phone-home requirement.</p><div class="hero-actions" style="margin-top:18px"><a class="btn primary" href="/download">Install Mycelium</a><a class="btn ghost" href="https://github.com/mycelium-linux/mycelium">View source</a></div></article>
  <article class="panel"><p class="eyebrow">Hosted early access</p><h2>We run the pager.</h2><p>Join the first hosted teams. We will provision your workspace, help connect the important tools, and set up billing when you are ready to keep it.</p>
    <form action="mailto:hello@fpl.dev?subject=Mycelium%20hosted%20early%20access" method="post" enctype="text/plain" style="margin-top:18px">
      <div class="field"><label for="signup-email">Work email</label><input id="signup-email" name="email" type="email" autocomplete="email" placeholder="you@company.com" required></div>
      <div class="field"><label for="signup-company">Company or team</label><input id="signup-company" name="company" type="text" placeholder="Northstar Studio"></div>
      <div class="auth-actions"><button class="btn primary" type="submit">Request early access <span class="arrow" aria-hidden="true">→</span></button></div>
    </form>
    <p class="auth-small">Prefer to talk first? <a href="mailto:hello@fpl.dev?subject=Mycelium">hello@fpl.dev</a>.</p>
  </article>
</div></section>
<section class="section"><div class="wrap"><div class="three reveal">
  <article class="feature"><span class="num">01</span><h3>Passkeys, not passwords</h3><p>Sign in with the device you already trust. Magic links handle recovery and new devices.</p></article>
  <article class="feature"><span class="num">02</span><h3>Stripe when you are ready</h3><p>Start the hosted workspace first. Pick a plan and add payment details when the team is in.</p></article>
  <article class="feature"><span class="num">03</span><h3>Leave with your data</h3><p>Export the workspace and move to self-hosted at any time. Open source means the exit is real.</p></article>
</div></div></section>
''')

page("docs/self-hosting.html", "Self-hosting guide — Mycelium", "Install Mycelium on a laptop or server, connect a model, and run a persistent workspace with TLS, backups, and updates.", '''
<section class="page-hero"><div class="wrap"><p class="eyebrow">Docs / Self-hosting</p><h1>Get a server running.</h1><p class="lede">This is the short path. The full documentation lives in the Mycelium repository. For production, read the server notes before exposing the workspace to the internet.</p></div></section>
<section class="section" style="padding-top:20px"><div class="wrap page-grid">
  <article class="panel" id="laptop"><p class="eyebrow">01 / Laptop</p><h2>Evaluate locally.</h2><p>Use this path to kick the tires. It installs the core binaries, enrolls the host, and prompts for optional pieces.</p><div class="code-block"><span class="c"># macOS or Linux</span><br><span class="g">curl</span> --proto '=https' --tlsv1.2 -fsS \\<br>&nbsp;&nbsp;https://raw.githubusercontent.com/mycelium-linux/mycelium/master/install.sh | bash</div><p>Then run <code class="mono">mycelium doctor</code> and follow the prompts. You can re-run the installer safely.</p></article>
  <article class="panel" id="server"><p class="eyebrow">02 / Server</p><h2>Make it persistent.</h2><p>Use a Linux host with systemd. Put a reverse proxy in front of the Mycelium frontdoor, terminate TLS, and back up the workspace volume and database.</p><ul class="checklist"><li>Ubuntu 24.04 or a current systemd distribution</li><li>4 vCPU, 8 GB RAM, 100 GB SSD</li><li>DNS record pointing at the host</li><li>Caddy, Traefik, or nginx for TLS</li><li>Object storage for larger file workspaces</li></ul></article>
</div></section>
<section class="section"><div class="wrap">
  <div class="section-head reveal"><div><p class="eyebrow">Server checklist</p><h2>Before you invite the team.</h2></div><p class="lede">A workspace that holds the business should be boring to operate: TLS, backups, updates, and a way back in.</p></div>
  <div class="three reveal">
    <article class="feature"><span class="num">01</span><h3>TLS and DNS</h3><p>Point a hostname at the server, terminate TLS at the proxy, and redirect HTTP to HTTPS. Do not expose the daemon socket to the network.</p></article>
    <article class="feature"><span class="num">02</span><h3>Backups</h3><p>Back up the workspace database, object storage, and configuration. Test a restore before you need one.</p></article>
    <article class="feature"><span class="num">03</span><h3>Updates</h3><p>Use the signed release channel and read the changelog. Re-run the installer or follow the package update path.</p></article>
  </div>
  <p class="note reveal" style="margin-top:18px">Need the complete commands, service units, and security notes? Use the repository docs: <a href="https://github.com/mycelium-linux/mycelium/tree/master/docs" style="color:var(--violet-2)">mycelium-linux/mycelium/docs</a>. For managed hosting, see <a href="/pricing" style="color:var(--violet-2)">Pricing</a>.</p>
</div></section>
<section class="section"><div class="wrap"><div class="enterprise reveal"><div><p class="eyebrow">Stuck?</p><h2>We can help.</h2><p class="lede" style="margin-bottom:20px">Self-hosting is free. If you want help with architecture, migration, or a private deployment, talk to us.</p><div class="hero-actions"><a class="btn primary" href="/enterprise">Enterprise support <span class="arrow" aria-hidden="true">→</span></a><a class="btn" href="https://github.com/mycelium-linux/mycelium/issues">Open an issue</a></div></div><ul class="enterprise-list"><li>Install and upgrade review</li><li>Private cloud architecture</li><li>SSO and access model</li><li>Backup and recovery plan</li></ul></div></div></section>
''')

legal_style = 'class="legal"'
privacy_body = f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow">Legal</p><h1>Privacy.</h1><p class="lede">A plain-language summary of what the Mycelium website and hosted service collect, why, and how to get your data out.</p></div></section>
<section class="section"><div class="wrap"><div class="legal">
<h2>What this policy covers</h2><p>This policy covers the Mycelium website at mycelium.fpl.dev and the hosted Mycelium service operated by Future Present Labs LLC. Self-hosted installations are operated by you; your own policies apply.</p>
<h2>What we collect</h2><p>Account details (name, email, organization), authentication events, billing records, support messages, and product usage needed to run the service. We do not train models on customer workspace data.</p>
<h2>What we do not do</h2><p>We do not sell personal data. We do not use workspace content for advertising. We do not claim a certification we have not earned.</p>
<h2>Processors</h2><p>We use infrastructure and payment processors to operate the service, including Cloudflare and Stripe. Enterprise customers can review the current subprocessor list under a DPA.</p>
<h2>Your choices</h2><p>You can request access, correction, export, or deletion by emailing <a href="mailto:privacy@fpl.dev" style="color:var(--violet-2)">privacy@fpl.dev</a>. Hosted workspaces have an export window after cancellation.</p>
<h2>Contact</h2><p>Future Present Labs LLC · privacy@fpl.dev</p>
<p class="note">This is a working draft for the launch site, not a substitute for counsel-reviewed terms. Replace before taking payment.</p>
</div></div></section>
'''
page("legal/privacy.html", "Privacy — Mycelium", "How Mycelium handles account, billing, support, and workspace data.", privacy_body)
terms_body = f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow">Legal</p><h1>Terms.</h1><p class="lede">The rules for using the Mycelium website and hosted service.</p></div></section>
<section class="section"><div class="wrap"><div class="legal">
<h2>Open source</h2><p>The Mycelium core is licensed under MIT OR Apache-2.0. Your use of the source is governed by those licenses, not these terms.</p>
<h2>Hosted service</h2><p>Hosted plans are billed monthly or annually through Stripe. You are responsible for your account, your users, and the actions you authorize agents to take. Do not use the service to violate law or the rights of others.</p>
<h2>Availability</h2><p>Business plans target 99.9% monthly availability. Enterprise plans may include a separate 99.95% SLA. Targets, credits, and exclusions are defined in the applicable order form.</p>
<h2>Cancellation and export</h2><p>You can cancel at any time. Hosted workspaces remain available through the current billing period and for a defined export window afterward. We will delete workspace data on the published schedule unless a legal or security obligation requires retention.</p>
<h2>No warranty</h2><p>The service is provided as-is except where an enterprise agreement says otherwise. You are responsible for reviewing agent actions and maintaining backups of self-hosted installations.</p>
<h2>Contact</h2><p>Future Present Labs LLC · legal@fpl.dev</p>
<p class="note">This is a working draft for the launch site, not a substitute for counsel-reviewed terms. Replace before taking payment.</p>
</div></div></section>
'''
page("legal/terms.html", "Terms — Mycelium", "Terms for the Mycelium website and hosted service.", terms_body)
dpa_body = f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow">Legal</p><h1>Data processing addendum.</h1><p class="lede">For enterprise customers who need a defined data boundary, subprocessor review, and a signed DPA before deployment.</p></div></section>
<section class="section"><div class="wrap"><div class="legal">
<h2>Status</h2><p>The launch site publishes this summary as a placeholder. A counsel-reviewed DPA is available on request for Enterprise customers.</p>
<h2>Scope</h2><p>The DPA will cover the hosted Mycelium service, the categories of personal data processed, the purpose of processing, retention, security measures, subprocessors, and the customer's instructions.</p>
<h2>Data location</h2><p>Hosted workspaces run on FPL Cloud infrastructure. Enterprise customers can request a dedicated deployment and a specific data boundary.</p>
<h2>Subprocessors</h2><p>Current infrastructure and payment providers include Cloudflare and Stripe. The signed DPA will list the current subprocessors and the notice period for changes.</p>
<h2>Request a copy</h2><p>Email <a href="mailto:legal@fpl.dev" style="color:var(--violet-2)">legal@fpl.dev</a> with the subject “Mycelium DPA”.</p>
</div></div></section>
'''
page("legal/dpa.html", "DPA — Mycelium", "Request the Mycelium data processing addendum for enterprise deployments.", dpa_body)

page("404.html", "Not found — Mycelium", "That page is not part of the Mycelium workspace.", '''
<section class="page-hero"><div class="wrap"><p class="eyebrow">404</p><h1>This path has not grown yet.</h1><p class="lede">The page you were looking for is not here. Try the product, the pricing, or the source.</p><div class="hero-actions"><a class="btn primary" href="/">Back to Mycelium</a><a class="btn" href="/download">Self-host</a></div></div></section>
''', canonical="https://mycelium.fpl.dev/404")

# basic text files
(PUBLIC / "robots.txt").write_text("""User-agent: *\nAllow: /\n\nSitemap: https://mycelium.fpl.dev/sitemap.xml\n""")
urls = ["/", "/pricing", "/download", "/integrations", "/security", "/enterprise", "/login", "/signup", "/docs/self-hosting"]
sitemap = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n" + "\n".join(f"  <url><loc>https://mycelium.fpl.dev{u}</loc></url>" for u in urls) + "\n</urlset>\n"
(PUBLIC / "sitemap.xml").write_text(sitemap)
print("rendered pages")
