#!/usr/bin/env python3
"""Generate redesigned family warehouse prototype V2 — Dark Premium Data Drift."""
import os

CSS = open("/var/minis/workspace/gen_v2_css.txt").read() if os.path.exists("/var/minis/workspace/gen_v2_css.txt") else ""

def icon(name, cls=""):
    return f'<svg class="{cls}" viewBox="0 0 24 24"><use href="#{name}"/></svg>'

def pg(title, screens, group_title=None):
    g = f'<div class="group-title"><span>{group_title}</span></div>' if group_title else ''
    return g + '<div class="row">' + "".join(screens) + '</div>'

def phone(inner, has_bottom=False, bottom_active="home"):
    bottom_html = ""
    if has_bottom:
        tabs = [("home","首页","i-home"),("manage","管理","i-box"),("items","物品","i-list"),("mine","我的","i-user")]
        pieces = []
        for k,l,i in tabs:
            act = " active" if k == bottom_active else ""
            pieces.append(f'<div class="tab{act}">{icon("i-"+i)}<span>{l}</span></div>')
        mid = len(pieces)//2
        scan = f'<div class="scan-slot"><div class="scan-fab">{icon("i-scan")}</div></div>'
        bottom_html = '<div class="bottom">' + "".join(pieces[:mid]) + scan + "".join(pieces[mid:]) + '</div>'
    return f'<section class="shot"><div class="phone"><div class="screen">{inner}{bottom_html}</div></div></section>'

def nav(title, back=True, right=""):
    bk = f'<span class="nav-back">{icon("i-back")}</span>' if back else ""
    r = f'<span class="nav-right">{right}</span>' if right else ""
    return f'<div class="status"><b>09:41</b><span>5G&nbsp;&nbsp;82%</span></div><div class="nav">{bk}<b>{title}</b>{r}</div><main class="scroll"><div class="content clean">'

def nav_end():
    return '</div></main>'

def label(text):
    return f'<div class="label">{text}</div>'

def shot(inner, lbl, has_bottom=False, bottom_active="home"):
    return f'<section class="shot">{label(lbl)}{phone(inner, has_bottom, bottom_active)}</section>'

def shot_nav(title, body, lbl, back=True, right="", has_bottom=False, bottom_active="home"):
    return f'<section class="shot">{label(lbl)}{phone(nav(title,back,right) + body + nav_end(), has_bottom, bottom_active)}</section>'

# ====== SCREENS ======

# 1. LOGIN
login_screen = '''
<div class="login-screen">
  <div class="login-badge"><svg viewBox="0 0 24 24" width="36" height="36" fill="#fff"><use href="#i-storage"/></svg></div>
  <div class="login-brand">HomeBox</div>
  <div class="login-desc">扫码、定位、消耗、补货<br>一套管住家里所有物品</div>
  <div class="glass-input-group">
    <input class="glass-input" placeholder="+86 手机号" value="138 **** 8888">
    <input class="glass-input" placeholder="密码" type="password" value="••••••••">
  </div>
  <button class="btn-primary">登 录</button>
  <div class="login-divider">or continue with</div>
  <button class="btn-secondary">使用验证码登录</button>
  <div class="login-features">
    <div class="login-feat"><div class="icon">📦</div><b>空间管理</b><small>柜子/层/盒</small></div>
    <div class="login-feat"><div class="icon">📱</div><b>扫码录入</b><small>快速绑定</small></div>
    <div class="login-feat"><div class="icon">📊</div><b>库存提醒</b><small>临期/低库存</small></div>
  </div>
</div>'''

