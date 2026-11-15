"""Generates boards.html: the Kuhle Bank UI/UX case-study boards (1440 px wide)."""

from pathlib import Path
from common import BASE_CSS, TOKENS, icon

CSS = BASE_CSS + """
.board{width:1440px;background:var(--surface);padding:88px 96px;display:flex;flex-direction:column;gap:48px}
.eyebrow{font-size:16px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--primary)}
.title{font-size:56px;font-weight:800;letter-spacing:-1.5px;line-height:1.05;max-width:1000px}
.lead{font-size:22px;line-height:1.55;color:var(--muted);max-width:900px}
.grid2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.grid4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px}
.card{background:var(--bg);border-radius:24px;padding:32px;display:flex;flex-direction:column;gap:14px}
.card h3{font-size:22px;font-weight:700}
.card p,.card li{font-size:17px;line-height:1.55;color:var(--muted)}
.card ul{padding-left:20px;display:flex;flex-direction:column;gap:6px}
.ico{width:52px;height:52px;border-radius:16px;display:flex;align-items:center;justify-content:center}
.tag{display:inline-flex;font-size:13px;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:6px 12px;border-radius:8px}
.step{display:flex;flex-direction:column;gap:10px}
.step .n{font-size:15px;font-weight:800;color:var(--primary)}
.step b{font-size:20px}
.step span{font-size:15px;line-height:1.5;color:var(--muted)}
.node{border-radius:16px;padding:16px 18px;font-size:16px;font-weight:600;text-align:center;min-width:150px}
.arrow{display:flex;align-items:center;color:var(--muted)}
.wf{width:260px;height:540px;border:3px solid var(--ink);border-radius:36px;padding:28px 18px;display:flex;flex-direction:column;gap:12px;background:#fff}
.wf i{display:block;background:#E3E1EC;border-radius:8px}
.wf .t{background:#C9C6D8}
.ann{display:flex;gap:12px;font-size:16px;line-height:1.5;color:var(--muted)}
.ann b{color:var(--ink)}
.num{width:28px;height:28px;border-radius:50%;background:var(--coral);color:#fff;font-size:14px;font-weight:800;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.sw{border-radius:18px;overflow:hidden;border:1px solid var(--line)}
.sw div:first-child{height:110px}
.sw div:last-child{padding:12px 14px;font-size:14px;line-height:1.45}
.btn{height:56px;border-radius:16px;display:flex;align-items:center;justify-content:center;gap:10px;font-size:16px;font-weight:700;padding:0 28px}
.toggle{width:52px;height:32px;border-radius:16px;background:var(--line);padding:3px;display:flex}
.toggle i{width:26px;height:26px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(23,21,59,.25)}
.toggle.on{background:var(--mint);justify-content:flex-end}
"""

BOARDS = []

# 1. Cover
BOARDS.append(("00 Cover", f"""
<div class="board" style="background:var(--ink);color:#fff;height:900px;position:relative;overflow:hidden;justify-content:space-between">
  <div style="position:absolute;width:520px;height:520px;border-radius:50%;background:var(--primary);right:-120px;top:-140px"></div>
  <div style="position:absolute;width:280px;height:280px;border-radius:50%;background:var(--coral);right:110px;top:300px"></div>
  <div style="position:absolute;width:160px;height:160px;border-radius:50%;background:var(--gold);right:40px;top:520px"></div>
  <div style="display:flex;align-items:center;gap:14px;position:relative"><div style="width:56px;height:56px;border-radius:17px;background:#fff;color:var(--primary);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:31px">k</div><span style="font-weight:800;font-size:34px">kuhle</span></div>
  <div style="position:relative;display:flex;flex-direction:column;gap:22px">
    <div class="eyebrow" style="color:var(--gold)">UI/UX case study · Mobile banking</div>
    <div class="title" style="font-size:76px;max-width:880px">Banking for first-time digital bankers in rural KwaZulu-Natal</div>
  </div>
  <div style="position:relative;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;border-top:1px solid rgba(255,255,255,.2);padding-top:28px">
    <div><div style="opacity:.6;font-size:15px">Role</div><div style="font-size:20px;font-weight:600;margin-top:6px">UI/UX designer (solo)</div></div>
    <div><div style="opacity:.6;font-size:15px">Tools</div><div style="font-size:20px;font-weight:600;margin-top:6px">Figma</div></div>
    <div><div style="opacity:.6;font-size:15px">Platform</div><div style="font-size:20px;font-weight:600;margin-top:6px">Android and iOS app</div></div>
    <div><div style="opacity:.6;font-size:15px">Type</div><div style="font-size:20px;font-weight:600;margin-top:6px">Concept project · fictional bank</div></div>
  </div>
</div>"""))

