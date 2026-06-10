#!/usr/bin/env python3
"""HomeBox V3 — Bento Grid prototype. Generates single-file HTML."""

CSS = r'''
:root{--bg:#F5F5F7;--card:#FFFFFF;--ink:#1D1D1F;--muted:#6E6E73;--line:#E5E5EA;--accent:#2563EB;--accent2:#059669;--warn:#F59E0B;--red:#DC2626;--radius:22px;--radius-sm:14px;--shadow:0 2px 12px rgba(0,0,0,.04);--shadow-lg:0 8px 30px rgba(0,0,0,.06)}*{box-sizing:border-box;margin:0;padding:0}body{background:var(--bg);font-family:-apple-system,BlinkMacSystemFont,'PingFang SC',sans-serif;color:var(--ink);padding:40px 28px;-webkit-font-smoothing:antialiased}h1{font-size:28px;text-align:center;font-weight:700;letter-spacing:-.4px}.subtitle{text-align:center;color:var(--muted);font-size:13px;margin:8px 0 36px}.page{max-width:1560px;margin:0 auto;display:flex;flex-wrap:wrap;gap:32px;justify-content:center}.row{width:100%;display:flex;flex-wrap:wrap;gap:32px;justify-content:center}.shot{display:flex;flex-direction:column;align-items:center;gap:10px}.label{font-size:12px;color:var(--muted);background:var(--card);border:1px solid var(--line);padding:5px 14px;border-radius:999px;font-weight:600;box-shadow:var(--shadow)}.phone{width:290px;height:620px;background:#1D1D1F;border-radius:32px;padding:10px;box-shadow:0 20px 50px rgba(0,0,0,.12);position:relative}.phone::before{content:"";position:absolute;top:9px;left:50%;transform:translateX(-50%);width:76px;height:5px;background:#3A3A3C;border-radius:999px;z-index:2}.screen{height:100%;background:var(--bg);border-radius:24px;overflow:hidden;display:flex;flex-direction:column}.status{height:30px;display:flex;align-items:center;justify-content:space-between;padding:0 20px;background:rgba(245,245,247,.92);backdrop-filter:blur(20px);font-size:11px;font-weight:600;flex-shrink:0}.nav{height:50px;background:rgba(245,245,247,.88);backdrop-filter:blur(20px);display:flex;align-items:center;gap:10px;padding:0 16px;flex-shrink:0;border-bottom:.5px solid var(--line)}.nav b{font-size:15px;font-weight:650}.nav-back{color:var(--accent);width:30px;height:30px;display:flex;align-items:center;justify-content:center;background:rgba(37,99,235,.08);border-radius:999px}.nav-right{margin-left:auto;color:var(--accent);font-size:12px;font-weight:600}.scroll{flex:1;min-height:0;overflow:auto}.scroll::-webkit-scrollbar{display:none}.content{padding:16px;display:flex;flex-direction:column;gap:14px;padding-bottom:80px}.bottom{height:60px;background:rgba(245,245,247,.92);backdrop-filter:blur(24px);border-top:.5px solid var(--line);display:flex;align-items:center;flex-shrink:0}.tab{flex:1;text-align:center;color:#8E8E93;font-size:10px;display:flex;flex-direction:column;align-items:center;gap:3px;font-weight:500}.tab.active{color:var(--accent)}.scan-slot{width:60px;position:relative;display:flex;justify-content:center}.scan-fab{position:absolute;bottom:8px;width:52px;height:52px;border-radius:18px;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 20px rgba(37,99,235,.25);border:3px solid var(--bg)}svg{width:18px;height:18px;fill:currentColor}.scan-fab svg{width:22px;height:22px}.bento-grid{display:grid;gap:12px}.bento-2{grid-template-columns:1fr 1fr}.bento-3{grid-template-columns:1fr 1fr 1fr}.bento-hero{display:grid;gap:12px;grid-template-columns:2fr 1fr}.card{background:var(--card);border-radius:var(--radius);padding:16px;box-shadow:var(--shadow);border:.5px solid rgba(0,0,0,.04)}.home-hero{background:linear-gradient(135deg,#1E3A6E,#2563EB);color:#fff;border-radius:var(--radius);padding:18px}.home-hero h2{font-size:26px;font-weight:700;margin:4px 0;letter-spacing:-.4px}.home-hero small{opacity:.82;font-size:11px}.search-pill{height:42px;background:var(--card);border:.5px solid var(--line);border-radius:var(--radius-sm);display:flex;align-items:center;gap:8px;padding:0 16px;color:var(--muted);font-size:12px;box-shadow:var(--shadow)}.stat-card{text-align:center}.stat-card b{display:block;font-size:26px;font-weight:700;letter-spacing:-.5px}.stat-card span{font-size:10px;color:var(--muted);margin-top:2px;display:block}.stat-card.warn b{color:var(--warn)}.stat-card.danger b{color:var(--red)}.insight{background:linear-gradient(135deg,#EFF6FF,#F0FDF4);border:.5px solid rgba(37,99,235,.12);border-radius:var(--radius);padding:16px}.insight b{font-size:14px;display:block;margin-bottom:4px}.insight p{font-size:11px;color:var(--muted);line-height:1.5}.action-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}.action-tile{background:var(--card);border:.5px solid var(--line);border-radius:var(--radius);padding:14px;box-shadow:var(--shadow);display:flex;flex-direction:column;gap:6px;min-height:72px;justify-content:center}.action-tile b{font-size:12px}.action-tile small{font-size:10px;color:var(--muted);display:block}.recent-list{display:flex;flex-direction:column}.recent-item{display:flex;align-items:center;gap:10px;padding:13px 0;border-bottom:.5px solid var(--line)}.recent-item:last-child{border-bottom:0}.recent-avatar{width:36px;height:36px;border-radius:12px;background:rgba(37,99,235,.08);color:var(--accent);display:flex;align-items:center;justify-content:center;flex-shrink:0}.grow{flex:1;min-width:0}.grow b{font-size:13px;display:block;font-weight:600}.grow small{font-size:10px;color:var(--muted);display:block;margin-top:2px}.tag{font-size:9px;border-radius:999px;padding:3px 8px;font-weight:600;background:rgba(37,99,235,.08);color:var(--accent);white-space:nowrap}.tag.warn{background:rgba(245,158,11,.1);color:var(--warn)}.tag.danger{background:rgba(220,38,38,.08);color:var(--red)}.tag.good{background:rgba(5,150,105,.08);color:var(--accent2)}.section-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:-4px}.section-head b{font-size:14px;font-weight:650}.section-head span{font-size:11px;color:var(--accent);font-weight:600}.space-card{padding:14px;display:flex;align-items:center;gap:10px}.space-icon{width:40px;height:40px;border-radius:14px;background:rgba(37,99,235,.06);color:var(--accent);display:flex;align-items:center;justify-content:center;flex-shrink:0}.cat-emoji{font-size:22px;width:40px;height:40px;display:flex;align-items:center;justify-content:center;border-radius:14px;background:rgba(37,99,235,.05);flex-shrink:0}.toolbar{display:flex;gap:6px;overflow-x:auto}.toolbar span{padding:7px 13px;border-radius:999px;font-size:11px;font-weight:600;background:var(--card);color:var(--muted);white-space:nowrap;border:.5px solid var(--line)}.toolbar .on{background:var(--accent);color:#fff;border-color:var(--accent)}.mine-hero{display:flex;align-items:center;gap:14px}.mine-avatar{width:62px;height:62px;border-radius:20px;background:linear-gradient(135deg,#2563EB,#7C3AED);color:#fff;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700}.mine-hero h2{font-size:18px;margin-bottom:2px}.mine-hero p{font-size:11px;color:var(--muted)}.mine-item{display:flex;align-items:center;gap:12px;padding:14px 0;border-bottom:.5px solid var(--line)}.mine-item:last-child{border-bottom:0}.mine-ico{width:40px;height:40px;border-radius:14px;background:rgba(37,99,235,.06);color:var(--accent);display:flex;align-items:center;justify-content:center;flex-shrink:0}.mine-arrow{color:var(--muted);margin-left:auto;font-size:20px}.login-wrap{height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:40px 28px}.login-logo{width:68px;height:68px;border-radius:20px;background:linear-gradient(135deg,#2563EB,#7C3AED);color:#fff;display:flex;align-items:center;justify-content:center;margin-bottom:18px;box-shadow:0 12px 30px rgba(37,99,235,.2)}.login-logo svg{width:32px;height:32px}.login-brand{font-size:22px;font-weight:700;letter-spacing:-.3px;margin-bottom:6px}.login-desc{font-size:12px;color:var(--muted);margin-bottom:28px;text-align:center}.login-field{width:100%;height:48px;background:var(--card);border:.5px solid var(--line);border-radius:var(--radius-sm);padding:0 16px;font-size:14px;color:var(--ink);outline:none;margin-bottom:12px}.login-btn{width:100%;height:48px;border:none;border-radius:var(--radius-sm);background:var(--accent);color:#fff;font-size:15px;font-weight:650;box-shadow:0 6px 18px rgba(37,99,235,.18)}.login-sub{width:100%;height:48px;border:.5px solid var(--line);border-radius:var(--radius-sm);background:var(--card);color:var(--accent);font-size:14px;font-weight:600;margin-top:10px}.group-title{width:100%;max-width:1560px;margin:24px auto 4px;display:flex;align-items:center;gap:12px;color:var(--ink);font-size:15px;font-weight:700}.group-title::after{content:"";flex:1;height:.5px;background:var(--line)}
'''

