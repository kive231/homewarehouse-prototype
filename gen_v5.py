import os

with open("/home/dev/仓库原型/v5_css.css") as f:
    CSS = f.read()

FONT_URL = "https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap"

def nav(title, back=True, right=""):
    bk = f"<span class=\"nav-back\"><svg viewBox=\"0 0 24 24\"><use href=\"#i-back\"/></svg></span>" if back else ""
    r = f"<span class=\"nav-right\">{right}</span>" if right else ""
    return f"<div class=\"status\"><b>09:41</b><span>5G&nbsp;&nbsp;82%</span></div><div class=\"nav\">{bk}<b>{title}</b>{r}</div><main class=\"scroll\">"
def nav_end(): return "</main>"

BT={"home":"""<div class="tab active"><svg viewBox="0 0 24 24"><use href="#i-home"/></svg><span>首页</span></div><div class="tab"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg><span>管理</span></div>""",
"manage":"""<div class="tab"><svg viewBox="0 0 24 24"><use href="#i-home"/></svg><span>首页</span></div><div class="tab active"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg><span>管理</span></div>""",
"items":"""<div class="tab"><svg viewBox="0 0 24 24"><use href="#i-home"/></svg><span>首页</span></div><div class="tab"><svg viewBox="0 0 24 24"><use href="#i-list"/></svg><span>物品</span></div>""",
"mine":"""<div class="tab"><svg viewBox="0 0 24 24"><use href="#i-home"/></svg><span>首页</span></div><div class="tab"><svg viewBox="0 0 24 24"><use href="#i-user"/></svg><span>我的</span></div>"""}
BT_TAIL="""<div class="tab"><svg viewBox="0 0 24 24"><use href="#i-list"/></svg><span>物品</span></div><div class="tab"><svg viewBox="0 0 24 24"><use href="#i-user"/></svg><span>我的</span></div>"""
SCAN="""<div class="scan-slot"><div class="scan-fab"><svg viewBox="0 0 24 24"><use href="#i-scan"/></svg></div></div>"""
def bottom(act): return f"<div class=\"bottom\">{BT[act]}{SCAN}{BT_TAIL}</div>"
def phone(b,ba=""): return f"<div class=\"phone\"><div class=\"screen\">{b}{bottom(ba) if ba else ""}</div></div>"
def shot(b,l,ba=""): return f"<section class=\"shot\"><div class=\"label\">{l}</div>{phone(b,ba)}</section>"
def shot_nav(t,b,l,ba="",bk=True,r=""): return shot(nav(t,bk,r)+f"<div class=\"content\">{b}</div>"+nav_end(),l,ba)

SVG="""<svg xmlns="http://www.w3.org/2000/svg" style="display:none"><defs>
<path id="i-home" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
<path id="i-box" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/>
<path id="i-user" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
<path id="i-search" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
<path id="i-scan" d="M12 4v1m6 11h2m-6 0h-2m4-8h2m-4 4h-2m0-8h-2m4 4h-2m-4 4h-2M4 16h2m0-8H4m2 4H4m8-8V3"/>
<path id="i-storage" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V7M3 7l9-4 9 4M3 7h18"/>
<path id="i-back" d="M15 19l-7-7 7-7"/>
<path id="i-settings" d="M12 15a3 3 0 100-6 3 3 0 000 6z"/><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 01-2.83 2.83l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-4 0v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83-2.83l.06-.06A1.65 1.65 0 004.68 15a1.65 1.65 0 00-1.51-1H3a2 2 0 010-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 012.83-2.83l.06.06A1.65 1.65 0 009 4.68a1.65 1.65 0 001-1.51V3a2 2 0 014 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 2.83l-.06.06A1.65 1.65 0 0019.4 9a1.65 1.65 0 001.51 1H21a2 2 0 010 4h-.09a1.65 1.65 0 00-1.51 1z"/>
<path id="i-qr" d="M6 6h5v5H6V6zm7 0h5v5h-5V6zm-7 7h5v5H6v-5zm7 0h5v5h-5v-5z"/>
<path id="i-export" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
<path id="i-clock" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
<path id="i-list" d="M4 6h16M4 10h16M4 14h16M4 18h16"/>
</defs></svg>"""

