#!/usr/bin/env python3
"""HomeBox V2 — self-contained generator. Reads CSS from v2_css.txt in same dir."""
import os

DIR = os.path.dirname(os.path.abspath(__file__))
CSS_PATH = os.path.join(DIR, "v2_css.txt")
OUT_PATH = os.path.join(DIR, "index_v2.html")

with open(CSS_PATH) as f:
    CSS = f.read()

SVG = '''<svg style="display:none"><defs>
<path id="i-home" d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline id="i-up" points="9 22 9 12 15 12 15 22"/>
<path id="i-box" d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline id="i-down" points="3.27 6.96 12 12.01 20.73 6.96"/>
<line id="i-map" x1="12" y1="2" x2="12" y2="22"/><path id="i-search" d="M21 21l-6-6m2-5a7 7 0 1 1-14 0 7 7 0 0 1 14 0z"/>
<path id="i-plus" d="M12 5v14m-7-7h14"/><path id="i-scan" d="M3 7V5a2 2 0 012-2h2m10 0h2a2 2 0 012 2v2m0 10v2a2 2 0 01-2 2h-2m-10 0H5a2 2 0 01-2-2v-2"/>
<path id="i-user" d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>
<path id="i-back" d="M19 12H5m7-7l-7 7 7 7"/>
<path id="i-storage" d="M3 10h18M3 10l3-6h12l3 6M3 10v9a2 2 0 002 2h14a2 2 0 002-2v-9"/>
<path id="i-tag" d="M7 7h.01M2 2h7l13 13-7 7L2 9V2z"/>
<path id="i-settings" d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z" id="i-gear"/>
<path id="i-list" d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>
<path id="i-clock" d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/><path d="M12 6v6l4 2"/>
<path id="i-export" d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/>
<path id="i-qr" d="M5 5h5v5H5zM14 5h5v5h-5zM5 14h5v5H5zM14 17v-2a2 2 0 1 1 4 0v2m-4 2h4"/></defs></svg>'''

def ic(name):
    return '<svg viewBox="0 0 24 24"><use href="#{}"/></svg>'.format(name)

def L(text):
    return '<div class="label">{}</div>'.format(text)

def phone_body(inner):
    return '<div class="phone"><div class="screen">{}</div></div>'.format(inner)

def shot(inner, lbl):
    return '<section class="shot">{}<div class="phone"><div class="screen">{}</div></div></section>'.format(L(lbl), inner)

def bottom_bar(active="home"):
    tabs = [("home","首页","i-home"),("manage","管理","i-box"),("items","物品","i-list"),("mine","我的","i-user")]
    p = []
    for k,l,i in tabs:
        a = " active" if k==active else ""
        p.append('<div class="tab{}">{}{}<span>{}</span></div>'.format(a,ic(i),"",l))
    scan = '<div class="scan-slot"><div class="scan-fab">{}</div></div>'.format(ic("i-scan"))
    p.insert(2, scan)
    return '<div class="bottom">{}</div>'.format("".join(p))

def nav(title, back=True, right=""):
    bk = '<span class="nav-back">{}</span>'.format(ic("i-back")) if back else ""
    r = '<span class="nav-right">{}</span>'.format(right) if right else ""
    return '<div class="status"><b>09:41</b><span>5G&nbsp;&nbsp;82%</span></div><div class="nav">{}<b>{}</b>{}</div><main class="scroll"><div class="content clean">'.format(bk,title,r)

def shot_nav(title, body, lbl, back=True, right="", has_bottom=False, ba="home"):
    inner = nav(title, back, right) + body + '</div></main>'
    bt = bottom_bar(ba) if has_bottom else ""
    return '<section class="shot">{}<div class="phone"><div class="screen">{}{}</div></div></section>'.format(L(lbl), inner, bt)

def shot_bare(inner, lbl, has_bottom=False, ba="home"):
    bt = bottom_bar(ba) if has_bottom else ""
    return '<section class="shot">{}<div class="phone"><div class="screen">{}{}</div></div></section>'.format(L(lbl), inner, bt)