# 2. Overview
steps = [("01", "Discover", "Desk research on mobile banking in small towns: data costs, older phones, fraud."),
         ("02", "Define", "Proto-persona, pain points and How Might We statements."),
         ("03", "Ideate", "User flows and low-fidelity wireframes for the key tasks."),
         ("04", "Design", "Design system, high-fidelity screens and a clickable prototype."),
         ("05", "Test", "Usability test plan with five tasks and success measures.")]
BOARDS.append(("01 Overview", f"""
<div class="board">
  <div class="eyebrow">01 · Overview</div>
  <div class="title">Most banking apps assume fast data, new phones and English.</div>
  <div class="grid3">
    <div class="card"><div class="ico" style="background:var(--coral-50);color:var(--coral)">{icon('alert', 26)}</div><h3>The problem</h3><p>People in towns like Greytown often run their money on cash, airtime and stokvels. Many banking apps feel risky and confusing, and they use a lot of mobile data.</p></div>
    <div class="card"><div class="ico" style="background:var(--primary-50);color:var(--primary)">{icon('check', 26)}</div><h3>The goal</h3><p>Design a banking app a first-time user can use with confidence to send money, buy airtime, track spending and save with a stokvel.</p></div>
    <div class="card"><div class="ico" style="background:var(--gold-50);color:#8A5A00">{icon('lite', 26)}</div><h3>Constraints</h3><ul><li>Low data and slow networks</li><li>Entry-level Android phones</li><li>Four languages</li><li>High fear of scams</li></ul></div>
  </div>
  <div style="display:flex;flex-direction:column;gap:24px">
    <div style="font-size:24px;font-weight:700">My process</div>
    <div style="display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:20px;border-top:4px solid var(--ink);padding-top:22px">
      {''.join(f'<div class="step"><span class="n">{n}</span><b>{t}</b><span>{d}</span></div>' for n, t, d in steps)}
    </div>
  </div>
</div>"""))

# 3. Persona
BOARDS.append(("02 Proto-persona", f"""
<div class="board">
  <div class="eyebrow">02 · Define</div>
  <div class="title">Who we're designing for</div>
  <div style="display:grid;grid-template-columns:420px minmax(0,1fr);gap:24px">
    <div class="card" style="background:var(--primary);color:#fff;gap:18px">
      <div style="width:120px;height:120px;border-radius:50%;background:#fff;color:var(--primary);display:flex;align-items:center;justify-content:center;font-size:42px;font-weight:800">TM</div>
      <div><div style="font-size:32px;font-weight:800">Thandi Mkhize</div><div style="font-size:18px;opacity:.85;margin-top:4px">34 · Teacher's assistant · Greytown</div></div>
      <div style="font-size:20px;line-height:1.5;font-style:italic;opacity:.95">"I send money to my gogo every month, but I'm scared I'll press the wrong thing and lose it."</div>
      <span class="tag" style="background:rgba(255,255,255,.15);color:#fff;align-self:flex-start">Proto-persona · to be validated</span>
    </div>
    <div class="grid2">
      <div class="card"><h3>Goals</h3><ul><li>Send money to family quickly and safely</li><li>Buy airtime and electricity without queues</li><li>See where her money goes each month</li><li>Keep paying into her stokvel</li></ul></div>
      <div class="card"><h3>Frustrations</h3><ul><li>Apps eat her prepaid data</li><li>Hidden fees she only sees afterwards</li><li>Banking language is hard to follow</li><li>Scam SMSes make her distrust every message</li></ul></div>
      <div class="card"><h3>Device and context</h3><ul><li>Entry-level Android phone, often low on storage</li><li>Prepaid data, mostly bought in small bundles</li><li>Speaks isiZulu at home and English at work</li></ul></div>
      <div class="card" style="background:var(--gold-50)"><h3>How might we…</h3><ul><li>make every fee visible before she pays?</li><li>help her feel safe at the moment of sending?</li><li>keep the app useful on a slow, costly connection?</li><li>bring her stokvel into the app without losing trust?</li></ul></div>
    </div>
  </div>
</div>"""))

