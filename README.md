# Mycelium website

Public website and hosted-product surface for **Mycelium**, the agent-native
business operating system from Future Present Labs.

Canonical domain: **https://mycelium.fpl.dev/**

## Status

Design phase. The product, brand, information architecture, pricing, auth,
billing, provisioning, and launch plan are written in
[`docs/DESIGN.md`](docs/DESIGN.md). The launch copy deck is in
[`docs/COPY.md`](docs/COPY.md). Research notes and sources are in
[`docs/SOURCES.md`](docs/SOURCES.md).

No production site is deployed yet.

## Intended shape

- Static marketing site: home, pricing, download/self-host, integrations,
  security, enterprise, docs.
- Hosted product entry points: `/login`, `/signup`, `/app`, `/billing`.
- Commerce: Stripe Checkout + Customer Portal for recurring plans.
- Auth: passkey-first customer accounts, FPL SSO for staff, enterprise SSO later.
- Provisioning: hosted Mycelium workspaces on FPL Cloud; self-hosted path stays
  free and first-class.
- Canonical URL: `mycelium.fpl.dev`; redirect the owned aliases to it.

## Deploy target

Cloudflare Workers static assets on the `fpl.dev` zone, with a separate Worker
or route for authenticated product surfaces and Stripe webhooks.

```toml
name = "mycelium-landing"
routes = [{ pattern = "mycelium.fpl.dev/*", zone_name = "fpl.dev" }]

[assets]
directory = "./dist"
not_found_handling = "404-page"
```

Build and deploy commands will be added when the first site implementation
lands.

## Working notes

- Keep the open-source project first. Hosted plans sell uptime, convenience,
  isolation, support, and SLA — not a paywall around the core.
- Do not publish internal infrastructure sourcing or arbitrage details.
- Do not claim certifications, customer counts, or integrations that are not
  actually live.
- `fungos.dev` is a separate product site and should not redirect to Mycelium.