# 2. HOME
home_screen = '''
<div class="home-fixed">
  <div class="search-pill"><svg viewBox="0 0 24 24"><use href="#i-search"/></svg><span>搜索物品、分类、位置、二维码</span></div>
  <div class="hero">
    <div><small>今日概览</small><h2>128</h2><small>管理物品 · 5空间</small></div>
    <div class="hero-mark"><svg viewBox="0 0 24 24"><use href="#i-storage"/></svg></div>
  </div>
  <div class="metric-strip">
    <div><b>4</b><span>空间</span></div>
    <div class="orange"><b>3</b><span>临期</span></div>
    <div class="red"><b>2</b><span>低库存</span></div>
    <div><b>12</b><span>今日操作</span></div>
  </div>
</div>
<div class="content" style="padding-bottom:72px">
  <div class="insight-card">
    <small>⚡ 智能提醒</small>
    <h3>3 件物品临期 30 天内</h3>
    <p>温莎颜料 · 美纹纸胶带 · 丙烯补充装 — 建议本月使用或处理</p>
  </div>
  <div class="section-head"><b>快捷操作</b><span>查看全部 →</span></div>
  <div class="action-dock">
    <div class="action-tile"><div><b>📦 新增物品</b><small>扫码或手动录入</small></div><svg viewBox="0 0 24 24"><use href="#i-plus"/></svg></div>
    <div class="action-tile"><div><b>📋 消耗记录</b><small>最近 7 天消耗</small></div><svg viewBox="0 0 24 24"><use href="#i-down"/></svg></div>
    <div class="action-tile"><div><b>🔄 补货提醒</b><small>2 件需要补货</small></div><svg viewBox="0 0 24 24"><use href="#i-up"/></svg></div>
    <div class="action-tile"><div><b>🗂️ 分类浏览</b><small>5 大类 · 14 子类</small></div><svg viewBox="0 0 24 24"><use href="#i-tag"/></svg></div>
  </div>
  <div class="section-head"><b>最近使用</b><span>全部 →</span></div>
  <div class="soft-list">
    <div class="soft-row"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><strong>温莎牛顿 24 色颜料</strong><small>书房 A柜 · 2层 · 蓝盒</small></div><span class="tag orange">临期</span></div>
    <div class="soft-row"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><strong>3M 美纹纸胶带</strong><small>工具柜 · 1层</small></div><span class="meta">×4</span></div>
    <div class="soft-row"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><strong>7号电池</strong><small>储物间 · A层</small></div><span class="tag red">低库存</span></div>
  </div>
</div>'''

# 3. MANAGE (space management)
manage_screen = '''
<div class="home-fixed">
  <div class="search-pill"><svg viewBox="0 0 24 24"><use href="#i-search"/></svg><span>搜索柜子、分类、盒码</span></div>
</div>
<div class="content" style="padding-bottom:72px">
  <div class="section-head"><b>📐 存储空间</b><span>管理 →</span></div>
  <div class="quick-grid">
    <div class="quick-card"><b>🏠 书房 A 柜</b><small>3层 · 8盒 · 46件</small><span class="tag green" style="display:inline-block;margin-top:6px">正常</span></div>
    <div class="quick-card"><b>🔧 工具柜</b><small>2层 · 5盒 · 31件</small><span class="tag orange" style="display:inline-block;margin-top:6px">1临期</span></div>
    <div class="quick-card"><b>📦 储物间</b><small>2层 · 3盒 · 23件</small><span class="tag red" style="display:inline-block;margin-top:6px">2低</span></div>
    <div class="quick-card" style="border-style:dashed;justify-content:center;align-items:center;color:var(--muted)"><b>+ 新增空间</b></div>
  </div>
  <div class="section-head"><b>📂 存货分类</b><span>管理 →</span></div>
  <div class="soft-list">
    <div class="soft-row"><div class="cat-emoji">🎨</div><div class="grow"><strong>画材</strong><small>3子类 · 46件</small></div><span class="tag orange">临期</span></div>
    <div class="soft-row"><div class="cat-emoji">🔧</div><div class="grow"><strong>工具</strong><small>2子类 · 31件</small></div><span class="meta">正常</span></div>
    <div class="soft-row"><div class="cat-emoji">✏️</div><div class="grow"><strong>文具</strong><small>4子类 · 28件</small></div><span class="meta">正常</span></div>
  </div>
</div>'''

