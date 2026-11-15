"""Generates screens.html: the ten hi-fi Kuhle Bank app screens (390 x 844)."""

from pathlib import Path
from common import BASE_CSS, icon

CSS = BASE_CSS + """
.screen{width:390px;height:844px;background:var(--bg);position:relative;overflow:hidden;display:flex;flex-direction:column;border-radius:0}
.status{height:47px;padding:16px 28px 0 32px;display:flex;justify-content:space-between;align-items:center;font-size:15px;font-weight:600;flex-shrink:0}
.status .sys{display:flex;gap:6px;align-items:center}
.bat{width:24px;height:12px;border:1.5px solid currentColor;border-radius:3px;padding:1.5px}
.bat i{display:block;width:70%;height:100%;background:currentColor;border-radius:1px}
.sig{display:flex;gap:2px;align-items:flex-end;height:12px}
.sig i{width:3px;background:currentColor;border-radius:1px}
.body{flex:1;padding:8px 20px 0;display:flex;flex-direction:column;gap:20px;overflow:hidden}
.top{display:flex;align-items:center;gap:12px;min-height:44px}
.top h1{font-size:20px;font-weight:700;flex:1}
.iconbtn{width:44px;height:44px;border-radius:14px;background:var(--surface);border:1px solid var(--line);display:flex;align-items:center;justify-content:center;color:var(--ink)}
.avatar{width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:15px;flex-shrink:0}
.h-sub{font-size:13px;color:var(--muted)}
.h-title{font-size:18px;font-weight:700}
.bal{background:var(--primary);color:#fff;border-radius:24px;padding:20px;display:flex;flex-direction:column;gap:14px;position:relative;overflow:hidden}
.bal .ring{position:absolute;border-radius:50%;border:28px solid rgba(255,255,255,.07)}
.bal .lbl{font-size:13px;opacity:.85;display:flex;justify-content:space-between;align-items:center}
.bal .amt{font-size:36px;font-weight:800;letter-spacing:-1px;display:flex;align-items:center;gap:12px}
.bal .amt small{font-size:20px;font-weight:700}
.bal .split{display:flex;gap:10px}
.bal .split div{flex:1;background:rgba(255,255,255,.12);border-radius:14px;padding:10px 12px;font-size:12px}
.bal .split b{display:block;font-size:15px;margin-top:2px}
.actions{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.act{display:flex;flex-direction:column;align-items:center;gap:8px;font-size:12px;font-weight:600;text-align:center;line-height:1.25}
.act .c{width:56px;height:56px;border-radius:18px;background:var(--surface);border:1px solid var(--line);display:flex;align-items:center;justify-content:center;color:var(--primary)}
.pill{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:600;padding:10px 14px;border-radius:14px}
.sec-t{display:flex;justify-content:space-between;align-items:baseline}
.sec-t h2{font-size:16px;font-weight:700}
.sec-t a{font-size:13px;font-weight:600;color:var(--primary);text-decoration:none}
.list{background:var(--surface);border:1px solid var(--line);border-radius:20px;padding:4px 16px}
.row{display:flex;align-items:center;gap:12px;padding:12px 0;border-bottom:1px solid var(--line)}
.row:last-child{border-bottom:none}
.row .ic{width:40px;height:40px;border-radius:12px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.row .t{flex:1;min-width:0}
.row .t b{display:block;font-size:14px;font-weight:600}
.row .t span{font-size:12px;color:var(--muted)}
.row .v{font-size:14px;font-weight:700;text-align:right;white-space:nowrap}
.row .v.in{color:var(--mint)}
.tabbar{height:84px;background:var(--surface);border-top:1px solid var(--line);display:flex;justify-content:space-around;padding:10px 12px 0;flex-shrink:0}
.tab{display:flex;flex-direction:column;align-items:center;gap:4px;font-size:11px;font-weight:600;color:var(--muted);width:72px}
.tab.on{color:var(--primary)}
.btn{height:56px;border-radius:16px;display:flex;align-items:center;justify-content:center;gap:10px;font-size:16px;font-weight:700;width:100%}
.btn.p{background:var(--primary);color:#fff}
.btn.s{background:var(--surface);color:var(--primary);border:1.5px solid var(--primary)}
.btn.g{color:var(--primary)}
.foot{padding:12px 20px 34px;display:flex;flex-direction:column;gap:10px;flex-shrink:0}
.input{height:52px;border-radius:16px;background:var(--surface);border:1px solid var(--line);display:flex;align-items:center;gap:10px;padding:0 16px;font-size:15px;color:var(--muted)}
.chips{display:flex;gap:8px;flex-wrap:wrap}
.chip{height:40px;padding:0 16px;border-radius:12px;background:var(--surface);border:1px solid var(--line);display:flex;align-items:center;font-size:14px;font-weight:600}
.chip.on{background:var(--primary-50);border-color:var(--primary);color:var(--primary)}
.pad{display:grid;grid-template-columns:repeat(3,1fr);row-gap:4px}
.pad div{height:56px;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:600}
.pad span{display:block;font-size:9px;letter-spacing:2px;color:var(--muted);font-weight:600;text-align:center}
.toggle{width:52px;height:32px;border-radius:16px;background:var(--line);padding:3px;display:flex;flex-shrink:0}
.toggle i{width:26px;height:26px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(23,21,59,.25)}
.toggle.on{background:var(--mint);justify-content:flex-end}
.note{border-radius:16px;padding:14px;display:flex;gap:12px;font-size:13px;line-height:1.45}
.kv{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--line);font-size:14px}
.kv:last-child{border-bottom:none}
.kv span{color:var(--muted)}
.kv b{font-weight:600}
.bar{height:10px;border-radius:5px;background:var(--line);overflow:hidden;display:flex}
.bar i{display:block;height:100%}
"""