# Screens
login_s = shot("""<div class="login-wrap"><div class="login-logo"><svg viewBox="0 0 24 24"><use href="#i-storage"/></svg></div><div class="login-brand">HomeBox</div><div class="login-desc">手机号注册 · 扫码定位 · 消耗补货<br>一套管住家里所有物品</div><input class="login-field" placeholder="+86 手机号" value="138 **** 8888"><input class="login-field" placeholder="密码" type="password" value="••••••••"><button class="login-btn">登 录</button><button class="login-sub">使用验证码登录</button></div>""", "1. 登录")

home_s = shot("""<div class="content"><div class="search-pill"><svg viewBox="0 0 24 24"><use href="#i-search"/></svg><span>搜索物品、分类、位置、二维码</span></div>
<div class="hero-card"><small>今日概览</small><h2>128</h2><div class="sub">管理物品 · 5 空间 · 12 今日操作</div></div>
<div class="stats-row"><div class="card stat-card"><b>4</b><span>空间</span></div><div class="card stat-card warn"><b>3</b><span>临期</span></div><div class="card stat-card danger"><b>2</b><span>低库存</span></div><div class="card stat-card good"><b>12</b><span>今日操作</span></div></div>
<div class="insight"><b>⚡ 智能提醒</b><p>温莎颜料、美纹纸胶带、丙烯补充装 — 3 件物品临期 30 天内，建议本周处理</p></div>
<div class="section-head"><b>快捷操作</b><span></span></div>
<div class="action-grid"><div class="action-tile"><b>📦 新增物品</b><small>扫码或手动录入</small></div><div class="action-tile"><b>📋 消耗记录</b><small>最近 7 天消耗</small></div><div class="action-tile"><b>🔄 补货提醒</b><small>2 件需要补货</small></div><div class="action-tile"><b>🗂️ 分类浏览</b><small>5 大类 · 14 子类</small></div></div>
<div class="section-head"><b>最近使用</b><span>全部 →</span></div>
<div class="flex-col"><div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>温莎牛顿 24 色颜料</b><small>书房 A柜 · 2层 · 蓝盒</small></div><span class="tag warn">临期</span></div>
<div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>3M 美纹纸胶带</b><small>工具柜 · 1层</small></div><span class="tag">x4</span></div>
<div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>7号电池</b><small>储物间 · A层</small></div><span class="tag danger">低库存</span></div></div></div>""", "2. 首页", "home")

manage_s = shot("""<div class="content"><div class="search-pill"><svg viewBox="0 0 24 24"><use href="#i-search"/></svg><span>搜索柜子、分类、盒码</span></div>
<div class="section-head"><b>存储空间</b><span></span></div>
<div class="flex-col"><div class="space-row"><div class="space-icon"><svg viewBox="0 0 24 24"><use href="#i-storage"/></svg></div><div class="grow"><b>书房 A 柜</b><small>3层 · 8盒 · 46件</small></div></div>
<div class="space-row"><div class="space-icon"><svg viewBox="0 0 24 24"><use href="#i-storage"/></svg></div><div class="grow"><b>工具柜</b><small>2层 · 5盒 · 31件</small></div></div>
<div class="space-row"><div class="space-icon"><svg viewBox="0 0 24 24"><use href="#i-storage"/></svg></div><div class="grow"><b>储物间</b><small>2层 · 3盒 · 23件</small></div></div>
<div class="space-row" style="border-style:dashed;justify-content:center;color:var(--muted)"><b>+ 新增空间</b></div></div>
<div class="section-head"><b>存货分类</b><span></span></div>
<div class="flex-col"><div class="recent-item"><div class="cat-emoji">🎨</div><div class="grow"><b>画材</b><small>3子类 · 46件</small></div><span class="tag warn">临期</span></div>
<div class="recent-item"><div class="cat-emoji">🔧</div><div class="grow"><b>工具</b><small>2子类 · 31件</small></div><span class="tag good">正常</span></div>
<div class="recent-item"><div class="cat-emoji">✏</div><div class="grow"><b>文具</b><small>4子类 · 28件</small></div><span class="tag good">正常</span></div></div></div>""", "3. 管理", "manage")

