# CV 项目基础信息

个人简历站点(双语),静态站,`gh-pages` 分支既是源码分支也是部署分支。

## 站点结构
- `cn.html` — 中文简历(主战场,内容最全)
- `index.html` — 英文简历(与 cn 通过右上角语言切换联动)
- 主题:深色工程风,单一 accent(`--accent:#38bdf8`);全部样式为 `cn.html`/`index.html` 内联 `<style>`,CSS 变量驱动。刻意克制,无 AI-glitch 风格。
- 交互:普通滚动站(scroll-progress + IntersectionObserver 侧边导航);工作经历/重点项目用「时间线卡片 → 右侧详情面板」;开源项目用「点击卡片 → 全屏 Modal(FLIP 放大 + stagger + 数字滚动)」。
- 资源:`img/`(含 `oss-*.svg` 开源封面、`avatar.svg`);`tools/md-to-pdf`(Markdown→A4 PDF)、`tools/transparent-svg`(头像 SVG 生成)。
- 简历源文件:`2026-简历.md`;导出的 PDF 单独托管在 weilantech CDN(见下),不从仓库直接提供。

## 部署(快速)
源站与部署站同为 `gh-pages`。改完 → 提交推送 → ms 服务器 `git pull` 即上线(静态文件 bind-mount,**无需重启容器**)。

```bash
# 1. 本地提交并推送(本地 remote 走 SSH: git@github.com:Allen-LPL/cv.git)
git add -A && git commit -m "..." && git push origin gh-pages

# 2. 部署到 ms 服务器(一步到位)
ssh ms 'cd /data/cv && git pull --ff-only'

# 3. 验证线上
curl -s -o /dev/null -w "%{http_code}\n" https://cv.liupengliang.com/cn.html
```

## 部署环境事实
- SSH 别名:`ms`(主机名 `JP-MS`)
- 仓库路径:`/data/cv`,分支 `gh-pages`;**ms 上的 remote 走 HTTPS**(`https://github.com/Allen-LPL/cv.git`),本地走 SSH。
- 对外服务:Docker 容器 `docker-openresty-1`(镜像 `pxb7/backend_openresty`,占用 80/81/443),bind-mount `/data/cv` 直接提供静态文件 → `git pull` 后即时生效,无需 build/restart。
- 线上域名:`https://cv.liupengliang.com`(中文默认 `cn.html`;英文 `index.html`)。
- 简历 PDF 下载地址:`https://wl-statics.weilantech.com/yx/2026-%E7%AE%80%E5%8E%86.pdf`(独立 CDN,**换 PDF 需单独上传到该 CDN 路径**,不随 git 部署同步)。

## 注意
- `gh-pages` 是默认分支且用于部署,直接在其上提交(不要为部署另开分支)。
- ms 服务器历史上可能落后多个提交,`git pull` 会一并同步(正常)。