# 4. User flow
def node(text, bg, fg="var(--ink)", extra=""):
    return f'<div class="node" style="background:{bg};color:{fg};{extra}">{text}</div>'

arrow = f'<div class="arrow">{icon("send", 26).replace("M7 17L17 7M8 7h9v9", "M4 12h16M14 6l6 6-6 6")}</div>'
down = f'<div class="arrow" style="justify-content:center">{icon("send", 26).replace("M7 17L17 7M8 7h9v9", "M12 4v16M6 14l6 6 6-6")}</div>'
BOARDS.append(("03 User flow", f"""
<div class="board">
  <div class="eyebrow">03 · Ideate</div>
  <div class="title">User flow: sending money to family</div>
  <p class="lead">The most important task. I kept it to five steps, put fees and a safety check before the money moves, and made proof of payment easy to share.</p>
  <div style="display:flex;align-items:center;gap:14px;flex-wrap:nowrap">
    {node('Home', 'var(--bg)')}{arrow}{node('Tap Send', 'var(--bg)')}{arrow}{node('Choose recipient', 'var(--primary-50)', 'var(--primary)')}{arrow}{node('Enter amount', 'var(--primary-50)', 'var(--primary)')}{arrow}
    {node('Enough money?', 'var(--gold-50)', '#6B4A00', 'transform:none;border:2px dashed #C99A2E')}{arrow}{node('Check details<br>and fee', 'var(--primary-50)', 'var(--primary)')}
  </div>
  <div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px">
    <div class="card" style="gap:16px">
      <div style="font-weight:700;font-size:18px;color:var(--mint)">If yes</div>
      <div style="display:flex;align-items:center;gap:14px">{node('Confirm with PIN', 'var(--primary)', '#fff')}{arrow}{node('Money sent', 'var(--mint-50)', 'var(--mint)')}{arrow}{node('Share proof', 'var(--bg)', 'var(--ink)', 'border:1px solid var(--line);background:#fff')}</div>
    </div>
    <div class="card" style="gap:16px">
      <div style="font-weight:700;font-size:18px;color:var(--danger)">If no</div>
      <div style="display:flex;align-items:center;gap:14px">{node('Friendly message<br>with balance', 'var(--coral-50)', '#9A2E16')}{arrow}{node('Change amount', 'var(--primary-50)', 'var(--primary)')}</div>
    </div>
  </div>
  <div class="grid3">
    <div class="ann"><span class="num">1</span><span><b>Recent recipients first.</b> Most people send to the same few family members.</span></div>
    <div class="ann"><span class="num">2</span><span><b>Fee shown while typing.</b> No surprise costs after the money has moved.</span></div>
    <div class="ann"><span class="num">3</span><span><b>Safety reminder at the risky moment,</b> not hidden in settings.</span></div>
  </div>
</div>"""))

# 5. Wireframes
def wf(blocks):
    return '<div class="wf">' + "".join(f'<i class="{c}" style="height:{h}px;{e}"></i>' for h, c, e in blocks) + "</div>"

