# Brand rules

These rules apply to every app that uses brand-kit. Follow them exactly so that
any two apps look like the same product. Values come from `tokens.css`;
ready-made classes come from `components.css`; `reference.html` shows all of it
on one page.

Status: version 1.1.1, 2026-11-22 (version 1 confirmed the same day). Round corners, glass floating layers,
cool neutrals and a deep blue accent.

## 1. Ground rules

1. Never write a raw colour, font size, radius, shadow or spacing value in app
   code. Use a `--bk-*` token. If a token is missing, add it to brand-kit first.
2. Light and dark both ship, always. The theme follows the system setting.
   An app may offer a manual switch by setting `data-theme="light"` or
   `data-theme="dark"` on `<html>`; with no attribute the system decides.
3. One accent colour. Blue marks what is interactive or selected. Do not use it
   for decoration, and do not add a second brand colour.
4. Status is never shown by colour alone. Every status has an icon and a label.
5. App-specific colours (chart series, map layers) live in the app, are named
   for what they mean, and must be defined for both themes.

## 2. Type

Font: SF on Apple devices, Inter everywhere else. Apple does not license SF as
a web font, so Inter is the fallback. Load Inter at weights 400, 500, 600, 700.

    font-family: var(--bk-font);

| Role | Token | Size / weight | Use |
|---|---|---|---|
| Large | `--bk-type-large` | 34 / 700 | The page title. Exactly one per page. |
| Title 1 | `--bk-type-title-1` | 28 / 700 | Section titles. |
| Title 2 | `--bk-type-title-2` | 22 / 700 | Card and sheet titles. |
| Headline | `--bk-type-headline` | 17 / 600 | Row titles, emphasis. |
| Body | `--bk-type-body` | 15 / 400 | Default text. |
| Caption | `--bk-type-caption` | 13 / 400 | Secondary lines, labels, table headers. |
| Micro | `--bk-type-micro` | 11 / 500 | Tab bar labels only. |

- Apply with the `font` shorthand: `font: var(--bk-type-title-1)`.
- Large takes `letter-spacing: var(--bk-track-large)`; titles take `--bk-track-title`.
- Sentence case everywhere. No all-caps labels.
- Weights are 400, 500, 600 and 700 only.
- Numbers that line up or change in place use `font-variant-numeric: tabular-nums`.
- Running text is at most `--bk-width-prose` wide.
- Text colours: `--bk-text` for content, `--bk-text-2` for secondary,
  `--bk-text-3` for placeholders and chevrons.

## 3. Space

A 4px grid: `--bk-space-1` to `--bk-space-8` are 4, 8, 12, 16, 24, 32, 48, 64.

| Where | Step |
|---|---|
| Icon to its label | 6px inside controls, otherwise space-2 |
| Between related controls | space-2 |
| Between cards in a grid | space-3 |
| Inside a card | space-4 |
| Section title to its content | space-3 |
| Between columns | space-5 |
| Between page sections | space-6 |
| Page side gutter | space-4 minimum |

Lay out with flex or grid and `gap`. Do not space siblings with margins.
Page content is at most `--bk-width-page` (1120px) wide and centred.

## 4. Shape and surfaces

| Token | Value | Use |
|---|---|---|
| `--bk-radius-card` | 22px | Cards, sheets, panels, maps |
| `--bk-radius-inner` | 14px | Anything nested inside a card; multi-line fields |
| `--bk-radius-tile` | 8px | Small icon tiles |
| `--bk-radius-control` | pill | Buttons, pills, single-line fields, segmented controls |

Three surface levels, and nothing else:

1. **Page**: `--bk-bg`. No border.
2. **Card**: `--bk-surface` with a 1px `--bk-line` border. No shadow.
3. **Floating layer**: glass (`.bk-float`): `--bk-glass` background,
   `--bk-glass-blur` backdrop filter, 1px line, `--bk-shadow-float`. Popovers,
   tooltips and dialogs sit over text, so they use the denser
   `--bk-glass-strong`; `--bk-glass` is for layers over maps and media.

Glass is only for things that sit on top of other content: the navbar, sheets
and search bars over a map, popovers, toasts. A card in the normal page flow is
never glass and never has a shadow. Do not nest a card inside a card; use a
grouped list or `--bk-sunk` for an inset area.

## 5. Icons

Lucide, and only Lucide (`lucide-react` in React apps). Do not mix in another
set or hand-draw icons that Lucide already has.

| Size | Token | Use |
|---|---|---|
| 16px | `--bk-icon-sm` | Inside buttons, labels, nav links, tile labels |
| 20px | `--bk-icon` | Default; list rows |
| 24px | `--bk-icon-lg` | Tab bars, empty states |

Two components set their own icon size, and the classes do it for you: a
status pill draws its icon at 14px with a 2.25 stroke (12px in the small pill)
so it reads at caption size, and a row's icon tile draws it at 17px.