# 4. FULL ITEMS LIST
items_screen = '''
<div class="home-fixed">
  <div class="search-pill"><svg viewBox="0 0 24 24"><use href="#i-search"/></svg><span>搜索名称、分类、位置</span></div>
  <div class="toolbar"><span class="seg-on">全部</span><span>画材</span><span>工具</span><span>文具</span><span>耗材</span></div>
</div>
<div class="content" style="padding-bottom:72px">
  <div class="section-head"><b>全部物料</b><span>128件</span></div>
  <div class="clean-list">
    <div class="clean-row"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div><b>温莎牛顿 24 色颜料</b><small>画材 · 书房A柜/2层/蓝盒</small></div><span class="tag orange">临期</span></div>
    <div class="clean-row"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div><b>白夜固体水彩</b><small>画材 · 书房A柜/2层</small></div><span class="right">×1</span></div>
    <div class="clean-row"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div><b>丙烯颜料补充装</b><small>画材 · 工具柜/2层</small></div><span class="tag red">低库存</span></div>
    <div class="clean-row"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div><b>3M 美纹纸胶带</b><small>耗材 · 工具柜/1层</small></div><span class="right">×4</span></div>
    <div class="clean-row"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div><b>7号电池</b><small>耗材 · 储物间/A层</small></div><span class="tag red">低库存</span></div>
    <div class="clean-row"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div><b>素描本 A4</b><small>文具 · 书房A柜/1层</small></div><span class="right">×2</span></div>
  </div>
</div>'''

# 5. MINE
mine_screen = '''
<div class="content clean">
  <div class="mine-hero">
    <div class="profile-avatar">曦</div>
    <div><h2>曦曦</h2><p>个人版 · 管理员</p></div>
  </div>
  <div class="mine-stats">
    <div class="stat-card"><b>128</b><span>管理物品</span></div>
    <div class="stat-card"><b>5</b><span>存储空间</span></div>
    <div class="stat-card"><b>86</b><span>已绑二维码</span></div>
  </div>
  <div class="mine-section-title">设置</div>
  <div class="mine-list">
    <div class="mine-item"><div class="mine-ico"><svg viewBox="0 0 24 24"><use href="#i-user"/></svg></div><div class="mine-text"><b>个人资料</b><small>头像、昵称、安全</small></div><span class="mine-arrow">›</span></div>
    <div class="mine-item"><div class="mine-ico"><svg viewBox="0 0 24 24"><use href="#i-settings"/></svg></div><div class="mine-text"><b>用户与偏好</b><small>主题、视图、提醒</small></div><span class="mine-arrow">›</span></div>
    <div class="mine-item"><div class="mine-ico"><svg viewBox="0 0 24 24"><use href="#i-qr"/></svg></div><div class="mine-text"><b>二维码管理</b><small>生成、打印、绑定</small></div><span class="mine-arrow">›</span></div>
    <div class="mine-item"><div class="mine-ico"><svg viewBox="0 0 24 24"><use href="#i-export"/></svg></div><div class="mine-text"><b>导入导出</b><small>Excel 备份与恢复</small></div><span class="mine-arrow">›</span></div>
    <div class="mine-item"><div class="mine-ico"><svg viewBox="0 0 24 24"><use href="#i-clock"/></svg></div><div class="mine-text"><b>关于与帮助</b><small>版本 v0.1 · 反馈</small></div><span class="mine-arrow">›</span></div>
  </div>
</div>'''