home_wf = wf([(18, "t", "width:60%"), (120, "", "background:#B9B4D6"), (56, "", ""), (24, "", "width:80%"), (18, "t", "width:45%"), (52, "", ""), (52, "", ""), (52, "", ""), (40, "", "margin-top:auto")])
amt_wf = wf([(30, "t", "width:55%"), (60, "", "width:60%;align-self:center;background:#B9B4D6"), (32, "", ""), (40, "", ""), (24, "", ""), (170, "", ""), (48, "", "background:#B9B4D6;margin-top:auto")])
conf_wf = wf([(30, "t", "width:70%"), (60, "", "width:60px;border-radius:50%;align-self:center"), (40, "", "width:60%;align-self:center;background:#B9B4D6"), (170, "", ""), (56, "", "background:#F3E2B5"), (48, "", "background:#B9B4D6;margin-top:auto"), (24, "", "width:50%;align-self:center")])
BOARDS.append(("04 Wireframes", f"""
<div class="board">
  <div class="eyebrow">04 · Wireframes</div>
  <div class="title">Low-fidelity first: structure before style</div>
  <div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:40px;align-items:start">
    <div style="display:flex;flex-direction:column;gap:20px;align-items:center">{home_wf}<div class="ann"><span class="num">A</span><span><b>Home.</b> Balance card at the top, four big actions, then recent activity. Everything most people need without scrolling.</span></div></div>
    <div style="display:flex;flex-direction:column;gap:20px;align-items:center">{amt_wf}<div class="ann"><span class="num">B</span><span><b>Amount.</b> A large number and quick-amount chips. A built-in keypad means no jumping system keyboard.</span></div></div>
    <div style="display:flex;flex-direction:column;gap:20px;align-items:center">{conf_wf}<div class="ann"><span class="num">C</span><span><b>Confirm.</b> One clear summary, the fee, a safety note and a single primary button.</span></div></div>
  </div>
</div>"""))

# 6. Design system
swatches = [("primary", "Kuhle Violet", "Primary actions, brand"), ("ink", "Ink", "Text, dark surfaces"), ("coral", "Coral", "Accent, spending"),
            ("mint", "Mint", "Success, money in"), ("gold", "Gold", "Warnings, safety notes"), ("danger", "Red", "Destructive actions"),
            ("bg", "Mist", "App background"), ("line", "Line", "Borders, dividers")]
sw_html = "".join(f'<div class="sw"><div style="background:{TOKENS[k]}"></div><div><b>{n}</b><br><span style="color:var(--muted)">{TOKENS[k]} · {u}</span></div></div>' for k, n, u in swatches)
type_scale = [("Display", 36, 800, "R4 285.60"), ("Title", 24, 700, "Send money"), ("Heading", 18, 700, "Recent activity"),
              ("Body", 16, 400, "Kuhle to Kuhle is free"), ("Label", 14, 600, "Available balance"), ("Caption", 12, 500, "Groceries · Today")]
type_html = "".join(f'<div style="display:flex;align-items:baseline;gap:24px;border-bottom:1px solid var(--line);padding:10px 0"><span style="width:110px;font-size:14px;color:var(--muted)">{n}<br>{s}/{w}</span><span style="font-size:{s}px;font-weight:{w}">{t}</span></div>' for n, s, w, t in type_scale)
icons_html = "".join(f'<div style="width:56px;height:56px;border-radius:16px;background:var(--bg);display:flex;align-items:center;justify-content:center;color:var(--primary)">{icon(i, 26)}</div>' for i in ["home", "send", "receipt", "phone", "cash", "chart", "card", "users", "bell", "lock", "shield", "lite", "snow", "share"])
BOARDS.append(("05 Design system", f"""
<div class="board">
  <div class="eyebrow">05 · Design system</div>
  <div class="title">Friendly, high-contrast and easy to tap</div>
  <div style="display:flex;flex-direction:column;gap:20px"><div style="font-size:22px;font-weight:700">Colour</div><div class="grid4">{sw_html}</div></div>
  <div class="grid2" style="gap:48px">
    <div style="display:flex;flex-direction:column;gap:12px"><div style="font-size:22px;font-weight:700">Type · Inter</div>{type_html}</div>
    <div style="display:flex;flex-direction:column;gap:20px">
      <div style="font-size:22px;font-weight:700">Components</div>
      <div style="display:flex;gap:14px;flex-wrap:wrap">
        <div class="btn" style="background:var(--primary);color:#fff">Primary</div>
        <div class="btn" style="border:1.5px solid var(--primary);color:var(--primary)">Secondary</div>
        <div class="btn" style="color:var(--primary)">Text</div>
        <div class="btn" style="color:var(--danger)">{icon('alert', 20)} Destructive</div>
      </div>
      <div style="height:52px;border-radius:16px;border:1px solid var(--line);display:flex;align-items:center;gap:10px;padding:0 16px;font-size:15px;color:var(--muted)">{icon('search', 20)} Search input · 52 px high</div>
      <div style="display:flex;gap:10px;align-items:center">
        <div style="height:40px;padding:0 16px;border-radius:12px;background:var(--primary-50);border:1px solid var(--primary);color:var(--primary);display:flex;align-items:center;font-weight:600">Chip on</div>
        <div style="height:40px;padding:0 16px;border-radius:12px;border:1px solid var(--line);display:flex;align-items:center;font-weight:600">Chip off</div>
        <div class="toggle on"><i></i></div><div class="toggle"><i></i></div>
      </div>
      <div style="font-size:22px;font-weight:700;margin-top:8px">Icons · 24 px, 2 px stroke</div>
      <div style="display:flex;gap:10px;flex-wrap:wrap">{icons_html}</div>
      <div style="font-size:15px;color:var(--muted)">Spacing: 4 px base · 20 px screen margins · radius 12 / 16 / 24 px · minimum touch target 44 × 44 px</div>
    </div>
  </div>
</div>"""))

