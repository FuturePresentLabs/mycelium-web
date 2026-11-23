# Mycelium website

Public website and hosted-product surface for **Mycelium**, the agent-native
business operating system from Future Present Labs.

Canonical domain: **https://mycelium.fpl.dev/**
Repository: **https://github.com/FuturePresentLabs/mycelium-web**

## Status

The first marketing site is live. The product, brand, pricing, auth, billing,
provisioning, and launch plan are in [`docs/DESIGN.md`](docs/DESIGN.md).
Hosted signup, passkey auth, Stripe checkout, and provisioning are the next
implementation phase; the current `/login` and `/signup` pages request early
access by email.

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

The Worker name is `mycelium-landing`, and the route is
`mycelium.fpl.dev/*` on the `fpl.dev` zone. Assets are served from `./public`.

```sh
python3 scripts/render-pages.py   # regenerate inner pages from the shared shell
wrangler deploy                   # deploy to Cloudflare Workers
```

Preview: <https://mycelium-landing.ajmwagar.workers.dev>

## Working notes

- Keep the open-source project first. Hosted plans sell uptime, convenience,
  isolation, support, and SLA — not a paywall around the core.
- Do not publish internal infrastructure sourcing or arbitrage details.
- Do not claim certifications, customer counts, or integrations that are not
  actually live.
- `fungos.dev` is a separate product site and should not redirect to Mycelium.