# Secondary screens
space_structure = nav("空间结构",True,"") + '''
<div class="space-path">家庭仓库 › 空间管理</div>
<div class="space-hero"><b>我的空间</b><small>柜子 · 层 · 盒三级结构</small></div>
<div class="space-list">
  <div class="space-item"><div class="space-icon"><svg viewBox="0 0 24 24"><use href="#i-storage"/></svg></div><div><b>书房 A 柜</b><small>3层 · 8盒 · 46件</small></div><span class="space-meta">正常</span></div>
  <div class="space-item"><div class="space-icon"><svg viewBox="0 0 24 24"><use href="#i-storage"/></svg></div><div><b>工具柜</b><small>2层 · 5盒 · 31件</small></div><span class="space-meta warn">1临期</span></div>
  <div class="space-item"><div class="space-icon"><svg viewBox="0 0 24 24"><use href="#i-storage"/></svg></div><div><b>储物间</b><small>2层 · 3盒 · 23件</small></div><span class="space-meta red">低库存</span></div>
</div>
<div class="space-actions"><div class="space-action"><div class="space-icon"><svg viewBox="0 0 24 24"><use href="#i-plus"/></svg></div><div><b>新增柜子</b></div></div></div>
''' + nav_end()

cat_maintain = nav("分类维护",True,"") + '''
<div class="cat-head"><h2>选择分类</h2><small>按大类进入子类和细类</small></div>
<div class="search-pill" style="margin:6px 0"><svg viewBox="0 0 24 24"><use href="#i-search"/></svg><span>搜索分类、物品</span></div>
<div class="cat-overview"><div><b>5</b><span>大类</span></div><div><b>14</b><span>子类</span></div><div><b>128</b><span>物品</span></div></div>
<div class="cat-actions"><div class="cat-action"><div class="cat-icon">＋</div><div><b>新增大类</b></div></div></div>
<div class="cat-list">
  <div class="cat-item"><div class="cat-emoji">🎨</div><div><b>画材</b><small>3子类 · 46件</small></div><span class="cat-meta warn">1临期</span></div>
  <div class="cat-item"><div class="cat-emoji">🔧</div><div><b>工具</b><small>2子类 · 31件</small></div><span class="cat-meta">正常</span></div>
  <div class="cat-item"><div class="cat-emoji">✏️</div><div><b>文具</b><small>4子类 · 28件</small></div><span class="cat-meta">正常</span></div>
  <div class="cat-item"><div class="cat-emoji">🧪</div><div><b>耗材</b><small>3子类 · 23件</small></div><span class="cat-meta red">2低</span></div>
  <div class="cat-item"><div class="cat-emoji">☰</div><div><b>全部物料</b><small>不参与分类 · 128件</small></div><span class="cat-meta">128件</span></div>
</div>''' + nav_end()

item_detail = nav("物品详情",True,"") + '''
<div class="item-card"><div class="item-title"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div><b>温莎牛顿 24 色颜料</b><small>水彩颜料 · 书房A柜/2层/蓝盒</small></div></div></div>
<div class="item-actions">
  <div class="item-action"><div class="cat-icon">✎</div><b>修改信息</b></div>
  <div class="item-action danger"><div class="cat-icon">🗑</div><b>删除物品</b></div>
  <div class="item-action"><div class="cat-icon">⇄</div><b>移动分类</b></div>
  <div class="item-action"><div class="cat-icon">⇅</div><b>移动位置</b></div>
</div>
<div class="clean-list" style="margin-top:6px">
  <div class="clean-row"><div><b>数量</b><small>1 盒</small></div><span class="right">正常</span></div>
  <div class="clean-row"><div><b>分类</b><small>画材 / 颜料 / 水彩颜料</small></div></div>
  <div class="clean-row"><div><b>位置</b><small>书房A柜 / 2层 / 蓝盒</small></div></div>
  <div class="clean-row"><div><b>二维码</b><small>ITM-0001</small></div></div>
</div>''' + nav_end()

add_item = nav("新增物品",True,"") + '''
<div class="item-head"><h2>录入物品</h2><small>分类录到最小类，位置可选柜子/层/盒子</small></div>
<div class="item-field"><span>物品名称</span><b>温莎牛顿 24 色颜料</b></div>
<div class="item-field"><span>分类</span><b>画材 / 颜料 / 水彩颜料</b></div>
<div class="item-field"><span>位置类型</span><div class="choice-row"><span>柜子</span><span>层</span><span class="on">盒子</span></div></div>
<div class="item-field"><span>位置</span><b>书房A柜 / 2层 / 蓝盒</b></div>
<div class="item-field"><span>数量</span><b>1 盒</b></div>
<div class="item-field"><span>二维码</span><b>扫码绑定</b></div>
<button class="item-save">保存物品</button>''' + nav_end()

