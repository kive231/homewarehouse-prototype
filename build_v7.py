#!/usr/bin/env python3
"""HomeBox V7 — Matched to reference: lavender purple accent, white/grey BG, compact UI."""
import os

CSS = r'''
:root{--bg:#F0F0F0;--card:#FFFFFF;--ink:#3A3A3A;--muted:#989898;--line:#E0E0E0;--accent:#A098F0;--accent2:#8B7CF6;--good:#34C759;--warn:#FF9500;--red:#FF3B30;--radius:12px;--radius-sm:8px;--shadow:0 2px 8px rgba(0,0,0,.06)}
*{box-sizing:border-box;margin:0;padding:0}body{background:var(--bg);font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;color:var(--ink);padding:40px 28px;min-height:100vh}h1{font-size:26px;text-align:center;font-weight:700;letter-spacing:-.3px}.subtitle{text-align:center;color:var(--muted);font-size:13px;margin:6px 0 34px}.page{max-width:1560px;margin:0 auto;display:flex;flex-wrap:wrap;gap:30px;justify-content:center}.row{width:100%;display:flex;flex-wrap:wrap;gap:30px;justify-content:center}.shot{display:flex;flex-direction:column;align-items:center;gap:8px}.label{font-size:11px;color:var(--muted);background:var(--card);border:1px solid var(--line);padding:4px 12px;border-radius:999px;font-weight:600}.phone{width:286px;height:618px;background:#1C1C1E;border-radius:36px;padding:10px;box-shadow:0 24px 48px rgba(0,0,0,.12);position:relative}.phone::before{content:"";position:absolute;top:10px;left:50%;transform:translateX(-50%);width:76px;height:5px;background:#3A3A3C;border-radius:999px;z-index:2}.screen{height:100%;background:var(--bg);border-radius:28px;overflow:hidden;display:flex;flex-direction:column}.status{height:28px;display:flex;align-items:center;justify-content:space-between;padding:0 16px;font-size:10px;font-weight:600;flex-shrink:0;color:var(--muted);background:#F0F0F0}.nav{height:44px;background:#FFFFFF;display:flex;align-items:center;gap:8px;padding:0 14px;flex-shrink:0;border-bottom:1px solid var(--line)}.nav b{font-size:16px;font-weight:600;letter-spacing:-.2px}.nav-back{width:28px;height:28px;display:flex;align-items:center;justify-content:center;flex-shrink:0}.scroll{flex:1;min-height:0;overflow:auto}.scroll::-webkit-scrollbar{display:none}.content{padding:12px;display:flex;flex-direction:column;gap:10px}.bottom{height:56px;background:#FFFFFF;border-top:1px solid var(--line);display:flex;align-items:center;flex-shrink:0;padding:0 4px}.tab{flex:1;text-align:center;color:#B0B0B0;font-size:9px;display:flex;flex-direction:column;align-items:center;gap:2px;font-weight:500}.tab.active{color:var(--accent)}.scan-slot{width:56px;position:relative;display:flex;justify-content:center;align-items:flex-end}.scan-btn{width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,#A59AF0,#8B7CF6);color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 16px rgba(139,124,246,.3);border:3px solid var(--bg)}svg{width:18px;height:18px;fill:currentColor}.scan-btn svg{width:22px;height:22px}
.card{background:var(--card);border-radius:var(--radius);box-shadow:var(--shadow)}.search-bar{height:38px;background:#ECECEE;border-radius:10px;display:flex;align-items:center;gap:6px;padding:0 12px;color:var(--muted);font-size:13px}.search-bar svg{width:14px;height:14px}.search-bar span{color:#B0B0B0}
.head-row{display:flex;align-items:center;justify-content:space-between;gap:8px}.head-row b{font-size:17px;font-weight:650;letter-spacing:-.2px}.head-row svg{width:20px;height:20px;color:var(--ink)}.cat-scroll{display:flex;gap:8px;overflow-x:auto;padding:2px 0}.cat-tag{padding:6px 14px;border-radius:20px;font-size:12px;white-space:nowrap;background:#ECECEE;color:var(--muted);font-weight:500}.cat-tag.on{background:var(--accent);color:#fff}.item-card{display:flex;gap:10px;padding:12px;align-items:center}.item-thumb{width:56px;height:56px;border-radius:8px;background:#F0EFFA;display:flex;align-items:center;justify-content:center;flex-shrink:0;color:var(--accent);font-size:24px}.item-info{flex:1;min-width:0}.item-info b{font-size:14px;display:block;font-weight:600}.item-info small{font-size:11px;color:var(--muted);display:block;margin-top:1px}.item-row{display:flex;align-items:center;gap:4px;margin-top:2px}.item-row span{font-size:12px;color:var(--muted)}.item-row b{font-size:14px;font-weight:700}.item-row .price{font-size:12px;color:var(--muted);margin-left:auto}.action-btn{height:28px;padding:0 12px;border-radius:14px;border:1px solid var(--accent);color:var(--accent);font-size:11px;font-weight:600;background:transparent;display:flex;align-items:center;gap:3px}.action-btn svg{width:12px;height:12px}.icon-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.icon-cell{text-align:center;padding:14px 6px;background:var(--card);border-radius:var(--radius);box-shadow:var(--shadow);display:flex;flex-direction:column;align-items:center;gap:6px;font-size:11px;color:var(--ink);font-weight:500}.icon-cell .ico{width:44px;height:44px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:22px}.stats-bar{display:flex;align-items:center;justify-content:space-between;background:var(--card);border-radius:var(--radius);padding:14px;box-shadow:var(--shadow)}.stats-bar b{font-size:15px}.stats-bar span{font-size:11px;color:var(--accent);font-weight:600}.chart-box{background:var(--card);border-radius:var(--radius);padding:14px;box-shadow:var(--shadow);display:flex;align-items:flex-end;gap:6px;height:120px}.chart-bar{flex:1;background:var(--accent);border-radius:4px 4px 0 0;min-width:12px}.chart-bar.short{height:30%}.chart-bar.mid{height:55%}.chart-bar.tall{height:80%}.chart-bar.full{height:100%}.section-head{display:flex;align-items:center;justify-content:space-between;margin:2px 0 -4px}.section-head b{font-size:14px;font-weight:600}.section-head span{font-size:11px;color:var(--accent);font-weight:500}.col{display:flex;flex-direction:column;gap:8px}.login-screen{height:100%;background:#FFFFFF;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:40px 28px}.login-icon{width:64px;height:64px;border-radius:16px;background:linear-gradient(135deg,#A59AF0,#8B7CF6);color:#fff;display:flex;align-items:center;justify-content:center;margin-bottom:16px;box-shadow:0 8px 24px rgba(139,124,246,.2)}.login-icon svg{width:30px;height:30px}.login-brand{font-size:20px;font-weight:700;letter-spacing:-.2px;margin-bottom:6px}.login-desc{font-size:12px;color:var(--muted);margin-bottom:26px;text-align:center;line-height:1.5}.login-field{width:100%;height:48px;background:#F5F5F7;border:1px solid #E5E5EA;border-radius:10px;padding:0 14px;font-size:14px;color:var(--ink);outline:none;margin-bottom:12px}.login-btn{width:100%;height:48px;border:none;border-radius:10px;background:var(--accent);color:#fff;font-size:15px;font-weight:600}.login-sub{width:100%;height:48px;border:1px solid var(--line);border-radius:10px;background:#fff;color:var(--muted);font-size:14px;font-weight:500;margin-top:8px}.group-title{width:100%;max-width:1560px;margin:22px auto 4px;display:flex;align-items:center;gap:12px;color:var(--ink);font-size:14px;font-weight:700}.group-title::after{content:"";flex:1;height:1px;background:var(--line)}
'''

