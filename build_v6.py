#!/usr/bin/env python3
"""HomeBox V6 — Soft UI Evolution. Login + Home only."""
import os

CSS = r'''
:root{--bg:#F0F4F8;--card:#FFFFFF;--ink:#1A202C;--muted:#64748B;--line:#E2E8F0;--accent:#4F46E5;--accent2:#7C3AED;--good:#059669;--warn:#D97706;--red:#DC2626;--radius:16px;--radius-sm:12px;--shadow-sm:0 1px 3px rgba(0,0,0,.04),0 1px 2px rgba(0,0,0,.06);--shadow:0 4px 6px rgba(0,0,0,.04),0 2px 4px rgba(0,0,0,.04);--shadow-lg:0 10px 15px rgba(0,0,0,.06),0 4px 6px rgba(0,0,0,.04);--shadow-accent:0 4px 14px rgba(79,70,229,.15);--shadow-inset:inset 0 2px 4px rgba(0,0,0,.04)}
*{box-sizing:border-box;margin:0;padding:0}body{background:linear-gradient(180deg,#F8FAFC,#E8EDF2);font-family:"Open Sans",-apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif;color:var(--ink);padding:40px 28px;min-height:100vh;-webkit-font-smoothing:antialiased}h1{font-size:28px;text-align:center;font-weight:700;letter-spacing:-.4px;font-family:Poppins,sans-serif}.subtitle{text-align:center;color:var(--muted);font-size:13px;margin:8px 0 36px}.page{max-width:1560px;margin:0 auto;display:flex;flex-wrap:wrap;gap:34px;justify-content:center}.row{width:100%;display:flex;flex-wrap:wrap;gap:34px;justify-content:center}.shot{display:flex;flex-direction:column;align-items:center;gap:10px}.label{font-size:11px;color:var(--muted);background:var(--card);border:1px solid var(--line);padding:5px 14px;border-radius:999px;font-weight:600;box-shadow:var(--shadow-sm)}.phone{width:292px;height:624px;background:#1E293B;border-radius:34px;padding:11px;box-shadow:0 30px 60px rgba(15,23,42,.12);position:relative}.phone::before{content:"";position:absolute;top:10px;left:50%;transform:translateX(-50%);width:80px;height:5px;background:#334155;border-radius:999px;z-index:2}.screen{height:100%;background:var(--bg);border-radius:26px;overflow:hidden;display:flex;flex-direction:column}.status{height:32px;display:flex;align-items:center;justify-content:space-between;padding:0 20px;background:rgba(240,244,248,.92);backdrop-filter:blur(24px);font-size:11px;font-weight:600;flex-shrink:0;color:var(--muted);border-bottom:1px solid rgba(226,232,240,.5)}.nav{height:52px;background:rgba(240,244,248,.9);backdrop-filter:blur(24px);display:flex;align-items:center;gap:10px;padding:0 16px;flex-shrink:0;border-bottom:1px solid rgba(226,232,240,.5)}.nav b{font-size:15px;font-weight:650;font-family:Poppins,sans-serif}.nav-back{color:var(--accent);width:32px;height:32px;display:flex;align-items:center;justify-content:center;background:rgba(79,70,229,.06);border-radius:10px}.scroll{flex:1;min-height:0;overflow:auto}.scroll::-webkit-scrollbar{display:none}.content{padding:16px;display:flex;flex-direction:column;gap:14px;padding-bottom:80px}.bottom{height:64px;background:rgba(240,244,248,.96);backdrop-filter:blur(28px);border-top:1px solid rgba(226,232,240,.5);display:flex;align-items:center;flex-shrink:0}.tab{flex:1;text-align:center;color:#94A3B8;font-size:10px;display:flex;flex-direction:column;align-items:center;gap:3px;font-weight:500}.tab.active{color:var(--accent)}.scan-slot{width:62px;position:relative;display:flex;justify-content:center}.scan-fab{position:absolute;bottom:10px;width:54px;height:54px;border-radius:16px;background:linear-gradient(135deg,#4F46E5,#7C3AED);color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 24px rgba(79,70,229,.3);border:3px solid var(--bg)}svg{width:18px;height:18px;fill:currentColor}.scan-fab svg{width:24px;height:24px}.card{background:var(--card);border-radius:var(--radius);padding:16px;box-shadow:var(--shadow);border:1px solid rgba(226,232,240,.6)}.search-pill{height:44px;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);display:flex;align-items:center;gap:8px;padding:0 16px;color:var(--muted);font-size:12px;box-shadow:var(--shadow-sm)}.section-head{display:flex;align-items:center;justify-content:space-between;margin:2px 0 -4px}.section-head b{font-size:14px;font-weight:650;font-family:Poppins,sans-serif}.section-head span{font-size:11px;color:var(--accent);font-weight:600}.hero{background:linear-gradient(135deg,#4F46E5,#7C3AED);color:#fff;border-radius:18px;padding:22px;box-shadow:0 12px 30px rgba(79,70,229,.18),0 4px 8px rgba(0,0,0,.06)}.hero small{opacity:.82;font-size:11px;display:block;margin-bottom:4px;font-weight:500}.hero h2{font-size:32px;font-weight:700;margin:6px 0;font-family:Poppins,sans-serif;letter-spacing:-.5px}.hero .sub{font-size:11px;opacity:.78}.stats-row{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.stat{text-align:center;padding:14px 8px;box-shadow:var(--shadow-sm)}.stat b{display:block;font-size:22px;font-weight:700;font-family:Poppins,sans-serif;color:var(--ink)}.stat span{font-size:10px;color:var(--muted);margin-top:2px;display:block}.stat.warn b{color:var(--warn)}.stat.danger b{color:var(--red)}.stat.good b{color:var(--good)}.insight{background:linear-gradient(135deg,#EEF2FF,#F5F3FF);border:1px solid rgba(79,70,229,.1);border-radius:var(--radius);padding:16px;box-shadow:var(--shadow-sm)}.insight b{font-size:13px;display:block;margin-bottom:4px;color:var(--accent);font-family:Poppins,sans-serif}.insight p{font-size:11px;color:var(--muted);line-height:1.55}.action-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}.action-tile{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:14px;box-shadow:var(--shadow-sm);display:flex;flex-direction:column;gap:6px;min-height:76px;justify-content:center}.action-tile b{font-size:12px;color:var(--ink)}.action-tile small{font-size:10px;color:var(--muted);display:block}.row-item{display:flex;align-items:center;gap:10px;padding:14px;background:var(--card);border:1px solid var(--line);border-radius:var(--radius-sm);box-shadow:var(--shadow-sm)}.row-avatar{width:38px;height:38px;border-radius:12px;background:rgba(79,70,229,.06);color:var(--accent);display:flex;align-items:center;justify-content:center;flex-shrink:0}.grow{flex:1;min-width:0}.grow b{font-size:13px;display:block;font-weight:600;color:var(--ink)}.grow small{font-size:10px;color:var(--muted);display:block;margin-top:2px}.tag{font-size:9px;border-radius:999px;padding:4px 9px;font-weight:600;white-space:nowrap;background:rgba(79,70,229,.08);color:var(--accent)}.tag.warn{background:rgba(217,119,6,.08);color:var(--warn)}.tag.danger{background:rgba(220,38,38,.08);color:var(--red)}.tag.good{background:rgba(5,150,105,.08);color:var(--good)}.login-screen{height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:44px 30px;background:linear-gradient(180deg,#F0F4F8 0%,#FFFFFF 40%)}.login-icon{width:72px;height:72px;border-radius:20px;background:linear-gradient(135deg,#4F46E5,#7C3AED);color:#fff;display:flex;align-items:center;justify-content:center;margin-bottom:20px;box-shadow:0 14px 34px rgba(79,70,229,.22)}.login-icon svg{width:34px;height:34px}.login-brand{font-size:22px;font-weight:700;letter-spacing:-.3px;margin-bottom:6px;font-family:Poppins,sans-serif}.login-desc{font-size:12px;color:var(--muted);margin-bottom:30px;text-align:center;line-height:1.5}.login-field{width:100%;height:50px;background:var(--card);border:1px solid var(--line);border-radius:var(--radius-sm);padding:0 16px;font-size:14px;color:var(--ink);outline:none;margin-bottom:12px;box-shadow:var(--shadow-inset)}.login-btn{width:100%;height:50px;border:none;border-radius:var(--radius-sm);background:linear-gradient(135deg,#4F46E5,#7C3AED);color:#fff;font-size:15px;font-weight:650;box-shadow:0 8px 20px rgba(79,70,229,.2);font-family:Poppins,sans-serif;cursor:pointer}.login-sub{width:100%;height:50px;border:1px solid var(--line);border-radius:var(--radius-sm);background:var(--card);color:var(--muted);font-size:14px;font-weight:600;margin-top:10px;box-shadow:var(--shadow-sm);cursor:pointer}.group-title{width:100%;max-width:1560px;margin:26px auto 4px;display:flex;align-items:center;gap:12px;color:var(--ink);font-size:16px;font-weight:700;font-family:Poppins,sans-serif}.group-title::after{content:"";flex:1;height:1px;background:linear-gradient(90deg,var(--line),transparent)}.col{display:flex;flex-direction:column;gap:10px}
'''