- Stroke width is `--bk-icon-stroke` (1.75) at every size, except in pills.
- Selected state: accent colour plus `--bk-icon-stroke-active` (2.25). Lucide
  has no filled icons, so do not fake a fill.
- Icons inherit `currentColor`. An icon next to text matches the text colour.
- An icon-only button needs an `aria-label`.
- One meaning per icon across all apps:

| Meaning | Lucide name |
|---|---|
| Location, map | `map-pin` |
| List | `list` |
| Charts, trends | `chart-column` |
| Notifications | `bell` |
| Settings | `settings` |
| Search | `search` |
| Time | `clock` |
| Go to detail | `chevron-right` |
| Status ok | `circle-check` |
| Status warning | `triangle-alert` |
| Status bad | `octagon-alert` |
| Status unknown | `circle-help` |
| Status info | `info` |
| Close, clear | `x` |
| Menu | `menu` |
| Opens another site | `external-link` |
| Sort | `arrow-up`, `arrow-down`, `arrow-up-down` |
| Expand, open a menu | `chevron-down` |
| Back | `arrow-left` |
| Forward, "see more" link | `arrow-right` |
| Play, pause | `play`, `pause` |
| Download | `download` |
| Reset the view, home | `house` |
| Map layers | `layers` |
| Airport, airplane | `plane` |
| Helicopter | `helicopter` |

Lucide has no heliport sign (an H in a circle). An app that needs one keeps
the letter H in kit type inside a `.bk-marker`, and says so in its own notes.

## 6. Components

Use the `bk-` classes from `components.css`, or rebuild the same thing from
tokens in the app's own component system. Either way the result must match
`reference.html`.

**Page header** (`.bk-header`): optional eyebrow in accent, the Large title, one
body-size line of description in `--bk-text-2`. Page-level controls such as a
time range sit on the right and wrap below on narrow screens.

**Navbar** (`.bk-navbar`): 56px, glass, sticky at the top. Brand mark and name
on the left, links next, utility buttons on the right. The current link is a
tinted pill with `aria-current="page"`.

**Buttons** (`.bk-btn`): heights 32, 40 (default), 48. Pill shaped, 600 weight.

| Variant | Use |
|---|---|
| `--primary` | The one main action in a view. At most one per view. |
| `--tinted` | Secondary actions. |
| `--plain` | Neutral actions such as Cancel. |
| `--danger` | Destructive actions. |
| `--icon` | Icon-only, square footprint, needs `aria-label`. |

Labels are verbs in sentence case: "Save alerts", not "Submit".

**Status pill** (`.bk-pill`): 26px, icon plus label, set with
`data-status="ok | warn | bad | info"`; no attribute means unknown.

**Card** (`.bk-card`) and **stat tile** (`.bk-tile`): a tile is a caption label
with a 16px icon, a Title 1 value in tabular numbers with the unit in a
smaller secondary style, and an optional one-line note.

**Grouped list** (`.bk-group` with `.bk-row`): rows are at least 48px tall.
Separators are inset to start at the text, not the icon. A row that navigates
ends with `chevron-right`; a row that toggles ends with a switch. Put a caption
label above the group, indented by space-4.

**Segmented control** (`.bk-seg`): for 2 to 4 mutually exclusive views of the
same content. Buttons are 32px tall. A choice that changes the view in place
is a `<button>` with `aria-pressed`; one that goes to another URL (a time
range kept in the address) is an `<a>` with `aria-current="true"`.

**Tabs** (`.bk-tabs`): for more than 4 views. A row of `role="tab"` items in a
`role="tablist"` that scrolls sideways on its own; the current one has
`aria-selected="true"` and the tinted pill.

**Switch** (`.bk-switch`): a checkbox. On is green (`--bk-ok`), not blue: a
switch shows a state, and blue is kept for what is selected or can be pressed.

**Field** (`.bk-field`): 40px, pill shaped, optional leading 16px icon. The
label sits above it in caption size, 600 weight. `.bk-field--sm` is 32px, for
filters in dense tools. A **select** is a `.bk-field.bk-select` holding the
`<select>` and a trailing `chevron-down`. A **textarea** (`.bk-textarea`) uses
the inner radius.

**Table** (`.bk-table`): inside a card, inside `.bk-table-wrap` so it scrolls
sideways on its own. Headers in caption size; numbers right-aligned and tabular.
`.bk-pill--sm` (22px) is the pill for table cells.

**Link** (`.bk-link`): an inline link in the accent, with an optional trailing
16px icon such as `arrow-right`. `.bk-btn--link` is the same look for a
`<button>`.

**Inset** (`.bk-inset`): a sunk area at the inner radius, for a note or a
nested block inside a card.

**Empty and error states** (`.bk-empty`): a 24px icon, a Headline line, one
caption line, and at most one small tinted button.

