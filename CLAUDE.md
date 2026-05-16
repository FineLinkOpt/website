# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 專案概述

佳聯光學科技 (FineLink Optical Technology) 的企業形象網站，透過 GitHub Pages 部署。

- GitHub Repo：`FineLinkOpt/website`，`main` 分支即為線上版本。
- 自訂網域：`www.finelinkopt.com`（由根目錄 `CNAME` 設定，**請勿刪除**）。
- 網域驗證檔：`googlef0a0df0193834f70.html`（Google Search Console 用，**請勿改名或刪除**）。
- 全站內容語言為**繁體中文 (`zh-TW`)**，編輯文案時請維持此語氣與用字。

## 建置與執行

本專案**沒有任何 build system、`package.json`、測試或 linter**。所有頁面皆為手寫 HTML，CSS 與 JS 全部以 `<style>` / `<script>` 內嵌。

- 本地預覽：直接以瀏覽器開啟 `.html`，或在根目錄執行 `python -m http.server` 之類的靜態伺服器即可。
- 部署：`git push origin main` 即上線，GitHub Pages 會直接從根目錄發布。

## 頁面結構

- `index.html`：首頁（Hero、關於我們、技術方案、企業優勢、實戰案例、聯絡）。
- `3d-profiler.html`：3D 輪廓量測設備產品詳細頁。由首頁「3D 輪廓量測技術」服務卡的 `onclick="window.location.href='3d-profiler.html'"` 連入。
- `sharpen_logo.py`：一次性 Pillow 腳本，僅用於 Logo 圖檔後製，**不屬於網站 runtime**。

**共用樣式**已抽到 `assets/styles.css`（設計 token、reset、header、nav、`.section-title`、footer、圖片保護等基底）。兩支 HTML 透過 `<link rel="stylesheet" href="./assets/styles.css">` 載入，剩下的 `<style>` 區塊只放各自頁面專屬樣式（如 hero、cards、gallery）。修改共用設計 token 只需動 `styles.css` 一處；CDN 連結（Google Fonts / Font Awesome）以及防右鍵 `<script>` 仍各自重複，這部分目前刻意保留以維持單檔可預覽。

## 必須保留的慣例

**圖片保護**：公司影像是業主明確要求保護的資產。
- 每一個 `<img>` 都要帶 `oncontextmenu='return false'` 與 `draggable='false'`。
- 保留 `img { -webkit-user-drag: none; user-select: none; ... }` 這段 CSS。
- **不可再加回 `pointer-events: none`**——此屬性曾導致行動裝置上圖片無法顯示／互動，已被移除，改用 `<body>` 底部委派的 `contextmenu` 事件監聽器來封鎖右鍵選單，請保留該段 JS。

**資產容量限制**：GitHub 拒絕超過 100MB 的檔案，且本 repo 歷史上已清理過多次大型影音原檔。提交前請確認：
- 不要直接 commit `.mov` 或數百 MB 的 `.mp4` 原檔，先壓縮再上傳。
- 大型 PNG（例如原始的 `height_map_20260515_215151.png` 約 52MB）請壓成 JPG 再引用。`assets/3D檢測/height_map_compressed.jpg` 即為此模式的範例。

**資產路徑**統一使用相對路徑 `./assets/...`。`assets/3D檢測/` 子資料夾的中文名稱是刻意保留的，引用時請維持中文路徑。

**Favicon** 固定為 `assets/FineLinK_Logo_Rect1.png`（注意結尾數字 `1`），同時用於 `rel="icon"` 與 `apple-touch-icon`。

## 內容更新流程

`docs/WORK_STATUS_REPORT.md` 是繁體中文的時序變更紀錄，依日期分節（例如 `## 2026-05-16 評估 3D 量測擴充素材`）。完成任何具體內容或資產修改後，請在當天的日期區塊下追加一筆條列（若該日期區塊尚未建立則新增之）。少數重大文案決策另存於 `docs/WEB.CONTENT-*.md`，僅在被明確要求時才仿此模式建立新檔。

## 設計 Token 參考

兩個頁面 `:root` 內定義相同：
- `--bg-color: #050b14`（深海軍藍底）、`--text-color: #e0e6ed`
- `--primary-color: #00e5ff`（青色主色，用於 CTA、連結、漸層字）
- `--secondary-color: #4da6ff`、`--accent-color: #7b2cbf`
- 玻璃擬態：`--card-bg` / `--glass-bg` / `--glass-border`
- 字體：Google Fonts 的 Inter + Noto Sans TC；圖示：Font Awesome 6.4 CDN
