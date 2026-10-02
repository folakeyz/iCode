# iCode Solutions

Responsive static website using HTML and CSS, with a shared visual system and a dedicated TrekPulse privacy policy.

## Preview

Run `python3 -m http.server 8080` from this directory, then open `http://localhost:8080`. No build step or JavaScript dependencies are needed.

## Design

Warm neutral backgrounds, dark green sections, lime accents, fluid typography, accessible focus states, a native mobile menu, reduced-motion support and printable legal content. All fonts use local system fallbacks; the artwork is CSS.

Contact and project actions open an email draft. They do not submit to a backend. Portfolio entries are capability examples; careers accepts expressions of interest rather than advertising unverified vacancies.

## Privacy publication

`privacy.html` is intended to be served at https://icode-site.netlify.app/privacy using Netlify's clean HTML URLs. The policy identifies TrekPulse and folaranmi, describes local health access and server-synced activity, and links to account deletion.

Read [the privacy publication review](docs/trekpulse-privacy-review.md) before resubmission. Website wording does not resolve app permissions, consent, SDK behavior or Play Console declarations. Changes in this repository are not deployed automatically by this editing session.

## Check

Run `python3 scripts/check_site.py` for local link, anchor and document structure checks.