def status(dark=False):
    color = "#fff" if dark else "var(--ink)"
    bg = "background:var(--primary);" if dark else ""
    return f"""<div class="status" style="color:{color};{bg}"><span>9:41</span><div class="sys">
<div class="sig"><i style="height:4px"></i><i style="height:6px"></i><i style="height:9px"></i><i style="height:12px"></i></div>
{icon('lite', 16, 'currentColor', 2.2)}<div class="bat"><i></i></div></div></div>"""


def tabbar(active):
    tabs = [("home", "Home"), ("chart", "Insights"), ("card", "Cards"), ("users", "Stokvel")]
    return '<div class="tabbar">' + "".join(
        f'<div class="tab{" on" if label == active else ""}">{icon(i, 24)}<span>{label}</span></div>' for i, label in tabs
    ) + "</div>"


def avatar(initials, bg, fg, size=44):
    return f'<div class="avatar" style="width:{size}px;height:{size}px;background:{bg};color:{fg}">{initials}</div>'


def row(ic, ic_bg, ic_fg, title, sub, value, cls=""):
    return (f'<div class="row"><div class="ic" style="background:{ic_bg};color:{ic_fg}">{icon(ic, 20)}</div>'
            f'<div class="t"><b>{title}</b><span>{sub}</span></div><div class="v {cls}">{value}</div></div>')