SVG = '''<svg xmlns="http://www.w3.org/2000/svg" style="display:none"><defs>
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
</defs></svg>'''

BOTTOM = '''<div class="bottom">
<div class="tab active"><svg viewBox="0 0 24 24"><use href="#i-home"/></svg><span>首页</span></div>
<div class="tab"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg><span>物品</span></div>
<div class="scan-slot"><div class="scan-fab"><svg viewBox="0 0 24 24"><use href="#i-scan"/></svg></div></div>
<div class="tab"><svg viewBox="0 0 24 24"><use href="#i-storage"/></svg><span>分类</span></div>
<div class="tab"><svg viewBox="0 0 24 24"><use href="#i-user"/></svg><span>我的</span></div>
</div>'''

login_html = '''<section class="shot">
<div class="label">1. 登录</div>
<div class="phone"><div class="screen"><div class="login-screen">
<div class="login-icon"><svg viewBox="0 0 24 24"><use href="#i-storage"/></svg></div>
<div class="login-brand">HomeBox</div>
<div class="login-desc">手机号注册 · 扫码定位 · 消耗补货<br>一套管住家里所有物品</div>
<input class="login-field" placeholder="+86 手机号" value="138 **** 8888">
<input class="login-field" placeholder="密码" type="password" value="••••••••">
<button class="login-btn">登 录</button>
<button class="login-sub">使用验证码登录</button>
</div></div></div></section>'''

