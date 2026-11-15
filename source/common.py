"""Shared design tokens, icons and CSS for the Kuhle Bank HTML sources."""

ICONS = {
    "send": "M7 17L17 7M8 7h9v9",
    "receipt": "M6 3h12v18l-3-2-3 2-3-2-3 2zM9 8h6M9 12h6",
    "phone": "M8 2h8a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2zM11 18h2",
    "cash": "M3 7h18v10H3zM12 14a2 2 0 1 0 0-4a2 2 0 0 0 0 4z",
    "home": "M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z",
    "chart": "M4 20V12M10 20V5M16 20v-9M2 20h20",
    "card": "M2 6h20v12H2zM2 10h20M6 15h4",
    "user": "M12 12a4 4 0 1 0 0-8a4 4 0 0 0 0 8zM4 21a8 8 0 0 1 16 0",
    "eye": "M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12zM12 15a3 3 0 1 0 0-6a3 3 0 0 0 0 6z",
    "bell": "M6 8a6 6 0 1 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10 21h4",
    "search": "M11 18a7 7 0 1 0 0-14a7 7 0 0 0 0 14zM21 21l-4.3-4.3",
    "back": "M15 18l-6-6 6-6",
    "check": "M5 12l5 5 9-10",
    "shield": "M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6zM9 12l2 2 4-4",
    "lock": "M5 11h14v10H5zM8 11V7a4 4 0 0 1 8 0v4",
    "finger": "M12 11v5M8.5 13a3.5 3.5 0 0 1 7 0v3M5 12a7 7 0 0 1 14 0v4M9 20v-2",
    "share": "M4 12v8h16v-8M12 3v13M7 8l5-5 5 5",
    "snow": "M12 2v20M4.9 7l14.2 10M19.1 7L4.9 17",
    "plus": "M12 5v14M5 12h14",
    "users": "M9 11a4 4 0 1 0 0-8a4 4 0 0 0 0 8zM2 21a7 7 0 0 1 14 0M16 3.5a4 4 0 0 1 0 7M22 21a7 7 0 0 0-4-6.3",
    "globe": "M12 22a10 10 0 1 0 0-20a10 10 0 0 0 0 20zM2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20",
    "lite": "M2 9a16 16 0 0 1 20 0M5 12.5a11 11 0 0 1 14 0M8.5 16a6 6 0 0 1 7 0M12 20h.01",
    "bag": "M5 8h14l-1 13H6zM9 8V6a3 3 0 0 1 6 0v2",
    "bus": "M5 4h14v12H5zM5 11h14M7 19v-3M17 19v-3",
    "bolt": "M13 2L4 14h7l-1 8 9-12h-7z",
    "in": "M17 7L7 17M16 17H7V8",
    "x": "M18 6L6 18M6 6l12 12",
    "info": "M12 22a10 10 0 1 0 0-20a10 10 0 0 0 0 20zM12 16v-4M12 8h.01",
    "del": "M21 5H8l-6 7 6 7h13zM12 9l6 6M18 9l-6 6",
    "alert": "M12 3L2 21h20zM12 10v4M12 18h.01",
    "calendar": "M3 5h18v16H3zM3 10h18M8 3v4M16 3v4",
    "wallet": "M3 6h16v14H3zM3 6l13-3v3M15 13h2",
}


def icon(name, size=24, color="currentColor", width=2):
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
        f'stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"><path d="{ICONS[name]}"/></svg>'
    )


TOKENS = {
    "ink": "#17153B",
    "primary": "#4B32D9",
    "primary-700": "#3722B0",
    "primary-50": "#EEEBFF",
    "coral": "#FF6B4A",
    "coral-50": "#FFEDE8",
    "mint": "#0E8A5F",
    "mint-50": "#E1F5EC",
    "gold": "#F5B83D",
    "gold-50": "#FFF4DC",
    "danger": "#C93838",
    "bg": "#F7F6FB",
    "surface": "#FFFFFF",
    "line": "#E6E4EF",
    "muted": "#625F78",
}

BASE_CSS = ":root{" + "".join(f"--{k}:{v};" for k, v in TOKENS.items()) + "}" + """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,system-ui,sans-serif;color:var(--ink);background:#D9D6E8;padding:40px;display:flex;flex-wrap:wrap;gap:60px;align-items:flex-start}
svg{display:block;flex-shrink:0}
"""
