import json, os, re, sys

S = os.path.dirname(os.path.abspath(__file__))
NM = os.path.join(S, "node_modules")

ROLES = ["pin", "list", "chart", "bell", "settings", "search", "clock", "alert", "chev", "nav", "boat"]
SETS = {
    "lucide": dict(
        dir="lucide-static/icons", fill=None,
        names=["map-pin", "list", "chart-column", "bell", "settings", "search", "clock",
               "triangle-alert", "chevron-right", "navigation", "ship"]),
    "phosphor": dict(
        dir="@phosphor-icons/core/assets/regular", fill="@phosphor-icons/core/assets/fill", fill_suffix="-fill",
        names=["map-pin", "list-bullets", "chart-bar", "bell", "gear", "magnifying-glass", "clock",
               "warning", "caret-right", "navigation-arrow", "boat"]),
    "tabler": dict(
        dir="@tabler/icons/icons/outline", fill="@tabler/icons/icons/filled", fill_suffix="",
        names=["map-pin", "list", "chart-bar", "bell", "settings", "search", "clock",
               "alert-triangle", "chevron-right", "navigation", "ship"]),
}


def clean(path):
    t = open(path, encoding="utf-8").read()
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S).strip()
    m = re.match(r"<svg([^>]*)>", t)
    attrs = m.group(1)
    attrs = re.sub(r'\s(width|height|class)="[^"]*"', "", attrs)
    t = '<svg class="ic"' + attrs + ">" + t[m.end():]
    return re.sub(r"\s*\n\s*", "", t)


icons = {}
for key, s in SETS.items():
    icons[key] = {"o": {}, "f": {}}
    for role, name in zip(ROLES, s["names"]):
        icons[key]["o"][role] = clean(os.path.join(NM, s["dir"], name + ".svg"))
        if s["fill"]:
            p = os.path.join(NM, s["fill"], name + s["fill_suffix"] + ".svg")
            if os.path.exists(p):
                icons[key]["f"][role] = clean(p)

NEUTRALS = {
    "cool": (dict(bg="#f2f2f7", surface="#ffffff", sunk="#e6e6ec", text="#0b0b0f", text2="#5c5c66", text3="#8a8a94", line="rgba(60,60,67,.16)"),
             dict(bg="#000000", surface="#1c1c1e", sunk="#2c2c2e", text="#ffffff", text2="#aeaeb8", text3="#7c7c86", line="rgba(255,255,255,.14)")),
    "true": (dict(bg="#f5f5f5", surface="#ffffff", sunk="#e9e9e9", text="#0a0a0a", text2="#5a5a5a", text3="#8a8a8a", line="rgba(0,0,0,.14)"),
             dict(bg="#0a0a0a", surface="#171717", sunk="#262626", text="#fafafa", text2="#a8a8a8", text3="#777777", line="rgba(255,255,255,.14)")),
    "warm": (dict(bg="#f4f3ee", surface="#fdfdfb", sunk="#e8e6df", text="#14130f", text2="#5d5a52", text3="#8c887e", line="rgba(40,35,20,.16)"),
             dict(bg="#0e0e0c", surface="#1b1a17", sunk="#2a2925", text="#fbfaf6", text2="#b3afa4", text3="#7e7a70", line="rgba(255,250,235,.14)")),
}
ACCENTS = {
    "blue": (("#0a6fe8", "#ffffff"), ("#3b94ff", "#ffffff")),
    "green": (("#1b8f45", "#ffffff"), ("#34c759", "#04140a")),
    "indigo": (("#5451d6", "#ffffff"), ("#7d7aff", "#ffffff")),
    "orange": (("#c9570a", "#ffffff"), ("#ff9f0a", "#1a0f00")),
}
THEME = (
    dict(ok="#1b8f45", warn="#a86a00", bad="#cf3a3a", edge="transparent",
         shadow="0 1px 2px rgba(0,0,0,.06), 0 10px 28px rgba(0,0,0,.08)", water="#bcd7f2", park="#cfe6cf"),
    dict(ok="#34c759", warn="#f0b429", bad="#ff6b63", edge="rgba(255,255,255,.10)",
         shadow="0 1px 2px rgba(0,0,0,.5), 0 12px 32px rgba(0,0,0,.55)", water="#152a40", park="#17281b"),
)


def tokens(i):
    out = []
    for n, pair in NEUTRALS.items():
        for k, v in pair[i].items():
            out.append(f"--{n}-{k}:{v}")
    for a, pair in ACCENTS.items():
        out.append(f"--{a}:{pair[i][0]}")
        out.append(f"--on-{a}:{pair[i][1]}")
    for k, v in THEME[i].items():
        out.append(f"--{k}:{v}")
    return ";".join(out)


light, dark = tokens(0), tokens(1)
variants = []
for n, pair in NEUTRALS.items():
    variants.append(f'body[data-neutral="{n}"]{{' + ";".join(f"--{k}:var(--{n}-{k})" for k in pair[0]) + "}")
for a in ACCENTS:
    variants.append(f'body[data-accent="{a}"]{{--accent:var(--{a});--on-accent:var(--on-{a})}}')

tpl = open(os.path.join(S, "template.html"), encoding="utf-8").read()
html = (tpl.replace("/*LIGHT*/", light).replace("/*DARK*/", dark)
        .replace("/*VARIANTS*/", "\n".join(variants))
        .replace("/*ICONS*/", json.dumps(icons, separators=(",", ":"))))
out = os.path.join(S, "index.html")
open(out, "w", encoding="utf-8").write(html)
print(out, len(html), {k: (len(v["o"]), len(v["f"])) for k, v in icons.items()})