def nav(title, back=True, right=""):
    bk = f'<span class="nav-back"><svg viewBox="0 0 24 24"><use href="#i-back"/></svg></span>' if back else ""
    r = f'<span class="nav-right">{right}</span>' if right else ""
    return f'<div class="status"><b>09:41</b><span>5G&nbsp;&nbsp;82%</span></div><div class="nav">{bk}<b>{title}</b>{r}</div><main class="scroll">'

def nav_end():
    return '</main>'

BTABS = {
    "home": ('<div class="tab active"><svg viewBox="0 0 24 24"><use href="#i-home"/></svg><span>首页</span></div><div class="tab"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg><span>管理</span></div>'),
    "manage": ('<div class="tab"><svg viewBox="0 0 24 24"><use href="#i-home"/></svg><span>首页</span></div><div class="tab active"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg><span>管理</span></div>'),
    "items": ('<div class="tab"><svg viewBox="0 0 24 24"><use href="#i-home"/></svg><span>首页</span></div><div class="tab"><svg viewBox="0 0 24 24"><use href="#i-list"/></svg><span>物品</span></div>'),
    "mine": ('<div class="tab"><svg viewBox="0 0 24 24"><use href="#i-home"/></svg><span>首页</span></div><div class="tab"><svg viewBox="0 0 24 24"><use href="#i-user"/></svg><span>我的</span></div>'),
}

