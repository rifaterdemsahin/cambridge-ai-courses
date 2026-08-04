# Protecting Internal Sales Collateral — Plan (CONF-01)

**Status:** draft plan, not yet executed beyond the "Done now" section below.

## The problem

`business/onboarding.html`, `b2b-outreach.html`, `pricing.html`, `partnerships.html`,
and `enterprise-pitch.html` contain internal-only material: cold outreach
templates, the corporate pricing formula, and institutional/NHS pitch strategy.
The site is a static GitHub Pages deployment — everything in the repo is public
by default, whether or not it's linked from the nav.

## Done now (this pass, zero-cost, static-hosting-compatible)

- Added `<meta name="robots" content="noindex, nofollow">` to all five internal
  documents so they stop appearing in search results.
- Added matching `Disallow` rules to `/robots.txt`.
- Removed the internal hub (`business/index.html`) from the site's primary
  navigation; the public "Business Hub" nav link now points to the new
  sanitized summary at `business/overview.html`, which does not link out to
  the raw documents.

**This is obscurity, not protection.** The files are still publicly fetchable
by direct URL or by cloning the repo. Treat this as step 1, not the fix.

## Real protection — options, ranked

1. **Move the repo to a private GitHub repo + GitHub Pages with access
   control** (requires GitHub Enterprise or a paid plan with Pages visibility
   controls), or serve the whole site from a host that supports it.
2. **Split hosting**: keep the public marketing site on GitHub Pages, move
   `business/*` internal docs into a separate private repo, and share them
   directly (Google Drive, Notion, PDF over email) with prospects instead of
   publishing them as web pages at all. Lowest engineering cost, matches how
   the docs are actually used today (per-prospect sharing, not organic
   discovery).
3. **Migrate to a host with native access control** (Netlify/Vercel password
   protection, Cloudflare Access, or a lightweight serverless auth check) if
   these documents need to stay live HTML pages. Client-side JS password
   gates are not real security (the HTML ships to the browser regardless) —
   don't use one and call it "protected."

## Recommendation

Option 2. These are sales-enablement documents meant for one-to-one prospect
conversations, not organic traffic — they don't need to be web pages at all.
Convert them to PDFs or a shared Drive folder, link them from
`business/overview.html`'s "email us" call-to-action, and delete them from
the public repo once the replacement is in place.

## Next step

Owner decision needed: pick option 2 vs. 3 above, then execute. Not done in
this pass — this file is the plan, not the migration.