def numpad(with_dot=False):
    letters = ["", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    keys = "".join(f'<div style="flex-direction:column">{i + 1}<span>{letters[i]}</span></div>' for i in range(9))
    left = "<div>,</div>" if with_dot else '<div style="font-size:14px;color:var(--muted)"></div>'
    return f'<div class="pad">{keys}{left}<div>0</div><div>{icon("del", 26)}</div></div>'


def logo(size=40, light=False):
    fg = "#fff" if light else "var(--primary)"
    mark_bg = "#fff" if light else "var(--primary)"
    mark_fg = "var(--primary)" if light else "#fff"
    return (f'<div style="display:flex;align-items:center;gap:10px"><div style="width:{size}px;height:{size}px;border-radius:{size*0.3:.0f}px;'
            f'background:{mark_bg};color:{mark_fg};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:{size*0.55:.0f}px">k</div>'
            f'<span style="font-weight:800;font-size:{size*0.6:.0f}px;letter-spacing:-0.5px;color:{fg}">kuhle</span></div>')


SCREENS = []

# 1. Welcome
SCREENS.append(("01 Welcome", f"""
{status(True)}
<div style="flex:1;background:var(--primary);color:#fff;padding:24px 24px 0;display:flex;flex-direction:column;gap:22px;position:relative;overflow:hidden">
  <div style="position:absolute;width:240px;height:240px;border-radius:50%;background:var(--coral);right:-70px;top:30px"></div>
  <div style="position:absolute;width:120px;height:120px;border-radius:50%;background:var(--gold);right:150px;top:150px"></div>
  <div style="position:absolute;width:84px;height:84px;border-radius:24px;background:#fff;opacity:.16;left:24px;top:110px"></div>
  {logo(40, True)}
  <div style="margin-top:auto;position:relative;padding-bottom:28px">
    <h1 style="font-size:38px;line-height:1.05;font-weight:800;letter-spacing:-1px">Banking that speaks your language.</h1>
    <p style="font-size:16px;line-height:1.5;opacity:.9;margin-top:12px">Send money, buy airtime and save with your stokvel, even on a slow connection.</p>
  </div>
</div>
<div class="foot" style="background:var(--surface);padding-top:20px;gap:14px">
  <div style="display:flex;align-items:center;gap:8px;font-size:13px;font-weight:600;color:var(--muted)">{icon('globe', 18)} Choose your language</div>
  <div class="chips"><div class="chip on">English</div><div class="chip">isiZulu</div><div class="chip">isiXhosa</div><div class="chip">Afrikaans</div></div>
  <div class="btn p">Open an account</div>
  <div class="btn s">I already bank with Kuhle</div>
</div>"""))

# 2. PIN login
SCREENS.append(("02 Log in with PIN", f"""
{status()}
<div class="body" style="align-items:center;text-align:center;gap:14px;padding-top:28px">
  {avatar('TM', 'var(--primary-50)', 'var(--primary)', 72)}
  <div><div class="h-title" style="font-size:22px">Welcome back, Thandi</div><div class="h-sub" style="font-size:15px;margin-top:4px">Enter your 5-digit PIN</div></div>
  <div style="display:flex;gap:16px;margin:18px 0 10px">
    <i style="width:16px;height:16px;border-radius:50%;background:var(--primary)"></i><i style="width:16px;height:16px;border-radius:50%;background:var(--primary)"></i>
    <i style="width:16px;height:16px;border-radius:50%;border:2px solid var(--line)"></i><i style="width:16px;height:16px;border-radius:50%;border:2px solid var(--line)"></i><i style="width:16px;height:16px;border-radius:50%;border:2px solid var(--line)"></i>
  </div>
  <div style="width:100%;margin-top:auto">{numpad()}</div>
</div>
<div class="foot">
  <div class="btn s">{icon('finger', 22)} Use fingerprint</div>
  <div class="btn g" style="height:40px;font-size:15px">Forgot PIN?</div>
</div>"""))

# 3. Home
SCREENS.append(("03 Home", f"""
{status()}
<div class="body">
  <div class="top">{avatar('TM', 'var(--primary-50)', 'var(--primary)')}<div style="flex:1"><div class="h-sub">Sawubona,</div><div class="h-title">Thandi Mkhize</div></div><div class="iconbtn">{icon('bell', 22)}</div></div>
  <div class="bal">
    <div class="ring" style="width:220px;height:220px;right:-70px;top:-90px"></div>
    <div class="lbl"><span>Everyday account · 2041</span>{icon('eye', 20, '#fff')}</div>
    <div class="amt">R4 285<small>.60</small></div>
    <div class="split"><div>Savings<b>R1 200.00</b></div><div>Stokvel pot<b>R3 450.00</b></div></div>
  </div>
  <div class="actions">
    <div class="act"><div class="c">{icon('send')}</div>Send</div>
    <div class="act"><div class="c">{icon('receipt')}</div>Pay bills</div>
    <div class="act"><div class="c">{icon('phone')}</div>Airtime &amp; data</div>
    <div class="act"><div class="c">{icon('cash')}</div>Cash send</div>
  </div>
  <div class="pill" style="background:var(--mint-50);color:var(--mint)">{icon('lite', 18)} Lite mode is on: images off, uses less data</div>
  <div class="sec-t"><h2>Recent activity</h2><a>See all</a></div>
  <div class="list">
    {row('bag', 'var(--coral-50)', 'var(--coral)', 'Spar Greytown', 'Groceries · Today', '−R312.40')}
    {row('in', 'var(--mint-50)', 'var(--mint)', 'From Sipho Ndlovu', 'Payment received · Yesterday', '+R500.00', 'in')}
    {row('bolt', 'var(--gold-50)', '#9A6A00', 'Prepaid electricity', 'Umvoti · 12 Nov', '−R150.00')}
  </div>
</div>
{tabbar('Home')}"""))

# 4. Choose recipient
contacts = [("GZ", "Gogo Z.", "var(--coral-50)", "#B23A1E"), ("SN", "Sipho", "var(--mint-50)", "var(--mint)"),
            ("LD", "Lindiwe", "var(--gold-50)", "#8A5A00"), ("MD", "Mandla", "var(--primary-50)", "var(--primary)")]
recent = "".join(f'<div class="act">{avatar(i, b, f, 56)}{n}</div>' for i, n, b, f in contacts)
SCREENS.append(("04 Send – choose recipient", f"""
{status()}
<div class="body">
  <div class="top"><div class="iconbtn">{icon('back')}</div><h1>Send money</h1></div>
  <div class="input">{icon('search', 20)} Name, phone or account number</div>
  <div class="sec-t"><h2>Recent</h2></div>
  <div class="actions" style="margin-top:-6px">{recent}</div>
  <div class="sec-t"><h2>Send to</h2></div>
  <div class="list">
    {row('wallet', 'var(--primary-50)', 'var(--primary)', 'Kuhle account', 'Free and instant', icon('back', 20).replace('M15 18l-6-6 6-6', 'M9 18l6-6-6-6'))}
    {row('phone', 'var(--mint-50)', 'var(--mint)', 'Cash send to a phone', 'They withdraw at any ATM', icon('back', 20).replace('M15 18l-6-6 6-6', 'M9 18l6-6-6-6'))}
    {row('receipt', 'var(--gold-50)', '#8A5A00', 'Another bank', 'Arrives in 1–2 working days', icon('back', 20).replace('M15 18l-6-6 6-6', 'M9 18l6-6-6-6'))}
  </div>
  <div class="btn s" style="height:52px">{icon('plus', 20)} Add new recipient</div>
</div>
{tabbar('Home')}"""))

# 5. Enter amount
SCREENS.append(("05 Send – enter amount", f"""
{status()}
<div class="body" style="gap:16px">
  <div class="top"><div class="iconbtn">{icon('back')}</div><div style="flex:1;display:flex;align-items:center;gap:10px">{avatar('GZ', 'var(--coral-50)', '#B23A1E', 40)}<div><div class="h-sub">Sending to</div><div style="font-weight:700">Gogo Zodwa</div></div></div></div>
  <div style="text-align:center;padding-top:8px">
    <div style="font-size:56px;font-weight:800;letter-spacing:-2px">R350</div>
    <div class="h-sub" style="font-size:14px;margin-top:4px">Available: R4 285.60</div>
  </div>
  <div class="chips" style="justify-content:center"><div class="chip">R50</div><div class="chip">R100</div><div class="chip">R200</div><div class="chip">R500</div></div>
  <div class="input" style="color:var(--ink)">{icon('receipt', 20, 'var(--muted)')} For groceries</div>
  <div class="pill" style="background:var(--mint-50);color:var(--mint);justify-content:center">{icon('check', 18)} No fee: Kuhle to Kuhle is free</div>
  {numpad(True)}
</div>
<div class="foot"><div class="btn p">Continue</div></div>"""))

# 6. Confirm
SCREENS.append(("06 Send – confirm", f"""
{status()}
<div class="body">
  <div class="top"><div class="iconbtn">{icon('back')}</div><h1>Check before you send</h1></div>
  <div style="text-align:center;display:flex;flex-direction:column;align-items:center;gap:8px;padding:6px 0">
    {avatar('GZ', 'var(--coral-50)', '#B23A1E', 64)}
    <div style="font-size:15px;color:var(--muted)">You are sending</div>
    <div style="font-size:40px;font-weight:800;letter-spacing:-1px">R350.00</div>
    <div style="font-size:15px">to <b>Gogo Zodwa</b></div>
  </div>
  <div class="list">
    <div class="kv"><span>Account</span><b>Kuhle · 0732</b></div>
    <div class="kv"><span>Reference</span><b>For groceries</b></div>
    <div class="kv"><span>Fee</span><b style="color:var(--mint)">R0.00</b></div>
    <div class="kv"><span>Arrives</span><b>Immediately</b></div>
    <div class="kv"><span>Total</span><b style="font-size:16px">R350.00</b></div>
  </div>
  <div class="note" style="background:var(--gold-50);color:#6B4A00">{icon('shield', 22)}<span><b>Stay safe.</b> Kuhle will never call or SMS you to ask for your PIN or OTP.</span></div>
</div>
<div class="foot"><div class="btn p">{icon('lock', 20, '#fff')} Confirm with PIN</div><div class="btn g" style="height:44px">Edit details</div></div>"""))

# 7. Success
SCREENS.append(("07 Send – success", f"""
{status()}
<div class="body" style="align-items:center;text-align:center;justify-content:center;gap:18px">
  <div style="width:112px;height:112px;border-radius:50%;background:var(--mint-50);display:flex;align-items:center;justify-content:center">
    <div style="width:76px;height:76px;border-radius:50%;background:var(--mint);display:flex;align-items:center;justify-content:center">{icon('check', 40, '#fff', 3)}</div></div>
  <div><div style="font-size:30px;font-weight:800;letter-spacing:-.5px">R350.00 sent</div>
  <div style="font-size:16px;color:var(--muted);margin-top:6px;line-height:1.5">Gogo Zodwa will get an SMS<br>to let her know.</div></div>
  <div class="list" style="width:100%;text-align:left">
    <div class="kv"><span>Date</span><b>15 Nov 2026, 09:41</b></div>
    <div class="kv"><span>Reference no.</span><b>KB-1115-0841</b></div>
    <div class="kv"><span>New balance</span><b>R3 935.60</b></div>
  </div>
</div>
<div class="foot"><div class="btn s">{icon('share', 20)} Share proof of payment</div><div class="btn p">Done</div></div>"""))

# 8. Insights
cats = [("bag", "Groceries", "R1 420.00", 36, "var(--primary)"), ("bolt", "Electricity", "R650.00", 17, "var(--gold)"),
        ("bus", "Transport", "R840.00", 21, "var(--coral)"), ("phone", "Airtime &amp; data", "R420.00", 11, "var(--mint)"),
        ("receipt", "Other", "R582.40", 15, "#A7A3BD")]
stack = "".join(f'<i style="width:{p}%;background:{c}"></i>' for _, _, _, p, c in cats)
cat_rows = "".join(
    f'<div class="row"><div class="ic" style="background:var(--bg);color:{c}">{icon(i, 20)}</div><div class="t"><b>{n}</b>'
    f'<div class="bar" style="height:6px;margin-top:6px"><i style="width:{p * 2.6:.0f}%;background:{c}"></i></div></div><div class="v">{v}</div></div>'
    for i, n, v, p, c in cats)
SCREENS.append(("08 Insights", f"""
{status()}
<div class="body" style="gap:16px">
  <div class="top"><h1 style="font-size:24px">Insights</h1><div class="chip" style="gap:6px">{icon('calendar', 18)} November</div></div>
  <div class="list" style="padding:18px 16px;display:flex;flex-direction:column;gap:12px">
    <div class="h-sub">Spent this month</div>
    <div style="font-size:32px;font-weight:800;letter-spacing:-1px">R3 912.40</div>
    <div class="bar" style="height:14px;border-radius:7px">{stack}</div>
  </div>
  <div class="note" style="background:var(--mint-50);color:var(--mint)">{icon('chart', 22)}<span><b>Nice one!</b> You spent R240 less on transport than in October.</span></div>
  <div class="sec-t"><h2>By category</h2></div>
  <div class="list">{cat_rows}</div>
</div>
{tabbar('Insights')}"""))

# 9. Card controls
SCREENS.append(("09 Card controls", f"""
{status()}
<div class="body" style="gap:16px">
  <div class="top"><h1 style="font-size:24px">My card</h1></div>
  <div style="height:200px;border-radius:24px;background:var(--ink);color:#fff;padding:22px;display:flex;flex-direction:column;justify-content:space-between;position:relative;overflow:hidden">
    <div style="position:absolute;width:200px;height:200px;border-radius:50%;background:var(--primary);right:-70px;top:-90px"></div>
    <div style="position:absolute;width:80px;height:80px;border-radius:50%;background:var(--coral);right:90px;top:-36px"></div>
    <div style="position:relative">{logo(30, True)}</div>
    <div style="position:relative"><div style="font-size:18px;letter-spacing:3px;font-weight:600">•••• •••• •••• 4821</div>
    <div style="display:flex;justify-content:space-between;font-size:13px;margin-top:10px;opacity:.85"><span>THANDI MKHIZE</span><span>09/29</span></div></div>
  </div>
  <div class="list">
    <div class="row"><div class="ic" style="background:var(--primary-50);color:var(--primary)">{icon('snow', 20)}</div><div class="t"><b>Freeze card</b><span>Pause it if you can't find it</span></div><div class="toggle"><i></i></div></div>
    <div class="row"><div class="ic" style="background:var(--primary-50);color:var(--primary)">{icon('globe', 20)}</div><div class="t"><b>Online payments</b><span>Shopping on websites and apps</span></div><div class="toggle on"><i></i></div></div>
    <div class="row"><div class="ic" style="background:var(--primary-50);color:var(--primary)">{icon('lite', 20)}</div><div class="t"><b>Tap to pay</b><span>Contactless in shops</span></div><div class="toggle on"><i></i></div></div>
  </div>
  <div class="list" style="padding:16px">
    <div style="display:flex;justify-content:space-between;font-size:14px"><b>Daily spending limit</b><b style="color:var(--primary)">R2 000</b></div>
    <div style="position:relative;margin-top:16px;height:20px;display:flex;align-items:center"><div class="bar" style="width:100%;height:6px"><i style="width:40%;background:var(--primary)"></i></div>
    <div style="position:absolute;left:calc(40% - 10px);width:20px;height:20px;border-radius:50%;background:#fff;border:3px solid var(--primary)"></div></div>
  </div>
  <div class="btn" style="height:48px;color:var(--danger);font-size:15px">{icon('alert', 20)} Report lost or stolen card</div>
</div>
{tabbar('Cards')}"""))

# 10. Stokvel
members = [("TM", "var(--primary-50)", "var(--primary)"), ("LD", "var(--gold-50)", "#8A5A00"), ("NB", "var(--mint-50)", "var(--mint)"),
           ("ZK", "var(--coral-50)", "#B23A1E"), ("PM", "#E9E7F3", "var(--muted)")]
faces = "".join(f'<div style="margin-left:-10px;border:3px solid #fff;border-radius:50%">{avatar(i, b, f, 40)}</div>' for i, b, f in members)
SCREENS.append(("10 Stokvel savings", f"""
{status()}
<div class="body" style="gap:16px">
  <div class="top"><h1 style="font-size:24px">Stokvel</h1><div class="iconbtn">{icon('plus')}</div></div>
  <div class="list" style="padding:18px 16px;display:flex;flex-direction:column;gap:14px">
    <div style="display:flex;justify-content:space-between;align-items:center"><div><div class="h-title">Umoja Savings Club</div><div class="h-sub">12 members · R300 a month each</div></div></div>
    <div style="display:flex;padding-left:10px">{faces}<div style="margin-left:-10px;border:3px solid #fff;border-radius:50%"><div class="avatar" style="width:40px;height:40px;background:var(--ink);color:#fff;font-size:12px">+7</div></div></div>
    <div><div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-size:28px;font-weight:800;letter-spacing:-1px">R3 450</span><span class="h-sub">of R12 000 goal</span></div>
    <div class="bar" style="height:12px;border-radius:6px;margin-top:10px"><i style="width:29%;background:var(--mint)"></i></div></div>
  </div>
  <div class="note" style="background:var(--primary-50);color:var(--primary)">{icon('calendar', 22)}<span><b>Next payout: Lindiwe D.</b><br>30 November · everyone can see the pot, so it's fair and open.</span></div>
  <div class="sec-t"><h2>This month</h2><a>History</a></div>
  <div class="list">
    {row('check', 'var(--mint-50)', 'var(--mint)', 'Thandi M. (you)', 'Paid · 1 Nov', 'R300.00')}
    {row('check', 'var(--mint-50)', 'var(--mint)', 'Nomsa B.', 'Paid · 3 Nov', 'R300.00')}
    {row('calendar', 'var(--gold-50)', '#8A5A00', 'Zanele K.', 'Due 25 Nov', 'R300.00')}
  </div>
  <div class="btn p">Contribute R300</div>
</div>
{tabbar('Stokvel')}"""))


def build():
    screens = "\n".join(f'<section class="screen" data-name="{name}" id="s{i}">{html}\n</section>' for i, (name, html) in enumerate(SCREENS, 1))
    doc = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Kuhle Bank screens</title><style>{CSS}</style></head><body>{screens}</body></html>'
    Path(__file__).with_name("screens.html").write_text(doc, encoding="utf-8")
    return len(SCREENS)


if __name__ == "__main__":
    print(build(), "screens")
