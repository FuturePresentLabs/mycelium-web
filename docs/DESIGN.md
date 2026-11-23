# Mycelium website — product and launch design

Status: **v0.1 deployed marketing site**

Canonical: **https://mycelium.fpl.dev/**

Repo: **https://github.com/FuturePresentLabs/mycelium-web**

Reference model: **Rakazo** (`https://rakazo.com/`) — open-source agent workspace, free self-hosting, hosted tiers. The brief said “Ricaso”; Rakazo is the closest credible match.

## 1. Positioning

Mycelium is the **agent-native business operating system**: an open-source core, a hosted workspace, and a team of agents that connect the tools a business already uses, build the views it needs, and change those views in conversation.

It is not another chat app, a no-code builder, or a dashboard with an assistant bolted on. The product is the **living operating picture**: agents, shared apps, files, approvals, memory, and the context that connects them.

### Message hierarchy

1. **Open source first.** MIT OR Apache-2.0. Self-host without a license key.
2. **Agent-native, not agent-themed.** Agents have jobs, memory, permissions, and approval gates.
3. **Bring your stack.** Gmail, Slack, Drive, Notion, GitHub, Stripe, CRM, databases, and any MCP server.
4. **Own your data.** Export it, self-host it, or run it with us.
5. **Convenience is the paid product.** Hosted plans sell uptime, isolation, shared computers, support, and SLA.

### Copy guardrails

- Evoke “no build, no deploy, no release ceremony” through outcomes: *the workspace changes in conversation*.
- Do not publish internal sourcing, GPU arbitrage, or infrastructure-supply details.
- Do not claim certifications, customer counts, or live integrations that do not exist.
- Do not say “autonomous business.” Say agents act with approvals and scoped access.
- Keep the open-source core genuinely free. Hosted is a convenience layer.

## 2. Audience

| Audience | Job to be done | What convinces them |
|---|---|---|
| Operator-led teams (5–50) | Replace tool sprawl with one operating surface | Time-to-first-workspace, integrations, approvals |
| Technical founders | Make internal tools without a platform team | Open source, MCP, export, self-host |
| Agencies / studios | Reuse a workspace per client | Teams, isolation, shared computers |
| Enterprise | Keep uptime and data boundary | Private deployment, SSO, SLA, DPA |
| Self-hosters | Own the whole stack | Install path, docs, no license key |

## 3. Information architecture

Deployed pages:

- `/` — hero, product mock, workflow, agents, open-source band, pricing preview, enterprise, FAQ.
- `/pricing` — monthly/annual toggle, three hosted plans, comparison table, billing explainer, FAQ.
- `/download` — one-command install, requirements, laptop/server/fungOS paths.
- `/integrations` — representative catalog, MCP, Composio, request-an-integration.
- `/security` — open source, data, access, hosting, honest claims, disclosure.
- `/enterprise` — private deployment, SLA, migration, procurement.
- `/login` — hosted access request / passkey-first placeholder.
- `/signup` — self-host vs hosted early access.
- `/docs/self-hosting` — quickstart and server checklist.
- `/legal/{privacy,terms,dpa}` — working drafts, not counsel-reviewed.

Clean URLs are used everywhere. Cloudflare Workers static assets redirects `.html` to the clean path.

## 4. Visual system

- **Palette:** warm off-white paper, near-black ink, electric violet `#6a45ff`, deep violet `#24124e`, lime `#c9f36b` for live/approval states.
- **Type:** editorial serif display (Iowan/Palatino/Georgia fallback), Helvetica Neue body, mono for labels and data.
- **Shape:** large serif headlines, thin rules, 18–24px radii, one dark product stage, no rainbow gradients or generic 3D orbs.
- **Product evidence:** a hand-built workspace mock with agent cards, a live app, and a prompt bar. Real product UI, not an abstract illustration.
- **Motion:** marquee, blinking cursor, subtle hover. Respect `prefers-reduced-motion`; content is visible without JavaScript.

### FPL integration

- Header lockup: “Mycelium” + “A Future Present Labs product”.
- Footer links to FPL, FPL Cloud, mission, and contact.
- Shared restraint: warm neutrals, thin rules, real type. Mycelium adds violet, not a separate universe.
- Enterprise leads can route to FPL Cloud contact.
- Update `fpl.dev` project links from GitHub to `mycelium.fpl.dev` once the site is stable.

## 5. Pricing

The site launched with **$15 / $49 / $99**, not $15/$50/$100. The extra dollar buys psychological room and matches the Rakazo model.

| Plan | Monthly | Annual | Humans | Agents | Hosted computers | Storage |
|---|---:|---:|---:|---:|---:|---:|
| Self-hosted | $0 | — | Your hardware | Your hardware | Your hardware | Your storage |
| Starter | $15 | $150 | 1 | 3 | 1 | 10 GB |
| Team | $49 | $490 | 5 | 15 | 3 | 50 GB |
| Business | $99 | $990 | 15 | 50 | 10 | 200 GB |
| Enterprise | from $1,000 | custom | custom | custom | dedicated | custom |