# ===== SCREENS =====

search_home = '<div class="search-pill">{}<span>搜索物品、分类、位置、二维码</span></div>'.format(ic("i-search"))

login = '''<div class="login-screen">
  <div class="login-badge">{}</div>
  <div class="login-brand">HomeBox</div>
  <div class="login-desc">扫码·定位·消耗·补货<br>一套管住家里所有物品</div>
  <div class="glass-input-group">
    <input class="glass-input" placeholder="+86 手机号" value="138 **** 8888">
    <input class="glass-input" placeholder="密码" type="password" value="……">
  </div>
  <button class="btn-primary">登 录</button>
  <div class="login-divider">or continue with</div>
  <button class="btn-secondary">使用验证码登录</button>
  <div class="login-features">
    <div class="login-feat"><div class="icon">📦</div><b>空间管理</b><small>柜子/层/盒</small></div>
    <div class="login-feat"><div class="icon">📱</div><b>扫码录入</b><small>快速绑定</small></div>
    <div class="login-feat"><div class="icon">📊</div><b>库存提醒</b><small>临期/低库存</small></div>
  </div>
</div>'''.format(ic("i-storage"))

hero = '<div class="hero"><div><small>今日概览</small><h2>128</h2><small>管理物品 · 5空间</small></div><div class="hero-mark">{}</div></div>'.format(ic("i-storage"))
metrics = '<div class="metric-strip"><div><b>4</b><span>空间</span></div><div class="orange"><b>3</b><span>临期</span></div><div class="red"><b>2</b><span>低库存</span></div><div><b>12</b><span>今日操作</span></div></div>'
insight = '<div class="insight-card"><small>⚡ 智能提醒</small><h3>3 件物品临期 30 天内</h3><p>温莎·美纹纸·丙烯 — 建议本月处理</p></div>'

h_actions = '<div class="section-head"><b>快捷操作</b><span>查看全部 →</span></div><div class="action-dock"><div class="action-tile"><div>📦<b>新增物品</b><small>扫码或手动录入</small></div>{}</div><div class="action-tile"><div>📋<b>消耗记录</b><small>最近 7 天</small></div>{}</div><div class="action-tile"><div>🔄<b>补货提醒</b><small>2 件需补货</small></div>{}</div><div class="action-tile"><div>🗂️<b>分类浏览</b><small>5大类·14子类</small></div>{}</div></div>'.format(ic("i-plus"),ic("i-down"),ic("i-up"),ic("i-tag"))

recent = '<div class="section-head"><b>最近使用</b><span>全部 →</span></div><div class="soft-list"><div class="soft-row"><div class="avatar">{}</div><div class="grow"><strong>温莎牛顿 24 色颜料</strong><small>书房 · A柜 · 2层 · 蓝盒</small></div><span class="tag orange">临期</span></div><div class="soft-row"><div class="avatar">{}</div><div class="grow"><strong>3M 美纹纸胶带</strong><small>工具柜 · 1层</small></div><span class="meta">×4</span></div><div class="soft-row"><div class="avatar">{}</div><div class="grow"><strong>7号电池</strong><small>储物间 · A层</small></div><span class="tag red">低库存</span></div></div>'.format(ic("i-box"),ic("i-box"),ic("i-box"))

home_screen = '<div class="home-fixed">{}{}{}</div><div class="content" style="padding-bottom:72px">{}{}{}</div>'.format(search_home,hero,metrics,insight,h_actions,recent)