BTABS_TAIL = ('<div class="tab"><svg viewBox="0 0 24 24"><use href="#i-list"/></svg><span>物品</span></div><div class="tab"><svg viewBox="0 0 24 24"><use href="#i-user"/></svg><span>我的</span></div>')

def bottom(active):
    b = BTABS.get(active, BTABS["home"])
    scan = '<div class="scan-slot"><div class="scan-fab"><svg viewBox="0 0 24 24"><use href="#i-scan"/></svg></div></div>'
    return f'<div class="bottom">{b}{scan}{BTABS_TAIL}</div>'

def phone(body, b_act=""):
    b = bottom(b_act) if b_act else ""
    return f'<div class="phone"><div class="screen">{body}{b}</div></div>'

def shot(body, lbl, b_act=""):
    return f'<section class="shot"><div class="label">{lbl}</div>{phone(body, b_act)}</section>'

def shot_nav(title, body, lbl, back=True, right="", b_act=""):
    return shot(nav(title, back, right) + '<div class="content">' + body + '</div>' + nav_end(), lbl, b_act)

# === SCREENS ===

login_s = shot('''<div class="login-wrap"><div class="login-logo"><svg viewBox="0 0 24 24"><use href="#i-storage"/></svg></div><div class="login-brand">HomeBox</div><div class="login-desc">扫一扫 · 精准定位 · 消耗补货<br>一套管住家里所有物品</div><input class="login-field" placeholder="+86 手机号" value="138 **** 8888"><input class="login-field" placeholder="密码" type="password" value="••••••••" style="margin-top:0"><button class="login-btn">登 录</button><button class="login-sub">使用验证码登录</button></div>''', "1. 登录")