consume_screen = nav("消耗",True,"") + '''
<div class="item-card"><div class="item-title"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div><b>3M 美纹纸胶带</b><small>当前库存 4 卷</small></div></div></div>
<div class="stepper"><button>−</button><b>1</b><button>+</button></div>
<div class="item-field"><span>用途备注</span><b>贴画纸边缘固定</b></div>
<button class="item-save">确认消耗</button>''' + nav_end()

replenish_screen = nav("补货",True,"") + '''
<div class="item-card"><div class="item-title"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div><b>7号电池</b><small>当前库存 1 节 · 低库存</small></div></div></div>
<div class="stepper"><button>−</button><b>8</b><button>+</button></div>
<div class="item-field"><span>来源</span><b>京东补货</b></div>
<button class="item-save">确认补货</button>''' + nav_end()

move_screen = nav("移动物品",True,"") + '''
<div class="item-head"><h2>移动物品</h2><small>分类和位置可分别调整</small></div>
<div class="item-card"><div class="item-title"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div><b>温莎牛顿 24 色颜料</b><small>当前：水彩颜料 · 蓝盒</small></div></div></div>
<div class="item-field"><span>目标分类</span><b>画材 / 颜料 / 水彩颜料</b></div>
<div class="item-field"><span>目标位置类型</span><div class="choice-row"><span class="on">柜子</span><span>层</span><span>盒子</span></div></div>
<div class="item-field"><span>目标位置</span><b>书房 A 柜</b></div>
<button class="item-save">确认移动</button>''' + nav_end()

search_screen = nav("搜索",False,"") + '''
<div class="search-pill"><svg viewBox="0 0 24 24"><use href="#i-search"/></svg><span>颜料</span></div>
<div class="section-head"><b>搜索结果</b><span>12 条</span></div>
<div class="soft-list">
  <div class="soft-row"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><strong>温莎牛顿 24 色颜料</strong><small>书房 / A柜 / 2层 / 蓝盒</small></div><span class="tag orange">临期</span></div>
  <div class="soft-row"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><strong>白夜固体水彩</strong><small>书房 / A柜 / 2层</small></div><span class="meta">×1</span></div>
  <div class="soft-row"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-box"/></svg></div><div class="grow"><strong>丙烯颜料补充装</strong><small>工具柜 / 2层</small></div><span class="tag red">低库存</span></div>
</div>''' + nav_end()

records_screen = nav("出入库记录",False,"") + '''
<div class="toolbar"><span class="seg-on">全部</span><span>消耗</span><span>补货</span><span>移动</span></div>
<div class="soft-list">
  <div class="soft-row"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-down"/></svg></div><div class="grow"><strong>消耗 3M 美纹纸胶带</strong><small>今天 09:20 · −1 卷</small></div><span class="tag">消耗</span></div>
  <div class="soft-row"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-up"/></svg></div><div class="grow"><strong>补货 7号电池</strong><small>昨天 20:10 · +8 节</small></div><span class="tag green">补货</span></div>
  <div class="soft-row"><div class="avatar"><svg viewBox="0 0 24 24"><use href="#i-map"/></svg></div><div class="grow"><strong>移动 透明工具盒</strong><small>昨天 18:40 · 工具柜→书房</small></div><span class="tag">移动</span></div>
</div>''' + nav_end()

scan_screen = nav("扫码",False,"") + '''
<div class="scanner"><div class="scan-frame"><svg viewBox="0 0 24 24"><use href="#i-scan"/></svg></div><p>对准物品码或位置码</p></div>
<div class="scan-guide" style="margin-top:12px"><b>扫码后动作</b><small>物品码 → 物品详情；位置码 → 盒子/柜子详情，可快速入库、移动、绑定。</small></div>
''' + nav_end()