manage_body = '<div class="home-fixed"><div class="search-pill">{}<span>搜索柜子、分类、盒码</span></div></div><div class="content" style="padding-bottom:72px"><div class="section-head"><b>📐 存储空间</b><span>管理 →</span></div><div class="quick-grid"><div class="quick-card"><b>🏠 书房 A 柜</b><small>3层 · 8盒 · 46件</small><span class="tag green" style="display:inline-block;margin-top:6px">正常</span></div><div class="quick-card"><b>🔧 工具柜</b><small>2层 · 5盒 · 31件</small><span class="tag orange" style="display:inline-block;margin-top:6px">1临期</span></div><div class="quick-card"><b>📦 储物间</b><small>2层 · 3盒 · 23件</small><span class="tag red" style="display:inline-block;margin-top:6px">2低</span></div><div class="quick-card" style="border-style:dashed;justify-content:center;align-items:center;color:var(--muted)"><b>+ 新增空间</b></div></div><div class="section-head"><b>📂 存货分类</b><span>管理 →</span></div><div class="soft-list"><div class="soft-row"><div class="cat-emoji">🎨</div><div class="grow"><strong>画材</strong><small>3子类 · 46件</small></div><span class="tag orange">临期</span></div><div class="soft-row"><div class="cat-emoji">🔧</div><div class="grow"><strong>工具</strong><small>2子类 · 31件</small></div><span class="meta">正常</span></div><div class="soft-row"><div class="cat-emoji">✏️</div><div class="grow"><strong>文具</strong><small>4子类 · 28件</small></div><span class="meta">正常</span></div></div></div>'.format(ic("i-search"))

items_body = '<div class="home-fixed"><div class="search-pill">{}<span>搜索名称、分类、位置</span></div><div class="toolbar"><span class="seg-on">全部</span><span>画材</span><span>工具</span><span>文具</span><span>耗材</span></div></div><div class="content" style="padding-bottom:72px"><div class="section-head"><b>全部物料</b><span>128件</span></div><div class="clean-list"><div class="clean-row"><div class="avatar">{}</div><div><b>温莎牛顿 24 色颜料</b><small>画材 · 书房A柜/2层/蓝盒</small></div><span class="tag orange">临期</span></div><div class="clean-row"><div class="avatar">{}</div><div><b>白夜固体水彩</b><small>画材 · 书房A柜/2层</small></div><span class="right">×1</span></div><div class="clean-row"><div class="avatar">{}</div><div><b>丙烯颜料补充装</b><small>画材 · 工具柜/2层</small></div><span class="tag red">低库存</span></div><div class="clean-row"><div class="avatar">{}</div><div><b>3M 美纹纸胶带</b><small>耗材 · 工具柜/1层</small></div><span class="right">×4</span></div><div class="clean-row"><div class="avatar">{}</div><div><b>7号电池</b><small>耗材 · 储物间/A层</small></div><span class="tag red">低库存</span></div><div class="clean-row"><div class="avatar">{}</div><div><b>素描本 A4</b><small>文具 · 书房A柜/1层</small></div><span class="right">×2</span></div></div></div>'.format(ic("i-search"),ic("i-box"),ic("i-box"),ic("i-box"),ic("i-box"),ic("i-box"),ic("i-box"))

mine_body = '<div class="content clean"><div class="mine-hero"><div class="profile-avatar">曦</div><div><h2>曦曦</h2><p>个人版 · 管理员</p></div></div><div class="mine-stats"><div class="stat-card"><b>128</b><span>管理物品</span></div><div class="stat-card"><b>5</b><span>存储空间</span></div><div class="stat-card"><b>86</b><span>已绑码</span></div></div><div class="mine-section-title"><b>设置</b></div><div class="mine-list"><div class="mine-item"><div class="mine-ico">{}</div><div class="mine-text"><b>个人资料</b><small>头像、昵称、安全</small></div><span class="mine-arrow">›</span></div><div class="mine-item"><div class="mine-ico">{}</div><div class="mine-text"><b>用户与偏好</b><small>主题、视图、提醒</small></div><span class="mine-arrow">›</span></div><div class="mine-item"><div class="mine-ico">{}</div><div class="mine-text"><b>二维码管理</b><small>生成、打印、绑定</small></div><span class="mine-arrow">›</span></div><div class="mine-item"><div class="mine-ico">{}</div><div class="mine-text"><b>导入导出</b><small>Excel 备份与恢复</small></div><span class="mine-arrow">›</span></div><div class="mine-item"><div class="mine-ico">{}</div><div class="mine-text"><b>关于与帮助</b><small>版本 v0.1 · 反馈</small></div><span class="mine-arrow">›</span></div></div></div>'.format(ic("i-user"),ic("i-gear"),ic("i-qr"),ic("i-export"),ic("i-clock"))