**Skeleton** (`.bk-skeleton`): a still sunk block where content will appear.
It does not pulse; nothing loops.

**Legend** (`.bk-legend` with `.bk-legend-item` and `.bk-swatch`): the key for
a chart or a map layer. Set a swatch's color with `--bk-swatch`; `--dot` and
`--line` change its shape. The colors are the app's own (rule 5).

**Map** (`.bk-map`): the frame for any map. Markers are `.bk-marker` (34px,
accent fill, a surface halo), `.bk-marker--quiet` for the unselected, and
`.bk-marker--sm` (24px). Everything that sits on the map is a floating layer:
`.bk-map-control` for a button, `.bk-float.bk-map-search` for the search pill,
`.bk-float.bk-map-sheet` for a list docked at the bottom, `.bk-float.bk-chip`
for a one-row note.

**Popover, tooltip, dialog, sheet** (`.bk-popover`, `.bk-tooltip`,
`.bk-dialog` inside `.bk-scrim`, `.bk-sheet`): all glass. A dialog becomes a
bottom sheet at phone width. A dialog has one primary button.

## 7. Motion and accessibility

- Transitions use `--bk-ease` with `--bk-dur-fast` (120ms) for presses and
  `--bk-dur` (200ms) for state changes. Nothing bounces or loops.
- Honour `prefers-reduced-motion`. `components.css` does this for every
  element on the page, not only kit classes; it also draws the focus ring on
  every focusable element. Both are meant to be global.
- Text contrast is at least 4.5:1 in both themes. White text goes on
  `--bk-accent-fill`, never on `--bk-accent`.
- Every interactive element has a visible `:focus-visible` ring (2px accent,
  2px offset) and a hit area of at least 32px, 40px for primary actions.
- Layouts work at 400px wide with no sideways page scroll.

## 8. Landing pages

App screens stay calm: no scroll effects, ever. A landing or marketing page may
add the motion layer (`motion.css` and `motion.js`), shown in `landing.html`.
It uses the same tokens, components, font and icons; the only additions are
two larger type roles and scroll-driven movement.

| Role | Token | Use |
|---|---|---|
| Display | `--bk-type-display` | The hero line and the closing line. At most two per page. |
| Statement | `--bk-type-statement` | One large paragraph that carries the pitch. |

How it works: any element with `data-bk-progress` gets a CSS variable `--p`
that runs from 0 to 1 as the page scrolls past it. Effects are CSS built on
that number.

| Effect | Markup | Use |
|---|---|---|
| Expanding stage | `.bk-stage` > `.bk-stage-pin` > `.bk-stage-copy` + `.bk-expand` | The hero. Media grows from a rounded card to the full screen. One per page. |
| Word fill | `data-bk-words` inside a `data-bk-progress` section | The statement paragraph. |
| Pinned steps | `.bk-steps` with `.bk-steps-visual` and `.bk-step` | Explaining 2 to 4 steps beside a visual that changes. |
| Reveal | `data-bk-reveal`, optional `--bk-stagger` | Cards and headings rising in once. |
| Count up | `data-bk-count="1212"` | Headline numbers. |
| Marquee | `.bk-marquee` | One band of large words that slides with the scroll. |
| Finale | `.bk-finale` | The closing call to action. |

Rules:

- One pinned moment per screenful; never pin two things at once.
- Everything on the first screen is visible on load. Nothing waits hidden for a scroll.
- With reduced motion or no script the page is static and complete. Do not put
  content where only the animation reveals it. Pinned steps then show every
  visual: beside its step on wide screens, above the steps on narrow ones.
- The word fill keeps the sentence readable by screen readers: the full text
  once in a `.bk-sr-only` span, the animated words `aria-hidden`.
- Movement follows the scroll or eases once with `--bk-ease`. No looping
  animation, no autoplay carousels, no cursor effects.

## 9. Using the kit in an app

1. Add brand-kit as a dependency and import `tokens.css` (and
   `components.css` if the app uses the classes) before the app's own styles.
   In a Tailwind v4 app import the classes into a layer,
   `@import "brand-kit/components.css" layer(components);`, or they will
   override every utility on the same element.
2. Landing pages also load `motion.css` and `motion.js`.
3. Tailwind v4 apps also import `tailwind.css`, which maps the tokens to
   utilities such as `bg-surface`, `text-text-2` and `rounded-card`, the type
   roles (`text-large` to `text-micro`), `shadow-float` and `glass`.
4. `motion.js` is for plain pages. A React or other component app rebuilds it
   as components that render the same markup and set the same variables
   (`--p`, `--n`, `--i`), and reuses `motion.css` unchanged; it puts
   `bk-motion` on the landing page's own root, not on `<html>`.
5. Point the app's `CLAUDE.md` or `AGENTS.md` at this file so coding agents
   follow it.
