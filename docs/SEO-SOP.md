# SEO 與社群分享 SOP

本檔記錄本站 (https://www.finelinkopt.com/) 在 Google Search Console (GSC) 與社群分享 metadata 上的常用維護操作步驟，供後續接手者快速上手。

---

## 1. 提交或更新 Sitemap 至 Google Search Console

> 適用時機：新增 / 刪除 / 重大改版頁面，或更新 `sitemap.xml` 的 `<lastmod>` 後。

### 前置條件
- 已透過 `googlef0a0df0193834f70.html` 完成 GSC 網域驗證（檔案不可從 repo 移除）。
- 站台已部署，且 `https://www.finelinkopt.com/sitemap.xml` 可公開存取。

### 操作步驟
1. 登入 [Google Search Console](https://search.google.com/search-console)
2. 左上角「資源」下拉 → 選 **www.finelinkopt.com**
3. 左側選單 → **「Sitemap」**
4. 上方「新增 Sitemap」輸入框打：`sitemap.xml`（系統會自動帶網域前綴）
5. 按 **「提交」**

### 預期結果
下方「已提交的 Sitemap」會顯示：
```
sitemap.xml    狀態: 成功    已發現網址: 2（或最新頁數）
```

### 失敗排查
- **狀態: 無法擷取** → 確認 `https://www.finelinkopt.com/sitemap.xml` 在瀏覽器能打開
- **無法解析** → 用 XML 驗證器檢查格式（VS Code 直接打開能看到語法錯誤）
- **網址過少** → 比對 `sitemap.xml` 內 `<loc>` 數量是否正確

---

## 2. 要求單一網址重新被索引

> 適用時機：剛改完重大內容（如標題、首段文案、產品規格），不想等 Google 自然爬蟲。

### 操作步驟
1. GSC → 頂端搜尋框直接貼網址，例如 `https://www.finelinkopt.com/3d-profiler.html`
2. 系統會顯示「已索引 / 未索引」狀態
3. 按 **「要求建立索引」**
4. 重要頁面（首頁、3D 產品頁）各做一次

### 限制
- 每個資源每天約 **10 次** 額度。
- 不保證馬上被重抓，通常 1～3 天內生效。

---

## 3. 驗證 OG / Twitter Card 設定

> 適用時機：改完 `og:*` 或 `twitter:*` meta 後，或 LINE／FB 分享出來缺圖／缺說明時。

| 平台 | 工具 | 說明 |
|---|---|---|
| Facebook / LINE | [Sharing Debugger](https://developers.facebook.com/tools/debug/) | 貼 URL → 按「Debug」；若已快取舊版，按「Scrape Again」強制刷新 |
| X (Twitter) | [Card Validator](https://cards-dev.twitter.com/validator) | 需登入 X 帳號 |
| 通用 / 快速 | [opengraph.xyz](https://www.opengraph.xyz/) | 不需登入，看預覽最快 |
| 內部 | 直接貼到 LINE 群組（自己手機聊天室即可）| 真實預覽 |

### 常見問題
- **圖片沒顯示** → 確認 `og:image` 是「絕對網址」(以 `https://` 開頭) 且公開可下載
- **改了但 FB 還顯示舊版** → Sharing Debugger 按「Scrape Again」即可
- **LINE 顯示舊版** → LINE 通常會自動更新，最長等 24 小時

---

## 4. 驗證 JSON-LD 結構化資料

> 適用時機：改完 `<script type="application/ld+json">` 後。

### 操作步驟
1. 打開 [Google Rich Results Test](https://search.google.com/test/rich-results)
2. 貼 URL → 按「測試網址」
3. 應看到：
   - 首頁 → 偵測到 `Organization`
   - 3D 產品頁 → 偵測到 `Product`
4. 若有「警告」或「錯誤」，照訊息修正

### 進階：Schema.org 規範查詢
- [Organization](https://schema.org/Organization) — 公司／組織資料
- [Product](https://schema.org/Product) — 產品資料
- [LocalBusiness](https://schema.org/LocalBusiness) — 若未來想加開店資訊／實體門市

---

## 5. 監看 GSC 成效指標

> 建議每 1~2 個月看一次。

| 報表 | 看什麼 |
|---|---|
| **成效 → 搜尋結果** | 點擊次數、曝光次數、平均排名、CTR；可篩選關鍵字／頁面 |
| **頁面索引** | 哪些頁被 Google 收錄、哪些被排除及原因 |
| **體驗 → 網頁體驗** | Core Web Vitals（LCP、CLS、INP）— 紅色＝差、黃色＝待改善 |
| **連結** | 哪些外部網站連到我們、最常被連的頁面 |

---

## 6. Sitemap 維護慣例

`sitemap.xml` 內欄位簡述：

```xml
<url>
  <loc>絕對網址</loc>
  <lastmod>最後更新日期 YYYY-MM-DD</lastmod>
  <changefreq>monthly / weekly / yearly</changefreq>
  <priority>0.0 ~ 1.0（相對權重，僅供 Google 參考）</priority>
</url>
```

**更新時機**：
- 新增／移除頁面 → 對應增刪 `<url>` 區塊
- 大改頁面內容 → 更新該頁的 `<lastmod>` 為當天日期
- 改完後依「步驟 1」重新提交 sitemap，並對重要頁依「步驟 2」要求重新索引

---

## 附錄：本站 SEO 相關資產一覽

| 檔案 | 用途 |
|---|---|
| `sitemap.xml` | 列出所有公開頁面供搜尋引擎索引 |
| `robots.txt` | 允許所有爬蟲、指向 sitemap |
| `googlef0a0df0193834f70.html` | GSC 網域驗證檔案，**不可刪除** |
| `CNAME` | 自訂網域設定（`www.finelinkopt.com`），**不可刪除** |
| `index.html` `<head>` | meta description、canonical、OG、Twitter Card、JSON-LD Organization |
| `3d-profiler.html` `<head>` | 同上，JSON-LD 為 Product |