space_body = '<div class="space-path">家庭仓库 › 空间管理</div><div class="space-hero"><b>我的空间</b><small>柜子 · 层 · 盒三级结构</small></div><div class="space-list"><div class="space-item"><div class="space-icon">{}</div><div><b>书房 A 柜</b><small>3层 · 8盒 · 46件</small></div><span class="space-meta">正常</span></div><div class="space-item"><div class="space-icon">{}</div><div><b>工具柜</b><small>2层 · 5盒 · 31件</small></div><span class="space-meta warn">1临期</span></div><div class="space-item"><div class="space-icon">{}</div><div><b>储物间</b><small>2层 · 3盒 · 23件</small></div><span class="space-meta red">低库存</span></div></div><div class="space-actions"><div class="space-action"><div class="space-icon">{}</div><div><b>新增柜子</b></div></div></div>'.format(ic("i-storage"),ic("i-storage"),ic("i-storage"),ic("i-plus"))

cat_body = '<div class="cat-head"><h2>选择分类</h2><small>按大类进入子类和细类</small></div><div class="search-pill" style="margin:6px 0">{}<span>搜索分类、物品</span></div><div class="cat-overview"><div><b>5</b><span>大类</span></div><div><b>14</b><span>子类</span></div><div><b>128</b><span>物品</span></div></div><div class="cat-actions"><div class="cat-action"><div class="cat-icon">＋</div><div><b>新增大类</b></div></div></div><div class="cat-list"><div class="cat-item"><div class="cat-emoji">🎨</div><div><b>画材</b><small>3子类 · 46件</small></div><span class="cat-meta warn">1临期</span></div><div class="cat-item"><div class="cat-emoji">🔧</div><div><b>工具</b><small>2子类 · 31件</small></div><span class="cat-meta">正常</span></div><div class="cat-item"><div class="cat-emoji">✏️</div><div><b>文具</b><small>4子类 · 28件</small></div><span class="cat-meta">正常</span></div><div class="cat-item"><div class="cat-emoji">🧪</div><div><b>耗材</b><small>3子类 · 23件</small></div><span class="cat-meta red">2低</span></div><div class="cat-item"><div class="cat-emoji">☰</div><div><b>全部物料</b><small>128件</small></div><span class="cat-meta">128件</span></div></div>'.format(ic("i-search"))

item_detail = '<div class="item-card"><div class="item-title"><div class="avatar">{}</div><div><b>温莎牛顿 24 色颜料</b><small>水彩颜料 · 书房A柜/2层/蓝盒</small></div></div></div><div class="item-actions"><div class="item-action"><div class="cat-icon">✎</div><b>修改信息</b></div><div class="item-action danger"><div class="cat-icon">🗑</div><b>删除物品</b></div><div class="item-action"><div class="cat-icon">⇄</div><b>移动分类</b></div><div class="item-action"><div class="cat-icon">⇅</div><b>移动位置</b></div></div><div class="clean-list" style="margin-top:6px"><div class="clean-row"><div><b>数量</b><small>1 盒</small></div><span class="right">正常</span></div><div class="clean-row"><div><b>分类</b><small>画材 / 颜料 / 水彩颜料</small></div></div><div class="clean-row"><div><b>位置</b><small>书房A柜 / 2层 / 蓝盒</small></div></div><div class="clean-row"><div><b>二维码</b><small>ITM-0001</small></div></div></div>'.format(ic("i-box"))