# 7. UX decisions + test plan
decisions = [("lite", "var(--mint-50)", "var(--mint)", "Lite mode", "Turns off images and animations to save data. It's on by default for prepaid users."),
             ("globe", "var(--primary-50)", "var(--primary)", "Four languages", "English, isiZulu, isiXhosa and Afrikaans, chosen on the very first screen."),
             ("receipt", "var(--gold-50)", "#8A5A00", "Fees up front", "Every fee shows before you confirm, written in plain words (\"No fee: Kuhle to Kuhle is free\")."),
             ("shield", "var(--coral-50)", "#B23A1E", "Safety at the right moment", "A scam warning appears on the confirm screen, exactly when it matters."),
             ("eye", "var(--primary-50)", "var(--primary)", "Hide balance", "One tap hides the balance for privacy in taxis and queues."),
             ("users", "var(--mint-50)", "var(--mint)", "Stokvel built in", "A shared pot everyone can see. That openness builds the trust stokvels depend on.")]
dec_html = "".join(f'<div class="card"><div class="ico" style="background:{b};color:{f}">{icon(i, 26)}</div><h3>{t}</h3><p>{d}</p></div>' for i, b, f, t, d in decisions)
tasks = ["Send R350 to a saved family member", "Buy R29 of airtime", "Find how much you spent on transport", "Freeze your card", "Check when your stokvel pays out"]
BOARDS.append(("06 UX decisions and testing", f"""
<div class="board">
  <div class="eyebrow">06 · Key decisions</div>
  <div class="title">Designed around trust, data and language</div>
  <div class="grid3">{dec_html}</div>
  <div class="grid2" style="gap:24px">
    <div class="card" style="background:var(--ink);color:#fff"><h3 style="color:#fff">Accessibility checklist</h3><ul style="color:#CFCDE0"><li style="color:#CFCDE0">Text contrast of at least 4.5:1 (WCAG AA)</li><li style="color:#CFCDE0">Touch targets of 44 × 44 px or larger</li><li style="color:#CFCDE0">Colour is never the only signal: icons and labels too</li><li style="color:#CFCDE0">Large 56 px buttons and a built-in number pad</li><li style="color:#CFCDE0">Works with screen readers: every icon has a label</li></ul></div>
    <div class="card"><h3>Usability test plan (next step)</h3><p>5 participants from Umvoti · moderated, in person · think-aloud</p><ul>{''.join(f'<li>{t}</li>' for t in tasks)}</ul><p><b style="color:var(--ink)">Measure:</b> task success, time on task, errors and confidence (1–5).</p></div>
  </div>
  <div style="font-size:15px;color:var(--muted);border-top:1px solid var(--line);padding-top:20px">Kuhle Bank is a fictional bank created for a portfolio project. Names, amounts and the persona are illustrative, not real customer data.</div>
</div>"""))


def build():
    boards = "\n".join(f'<section class="b" data-name="{n}">{h}\n</section>' for n, h in BOARDS)
    doc = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Kuhle Bank case study</title><style>{CSS}\n.b{{display:block}}</style></head><body style="flex-direction:column">{boards}</body></html>'
    Path(__file__).with_name("boards.html").write_text(doc, encoding="utf-8")
    return len(BOARDS)


if __name__ == "__main__":
    print(build(), "boards")