qr_manage = nav("二维码管理",True,"✎  ⋮") + '''
<div class="summary-card"><b>二维码资产</b><small>已生成 86 个 · 未绑定 4 个 · 已停用 2 个</small></div>
<div class="soft-list" style="margin-top:6px">
  <div class="soft-row"><div class="cat-emoji">📦</div><div class="grow"><strong>盒子码 BOX-001</strong><small>蓝色颜料盒 · 12件</small></div><span class="tag green">正常</span></div>
  <div class="soft-row"><div class="cat-emoji">🎨</div><div class="grow"><strong>物品码 ITM-0001</strong><small>温莎牛顿 24 色颜料</small></div><span class="tag">已绑定</span></div>
  <div class="soft-row"><div class="cat-emoji">⚠️</div><div class="grow"><strong>未绑定码 QR-0091</strong><small>待绑定</small></div><span class="tag red">未绑</span></div>
</div>
<button class="primary" style="margin-top:10px">生成二维码</button>''' + nav_end()

user_settings = nav("用户与偏好",True,"✎  ⋮") + '''
<div class="setting-list">
  <div class="settings-row"><div><b>主题色</b><small>暗夜紫</small></div><span class="tag">当前</span></div>
  <div class="settings-row"><div><b>首页默认视图</b><small>概览 + 最近使用</small></div><span class="chev">›</span></div>
  <div class="settings-row"><div><b>临期提醒</b><small>提前 30 天标记</small></div><span class="switch-el"></span></div>
  <div class="settings-row"><div><b>低库存阈值</b><small>按物品单独设置</small></div><span class="chev">›</span></div>
</div>''' + nav_end()

# ====== ASSEMBLE ======
screens = [
    ("一级页面", [
        shot(login_screen, "1. 登录"),
        shot(home_screen, "2. 首页", True, "home"),
        shot(manage_screen, "3. 空间管理", True, "manage"),
        shot(items_screen, "9-4. 全部物料", True, "items"),
        shot(mine_screen, "24. 我的", True, "mine"),
    ]),
    ("空间与分类", [
        shot_nav("空间结构", space_structure, "4. 空间结构"),
        shot_nav("分类维护", cat_maintain, "9. 分类维护"),
        shot_nav("物品详情", item_detail, "16. 物品详情"),
        shot_nav("新增物品", add_item, "17. 新增物品"),
    ]),
    ("操作流程", [
        shot_nav("消耗", consume_screen, "18. 消耗"),
        shot_nav("补货", replenish_screen, "19. 补货"),
        shot_nav("移动物品", move_screen, "20. 移动"),
        shot_nav("搜索", search_screen, "21. 搜索", False),
        shot_nav("出入库记录", records_screen, "22. 记录", False),
        shot_nav("扫码", scan_screen, "23. 扫码", False),
    ]),
    ("我的页面", [
        shot_nav("二维码管理", qr_manage, "11. 二维码"),
        shot_nav("用户与偏好", user_settings, "26. 用户偏好"),
    ]),
]

body = ""
for group_title, scr_list in screens:
    body += f'<div class="group-title"><span>{group_title}</span></div><div class="row">'
    for s in scr_list:
        body += s
    body += '</div>'

HTML = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>家庭仓库管理系统 — 原型设计 V2</title><style>{CSS}</style></head><body>
{SVG_ICONS}
<h1>HomeBox · 家庭仓库管理系统</h1>
<p class="subtitle">Dark Premium · Data Drift 风格 · 一级页面 + 核心流程 · 17 Screens</p>
<div class="grid">{body}</div>
</body></html>'''

OUT = "/home/dev/仓库原型/index_v2.html"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"Generated: {OUT} ({len(HTML)} bytes)")
print("Done!")