add_item = '<div class="item-head"><h2>录入物品</h2><small>分类录到最小类，位置可选柜子/层/盒子</small></div><div class="item-field"><span>物品名称</span><b>温莎牛顿 24 色颜料</b></div><div class="item-field"><span>分类</span><b>画材 / 颜料 / 水彩颜料</b></div><div class="item-field"><span>位置类型</span><div class="choice-row"><span>柜子</span><span>层</span><span class="on">盒子</span></div></div><div class="item-field"><span>位置</span><b>书房A柜 / 2层 / 蓝盒</b></div><div class="item-field"><span>数量</span><b>1 盒</b></div><div class="item-field"><span>二维码</span><b>扫码绑定</b></div><button class="item-save">保存物品</button>'

consume = '<div class="item-card"><div class="item-title"><div class="avatar">{}</div><div><b>3M 美纹纸胶带</b><small>当前库存 4 卷</small></div></div></div><div class="stepper"><button>−</button><b>1</b><button>+</button></div><div class="item-field"><span>用途备注</span><b>贴画纸边缘固定</b></div><button class="item-save">确认消耗</button>'.format(ic("i-box"))

replenish = '<div class="item-card"><div class="item-title"><div class="avatar">{}</div><div><b>7号电池</b><small>当前库存 1 节 · 低库存</small></div></div></div><div class="stepper"><button>−</button><b>8</b><button>+</button></div><div class="item-field"><span>来源</span><b>京东补货</b></div><button class="item-save">确认补货</button>'.format(ic("i-box"))

move = '<div class="item-head"><h2>移动物品</h2><small>分类和位置可分别调整</small></div><div class="item-card"><div class="item-title"><div class="avatar">{}</div><div><b>温莎牛顿 24 色颜料</b><small>当前：水彩颜料 · 蓝盒</small></div></div></div><div class="item-field"><span>目标分类</span><b>画材 / 颜料 / 水彩颜料</b></div><div class="item-field"><span>目标位置类型</span><div class="choice-row"><span class="on">柜子</span><span>层</span><span>盒子</span></div></div><div class="item-field"><span>目标位置</span><b>书房 A 柜</b></div><button class="item-save">确认移动</button>'.format(ic("i-box"))

search = '<div class="search-pill">{}<span>颜料</span></div><div class="section-head"><b>搜索结果</b><span>12 条</span></div><div class="soft-list"><div class="soft-row"><div class="avatar">{}</div><div class="grow"><strong>温莎牛顿 24 色颜料</strong><small>书房 / A柜 / 2层 / 蓝盒</small></div><span class="tag orange">临期</span></div><div class="soft-row"><div class="avatar">{}</div><div class="grow"><strong>白夜固体水彩</strong><small>书房 / A柜 / 2层</small></div><span class="meta">×1</span></div><div class="soft-row"><div class="avatar">{}</div><div class="grow"><strong>丙烯颜料补充装</strong><small>工具柜 / 2层</small></div><span class="tag red">低库存</span></div></div>'.format(ic("i-search"),ic("i-box"),ic("i-box"),ic("i-box"))

records = '<div class="toolbar"><span class="seg-on">全部</span><span>消耗</span><span>补货</span><span>移动</span></div><div class="soft-list"><div class="soft-row"><div class="avatar">{}</div><div class="grow"><strong>消耗 3M 美纹纸胶带</strong><small>今天 09:20 · −1 卷</small></div><span class="tag">消耗</span></div><div class="soft-row"><div class="avatar">{}</div><div class="grow"><strong>补货 7号电池</strong><small>昨天 20:10 · +8 节</small></div><span class="tag green">补货</span></div><div class="soft-row"><div class="avatar">{}</div><div class="grow"><strong>移动 透明工具盒</strong><small>昨天 18:40 · 工具柜→书房</small></div><span class="tag">移动</span></div></div>'.format(ic("i-down"),ic("i-up"),ic("i-map"))