home_s = shot('''<div class="content">
<div class="bento-grid bento-hero"><div class="home-hero"><small>今日概览</small><h2>128</h2><small>管理物品 · 5 空间</small></div><div class="card stat-card" style="align-self:stretch;display:flex;flex-direction:column;justify-content:center"><b style="font-size:20px">3</b><span>临期提醒</span></div></div>
<div class="bento-grid bento-3"><div class="card stat-card"><b>4</b><span>空间</span></div><div class="card stat-card warn"><b>3</b><span>临期</span></div><div class="card stat-card danger"><b>2</b><span>低库存</span></div></div>
<div class="search-pill"><svg viewBox="0 0 24 24"><use href="#i-search"/></svg><span>搜索物品、分类、位置</span></div>
<div class="insight"><b>&#x26A1; 智能提醒</b><p>温莎颜料 · 美纹纸胶带 · 丙烯补充装 — 3件物品30天内临期</p></div>
<div class="section-head"><b>快捷操作</b><span></span></div>
<div class="action-grid"><div class="action-tile"><b>&#x1F4E6; 新增物品</b><small>扫码或手动录入</small></div><div class="action-tile"><b>&#x1F4CB; 消耗记录</b><small>最近7天</small></div><div class="action-tile"><b>&#x1F504; 补货提醒</b><small>2件需补货</small></div><div class="action-tile"><b>&#x1F5C2; 分类浏览</b><small>5大类</small></div></div>
<div class="section-head"><b>最近使用</b><span>全部 &#x2192;</span></div>
<div class="recent-list">
<div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>温莎牛顿 24 色颜料</b><small>书房 A柜 · 2层 · 蓝盒</small></div><span class="tag warn">临期</span></div>
<div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>3M 美纹纸胶带</b><small>工具柜 · 1层</small></div><span class="tag">x4</span></div>
<div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>7号电池</b><small>储物间 · A层</small></div><span class="tag danger">低库存</span></div>
</div></div>''', "2. 首页", "home")

manage_s = shot('''<div class="content"><div class="search-pill"><svg viewBox="0 0 24 24"><use href="#i-search"/></svg><span>搜索柜子、分类、盒码</span></div>
<div class="section-head"><b>存储空间</b><span></span></div>
<div class="bento-grid bento-2">
<div class="card space-card"><div class="space-icon"><svg viewBox="0 0 24 24"><use href="#i-storage"/></svg></div><div class="grow"><b>书房 A 柜</b><small>3层 · 8盒 · 46件</small></div></div>
<div class="card space-card"><div class="space-icon"><svg viewBox="0 0 24 24"><use href="#i-storage"/></svg></div><div class="grow"><b>工具柜</b><small>2层 · 5盒 · 31件</small></div></div>
<div class="card space-card"><div class="space-icon"><svg viewBox="0 0 24 24"><use href="#i-storage"/></svg></div><div class="grow"><b>储物间</b><small>2层 · 3盒 · 23件</small></div></div>
<div class="card space-card" style="border-style:dashed;justify-content:center;color:var(--muted);text-align:center"><b>+ 新增空间</b></div>
</div>
<div class="section-head"><b>存货分类</b><span></span></div>
<div class="recent-list">
<div class="recent-item"><div class="cat-emoji">&#x1F3A8;</div><div class="grow"><b>画材</b><small>3子类 · 46件</small></div><span class="tag warn">临期</span></div>
<div class="recent-item"><div class="cat-emoji">&#x1F527;</div><div class="grow"><b>工具</b><small>2子类 · 31件</small></div><span class="tag good">正常</span></div>
<div class="recent-item"><div class="cat-emoji">&#x270F;&#xFE0F;</div><div class="grow"><b>文具</b><small>4子类 · 28件</small></div><span class="tag good">正常</span></div>
</div></div>''', "3. 管理", "manage")

items_s = shot('''<div class="content"><div class="search-pill"><svg viewBox="0 0 24 24"><use href="#i-search"/></svg><span>搜索名称、分类、位置</span></div>
<div class="toolbar"><span class="on">全部</span><span>画材</span><span>工具</span><span>文具</span><span>耗材</span></div>
<div class="recent-list">
<div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>温莎牛顿 24色颜料</b><small>画材 · 书房A柜/2层/蓝盒</small></div><span class="tag warn">临期</span></div>
<div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>白夜固体水彩</b><small>画材 · 书房A柜/2层</small></div><span class="tag">x1</span></div>
<div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>丙烯颜料补充装</b><small>画材 · 工具柜/2层</small></div><span class="tag danger">低库存</span></div>
<div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>3M 美纹纸胶带</b><small>耗材 · 工具柜/1层</small></div><span class="tag">x4</span></div>
<div class="recent-item"><div class="recent-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>7号电池</b><small>耗材 · 储物间/A层</small></div><span class="tag danger">低库存</span></div>
</div></div>''', "4. 全部物料", "items")