Add-ons: extra human, extra agent, extra hosted computer, storage, model credits. Annual = two months free. Seven-day trial. No setup fee.

### Research anchors

- **Rakazo:** free self-hosted; $15/$49/$99/$199 hosted; credits from $20; managed dedicated $300/mo.
- **Agenta:** Starter $29/mo, Business $299/mo, unlimited team members, credit top-ups.
- **Dify:** Professional from $590/yr, Team from $1,590/yr.
- **Lindy:** from $49.99 per active user/mo with 5,000 credits.
- **FPL support:** Basic $25/mo, Pro $250/mo, Enterprise from $2,500/mo; compute usage-based.

The approved plan is deliberately at the low end of hosted agent platforms. Hosting, support, and SLA carry the margin; the open-source core carries trust. If model credits are sold, keep the rate card transparent and avoid surprise overages.

## 6. Auth, billing, provisioning

### Auth recommendation

- **Customer auth:** Better Auth on Cloudflare Workers + D1/Postgres, using the passkey, organization, and Stripe plugins. Open source, self-hostable, passkey-first, and aligned with the product story.
- **Staff/admin:** Federate FPL SSO (`sso.fpl.dev`) as an OIDC provider. FPL Auth already supports passkeys, magic links, roles, and OIDC; it is currently internal-domain-oriented, so do not use it as the customer signup system yet.
- **Enterprise:** SSO/SCIM later through Better Auth SSO or WorkOS. Do not build SAML in-house for launch.
- **Fallback:** Clerk if speed matters more than ownership. It is excellent, but closed source and per-MAU; it weakens the “own your data” story.

### Customer flow

1. Email → passkey enrollment → organization name.
2. Choose plan → Stripe Checkout (tax, annual/monthly, promotion codes).
3. Webhook provisions workspace and sends the launch link.
4. Customer Portal handles payment method, invoices, upgrades, cancellation.
5. Export window on cancellation; deletion on a published schedule.

### Stripe objects

Products/Prices for Starter, Team, Business, Enterprise deposit. Use Checkout Sessions for signup, Customer Portal for changes, webhooks for entitlement sync. Idempotency table for events. Test clocks and test cards before live mode.

### Hosted provisioning

MVP: concierge/manual provisioning while the checkout flow is proven. Phase 2: a control-plane Worker + queue creates a single-tenant FPL Cloud microVM, attaches persistent storage, installs a signed Mycelium release, configures the organization, and health-checks before emailing the customer.

Isolation: shared managed runtime for Starter, dedicated microVM for Business/Scale, private deployment for Enterprise. Publish the boundary honestly.

## 7. Deployment and domains

- Cloudflare Worker `mycelium-landing`, route `mycelium.fpl.dev/*`, assets `./public`.
- Preview: `https://mycelium-landing.ajmwagar.workers.dev`.
- `myceliumos.dev`, `www.myceliumos.dev`, `mycos.dev`, `www.mycos.dev` should 301 to `https://mycelium.fpl.dev` with path/query preserved.
- Keep `fungos.dev` separate; it is the fungOS product site.
- The alias zones are currently misconfigured (Namecheap parking / 525). Fix proxied DNS or attach Worker custom domains before turning on redirects.

## 8. Launch sequence

1. **Now:** marketing site deployed. CTAs request hosted access by email; self-host path is live.
2. **Next:** Better Auth + passkey signup + Stripe Checkout in test mode; manual provisioning for first design partners.
3. **Then:** automated provisioning, billing portal, team invitations, usage metering.
4. **Later:** enterprise SSO/SCIM, SLA reporting, trust center, SOC 2 readiness.

## 9. Open decisions

- Canonical domain: `mycelium.fpl.dev` vs an independent `mycos.dev`/`myceliumos.dev`.
- Auth vendor final: Better Auth vs extending FPL Auth for customers.
- Hosted runtime: shared tenant vs dedicated microVM per plan.
- Model credits: pass-through pricing vs small platform fee.
- Whether `myceliumos.dev`/`mycos.dev` redirect or become product aliases.
- Public launch date and design-partner pricing.

## 10. Sources

- Rakazo: https://rakazo.com/ and https://rakazo.com/pricing/
- Agenta pricing: https://agenta.ai/pricing
- Dify pricing: https://dify.ai/pricing
- Lindy pricing: https://www.lindy.ai/pricing
- FPL pricing: https://fpl.dev/pricing/
- FPL Auth: https://sso.fpl.dev/ and https://github.com/FuturePresentLabs/fpl-auth
- Composio catalog: https://composio.dev/toolkits
- Mycelium source: https://github.com/mycelium-linux/mycelium