scan = '<div class="scanner"><div class="scan-frame">{}</div><p>对准物品码或位置码</p></div><div class="scan-guide" style="margin-top:12px"><b>扫码后动作</b><small>物品码 → 物品详情；位置码 → 盒子/柜子详情</small></div>'.format(ic("i-scan"))

qr_mgr = '<div class="summary-card"><b>二维码资产</b><small>已生成 86 个 · 未绑定 4 个 · 已停用 2 个</small></div><div class="soft-list" style="margin-top:6px"><div class="soft-row"><div class="cat-emoji">📦</div><div class="grow"><strong>盒子码 BOX-001</strong><small>蓝色颜料盒 · 12件</small></div><span class="tag green">正常</span></div><div class="soft-row"><div class="cat-emoji">🎨</div><div class="grow"><strong>物品码 ITM-0001</strong><small>温莎牛顿 24 色颜料</small></div><span class="tag">已绑定</span></div><div class="soft-row"><div class="cat-emoji">⚠️</div><div class="grow"><strong>未绑定码 QR-0091</strong><small>待绑定</small></div><span class="tag red">未绑</span></div></div><button class="primary" style="margin-top:10px">生成二维码</button>'

user_set = '<div class="setting-list"><div class="settings-row"><div><b>主题色</b><small>暗夜紫</small></div><span class="tag">当前</span></div><div class="settings-row"><div><b>首页默认视图</b><small>概览 + 最近使用</small></div><span class="chev">›</span></div><div class="settings-row"><div><b>临期提醒</b><small>提前 30 天标记</small></div><span class="switch-el"></span></div><div class="settings-row"><div><b>低库存阈值</b><small>按物品单独设置</small></div><span class="chev">›</span></div></div>'

# ===== ASSEMBLE =====
GRP = '<div class="group-title"><span>{}</span></div><div class="row">'

sections = [
    ("一级页面", [
        shot_bare(login, "1. 登录"),
        shot_bare(home_screen, "2. 首页", True, "home"),
        shot_bare(manage_body, "3. 空间管理", True, "manage"),
        shot_bare(items_body, "9-4. 全部物料", True, "items"),
        shot_bare(mine_body, "24. 我的", True, "mine"),
    ]),
    ("空间与分类", [
        shot_nav("空间结构", space_body, "4. 空间结构维护"),
        shot_nav("分类维护", cat_body, "9. 存货分类维护"),
        shot_nav("物品详情", item_detail, "16. 物品详情"),
        shot_nav("新增物品", add_item, "17. 新增物品"),
    ]),
    ("操作流程", [
        shot_nav("消耗", consume, "18. 消耗"),
        shot_nav("补货", replenish, "19. 补货"),
        shot_nav("移动物品", move, "20. 移动"),
        shot_nav("搜索", search, "21. 搜索", False),
        shot_nav("出入库记录", records, "22. 记录", False),
        shot_nav("扫码", scan, "23. 扫码", False),
    ]),
    ("我的页面", [
        shot_nav("二维码管理", qr_mgr, "11. 二维码管理"),
        shot_nav("用户与偏好", user_set, "26. 用户偏好"),
    ]),
]

body_html = ""
for grp_title, scr_list in sections:
    body_html += GRP.format(grp_title)
    for s in scr_list:
        body_html += s
    body_html += '</div>'

HTML = '''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>HomeBox · 家庭仓库管理系统 V2</title><style>{}</style></head><body>
{}
<h1>HomeBox · 家庭仓库原型 V2</h1>
<p class="subtitle">Dark Premium · Data Drift 风格 · 17 Screens · 2026-06-09</p>
<div class="grid">{}</div>
</body></html>'''.format(CSS, SVG, body_html)

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(HTML)

print("Generated: {} ({} bytes)".format(OUT_PATH, len(HTML)))
print("Done! Visit: http://47.99.149.119:8648/prototype/index_v2.html")
