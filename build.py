#!/usr/bin/env python3
"""Builds index.html for the Linacre OSINT HUD (v2) from osint_grouped.json."""
import json

grouped = json.load(open('osint_grouped.json'))

# ---------------------------------------------------------------- prime cards
PRIME = [
    ("Shodan", "shodan.io", "https://shodan.io", "INFRA",
     "Search engine for internet-connected devices — banners, open ports, webcams, ICS."),
    ("Have I Been Pwned", "haveibeenpwned.com", "https://haveibeenpwned.com/", "BREACH",
     "Check email & phone exposure across hundreds of known data breaches."),
    ("Intelligence X", "intelx.io", "https://intelx.io/", "BREACH",
     "Search Tor, I2P, data-leak collections and the darknet by any selector."),
    ("OSINT Framework", "osintframework.com", "https://osintframework.com/", "FRAMEWORK",
     "The canonical tree-map of OSINT resources, organised by collection type."),
    ("Bellingcat Toolkit", "docs.google.com", "https://docs.google.com/spreadsheets/d/18rtqh8EG2q1xBo2cLNyhIDuK9jrPGwYr9DI2UncoqJQ/edit", "FRAMEWORK",
     "Bellingcat's own maintained spreadsheet of proven investigation tools."),
    ("IntelTechniques OSINT", "inteltechniques.com", "https://inteltechniques.com/tools/", "MULTI",
     "Michael Bazzell's interactive multi-input search workstation."),
    ("Sherlock", "github.com", "https://github.com/sherlock-project/sherlock", "USERNAME",
     "Hunt down usernames across 400+ social networks from the command line."),
    ("Epieos", "epieos.com", "https://epieos.com/", "EMAIL",
     "Reverse email lookup revealing linked accounts and public profiles."),
    ("Facecheck.id", "facecheck.id", "https://facecheck.id/", "FACE",
     "Face-recognition search across the public web by photo upload."),
    ("Wayback Machine", "web.archive.org", "https://web.archive.org/", "ARCHIVE",
     "Time-travel the web — over 800 billion pages archived since 1996."),
    ("CyberChef", "gchq.github.io", "https://gchq.github.io/CyberChef/", "CRYPTO",
     "GCHQ's cyber Swiss-army knife: encode, decode, compress, analyse."),
    ("VirusTotal", "virustotal.com", "https://www.virustotal.com/gui/", "MALWARE",
     "Scan files, URLs, domains and hashes with 70+ antivirus engines at once."),
]

# ------------------------------------------------------- starred (in-panel ★)
STARRED = {
    "https://www.greynoise.io/viz/", "https://urlscan.io/", "https://crt.sh/",
    "https://dnsdumpster.com/", "https://pypi.org/project/holehe/",
    "https://github.com/mxrch/GHunt", "https://pypi.org/project/maigret/",
    "https://whatsmyname.app/", "https://demo.phoneinfoga.crvx.fr",
    "https://cse.google.com/cse?cx=c46b76bce1848d976", "https://www.192.com/",
    "https://pimeyes.com/en/", "https://tineye.com/", "https://fotoforensics.com/",
    "https://archive.is/", "https://app.any.run/", "https://globe.adsbexchange.com/",
    "https://www.flightradar24.com/", "https://www.marinetraffic.com/",
    "https://opencorporates.com/", "https://www.gov.uk/government/organisations/companies-house",
    "https://wigle.net/", "https://www.broadcastify.com/listen/", "https://ahmia.fi/",
    "https://cybermap.kaspersky.com/", "http://radio.garden/search",
    "https://www.exploit-db.com/google-hacking-database",
}

# --------------------------------------- community feeds (from the RSS widget)
COMMUNITY = {
    "name": "COMMUNITY & FEEDS", "id": "community",
    "cats": [{
        "cat": "OSINT COMMUNITIES",
        "links": [
            {"t": "OSINT Multifeed — live", "u": "https://www.reddit.com/r/OSINT+PrivateInvestigators+TraceAnObject+opsec/new/?feed=home", "h": "reddit.com"},
            {"t": "r/OSINT", "u": "https://www.reddit.com/r/OSINT/", "h": "reddit.com"},
            {"t": "r/TraceAnObject", "u": "https://www.reddit.com/r/TraceAnObject/", "h": "reddit.com"},
            {"t": "r/PrivateInvestigators", "u": "https://www.reddit.com/r/PrivateInvestigators/", "h": "reddit.com"},
            {"t": "r/opsec", "u": "https://www.reddit.com/r/opsec/", "h": "reddit.com"},
            {"t": "r/PrivacySecurityOSINT", "u": "https://www.reddit.com/r/PrivacySecurityOSINT/", "h": "reddit.com"},
        ]
    }]
}

# insert community group after SOCIAL NETWORKS
for i, g in enumerate(grouped):
    if g['id'] == 'social':
        grouped.insert(i + 1, COMMUNITY)
        break

# --------------------------------------- world clock zones (from the widget)
ZONES = [
    ("LAX", "America/Los_Angeles"), ("HOU", "America/Chicago"),
    ("NYC", "America/New_York"), ("LON", "Europe/London"),
    ("BER", "Europe/Berlin"), ("CAI", "Africa/Cairo"),
    ("THR", "Asia/Tehran"), ("DEL", "Asia/Kolkata"),
    ("HKG", "Asia/Hong_Kong"), ("TYO", "Asia/Tokyo"),
    ("SYD", "Australia/Sydney"),
]

payload = {"groups": grouped, "prime": PRIME, "starred": sorted(STARRED), "zones": ZONES}
DATA_JS = json.dumps(payload, separators=(',', ':'))

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Linacre OSINT HUD — __NF__ investigation tools, one dark glass console</title>
<meta name="description" content="A dark glass heads-up display curating __NF__ OSINT tools from the OSINT4ALL collection — people, breach data, infra, geo, social & records intel. Part of linacre.site.">
<meta name="theme-color" content="#05070c">
<meta property="og:type" content="website">
<meta property="og:title" content="Linacre OSINT HUD">
<meta property="og:description" content="__NF__ curated OSINT tools in one dark glass console — part of linacre.site.">
<meta property="og:image" content="__OGIMG__">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='13' fill='none' stroke='%2322d3ee' stroke-width='2'/%3E%3Ccircle cx='16' cy='16' r='6' fill='none' stroke='%2322d3ee' stroke-width='1.5' opacity='.6'/%3E%3Cpath d='M16 16 L27 8' stroke='%2334d399' stroke-width='2.5' stroke-linecap='round'/%3E%3Ccircle cx='16' cy='16' r='2' fill='%2322d3ee'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://www.google.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
/* ============ CSS4 / modern feature layer ============ */
@property --ang{syntax:'<angle>';initial-value:0deg;inherits:false}
@property --mx{syntax:'<percentage>';initial-value:50%;inherits:false}
@property --my{syntax:'<percentage>';initial-value:50%;inherits:false}

