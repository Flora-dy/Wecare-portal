# WECARE 临床/专利/SCI 检索（GitHub Pages 公网版）

本目录用于把离线检索页发布到 GitHub Pages（公网可访问）。

## 一次性部署（生成公开链接）

1. 在 GitHub 新建一个 **Public** 仓库（例如：`wecare-portal`）。
2. 在本机进入本目录并推送到 GitHub：
   - `cd /Users/zzp/Code/Design/Clinical/wecare_public_site`
   - `git init`
   - `git add -A`
   - `git commit -m "Publish portal"`
   - `git branch -M main`
   - `git remote add origin https://github.com/<你的账号>/<你的仓库>.git`
   - `git push -u origin main`
3. 在 GitHub 仓库设置：
   - Settings → Pages → Build and deployment
   - Source 选择 **Deploy from a branch**
   - Branch 选择 **main**，Folder 选择 **/(root)**，保存
4. 等待 1～2 分钟，GitHub 会给你一个公开链接：`https://<你的账号>.github.io/<你的仓库>/`

## 更新内容（以后每次更新数据）

1. 先在原目录生成最新离线页：`python3 /Users/zzp/Code/Design/Clinical/build_offline_portal.py`
2. 重新复制一份到本目录：
   - `cp /Users/zzp/Code/Design/Clinical/临床_专利_SCI_离线检索.html /Users/zzp/Code/Design/Clinical/wecare_public_site/index.html`
3. 提交并推送：
   - `cd /Users/zzp/Code/Design/Clinical/wecare_public_site`
   - `git add -A && git commit -m "Update portal" && git push`

## 注意

- 这是 **公开链接**：页面里包含的临床/专利/SCI 数据会对所有人可见。
- GitHub Pages 是静态托管：`ADD` 的新增只会保存在每个访问者自己的浏览器里（localStorage），不会自动同步给别人；可用页面里的“导出新增(JSON)”/“导入新增(JSON)”手工合并。