mine_s = shot('''<div class="content"><div class="card mine-hero"><div class="mine-avatar">&#x66E6;</div><div><h2>曦曦</h2><p>个人版 · 管理员</p></div></div>
<div class="bento-grid bento-3"><div class="card stat-card"><b>128</b><span>管理物品</span></div><div class="card stat-card"><b>5</b><span>存储空间</span></div><div class="card stat-card"><b>86</b><span>已绑码</span></div></div>
<div class="section-head"><b>设置</b><span></span></div>
<div class="recent-list">
<div class="mine-item"><div class="mine-ico"><svg viewBox="0 0 24 24"><use href="#i-user"/></svg></div><div class="grow"><b>个人资料</b><small>头像、昵称、安全</small></div><span class="mine-arrow">&#x203A;</span></div>
<div class="mine-item"><div class="mine-ico"><svg viewBox="0 0 24 24"><use href="#i-settings"/></svg></div><div class="grow"><b>用户与偏好</b><small>主题、视图、提醒</small></div><span class="mine-arrow">&#x203A;</span></div>
<div class="mine-item"><div class="mine-ico"><svg viewBox="0 0 24 24"><use href="#i-qr"/></svg></div><div class="grow"><b>二维码管理</b><small>生成、打印、绑定</small></div><span class="mine-arrow">&#x203A;</span></div>
<div class="mine-item"><div class="mine-ico"><svg viewBox="0 0 24 24"><use href="#i-export"/></svg></div><div class="grow"><b>导入导出</b><small>Excel 备份与恢复</small></div><span class="mine-arrow">&#x203A;</span></div>
<div class="mine-item"><div class="mine-ico"><svg viewBox="0 0 24 24"><use href="#i-clock"/></svg></div><div class="grow"><b>关于与帮助</b><small>v0.1 · 反馈</small></div><span class="mine-arrow">&#x203A;</span></div>
</div></div>''', "24. 我的", "mine")

# === ASSEMBLE ===
SVG_ICONS = '''<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
<defs>
<path id="i-home" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
<path id="i-box" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/>
<path id="i-user" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
<path id="i-search" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
<path id="i-scan" d="M12 4v1m6 11h2m-6 0h-2m4-8h2m-4 4h-2m0-8h-2m4 4h-2m-4 4h-2M4 16h2m0-8H4m2 4H4m8-8V3"/>
<path id="i-storage" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V7M3 7l9-4 9 4M3 7h18"/>
<path id="i-back" d="M15 19l-7-7 7-7"/>
<path id="i-settings" d="M10.325 4.317a1.724 1.724 0 013.35 0 1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.066 2.573c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.573 1.066c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.066-2.573c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37a1.724 1.724 0 002.573-1.065z"/><circle cx="12" cy="12" r="3" id="i-settings-c"/>
<path id="i-qr" d="M6 6h5v5H6V6zm7 0h5v5h-5V6zm-7 7h5v5H6v-5zm7 0h5v5h-5v-5z"/>
<path id="i-export" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
<path id="i-clock" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
<path id="i-list" d="M4 6h16M4 10h16M4 14h16M4 18h16"/>
</defs></svg>'''

HTML = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>HomeBox V3 · Bento Grid</title><style>{CSS}</style></head><body>{SVG_ICONS}
<h1>HomeBox · 家庭仓库管理 — 原型 V3</h1>
<p class="subtitle">Bento Grid 风格 · Apple 质感 · 5 个一级页面</p>
<div class="page">
<div class="group-title"><span>一级页面</span></div>
<div class="row">{login_s}{home_s}{manage_s}{items_s}{mine_s}</div>
</div></body></html>'''

OUT = "/home/dev/仓库原型/index_v3.html"
import os
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"Generated: {OUT} ({len(HTML)} bytes)")
print("Done!")