items_s = shot("""<div class="content"><div class="search-pill"><svg viewBox="0 0 24 24"><use href="#i-search"/></svg><span>搜索名称、分类、位置</span></div>
<div class="toolbar"><span class="on">全部</span><span>画材</span><span>工具</span><span>文具</span><span>耗材</span></div>
<div class="flex-col"><div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>温莎牛顿 24色颜料</b><small>画材 · 书房A柜/2层/蓝盒</small></div><span class="tag warn">临期</span></div>
<div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>白夜固体水彩</b><small>画材 · 书房A柜/2层</small></div><span class="tag">x1</span></div>
<div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>丙烯颜料补充装</b><small>画材 · 工具柜/2层</small></div><span class="tag danger">低库存</span></div>
<div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>3M 美纹纸胶带</b><small>耗材 · 工具柜/1层</small></div><span class="tag">x4</span></div>
<div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>7号电池</b><small>耗材 · 储物间/A层</small></div><span class="tag danger">低库存</span></div></div></div>""", "4. 全部物料", "items")

mine_s = shot("""<div class="content"><div class="card mine-row" style="padding:16px;margin-bottom:4px"><div class="mine-avatar">曦</div><div><b style="font-size:17px;font-family:Poppins,sans-serif;display:block">曦曦</b><span style="font-size:11px;color:var(--muted)">个人版 · 管理员</span></div></div>
<div class="stats-row"><div class="card stat-card"><b>128</b><span>管理物品</span></div><div class="card stat-card good"><b>5</b><span>存储空间</span></div><div class="card stat-card"><b>86</b><span>已绑码</span></div></div>
<div class="section-head"><b>设置</b><span></span></div>
<div class="flex-col"><div class="mine-row"><div class="mine-ico"><svg viewBox="0 0 24 24"><use href="#i-user"/></svg></div><div class="grow"><b>个人资料</b><small>头像、昵称、安全</small></div><span class="mine-arrow">›</span></div>
<div class="mine-row"><div class="mine-ico"><svg viewBox="0 0 24 24"><use href="#i-settings"/></svg></div><div class="grow"><b>用户与偏好</b><small>主题、视图、提醒</small></div><span class="mine-arrow">›</span></div>
<div class="mine-row"><div class="mine-ico"><svg viewBox="0 0 24 24"><use href="#i-qr"/></svg></div><div class="grow"><b>二维码管理</b><small>生成、打印、绑定</small></div><span class="mine-arrow">›</span></div>
<div class="mine-row"><div class="mine-ico"><svg viewBox="0 0 24 24"><use href="#i-export"/></svg></div><div class="grow"><b>导入导出</b><small>Excel 备份与恢复</small></div><span class="mine-arrow">›</span></div>
<div class="mine-row"><div class="mine-ico"><svg viewBox="0 0 24 24"><use href="#i-clock"/></svg></div><div class="grow"><b>关于与帮助</b><small>v0.1 · 反馈</small></div><span class="mine-arrow">›</span></div></div></div>""", "24. 我的", "mine")

HTML = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>HomeBox V5 · Soft UI Evolution</title><link href="{FONT_URL}" rel="stylesheet"><style>{CSS}</style></head><body>{SVG}
<h1>HomeBox · 家庭仓库管理 — V5 Soft UI Evolution</h1>
<p class="subtitle">多层软阴影 · 靛紫渐变 · Poppins + Open Sans · WCAG AA+</p>
<div class="page"><div class="group-title"><span>一级页面</span></div><div class="row">{login_s}{home_s}{manage_s}{items_s}{mine_s}</div></div></body></html>"""

OUT = "/home/dev/仓库原型/index_v5.html"
with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"V5: {OUT} ({len(HTML)} bytes)")