home_html = '''<section class="shot">
<div class="label">2. 首页</div>
<div class="phone"><div class="screen">
<div class="status"><b>09:41</b><span>5G&nbsp;&nbsp;82%</span></div>
<div class="content">
<div class="search-pill"><svg viewBox="0 0 24 24"><use href="#i-search"/></svg><span>搜索物品、分类、位置</span></div>
<div class="hero"><small>今日概览</small><h2>128</h2><div class="sub">管理物品 · 5 空间 · 12 今日操作</div></div>
<div class="stats-row">
  <div class="card stat"><b>4</b><span>空间</span></div>
  <div class="card stat warn"><b>3</b><span>临期</span></div>
  <div class="card stat danger"><b>2</b><span>低库存</span></div>
  <div class="card stat good"><b>12</b><span>今日操作</span></div>
</div>
<div class="insight"><b>&#x26A1; 智能提醒</b><p>温莎颜料、美纹纸胶带、丙烯补充装 — 3 件物品临期 30 天内，建议本周处理</p></div>
<div class="section-head"><b>快捷操作</b></div>
<div class="action-grid">
  <div class="action-tile"><b>&#x1F4E6; 新增物品</b><small>扫码或手动录入</small></div>
  <div class="action-tile"><b>&#x1F4CB; 消耗记录</b><small>最近 7 天</small></div>
  <div class="action-tile"><b>&#x1F504; 补货提醒</b><small>2 件需补货</small></div>
  <div class="action-tile"><b>&#x1F5C2; 分类浏览</b><small>5 大类</small></div>
</div>
<div class="section-head"><b>最近使用</b><span>全部 &#x2192;</span></div>
<div class="col">
  <div class="row-item"><div class="row-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>温莎牛顿 24 色颜料</b><small>书房 A柜 · 2层 · 蓝盒</small></div><span class="tag warn">临期</span></div>
  <div class="row-item"><div class="row-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>3M 美纹纸胶带</b><small>工具柜 · 1层</small></div><span class="tag">x4</span></div>
  <div class="row-item"><div class="row-avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><b>7号电池</b><small>储物间 · A层</small></div><span class="tag danger">低库存</span></div>
</div>
</div>''' + BOTTOM + '''</div></div></section>'''

HTML = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>HomeBox V6</title><link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet"><style>{CSS}</style></head><body>{SVG}
<h1>HomeBox · 家庭仓库管理 — V6</h1>
<p class="subtitle">Soft UI Evolution · 重构版 · 登录 + 首页</p>
<div class="page"><div class="group-title"><span>一级页面</span></div><div class="row">{login_html}{home_html}</div></div></body></html>'''

OUT = "/home/dev/仓库原型/index_v6.html"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"V6: {OUT} ({len(HTML)} bytes)")
print("DONE")