SVG = r'''<svg xmlns="http://www.w3.org/2000/svg" style="display:none"><defs>
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
<path id="i-chart" d="M18 20V10M12 20V4M6 20v-6"/>
</defs></svg>'''

BOTTOM = '''<div class="bottom">
<div class="tab active"><svg viewBox="0 0 24 24"><use href="#i-home"/></svg><span>首页</span></div>
<div class="tab"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg><span>物品</span></div>
<div class="scan-slot"><div class="scan-btn"><span style="font-size:24px;line-height:1">+</span></div></div>
<div class="tab"><svg viewBox="0 0 24 24"><use href="#i-list"/></svg><span>记录</span></div>
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
<div class="nav"><b>我的仓库</b><span style="margin-left:auto;color:var(--muted)"><svg viewBox="0 0 24 24" width="20" height="20"><use href="#i-settings"/></svg></span></div>
<div class="content">
<div class="search-bar"><svg viewBox="0 0 24 24"><use href="#i-search"/></svg><span>搜索</span></div>
<div class="icon-grid">
<div class="icon-cell"><div class="ico" style="background:#F0EEFF;color:var(--accent)">&#x1F4E6;</div>全部商品</div>
<div class="icon-cell"><div class="ico" style="background:#FFF3E0;color:#FF9500">&#x1F4E5;</div>待入库</div>
<div class="icon-cell"><div class="ico" style="background:#FFEBEE;color:#FF3B30">&#x26A0;</div>缺货预警</div>
<div class="icon-cell"><div class="ico" style="background:#E8F5E9;color:#34C759">&#x1F4CA;</div>积压库存</div>
<div class="icon-cell"><div class="ico" style="background:#F0EEFF;color:var(--accent)">&#x1F4CB;</div>库存盘点</div>
<div class="icon-cell"><div class="ico" style="background:#FFF3E0;color:#FF9500">&#x1F504;</div>调拨管理</div>
<div class="icon-cell"><div class="ico" style="background:#E8F5E9;color:#34C759">&#x1F4E4;</div>出库记录</div>
<div class="icon-cell"><div class="ico" style="background:#F0EEFF;color:var(--accent)">&#x1F3F7;</div>分类管理</div>
</div>
<div class="stats-bar"><div><b>商品总数</b><span style="display:block;font-size:11px;color:var(--muted);margin-top:2px">150 件</span></div><span>查看全部 &#x203A;</span></div>
<div class="chart-box">
<div class="chart-bar short"></div><div class="chart-bar mid"></div><div class="chart-bar tall"></div><div class="chart-bar short"></div><div class="chart-bar full"></div><div class="chart-bar mid"></div><div class="chart-bar short"></div>
</div>
</div>''' + BOTTOM + '''</div></div></section>'''

HTML = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>HomeBox V7</title><style>{CSS}</style></head><body>{SVG}
<h1>HomeBox · 家庭仓库管理 — V7</h1>
<p class="subtitle">薰衣草紫 · 匹配参考风格 · 登录 + 首页</p>
<div class="page"><div class="group-title"><span>一级页面</span></div><div class="row">{login_html}{home_html}</div></div></body></html>'''

OUT = "/home/dev/仓库原型/index_v7.html"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"V7: {OUT} ({len(HTML)} bytes)")
print("DONE")