:root{
  --bg:oklch(12% .015 250); --bg2:oklch(17% .02 250);
  --a1:#22d3ee; --a2:#34d399;                    /* active accents */
  --gold:#fbbf24; --violet:#a78bfa;
  --glass:color-mix(in srgb,#94a3b8 5.5%,transparent);
  --glass2:color-mix(in srgb,#94a3b8 9%,transparent);
  --line:color-mix(in srgb,var(--a1) 13%,transparent);
  --line2:color-mix(in srgb,var(--a1) 26%,transparent);
  --txt:#e2e8f0; --sub:#8b98ac; --dim:#5b6779;
  --r:18px; --ease:cubic-bezier(.2,.7,.3,1);
  --glow:0 0 32px color-mix(in srgb,var(--a1) 10%,transparent),0 24px 60px rgb(0 0 0/.45);
  scrollbar-color:color-mix(in srgb,var(--a1) 45%,#070b12) #070b12;
}
body[data-acc="violet"]{--a1:#a78bfa;--a2:#60a5fa}
body[data-acc="amber"]{--a1:#fbbf24;--a2:#fb923c}
body[data-acc="rose"]{--a1:#fb7185;--a2:#f472b6}

*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth;scrollbar-gutter:stable}
body{
  background:var(--bg);color:var(--txt);
  font-family:'Inter',system-ui,sans-serif;
  min-height:100vh;overflow-x:hidden;
  -webkit-font-smoothing:antialiased;
  accent-color:var(--a1);
  transition:background .5s;
}
::selection{background:color-mix(in srgb,var(--a1) 30%,transparent);color:#fff}
::-webkit-scrollbar{width:10px;height:10px}
::-webkit-scrollbar-track{background:#070b12}
::-webkit-scrollbar-thumb{background:linear-gradient(color-mix(in srgb,var(--a1) 55%,#0b1220),color-mix(in srgb,var(--a2) 55%,#0b1220));border-radius:8px;border:2px solid #070b12}
:focus-visible{outline:2px solid color-mix(in srgb,var(--a1) 70%,transparent);outline-offset:2px;border-radius:8px}

/* ---------- background layers ---------- */
#bgfx{position:fixed;inset:0;z-index:0;pointer-events:none}
.bg-grid{position:fixed;inset:0;z-index:0;pointer-events:none;
  background:
    radial-gradient(ellipse 90% 60% at 70% -10%,color-mix(in srgb,var(--a1) 11%,transparent),transparent 55%),
    radial-gradient(ellipse 60% 45% at 10% 110%,color-mix(in srgb,var(--a2) 7%,transparent),transparent 55%),
    linear-gradient(rgb(148 197 255/.035) 1px,transparent 1px),
    linear-gradient(90deg,rgb(148 197 255/.035) 1px,transparent 1px);
  background-size:auto,auto,44px 44px,44px 44px;
  mask-image:radial-gradient(ellipse 100% 100% at 50% 0%,#000 55%,transparent 100%);
  animation:gridDrift 60s linear infinite;
  transition:background 1s;
}
@keyframes gridDrift{to{background-position:0 0,0 0,44px 44px,44px 44px}}
.scanlines{position:fixed;inset:0;z-index:70;pointer-events:none;opacity:.5;mix-blend-mode:overlay;
  background:repeating-linear-gradient(0deg,rgb(255 255 255/.028) 0 1px,transparent 1px 3px)}
.vignette{position:fixed;inset:0;z-index:69;pointer-events:none;
  background:radial-gradient(ellipse 120% 90% at 50% 40%,transparent 60%,rgb(0 0 0/.5))}

/* ---------- scroll progress ---------- */
.progress{position:fixed;top:0;left:0;right:0;height:2.5px;z-index:100;pointer-events:none;
  background:color-mix(in srgb,var(--a1) 8%,transparent)}
.progress i{display:block;height:100%;width:0;
  background:linear-gradient(90deg,var(--a1),var(--a2));
  box-shadow:0 0 12px color-mix(in srgb,var(--a1) 70%,transparent)}
@supports (animation-timeline: scroll()){
  .progress i{width:100%;transform-origin:0 50%;transform:scaleX(0);
    animation:prog linear both;animation-timeline:scroll(root)}
}
@keyframes prog{from{transform:scaleX(0)}to{transform:scaleX(1)}}

/* ---------- boot overlay ---------- */
#boot{position:fixed;inset:0;z-index:200;background:oklch(9% .012 250);display:flex;align-items:center;justify-content:center;
  transition:opacity .7s ease,visibility .7s;cursor:pointer}
#boot.done{opacity:0;visibility:hidden}
.boot-box{width:min(560px,88vw);font-family:'JetBrains Mono',monospace;font-size:13px;line-height:2.1;color:#67e8f9}
body[data-acc="violet"] .boot-box{color:#c4b5fd}
body[data-acc="amber"] .boot-box{color:#fcd34d}
body[data-acc="rose"] .boot-box{color:#fda4af}
.boot-box .brand{color:#e2e8f0;font-weight:700;letter-spacing:.28em;margin-bottom:14px;font-size:14px}
.boot-line{opacity:0;translate:0 4px}
.boot-line.show{opacity:1;translate:0 0;transition:.25s}
.boot-line .ok{color:var(--a2)}
.boot-bar{height:3px;background:color-mix(in srgb,var(--a1) 14%,transparent);border-radius:3px;margin-top:18px;overflow:hidden}
.boot-bar i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--a1),var(--a2));border-radius:3px;transition:width .3s}
.boot-hint{margin-top:16px;color:var(--dim);font-size:11px;letter-spacing:.2em}

/* ---------- shell ---------- */
.wrap{position:relative;z-index:1;max-width:1320px;margin:0 auto;padding:0 26px 120px}

/* ---------- topbar ---------- */
header.top{display:flex;align-items:center;gap:18px;padding:22px 0 18px;position:sticky;top:0;z-index:60;
  background:linear-gradient(rgb(5 7 12/.92),rgb(5 7 12/.72) 70%,transparent);
  backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)}
.logo{display:flex;align-items:center;gap:12px;text-decoration:none;flex-shrink:0}
.logo-orb{width:38px;height:38px;border-radius:12px;position:relative;overflow:hidden;
  background:conic-gradient(from var(--ang),color-mix(in srgb,var(--a1) 40%,transparent),color-mix(in srgb,var(--a2) 8%,transparent) 35%,color-mix(in srgb,var(--a1) 40%,transparent));
  border:1px solid var(--line2);box-shadow:0 0 22px color-mix(in srgb,var(--a1) 30%,transparent);
  animation:orbspin 3.2s linear infinite}
@keyframes orbspin{to{--ang:360deg}}
.logo-orb::before{content:"";position:absolute;inset:6px;border-radius:50%;border:1.6px solid color-mix(in srgb,var(--a1) 85%,#fff 10%);background:rgb(5 7 12/.82)}
.logo-orb::after{content:"";position:absolute;left:50%;top:50%;width:2px;height:12px;
  background:linear-gradient(var(--a2),transparent);transform-origin:top center;
  animation:sweep 2.8s linear infinite;box-shadow:0 0 8px var(--a2)}
@keyframes sweep{to{rotate:360deg}}
.logo b{font-size:14.5px;letter-spacing:.24em;font-weight:800;color:#f1f5f9}
.logo small{display:block;font-family:'JetBrains Mono',monospace;font-size:9.5px;letter-spacing:.3em;color:var(--a1);margin-top:2px;transition:color .4s}
.crumbs{font-family:'JetBrains Mono',monospace;font-size:10.5px;letter-spacing:.14em;color:var(--dim);
  display:flex;gap:8px;align-items:center;white-space:nowrap}
.crumbs a{color:var(--sub);text-decoration:none;transition:.2s}
.crumbs a:hover{color:var(--a1)}
.crumbs .sep{color:#334155}
.top-right{margin-left:auto;display:flex;align-items:center;gap:14px}
.clock{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.12em;color:var(--sub);
  border:1px solid var(--line);border-radius:10px;padding:8px 13px;background:var(--glass);backdrop-filter:blur(8px);white-space:nowrap}
.clock b{color:var(--a1);font-weight:500}
.backlink{display:inline-flex;align-items:center;gap:7px;font-size:12px;font-weight:600;color:color-mix(in srgb,var(--a1) 80%,#fff);text-decoration:none;
  border:1px solid color-mix(in srgb,var(--a1) 32%,transparent);padding:8px 15px;border-radius:10px;
  background:color-mix(in srgb,var(--a1) 8%,transparent);transition:.25s;white-space:nowrap}
.backlink:hover{background:color-mix(in srgb,var(--a1) 17%,transparent);box-shadow:0 0 18px color-mix(in srgb,var(--a1) 28%,transparent);transform:translateX(-2px)}
@media(max-width:900px){.crumbs{display:none}}
@media(max-width:640px){.clock{display:none}}

/* ---------- hero ---------- */
.hero{position:relative;border-radius:26px;overflow:hidden;margin-top:14px;
  border:1px solid var(--line2);background:#060a12;box-shadow:var(--glow)}
.hero-img{position:absolute;inset:0;background:url('img/radar-hero.png') center/cover no-repeat;opacity:.85;
  animation:heroPan 40s ease-in-out infinite alternate}
@keyframes heroPan{from{transform:scale(1) translateX(0)}to{transform:scale(1.07) translateX(-1.6%)}}
.hero::before{content:"";position:absolute;inset:0;z-index:1;
  background:linear-gradient(100deg,rgb(5 7 12/.94) 22%,rgb(5 7 12/.55) 55%,rgb(5 7 12/.25))}
.hero::after{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;
  background:linear-gradient(transparent 60%,rgb(5 7 12/.9))}
.hero-in{position:relative;z-index:2;padding:64px 56px 50px;max-width:760px}
.tag{display:inline-flex;align-items:center;gap:9px;font-family:'JetBrains Mono',monospace;font-size:10.5px;
  letter-spacing:.3em;color:color-mix(in srgb,var(--a1) 75%,#fff);border:1px solid color-mix(in srgb,var(--a1) 38%,transparent);
  background:color-mix(in srgb,var(--a1) 10%,rgb(8 12 20/.5));
  padding:7px 14px;border-radius:99px;backdrop-filter:blur(6px)}
.tag .dot{width:7px;height:7px;border-radius:50%;background:var(--a2);box-shadow:0 0 10px var(--a2);animation:blink 1.6s ease infinite}
@keyframes blink{50%{opacity:.25}}
.hero h1{font-size:clamp(34px,5.2vw,58px);font-weight:800;line-height:1.04;letter-spacing:-.02em;margin:22px 0 16px;color:#f8fafc;text-wrap:balance}
.hero h1 span{display:inline-block;opacity:0;translate:0 22px;animation:hdrIn .8s var(--ease) forwards}
.hero h1 span:nth-child(2){animation-delay:.12s}.hero h1 span:nth-child(3){animation-delay:.24s}
@keyframes hdrIn{to{opacity:1;translate:0 0}}
.hero h1 .grad{background:linear-gradient(92deg,var(--a1) 10%,var(--a2) 60%,color-mix(in srgb,var(--a1) 40%,#fff));-webkit-background-clip:text;background-clip:text;color:transparent;
  filter:drop-shadow(0 0 26px color-mix(in srgb,var(--a1) 32%,transparent))}
.hero p.sub{color:#aab7c8;font-size:16px;line-height:1.7;max-width:58ch}
.hero p.sub b{color:#dbe7f3;font-weight:600}
.stats{display:flex;gap:34px;margin-top:30px;flex-wrap:wrap}
.stat .n{font-family:'JetBrains Mono',monospace;font-size:30px;font-weight:700;color:#f1f5f9;
  text-shadow:0 0 24px color-mix(in srgb,var(--a1) 38%,transparent)}
.stat .l{font-family:'JetBrains Mono',monospace;font-size:9.5px;letter-spacing:.28em;color:var(--sub);margin-top:4px}
@media(max-width:640px){.hero-in{padding:44px 26px 40px}}

/* ---------- search ---------- */
.searchbar{margin-top:32px;display:flex;align-items:center;gap:12px;max-width:640px;
  background:rgb(10 15 24/.72);border:1px solid var(--line2);border-radius:14px;padding:6px 8px 6px 18px;
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);transition:.3s;box-shadow:0 18px 44px rgb(0 0 0/.4)}
.searchbar:has(input:focus){border-color:color-mix(in srgb,var(--a1) 58%,transparent);
  box-shadow:0 0 0 4px color-mix(in srgb,var(--a1) 10%,transparent),0 18px 44px rgb(0 0 0/.4)}
.searchbar svg{flex-shrink:0}
.searchbar svg *{stroke:var(--a1)}
.searchbar input{flex:1;background:none;border:none;outline:none;color:#f1f5f9;font-size:15px;font-family:'Inter';padding:12px 0;min-width:0}
.searchbar input::placeholder{color:var(--dim)}
.searchbar kbd{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--sub);border:1px solid var(--line2);
  border-bottom-width:2px;border-radius:7px;padding:5px 9px;background:var(--glass2);white-space:nowrap}
.sugs{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:14px;max-width:640px}
.sugs .lbl{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.24em;color:var(--dim);margin-right:2px}
.sug{font-family:'JetBrains Mono',monospace;font-size:10.5px;color:var(--sub);background:rgb(10 15 24/.6);
  border:1px solid var(--line);border-radius:99px;padding:6px 13px;cursor:pointer;transition:.22s;backdrop-filter:blur(8px)}
.sug:hover{color:#fff;border-color:color-mix(in srgb,var(--a1) 55%,transparent);background:color-mix(in srgb,var(--a1) 16%,transparent);transform:translateY(-1px)}
.sugs .tip{margin-left:auto;font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.12em;color:#3d4757}
@media(max-width:640px){.sugs .tip{display:none}}
#matchinfo{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--a2);letter-spacing:.08em;margin-top:10px;min-height:16px;padding-left:4px;display:flex;gap:14px;align-items:center}
#matchinfo .share{color:var(--dim);cursor:pointer;border-bottom:1px dashed #334155;transition:.2s}
#matchinfo .share:hover{color:var(--a1)}

/* ---------- world clock strip ---------- */
.world{display:flex;gap:10px;overflow-x:auto;margin-top:18px;padding:12px 14px;scrollbar-width:none;
  border:1px solid var(--line);border-radius:16px;background:var(--glass);backdrop-filter:blur(10px)}
.world::-webkit-scrollbar{display:none}
.zone{flex-shrink:0;text-align:center;padding:8px 14px;border-radius:12px;border:1px solid transparent;transition:.25s;position:relative}
.zone:hover{border-color:var(--line2);background:rgb(10 15 24/.5)}
.zone .zc{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.22em;color:var(--dim)}
.zone .zt{font-family:'JetBrains Mono',monospace;font-size:15px;font-weight:500;color:#dbe7f3;margin-top:3px;font-variant-numeric:tabular-nums}
.zone.local{border-color:color-mix(in srgb,var(--a1) 45%,transparent);background:color-mix(in srgb,var(--a1) 9%,transparent)}
.zone.local .zc{color:var(--a1)}
.zone.local::after{content:"LOCAL";position:absolute;top:-7px;left:50%;translate:-50% 0;font-family:'JetBrains Mono',monospace;
  font-size:7px;letter-spacing:.18em;color:#04121a;background:linear-gradient(90deg,var(--a1),var(--a2));padding:2px 7px;border-radius:99px}

/* ---------- chips row + controls ---------- */
.chips-wrap{position:sticky;top:64px;z-index:55;display:flex;gap:10px;align-items:center;
  background:linear-gradient(rgb(5 7 12/.95) 65%,transparent);padding:18px 2px 8px}
.chips{display:flex;gap:9px;overflow-x:auto;scrollbar-width:none;flex:1}
.chips::-webkit-scrollbar{display:none}
.chip{flex-shrink:0;font-family:'JetBrains Mono',monospace;font-size:10.5px;letter-spacing:.14em;color:var(--sub);
  border:1px solid var(--line);background:var(--glass);padding:9px 16px;border-radius:99px;cursor:pointer;
  transition:.22s;backdrop-filter:blur(10px);user-select:none}
.chip .c{opacity:.55;font-size:9px;margin-left:6px}
.chip:hover{color:#dbe7f3;border-color:var(--line2);transform:translateY(-1px)}
.chip.on{color:#04121a;background:linear-gradient(92deg,var(--a1),var(--a2));border-color:transparent;font-weight:700;
  box-shadow:0 0 22px color-mix(in srgb,var(--a1) 42%,transparent)}
.chip.on .c{opacity:.8}
.chip.star.on{color:#1c1000;background:linear-gradient(92deg,var(--gold),#fde68a)}
.chip.mine.on{color:#1c1000;background:linear-gradient(92deg,var(--gold),#fef3c7)}
.ctrls{display:flex;gap:8px;align-items:center;flex-shrink:0}
.icobtn{width:34px;height:34px;border-radius:10px;border:1px solid var(--line);background:var(--glass);color:var(--sub);
  display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.22s;font-size:13px;backdrop-filter:blur(10px);font-family:'JetBrains Mono',monospace}
.icobtn:hover{color:var(--a1);border-color:color-mix(in srgb,var(--a1) 50%,transparent);box-shadow:0 0 14px color-mix(in srgb,var(--a1) 20%,transparent)}
.icobtn:active{transform:scale(.92)}
.acc{width:17px;height:17px;border-radius:50%;cursor:pointer;border:2px solid transparent;transition:.22s;position:relative;margin:0 3px}
.acc[data-set="cyan"]{background:linear-gradient(135deg,#22d3ee,#34d399)}
.acc[data-set="violet"]{background:linear-gradient(135deg,#a78bfa,#60a5fa)}
.acc[data-set="amber"]{background:linear-gradient(135deg,#fbbf24,#fb923c)}
.acc[data-set="rose"]{background:linear-gradient(135deg,#fb7185,#f472b6)}
.acc:hover{transform:scale(1.2)}
.acc.on{border-color:#fff;box-shadow:0 0 10px rgb(255 255 255/.35)}

/* ---------- recent strip ---------- */
#recent{margin-top:26px;border:1px dashed color-mix(in srgb,var(--a2) 30%,transparent);border-radius:16px;
  background:color-mix(in srgb,var(--a2) 4%,transparent);padding:14px 16px;display:none}
#recent.has{display:block;animation:fadeSlide .4s var(--ease)}
@keyframes fadeSlide{from{opacity:0;translate:0 8px}to{opacity:1;translate:0 0}}
#recent .r-head{display:flex;align-items:center;gap:10px;font-family:'JetBrains Mono',monospace;
  font-size:9.5px;letter-spacing:.26em;color:var(--a2);margin-bottom:10px}
#recent .r-clear{margin-left:auto;background:none;border:none;color:var(--dim);cursor:pointer;
  font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.2em;transition:.2s}
#recent .r-clear:hover{color:#f87171}
#recent .r-row{display:flex;gap:8px;flex-wrap:wrap}

/* ---------- section heads ---------- */
.sec-head{display:flex;align-items:baseline;gap:16px;margin:64px 4px 22px}
.sec-head .glyph{color:var(--a1);font-family:'JetBrains Mono',monospace;font-size:14px;transition:color .4s}
.sec-head h2{font-size:21px;font-weight:800;letter-spacing:.04em;color:#f1f5f9;text-wrap:balance}
.sec-head .meta{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.24em;color:var(--dim)}
.sec-head .rule{flex:1;height:1px;background:linear-gradient(90deg,var(--line2),transparent)}
@supports (animation-timeline: view()){
  .sec-head{animation:headDrift linear both;animation-timeline:view();animation-range:entry 0% entry 80%}
}
@keyframes headDrift{from{opacity:0;translate:0 18px}to{opacity:1;translate:0 0}}

/* ---------- prime cards ---------- */
.prime-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:16px}
.pcard{position:relative;display:block;text-decoration:none;color:var(--txt);border-radius:var(--r);
  background:linear-gradient(160deg,color-mix(in srgb,var(--a1) 8%,transparent),rgb(10 15 24/.55) 55%);
  border:1px solid var(--line2);padding:22px;overflow:hidden;
  transition:transform .18s ease,border-color .25s,box-shadow .3s;transform-style:preserve-3d;will-change:transform;
  opacity:0;translate:0 24px;container-type:inline-size}
.pcard::before{content:"";position:absolute;inset:0;pointer-events:none;opacity:0;transition:opacity .3s;
  background:radial-gradient(420px circle at var(--mx) var(--my),color-mix(in srgb,var(--a1) 11%,transparent),transparent 60%)}
.pcard:hover::before{opacity:1}
.pcard.shown{opacity:1;translate:0 0;transition:opacity .6s,translate .6s var(--ease),transform .18s,border-color .25s,box-shadow .3s}
.pcard:hover{border-color:color-mix(in srgb,var(--a1) 52%,transparent);
  box-shadow:0 0 0 1px color-mix(in srgb,var(--a1) 22%,transparent),0 22px 50px rgb(0 0 0/.5),0 0 40px color-mix(in srgb,var(--a1) 13%,transparent)}
.pcard .shine{position:absolute;inset:0;background:linear-gradient(115deg,transparent 30%,color-mix(in srgb,#a5f3fc 9%,transparent) 48%,transparent 62%);
  transform:translateX(-120%);pointer-events:none}
.pcard:hover .shine{transform:translateX(120%);transition:transform .9s ease}
.pcard .corner{position:absolute;width:14px;height:14px;opacity:.75;pointer-events:none;transition:.25s;border-color:var(--a1)}
.pcard:hover .corner{opacity:1;width:18px;height:18px}
.c-tl{top:8px;left:8px;border-top:1.5px solid;border-left:1.5px solid}
.c-tr{top:8px;right:8px;border-top:1.5px solid;border-right:1.5px solid}
.c-bl{bottom:8px;left:8px;border-bottom:1.5px solid;border-left:1.5px solid}
.c-br{bottom:8px;right:8px;border-bottom:1.5px solid;border-right:1.5px solid}
.pcard .top{display:flex;align-items:center;gap:14px;margin-bottom:14px}
.favi{width:44px;height:44px;border-radius:12px;background:rgb(5 10 18/.9);border:1px solid var(--line);
  display:flex;align-items:center;justify-content:center;overflow:hidden;flex-shrink:0;position:relative}
.favi img{width:24px;height:24px;position:relative;z-index:1}
.favi .mono{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:15px;color:var(--a1);position:absolute}
.pcard .name{font-weight:700;font-size:15.5px;color:#f1f5f9;letter-spacing:.01em}
.pcard .host{font-family:'JetBrains Mono',monospace;font-size:10.5px;color:var(--a1);margin-top:3px;opacity:.85}
.pcard .kind{margin-left:auto;font-family:'JetBrains Mono',monospace;font-size:8.5px;letter-spacing:.22em;color:var(--gold);
  border:1px solid color-mix(in srgb,var(--gold) 38%,transparent);background:color-mix(in srgb,var(--gold) 8%,transparent);padding:5px 9px;border-radius:99px;flex-shrink:0}
.pcard .desc{font-size:13px;line-height:1.6;color:#9aa8bc}
@container (max-width:300px){.pcard .desc{font-size:12px}}
.pcard .go{position:absolute;right:18px;bottom:16px;font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.18em;
  color:var(--dim);transition:.25s}
.pcard:hover .go{color:var(--a2);transform:translate(2px,-2px)}

/* ---------- groups & panels ---------- */
.group{margin-top:70px}
.group-head{display:flex;align-items:center;gap:16px;margin:0 4px 22px}
.g-tile{width:40px;height:40px;border-radius:12px;flex-shrink:0;display:flex;align-items:center;justify-content:center;
  font-family:'JetBrains Mono',monospace;font-weight:700;font-size:12px;letter-spacing:.06em;color:#04121a;
  background:linear-gradient(135deg,var(--a1),var(--a2));box-shadow:0 0 26px color-mix(in srgb,var(--a1) 38%,transparent);transition:.4s}
.group-head h2{font-size:22px;font-weight:800;letter-spacing:.05em;color:#f1f5f9}
.group-head .cnt{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.22em;color:var(--dim);margin-top:6px}
.group-head .rule{flex:1;height:1px;background:linear-gradient(90deg,var(--line2),transparent);position:relative;overflow:visible}
.group-head .rule::after{content:"";position:absolute;top:-1.5px;left:0;width:56px;height:3px;border-radius:3px;
  background:linear-gradient(90deg,var(--a1),transparent);opacity:.7;animation:scanRule 4.5s ease-in-out infinite}
@keyframes scanRule{0%,15%{translate:0 0;opacity:0}35%{opacity:.8}85%,100%{translate:calc(60vw) 0;opacity:0}}
.g-anchor{background:none;border:none;color:var(--dim);cursor:pointer;transition:.2s;padding:4px;display:flex;align-items:center}
.g-anchor:hover{color:var(--a1);transform:rotate(-8deg) scale(1.1)}
.panels{columns:3;column-gap:16px}
@media(max-width:1080px){.panels{columns:2}}
@media(max-width:700px){.panels{columns:1}}
.panel{break-inside:avoid;margin-bottom:16px;border-radius:var(--r);
  background:linear-gradient(170deg,var(--glass),rgb(8 12 20/.5));
  border:1px solid var(--line);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);overflow:hidden;
  transition:border-color .3s,box-shadow .3s;opacity:0;translate:0 26px;
  content-visibility:auto;contain-intrinsic-size:auto 260px;container-type:inline-size}
.panel.shown{opacity:1;translate:0 0;transition:opacity .55s,translate .55s var(--ease),border-color .3s,box-shadow .3s}
.panel:hover{border-color:var(--line2);box-shadow:0 14px 40px rgb(0 0 0/.4)}
.panel-h{display:flex;align-items:center;gap:11px;padding:15px 18px;border-bottom:1px solid var(--line);
  background:var(--glass);cursor:pointer;user-select:none}
.panel-h .code{font-family:'JetBrains Mono',monospace;font-size:9px;font-weight:700;letter-spacing:.08em;color:color-mix(in srgb,var(--a1) 75%,#fff);
  border:1px solid color-mix(in srgb,var(--a1) 32%,transparent);border-radius:7px;padding:4px 7px;
  background:color-mix(in srgb,var(--a1) 7%,transparent);flex-shrink:0;transition:.25s}
.panel:hover .panel-h .code{box-shadow:0 0 12px color-mix(in srgb,var(--a1) 30%,transparent)}
.panel-h h3{font-size:12.5px;font-weight:700;letter-spacing:.09em;color:#dbe7f3}
.panel-h .n{margin-left:auto;font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--dim)}
.panel-h .car{color:var(--dim);font-size:10px;transition:transform .3s;margin-left:4px}
.panel.closed .car{transform:rotate(-90deg)}
.panel-b{overflow:hidden;transition:max-height .45s var(--ease)}
.panel.closed .panel-b{max-height:0!important}
.links{display:flex;flex-wrap:wrap;gap:8px;padding:14px}

/* ------- tool cells ------- */
.cell{position:relative;display:inline-flex;max-width:100%}
.lnk{display:inline-flex;align-items:center;gap:8px;text-decoration:none;max-width:100%;
  background:var(--glass2);border:1px solid color-mix(in srgb,#94a3b8 9%,transparent);border-radius:10px;padding:7px 12px 7px 8px;
  color:#c8d3e2;font-size:12.5px;font-weight:500;transition:.2s;position:relative;overflow:hidden}
.lnk .fv{width:20px;height:20px;border-radius:6px;background:rgb(5 10 18/.85);display:flex;align-items:center;justify-content:center;
  flex-shrink:0;position:relative;overflow:hidden}
.lnk .fv img{width:13px;height:13px;position:relative;z-index:1}
.lnk .fv .mm{font-family:'JetBrains Mono',monospace;font-size:8.5px;font-weight:700;color:var(--a1);position:absolute}
.lnk span.t{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lnk:hover{background:color-mix(in srgb,var(--a1) 13%,transparent);border-color:color-mix(in srgb,var(--a1) 42%,transparent);
  color:#f0f9ff;transform:translateY(-1.5px);box-shadow:0 6px 18px color-mix(in srgb,var(--a1) 13%,transparent)}
.lnk:active{transform:translateY(0)}
.cell[data-cur="1"] .lnk{border-color:color-mix(in srgb,var(--gold) 34%,transparent)}
.cell[data-cur="1"] .lnk::before{content:"★";color:var(--gold);font-size:9px;position:absolute;top:3px;right:5px;text-shadow:0 0 8px color-mix(in srgb,var(--gold) 80%,transparent)}
.ustar{position:absolute;top:-7px;right:-7px;z-index:3;width:18px;height:18px;border-radius:50%;cursor:pointer;
  background:rgb(8 12 20/.95);border:1px solid color-mix(in srgb,var(--gold) 45%,transparent);color:var(--gold);
  font-size:9px;line-height:1;display:flex;align-items:center;justify-content:center;
  opacity:0;scale:.6;transition:.22s var(--ease)}
.cell:hover .ustar,.cell:focus-within .ustar{opacity:1;scale:1}
.ustar:hover{scale:1.25;box-shadow:0 0 10px color-mix(in srgb,var(--gold) 60%,transparent)}
.cell:has(.ustar[aria-pressed="true"]) .ustar{opacity:1;scale:1;background:linear-gradient(135deg,var(--gold),#fde68a);color:#1c1000;font-weight:700}
.cell:has(.ustar[aria-pressed="true"]) .lnk{border-color:color-mix(in srgb,var(--gold) 55%,transparent);
  box-shadow:0 0 10px color-mix(in srgb,var(--gold) 14%,transparent)}
.lnk.hide,.cell.hide{display:none}
.panel.empty,.group.empty{display:none}

/* custom tooltip */
[data-tip]{position:relative}
[data-tip]::after{content:attr(data-tip);position:absolute;bottom:calc(100% + 8px);left:50%;translate:-50% 4px;z-index:90;
  background:rgb(8 12 20/.96);border:1px solid var(--line2);color:#c8d3e2;font-family:'JetBrains Mono',monospace;
  font-size:9px;letter-spacing:.1em;padding:6px 10px;border-radius:8px;white-space:nowrap;pointer-events:none;
  opacity:0;transition:.18s;backdrop-filter:blur(8px)}
[data-tip]:hover::after{opacity:1;translate:-50% 0}

/* ---------- toasts ---------- */
#toasts{position:fixed;bottom:28px;left:50%;translate:-50% 0;z-index:210;display:flex;flex-direction:column;gap:8px;align-items:center;pointer-events:none}
.toast{font-family:'JetBrains Mono',monospace;font-size:10.5px;letter-spacing:.14em;color:#dbe7f3;
  background:rgb(8 12 20/.92);border:1px solid color-mix(in srgb,var(--a1) 40%,transparent);border-radius:10px;
  padding:10px 18px;backdrop-filter:blur(10px);box-shadow:0 10px 30px rgb(0 0 0/.5),0 0 20px color-mix(in srgb,var(--a1) 12%,transparent);
  animation:toastIn .3s var(--ease);white-space:nowrap;max-width:88vw;overflow:hidden;text-overflow:ellipsis}
.toast.gold{border-color:color-mix(in srgb,var(--gold) 50%,transparent)}
.toast.out{opacity:0;translate:0 8px;transition:.35s}
@keyframes toastIn{from{opacity:0;translate:0 10px;scale:.95}to{opacity:1;translate:0 0;scale:1}}

/* ---------- help modal ---------- */
#help{position:fixed;inset:0;z-index:190;display:none;align-items:center;justify-content:center;background:rgb(3 5 9/.7);backdrop-filter:blur(6px)}
#help.open{display:flex}
.help-card{width:min(420px,90vw);background:linear-gradient(170deg,#0b1220,#070b12);border:1px solid var(--line2);
  border-radius:20px;padding:30px;box-shadow:var(--glow);animation:toastIn .3s var(--ease)}
.help-card h3{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.3em;color:var(--a1);margin-bottom:20px}
.help-card .row{display:flex;justify-content:space-between;align-items:center;padding:9px 0;border-bottom:1px solid rgb(148 163 184/.07);font-size:12.5px;color:#aab7c8}
.help-card .row:last-child{border-bottom:none}
.help-card kbd{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--sub);border:1px solid var(--line2);
  border-bottom-width:2px;border-radius:6px;padding:3px 8px;background:var(--glass2)}
.help-card .close{margin-top:20px;width:100%;padding:11px;border-radius:11px;border:1px solid color-mix(in srgb,var(--a1) 40%,transparent);
  background:color-mix(in srgb,var(--a1) 10%,transparent);color:color-mix(in srgb,var(--a1) 80%,#fff);cursor:pointer;
  font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.24em;transition:.2s}
.help-card .close:hover{background:color-mix(in srgb,var(--a1) 18%,transparent)}

/* ---------- footer ---------- */
footer{margin-top:110px;border-top:1px solid var(--line);padding-top:44px;position:relative;z-index:1}
.foot-grid{display:flex;flex-wrap:wrap;gap:36px;justify-content:space-between}
.foot-brand{max-width:440px}
.foot-brand p{color:var(--sub);font-size:13px;line-height:1.75;margin-top:14px}
.foot-links{display:flex;gap:56px;flex-wrap:wrap}
.foot-links h4{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.28em;color:var(--dim);margin-bottom:16px}
.foot-links a{display:block;color:#9aa8bc;text-decoration:none;font-size:13px;padding:5px 0;transition:.2s}
.foot-links a:hover{color:var(--a1);transform:translateX(3px)}
.foot-base{margin-top:44px;padding-top:22px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;gap:14px;justify-content:space-between;
  font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.14em;color:var(--dim)}
.foot-base a{color:var(--a1);text-decoration:none}
.foot-base kbd{border:1px solid var(--line2);border-radius:5px;padding:2px 6px;font-size:9px}
.disclaim{margin-top:26px;font-size:11px;color:#4b5668;line-height:1.7;max-width:760px}

#toTop{position:fixed;right:26px;bottom:26px;z-index:80;width:46px;height:46px;border-radius:14px;cursor:pointer;
  border:1px solid var(--line2);background:rgb(10 15 24/.8);backdrop-filter:blur(10px);color:var(--a1);font-size:17px;
  display:flex;align-items:center;justify-content:center;opacity:0;visibility:hidden;transition:.3s;transform:translateY(12px)}
#toTop.vis{opacity:1;visibility:visible;transform:none}
#toTop:hover{box-shadow:0 0 24px color-mix(in srgb,var(--a1) 38%,transparent);border-color:color-mix(in srgb,var(--a1) 52%,transparent)}

/* compact density */
body.dens-compact .lnk{font-size:11px;padding:5px 10px 5px 6px}
body.dens-compact .links{padding:10px;gap:6px}
body.dens-compact .panel-h{padding:11px 14px}
body.dens-compact .hero-in{padding-top:44px;padding-bottom:36px}
body.dens-compact .group{margin-top:44px}

noscript .ns{display:block;margin:40px auto;max-width:600px;padding:26px;border:1px solid var(--line2);border-radius:16px;
  color:#dbe7f3;font-size:14px;line-height:1.7;text-align:center;background:var(--glass)}

@media (prefers-reduced-motion: reduce){
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
  html{scroll-behavior:auto}
}
</style>
</head>
<body data-acc="cyan">

<canvas id="bgfx"></canvas>
<div class="bg-grid"></div>
<div class="vignette"></div>
<div class="scanlines"></div>
<div class="progress"><i id="progressBar"></i></div>

<div id="boot">
  <div class="boot-box">
    <div class="brand">LINACRE // OSINT HUD</div>
    <div class="boot-line">&gt; establishing secure channel ......... <span class="ok">OK</span></div>
    <div class="boot-line">&gt; indexing __N__ modules across __C__ sectors ... <span class="ok">OK</span></div>
    <div class="boot-line">&gt; syncing OSINT4ALL collection ........ <span class="ok">OK</span></div>
    <div class="boot-line">&gt; deploying world clock array ........ <span class="ok">11 ZONES</span></div>
    <div class="boot-line">&gt; threat monitor online ............... <span class="ok">LIVE</span></div>
    <div class="boot-line">&gt; ACCESS GRANTED</div>
    <div class="boot-bar"><i id="bootbar"></i></div>
    <div class="boot-hint">CLICK / ANY KEY TO SKIP</div>
  </div>
</div>

<div class="wrap">

  <header class="top">
    <a class="logo" href="https://www.linacre.site/" title="Linacre Start">
      <span class="logo-orb"></span>
      <span><b>LINACRE</b><small>OSINT&nbsp;HUD</small></span>
    </a>
    <nav class="crumbs">
      <a href="https://www.linacre.site/">linacre.site</a><span class="sep">/</span>
      <span>tools</span><span class="sep">/</span>
      <span style="color:var(--a1)">osint-hud</span>
    </nav>
    <div class="top-right">
      <div class="clock" id="clock"><b>--:--:--</b></div>
      <a class="backlink" href="https://www.linacre.site/">← linacre.site</a>
    </div>
  </header>

  <section class="hero">
    <div class="hero-img"></div>
    <div class="hero-in">
      <span class="tag"><span class="dot"></span> LIVE COLLECTION · OSINT4ALL SYNCED</span>
      <h1><span>Open-source intel,</span><br><span class="grad">one heads-up display.</span></h1>
      <p class="sub">The most useful tools from the <b>OSINT4ALL</b> collection, rebuilt as a Linacre console.
      People, breach data, infrastructure, geo-tracking, social networks and public records — every module one tap away.</p>
      <div class="stats">
        <div class="stat"><div class="n" data-count="__N__">0</div><div class="l">TOOLS</div></div>
        <div class="stat"><div class="n" data-count="__C__">0</div><div class="l">CATEGORIES</div></div>
        <div class="stat"><div class="n" data-count="__G__">0</div><div class="l">SECTORS</div></div>
        <div class="stat"><div class="n" data-count="__S__">0</div><div class="l">STARRED</div></div>
      </div>
      <div class="searchbar">
        <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7" stroke="#22d3ee"/><path d="m20 20-3.8-3.8" stroke="#22d3ee"/></svg>
        <input id="q" type="text" placeholder="Search __NF__ tools — try 'username', 'vin', 'breach', 'flight'…" autocomplete="off" spellcheck="false" aria-label="Search tools">
        <kbd>/ to search</kbd>
      </div>
      <div class="sugs" id="sugs">
        <span class="lbl">TRY:</span>
        <span class="sug">username</span><span class="sug">breach</span><span class="sug">vin</span>
        <span class="sug">flight</span><span class="sug">face</span><span class="sug">github</span><span class="sug">webcam</span>
        <span class="tip">RIGHT-CLICK ANY TOOL TO COPY LINK · HOVER ★ TO PIN · PRESS ? FOR KEYS</span>
      </div>
      <div id="matchinfo"></div>
    </div>
  </section>

  <div class="world" id="world" aria-label="World clock"></div>

  <div class="chips-wrap">
    <div class="chips" id="chips"></div>
    <div class="ctrls">
      <span class="acc on" data-set="cyan" data-tip="CYAN THEME"></span>
      <span class="acc" data-set="violet" data-tip="VIOLET THEME"></span>
      <span class="acc" data-set="amber" data-tip="AMBER THEME"></span>
      <span class="acc" data-set="rose" data-tip="ROSE THEME"></span>
      <button class="icobtn" id="rollBtn" data-tip="OPEN RANDOM OP">⚄</button>
      <button class="icobtn" id="densBtn" data-tip="COMPACT DENSITY">▤</button>
      <button class="icobtn" id="foldBtn" data-tip="COLLAPSE ALL">▾</button>
    </div>
  </div>

  <section id="recent" aria-label="Recently opened tools">
    <div class="r-head">⏱ RECENT OPS <button class="r-clear" id="clearRecent">CLEAR ✕</button></div>
    <div class="r-row" id="recentRow"></div>
  </section>

  <div class="sec-head" id="primeHead">
    <span class="glyph">⌖</span>
    <h2>Priority modules</h2>
    <span class="meta">TIER-1 · HAND-PICKED</span>
    <span class="rule"></span>
  </div>
  <div class="prime-grid" id="prime"></div>

  <div id="sections"></div>

  <footer>
    <div class="foot-grid">
      <div class="foot-brand">
        <a class="logo" href="https://www.linacre.site/">
          <span class="logo-orb"></span>
          <span><b>LINACRE</b><small>OSINT HUD</small></span>
        </a>
        <p>A heads-up display for open-source intelligence work — part of the
        <a href="https://www.linacre.site/" style="color:var(--a1);text-decoration:none">linacre.site</a> toolbox.
        Curated from the public <a href="https://start.me/p/L1rEYQ/osint4all" style="color:var(--a1);text-decoration:none">OSINT4ALL</a> collection —
        <em>"a practical &amp; easy OSINT toolkit for researchers of all levels."</em></p>
        <p class="disclaim">Directory only — all tools are third-party sites under their own terms.
        Use for lawful research, journalism, security and due-diligence purposes. Respect privacy and applicable law in your jurisdiction.
        Favourites and recents live only in your browser's local storage — nothing is uploaded.</p>
      </div>
      <div class="foot-links">
        <div>
          <h4>LINACRE</h4>
          <a href="https://www.linacre.site/">← Start page</a>
          <a href="https://www.linacre.site/#projects">All projects</a>
          <a href="https://www.linacre.site/privacy">Privacy</a>
        </div>
        <div>
          <h4>OSINT</h4>
          <a href="https://start.me/p/L1rEYQ/osint4all">OSINT4ALL source</a>
          <a href="https://osintframework.com/">OSINT Framework</a>
          <a href="https://www.bellingcat.com/category/resources/">Bellingcat resources</a>
        </div>
      </div>
    </div>
    <div class="foot-base">
      <span>© 2026 LINACRE · BUILT IN LIVERPOOL, UK</span>
      <span>PRESS <kbd>?</kbd> FOR SHORTCUTS</span>
      <span>SYS STATUS: <span style="color:var(--a2)">● OPERATIONAL</span></span>
      <span><a href="#primeHead">BACK TO TOP ↑</a></span>
    </div>
  </footer>
</div>

<div id="help">
  <div class="help-card">
    <h3>⌨ KEYBOARD OPS</h3>
    <div class="row"><span>Focus search</span><kbd>/</kbd></div>
    <div class="row"><span>Open first match</span><kbd>Enter</kbd></div>
    <div class="row"><span>Clear / close</span><kbd>Esc</kbd></div>
    <div class="row"><span>This panel</span><kbd>?</kbd></div>
    <div class="row"><span>Copy a tool link</span><kbd>right-click</kbd></div>
    <div class="row"><span>Pin a tool</span><kbd>hover ★</kbd></div>
    <button class="close" id="helpClose">CLOSE</button>
  </div>
</div>

<div id="toasts"></div>
<button id="toTop" title="Back to top" aria-label="Back to top">↑</button>

<noscript><div class="ns">⚠ The Linacre OSINT HUD needs JavaScript to render its __NF__-tool index.
All tools come from the public <a href="https://start.me/p/L1rEYQ/osint4all">OSINT4ALL</a> collection.</div></noscript>

<script id="payload" type="application/json">__DATA__</script>
<script>
(function(){
"use strict";
const P = JSON.parse(document.getElementById('payload').textContent);
const $ = s => document.querySelector(s);
const REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ================= state ================= */
const store = {
  get(k,d){ try{ const v=localStorage.getItem('hud:'+k); return v===null?d:JSON.parse(v); }catch(e){ return d; } },
  set(k,v){ try{ localStorage.setItem('hud:'+k,JSON.stringify(v)); }catch(e){} }
};
let stars   = new Set(store.get('stars',[]));
let recents = store.get('recents',[]);
let accent  = store.get('accent','cyan');
let density = store.get('density','cozy');
let activeGroup='all', collapsedAll=false;

/* ================= theme & density ================= */
function applyAccent(){ document.body.dataset.acc=accent;
  document.querySelectorAll('.acc').forEach(a=>a.classList.toggle('on',a.dataset.set===accent));
  store.set('accent',accent); }
function applyDensity(){ document.body.classList.toggle('dens-compact',density==='compact');
  store.set('density',density); reflowPanels(); }
applyAccent(); applyDensity();
document.querySelectorAll('.acc').forEach(a=>a.addEventListener('click',()=>{accent=a.dataset.set;applyAccent();toast('THEME → '+accent.toUpperCase());}));
$('#densBtn').addEventListener('click',e=>{ density=density==='compact'?'cozy':'compact'; applyDensity();
  e.currentTarget.dataset.tip = density==='compact'?'COZY DENSITY':'COMPACT DENSITY';
  toast('DENSITY → '+density.toUpperCase()); });

/* ================= clock ================= */
function tick(){
  const d=new Date(), h=d.getHours(), p=n=>String(n).padStart(2,'0');
  const greet=h<12?'GOOD MORNING':h<18?'GOOD AFTERNOON':'GOOD EVENING';
  const days=['SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY'];
  const mon=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'];
  $('#clock').innerHTML=greet+'&nbsp;·&nbsp;'+days[d.getDay()]+' '+d.getDate()+' '+mon[d.getMonth()]
    +'&nbsp;·&nbsp;<b>'+p(h)+':'+p(d.getMinutes())+':'+p(d.getSeconds())+'</b>';
}
tick(); setInterval(tick,1000);

/* ================= world clock (from the source page's world-clock widget) ================= */
const localZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
const zoneFmt = new Map();
P.zones.forEach(([code,z])=>{
  zoneFmt.set(z, new Intl.DateTimeFormat('en-GB',{hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:false,timeZone:z}));
});
let worldHTML='';
P.zones.forEach(([code,z])=>{
  worldHTML+='<div class="zone'+(z===localZone?' local':'')+'" data-z="'+z+'"><div class="zc">'+code+'</div><div class="zt">--:--:--</div></div>';
});
$('#world').innerHTML=worldHTML;
function worldTick(){
  document.querySelectorAll('.zone').forEach(el=>{
    el.querySelector('.zt').textContent = zoneFmt.get(el.dataset.z).format(new Date());
  });
}
worldTick(); setInterval(worldTick,1000);

/* ================= boot ================= */
const boot=$('#boot'), lines=[...boot.querySelectorAll('.boot-line')], bar=$('#bootbar');
let bi=0, booted=false;
function bootStep(){
  if(booted) return;
  if(bi<lines.length){ lines[bi].classList.add('show'); bar.style.width=((bi+1)/lines.length*100)+'%'; bi++; setTimeout(bootStep,300); }
  else setTimeout(endBoot,450);
}
function endBoot(){ if(booted) return; booted=true; boot.classList.add('done'); sessionStorage.setItem('hud-booted','1'); }
if(sessionStorage.getItem('hud-booted')){ endBoot(); }
else{
  setTimeout(bootStep,300);
  boot.addEventListener('click',endBoot);
  addEventListener('keydown',function k(){ endBoot(); removeEventListener('keydown',k); },{once:false});
}
setTimeout(endBoot,5000);

/* ================= counters ================= */
function countUp(el){
  const target=+el.dataset.count; if(REDUCED){ el.textContent=target.toLocaleString(); return; }
  const t0=performance.now(),dur=1600;
  (function f(t){ const k=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-k,3);
    el.textContent=Math.round(target*e).toLocaleString(); if(k<1) requestAnimationFrame(f); })(t0);
}
document.querySelectorAll('[data-count]').forEach(countUp);

/* ================= helpers ================= */
const STAR=new Set(P.starred);
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
const hostOf=u=>{ try{ return new URL(u).hostname.toLowerCase().replace(/^www\./,''); }catch(e){ return ''; } };
function favHTML(host,cls){
  const mono=(host[0]||'#').toUpperCase();
  return '<span class="'+cls+'"><span class="'+(cls==='favi'?'mono':'mm')+'">'+mono+'</span>'
    +'<img loading="lazy" src="https://www.google.com/s2/favicons?sz=64&domain='+encodeURIComponent(host)+'" alt="" onerror="this.remove()"></span>';
}
function toast(msg,gold){
  const t=document.createElement('div');
  t.className='toast'+(gold?' gold':''); t.textContent=msg;
  $('#toasts').appendChild(t);
  setTimeout(()=>{ t.classList.add('out'); setTimeout(()=>t.remove(),400); },2200);
}
function copyText(txt,msg){
  const done=()=>toast(msg||'LINK COPIED TO CLIPBOARD');
  if(navigator.clipboard&&navigator.clipboard.writeText){ navigator.clipboard.writeText(txt).then(done).catch(()=>fallback()); }
  else fallback();
  function fallback(){ const ta=document.createElement('textarea'); ta.value=txt; document.body.appendChild(ta);
    ta.select(); try{ document.execCommand('copy'); done(); }catch(e){ toast('COPY FAILED'); } ta.remove(); }
}

/* ================= prime cards ================= */
let primeHTML='';
P.prime.forEach(c=>{
  primeHTML+='<a class="pcard" href="'+c[2]+'" target="_blank" rel="noopener" data-rc="1">'
    +'<span class="corner c-tl"></span><span class="corner c-tr"></span><span class="corner c-bl"></span><span class="corner c-br"></span><span class="shine"></span>'
    +'<span class="top">'+favHTML(c[1],'favi')
      +'<span><span class="name">'+esc(c[0])+'</span><br><span class="host">'+esc(c[1])+'</span></span>'
      +'<span class="kind">'+c[3]+'</span></span>'
    +'<span class="desc">'+c[4]+'</span><span class="go">LAUNCH ↗</span></a>';
});
$('#prime').innerHTML=primeHTML;

/* ================= sections ================= */
let html='';
P.groups.forEach(g=>{
  let gcount=0, cats='';
  g.cats.forEach(c=>{
    gcount+=c.links.length;
    let links='';
    c.links.forEach(l=>{
      const host=l.h||hostOf(l.u);
      const cur=STAR.has(l.u)?'1':'0';
      const search=(l.t+' '+host+' '+c.cat+' '+g.name).toLowerCase();
      links+='<span class="cell" data-cur="'+cur+'">'
        +'<a class="lnk" data-s="'+esc(search)+'" href="'+l.u+'" target="_blank" rel="noopener" '
        +'data-tip="'+esc(host)+'" data-url="'+esc(l.u)+'" data-title="'+esc(l.t)+'">'
        +favHTML(host,'fv')+'<span class="t">'+esc(l.t)+'</span></a>'
        +'<button class="ustar" aria-pressed="'+(stars.has(l.u)?'true':'false')+'" data-url="'+esc(l.u)+'" data-title="'+esc(l.t)+'" title="Pin/Unpin">★</button>'
        +'</span>';
    });
    const code=c.cat.replace(/[^A-Z0-9]/g,' ').trim().split(/\s+/).map(w=>w[0]).join('').slice(0,3);
    cats+='<div class="panel" data-cat="'+esc(c.cat.toLowerCase())+'">'
      +'<div class="panel-h"><span class="code">'+code+'</span><h3>'+esc(c.cat)+'</h3>'
      +'<span class="n">'+c.links.length+'</span><span class="car">▾</span></div>'
      +'<div class="panel-b"><div class="links">'+links+'</div></div></div>';
  });
  const initials=g.name.split(/[\s&]+/).filter(Boolean).map(w=>w[0]).join('').slice(0,2);
  html+='<section class="group" id="g-'+g.id+'" data-g="'+g.id+'">'
    +'<div class="group-head"><span class="g-tile">'+initials+'</span>'
    +'<div><h2>'+g.name+'</h2><div class="cnt">'+g.cats.length+' CATEGORIES · '+gcount+' TOOLS</div></div>'
    +'<span class="rule"></span>'
    +'<button class="g-anchor" data-tip="COPY SECTION LINK" data-g="'+g.id+'" aria-label="Copy section link"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></button></div>'
    +'<div class="panels">'+cats+'</div></section>';
});
$('#sections').innerHTML=html;

/* ================= chips ================= */
const chipsEl=$('#chips');
let chips='<span class="chip on" data-g="all">ALL<span class="c">'+P.groups.reduce((a,g)=>a+g.cats.reduce((b,c)=>b+c.links.length,0),0)+'</span></span>'
  +'<span class="chip star" data-g="__star">★ CURATED</span>'
  +'<span class="chip mine" data-g="__mine">✪ MY STARS<span class="c" id="mineCount">'+stars.size+'</span></span>';
P.groups.forEach(g=>{
  const n=g.cats.reduce((a,c)=>a+c.links.length,0);
  chips+='<span class="chip" data-g="'+g.id+'">'+g.name+'<span class="c">'+n+'</span></span>';
});
chipsEl.innerHTML=chips;

/* ================= panels: heights / collapse ================= */
function reflowPanels(openAll){
  document.querySelectorAll('.panel').forEach(p=>{
    const b=p.querySelector('.panel-b');
    if(openAll!==undefined){ p.classList.toggle('closed',!openAll); }
    b.style.maxHeight=p.classList.contains('closed')?'0px':b.scrollHeight+'px';
  });
}
document.querySelectorAll('.panel').forEach(p=>{
  p.querySelector('.panel-b').style.maxHeight=p.querySelector('.panel-b').scrollHeight+'px';
  p.querySelector('.panel-h').addEventListener('click',()=>{ p.classList.toggle('closed'); reflowPanel(p); });
});
function reflowPanel(p){
  const b=p.querySelector('.panel-b');
  b.style.maxHeight=p.classList.contains('closed')?'0px':b.scrollHeight+'px';
}
addEventListener('resize',()=>{ clearTimeout(window.__rz); window.__rz=setTimeout(()=>reflowPanels(),200); });
$('#foldBtn').addEventListener('click',e=>{
  collapsedAll=!collapsedAll;
  document.querySelectorAll('.panel').forEach(p=>{ p.classList.toggle('closed',collapsedAll); reflowPanel(p); });
  e.currentTarget.dataset.tip=collapsedAll?'EXPAND ALL':'COLLAPSE ALL';
  e.currentTarget.textContent=collapsedAll?'▸':'▾';
});

/* ================= filtering ================= */
const q=$('#q'), info=$('#matchinfo');
const supportsVT = 'startViewTransition' in document && !REDUCED;
function mutateFilter(){
  const term=q.value.trim().toLowerCase();
  const words=term.split(/\s+/).filter(Boolean);
  let matches=0;
  document.querySelectorAll('#sections .cell').forEach(cell=>{
    const a=cell.querySelector('.lnk');
    let vis=true;
    if(words.length){ const s=a.dataset.s; vis=words.every(w=>s.indexOf(w)>-1); }
    if(vis&&activeGroup==='__star') vis=cell.dataset.cur==='1';
    if(vis&&activeGroup==='__mine') vis=stars.has(a.dataset.url);
    cell.classList.toggle('hide',!vis); if(vis) matches++;
  });
  document.querySelectorAll('#sections .panel').forEach(p=>{
    const vis=p.querySelectorAll('.cell:not(.hide)').length;
    p.classList.toggle('empty',!vis);
    if(!p.classList.contains('closed')) p.querySelector('.panel-b').style.maxHeight=p.querySelector('.panel-b').scrollHeight+'px';
  });
  document.querySelectorAll('.group').forEach(g=>{
    const ok=(activeGroup==='all'||activeGroup==='__star'||activeGroup==='__mine'||g.dataset.g===activeGroup)
      && g.querySelectorAll('.panel:not(.empty)').length>0;
    g.classList.toggle('empty',!ok);
  });
  const filtered=term||activeGroup!=='all';
  $('#primeHead').style.display=filtered?'none':'';
  $('#prime').style.display=filtered?'none':'';
  info.innerHTML=filtered
    ? matches.toLocaleString()+' module'+(matches===1?'':'s')+' matching <span class="share" id="shareQ">» COPY SEARCH LINK</span>'
    : '';
  const sh=document.getElementById('shareQ');
  if(sh) sh.addEventListener('click',()=>copyText(location.href,'SEARCH LINK COPIED'));
  syncHash(term);
}
let vtBusy=false;
function applyFilter(){
  if(supportsVT&&!vtBusy){
    try{
      vtBusy=true;
      const t=document.startViewTransition(mutateFilter);
      t.finished.finally(()=>vtBusy=false);
      return;
    }catch(e){ vtBusy=false; }
  }
  mutateFilter();
}
q.addEventListener('input',applyFilter);

/* -------------- hash sync (shareable searches) -------------- */
let hashT=null;
function syncHash(term){
  clearTimeout(hashT);
  hashT=setTimeout(()=>{
    const parts=[];
    if(term) parts.push('q='+encodeURIComponent(term));
    if(activeGroup!=='all'&&!activeGroup.startsWith('__')) parts.push('g='+activeGroup);
    const h=parts.length?'#'+parts.join('&'):location.pathname+location.search;
    history.replaceState(null,'',h||' ');
  },250);
}
(function restoreHash(){
  const h=location.hash.slice(1); if(!h) return;
  h.split('&').forEach(kv=>{ const [k,v]=kv.split('=').map(decodeURIComponent);
    if(k==='q') q.value=v;
    if(k==='g'&&document.querySelector('.chip[data-g="'+v+'"]')) activeGroup=v;
  });
  if(q.value||activeGroup!=='all'){
    document.querySelectorAll('.chip').forEach(x=>x.classList.toggle('on',x.dataset.g===activeGroup));
    mutateFilter();
  }
})();

/* -------------- chips -------------- */
chipsEl.addEventListener('click',e=>{
  const c=e.target.closest('.chip'); if(!c) return;
  document.querySelectorAll('.chip').forEach(x=>x.classList.remove('on'));
  c.classList.add('on'); activeGroup=c.dataset.g;
  applyFilter();
  if(!activeGroup.startsWith('__')&&activeGroup!=='all'&&!q.value.trim()){
    const y=document.getElementById('g-'+activeGroup);
    if(y) y.scrollIntoView({behavior:REDUCED?'auto':'smooth',block:'start'});
  }
});

/* -------------- suggestion chips -------------- */
document.getElementById('sugs').addEventListener('click',e=>{
  const s=e.target.closest('.sug'); if(!s) return;
  q.value=s.textContent; q.focus(); applyFilter();
});

/* ================= stars / favourites ================= */
document.addEventListener('click',e=>{
  const b=e.target.closest('.ustar'); if(!b) return;
  e.preventDefault(); e.stopPropagation();
  const u=b.dataset.url, t=b.dataset.title;
  const on=!stars.has(u);
  if(on) stars.add(u); else stars.delete(u);
  document.querySelectorAll('.ustar[data-url]').forEach(x=>{ if(x.dataset.url===u) x.setAttribute('aria-pressed',on?'true':'false'); });
  store.set('stars',[...stars]);
  const mc=document.getElementById('mineCount'); if(mc) mc.textContent=stars.size;
  toast((on?'★ PINNED → ':'✕ UNPINNED → ')+t.toUpperCase().slice(0,42),true);
  if(activeGroup==='__mine') applyFilter();
});

/* ================= recents ================= */
function renderRecents(){
  const box=$('#recent');
  if(!recents.length){ box.classList.remove('has'); return; }
  box.classList.add('has');
  $('#recentRow').innerHTML=recents.map(r=>{
    const h=hostOf(r.u);
    return '<span class="cell"><a class="lnk" href="'+esc(r.u)+'" target="_blank" rel="noopener" data-tip="'+esc(h)+'" data-url="'+esc(r.u)+'" data-title="'+esc(r.t)+'">'
      +favHTML(h,'fv')+'<span class="t">'+esc(r.t)+'</span></a></span>';
  }).join('');
}
document.addEventListener('click',e=>{
  const a=e.target.closest('a.lnk'); if(!a||!a.dataset.url) return;
  recents=recents.filter(r=>r.u!==a.dataset.url);
  recents.unshift({u:a.dataset.url,t:a.dataset.title});
  recents=recents.slice(0,14);
  store.set('recents',recents); renderRecents();
});
$('#clearRecent').addEventListener('click',()=>{ recents=[]; store.set('recents',recents); renderRecents(); toast('RECENT OPS CLEARED'); });
renderRecents();

/* ================= right-click copy ================= */
document.addEventListener('contextmenu',e=>{
  const a=e.target.closest('a.lnk,a.pcard'); if(!a) return;
  e.preventDefault();
  copyText(a.href,'LINK COPIED → '+(a.dataset.title||a.host||a.textContent.trim()).toUpperCase().slice(0,40));
});

/* ================= section anchor copy ================= */
document.addEventListener('click',e=>{
  const b=e.target.closest('.g-anchor'); if(!b) return;
  copyText(location.href.split('#')[0]+'#g-'+b.dataset.g,'SECTION LINK COPIED');
});

/* ================= random op ================= */
$('#rollBtn').addEventListener('click',()=>{
  const vis=[...document.querySelectorAll('#sections .cell:not(.hide) .lnk')].filter(a=>a.offsetParent!==null);
  const pool=vis.length?vis:[...document.querySelectorAll('#sections .lnk[data-url]')];
  if(!pool.length){ toast('NO MODULES AVAILABLE'); return; }
  const a=pool[Math.floor(Math.random()*pool.length)];
  toast('⚄ DEPLOYING → '+(a.dataset.title||'').toUpperCase().slice(0,44),true);
  window.open(a.href,'_blank','noopener');
});

/* ================= keyboard ================= */
document.addEventListener('keydown',e=>{
  if(e.key==='/'&&document.activeElement!==q){ e.preventDefault(); q.focus(); q.select(); }
  else if(e.key==='Escape'){
    if($('#help').classList.contains('open')){ $('#help').classList.remove('open'); return; }
    if(document.activeElement===q){ q.value=''; applyFilter(); q.blur(); }
  }
  else if(e.key==='Enter'&&document.activeElement===q){
    const first=[...document.querySelectorAll('#sections .cell:not(.hide) .lnk')].find(a=>a.offsetParent!==null);
    if(first){ toast('OPENING FIRST MATCH → '+(first.dataset.title||'').toUpperCase().slice(0,40)); window.open(first.href,'_blank','noopener'); }
  }
  else if((e.key==='?'||(e.shiftKey&&e.key==='/'))&&document.activeElement!==q){
    e.preventDefault(); $('#help').classList.toggle('open');
  }
});
$('#helpClose').addEventListener('click',()=>$('#help').classList.remove('open'));
$('#help').addEventListener('click',e=>{ if(e.target.id==='help') $('#help').classList.remove('open'); });

/* ================= scrollspy / progress / toTop ================= */
const toTop=$('#toTop');
const spy=new IntersectionObserver(es=>{
  if(activeGroup!=='all'||q.value.trim()) return;
  es.forEach(en=>{
    if(en.isIntersecting){
      const id=en.target.dataset.g;
      document.querySelectorAll('.chip').forEach(x=>x.classList.toggle('on',x.dataset.g===id));
    }
  });
},{rootMargin:'-30% 0px -60%'});
document.querySelectorAll('.group').forEach(g=>spy.observe(g));

const useCssScroll=CSS.supports('animation-timeline: scroll()');
const pbar=$('#progressBar');
addEventListener('scroll',()=>{
  toTop.classList.toggle('vis',scrollY>800);
  if(!useCssScroll){
    const max=document.documentElement.scrollHeight-innerHeight;
    pbar.style.width=(max>0?(scrollY/max*100):0)+'%';
  }
},{passive:true});
toTop.addEventListener('click',()=>scrollTo({top:0,behavior:REDUCED?'auto':'smooth'}));

/* ================= reveal on scroll ================= */
const io=new IntersectionObserver(es=>{
  es.forEach((en,i)=>{ if(en.isIntersecting){
    setTimeout(()=>en.target.classList.add('shown'),REDUCED?0:(i%8)*55);
    io.unobserve(en.target);
  }});
},{rootMargin:'0px 0px -6%'});
document.querySelectorAll('.pcard,.panel').forEach(el=>io.observe(el));

/* ================= tilt + glow on prime cards ================= */
if(!REDUCED&&matchMedia('(pointer:fine)').matches){
  document.querySelectorAll('.pcard').forEach(card=>{
    card.addEventListener('mousemove',e=>{
      const r=card.getBoundingClientRect();
      const x=(e.clientX-r.left)/r.width, y=(e.clientY-r.top)/r.height;
      card.style.setProperty('--mx',(x*100)+'%');
      card.style.setProperty('--my',(y*100)+'%');
      card.style.transform='perspective(700px) rotateY('+((x-.5)*7)+'deg) rotateX('+((0.5-y)*7)+'deg) translateY(-3px)';
    });
    card.addEventListener('mouseleave',()=>{ card.style.transform=''; });
  });
}

/* ================= particle network ================= */
if(!REDUCED){
  const cv=$('#bgfx'),ctx=cv.getContext('2d');
  let W,H,pts=[],mouse={x:-999,y:-999};
  function resize(){ W=cv.width=innerWidth; H=cv.height=innerHeight; }
  resize(); addEventListener('resize',resize);
  addEventListener('mousemove',e=>{ mouse.x=e.clientX; mouse.y=e.clientY; },{passive:true});
  const N=Math.min(110,Math.floor(innerWidth/13));
  for(let i=0;i<N;i++) pts.push({x:Math.random()*innerWidth,y:Math.random()*innerHeight,
    vx:(Math.random()-.5)*.32,vy:(Math.random()-.5)*.32,r:Math.random()*1.6+.4});
  let run=true;
  document.addEventListener('visibilitychange',()=>{ run=!document.hidden; if(run) loop(); });
  function accentRGB(){
    const s=getComputedStyle(document.body).getPropertyValue('--a1').trim();
    const t=document.createElement('canvas').getContext('2d'); t.fillStyle=s;
    const m=t.fillStyle.match(/[\d.]+/g);
    return m?m.slice(0,3).join(','):'34,211,238';
  }
  let aRGB=accentRGB();
  document.querySelectorAll('.acc').forEach(a=>a.addEventListener('click',()=>setTimeout(()=>aRGB=accentRGB(),60)));
  function loop(){
    if(!run) return;
    ctx.clearRect(0,0,W,H);
    for(const p of pts){
      p.x+=p.vx; p.y+=p.vy;
      if(p.x<0||p.x>W) p.vx*=-1; if(p.y<0||p.y>H) p.vy*=-1;
      const dm=Math.hypot(p.x-mouse.x,p.y-mouse.y);
      if(dm>0&&dm<160){ p.x+=(p.x-mouse.x)/dm*.6; p.y+=(p.y-mouse.y)/dm*.6; }
      ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,7);
      ctx.fillStyle='rgba('+aRGB+',.5)'; ctx.fill();
    }
    for(let i=0;i<pts.length;i++) for(let j=i+1;j<pts.length;j++){
      const a=pts[i],b=pts[j],d=Math.hypot(a.x-b.x,a.y-b.y);
      if(d<130){
        ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y);
        ctx.strokeStyle='rgba('+aRGB+','+((1-d/130)*.13)+')'; ctx.lineWidth=.7; ctx.stroke();
      }
    }
    requestAnimationFrame(loop);
  }
  loop();
}
})();
</script>
</body>
</html>
"""

n_tools = sum(len(c['links']) for g in grouped for c in g['cats'])
n_cats = sum(len(g['cats']) for g in grouped)
n_fmt = f"{n_tools:,}"
html_out = (TEMPLATE
    .replace('__DATA__', DATA_JS)
    .replace('__OGIMG__', 'https://raw.githubusercontent.com/LIN4CRE/linacre-osint-hud/main/assets/banner.png')
    .replace('__N__', str(n_tools))
    .replace('__C__', str(n_cats))
    .replace('__G__', str(len(grouped)))
    .replace('__S__', str(len(PRIME) + len(STARRED)))
    .replace('__NF__', n_fmt)
)
with open('index.html', 'w') as f:
    f.write(html_out)
print(f"Built index.html — {n_tools} tools, {n_cats} categories, {len(grouped)} sectors, {len(html_out)/1024:.0f} KB")
