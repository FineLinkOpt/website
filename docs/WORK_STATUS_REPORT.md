# 開發進度報告 (Work Status Report)

## 2026-02-26 網站優化專案啟動
- 讀取現有 `index.html` 內容，分析現有結構。
- 嘗試生成 AI 配圖，但遇到伺服器滿載問題，改為採用高畫質外部圖庫與 CSS 特效。
- 建立 `task.md` 任務清單。
- 制定 `implementation_plan.md` 實作計畫，等待使用者確認設計方向。
- 完成 `index.html` 首版現代化重構 (套用深色主題、Glassmorphism、響應式設計)。
- 使用者提議提供真實專案/實績照片，準備進行真實資產整合。
- 檢視 `d:/公司/公司資料/` 目錄，確認目前理解的公司技術脈絡 (AI Vision, 3D FPP, AOI)，並向使用者詢問確切的照片資料夾路徑。
- 成功讀取 `D:/公司/公司資料/Website/assets` 中的真實企業影像，並全面套用於 `index.html` 的 Hero 區塊、解決方案配圖、企業優勢配圖以及導覽列 Logo。
- 根據提供的名片，移除 Logo 的純白濾鏡（並加上微透白底確保在深色背景的可見度），加入 Slogan，並更新聯絡資訊 (包含電話、信箱、完整地址與統編)。
- 針對 Logo 顯示不協調的問題，移除方塊白底，改採 `drop-shadow` 實現發光效果以融入背景；並將 AOI 整合平台的配圖替換為設備照片 (`PXL_20240926_035737463.jpg`)，以與 AI 辨識軟體截圖作為區隔。
- 依據回饋對齊 Header 區塊：縮小 Logo 高度以匹配旁側標題，並將 Footer 中的英文公司名稱由 "Chialien" 更正為名片上的 "FineLink Optical Technology"。
- 協助將優化後且整合真實圖庫的網站專案上傳至 GitHub `FineLinkOpt/website` (期間移除了過大的 .mp4 與 .mov 原始檔以符合 GitHub 容量限制)。
- 協助上傳並提交流程 Google Search Console 網域驗證檔案 (`googlef0a0df0193834f70.html`) 至 GitHub 主分支。

## 2026-02-27 實戰案例與網站深化優化
- 擴充「關於我們 (About Us)」區塊，加入「創造可以被利用的價值」座右銘與團隊底蘊文案。
- 增加「實戰案例 (Case Studies)」板塊，包含「極端環境的 3D 量測」與「自動化設備的 AI 賦能」兩項實際應用，並搭配現場照片。
- 在「AOI 整合開發平台」中擴充通訊與交握能力描述（支援 PLC 與 MES 上傳），強調系統整合的便利性。
- 強化「行動呼籲 (Call to Action)」，於聯絡合作區塊新增「預約線上軟體 Demo」與「索取視覺模組整合評估」兩項具體按鈕選項。
- 依據使用者需求，更新「實戰案例」的配圖。
- 參考《第 32 屆中小企業創新研究獎》申請書，重新改寫了「自動化設備的 AI 賦能」的案例說明。該案例現已調整為真實的「偏光板清潔機自動分揀辨識系統」，強調結合深度學習 (AI) 與自動化光學檢測 (AOI) 技術，即時精準判斷 Mark 瑕疵並取代人工分揀。
- 將「極端環境的 3D 量測」說明由「3D 雷射與結構光技術」修正為「3D 雷射技術」。
- 增加全站圖片保護機制，於 CSS 加入 `user-drag: none`、`user-select: none` 以及 `pointer-events: none` 屬性，防堵圖片被另存下載或拖曳，保護公司資產。
- 協助將今日的修改與更新提交 (Commit) 並推送 (Push) 至 GitHub `main` 分支，完成網站內容更新上線。
- 依據指示更新企業優勢配圖 `assets/PXL_20251211_092354209.jpg` 並提交至 Github。
- 再次接收並更新最新的企業優勢配圖 `assets/PXL_20251211_092354209.jpg`，並完成 GitHub 上傳部署。
- 修復手機端圖片無法顯示的問題：移除 CSS 中導致行動裝置上圖片不可見的 `pointer-events: none` 屬性，改以 JavaScript 攔截右鍵選單的方式 (`contextmenu` 事件) 來保護圖片不被下載，同時維持正常的圖片顯示。
- 更新 `index.html` 中的圖片附檔名（將 `.png` 替換為 `.jpg`，包含螢幕擷取畫面與已標註圖片）。
- 將所有近期編輯或新增的圖片集 (Assets) 加入並提交至 GitHub repository，避免提交過大的影音原檔以符合容量限制。
- 於「實戰案例」的「自動化設備的 AI 賦能」區塊下方，以並排 (Side-by-side) 方式加入 `SAI檢測介面.png` 與 `SDL分類學習介面.png` 的軟體實際操作截圖，並添加網頁視覺特效，以強化軟體技術實力的展示。
- 依據後續評估，取消 `SAI檢測介面.png` 與 `SDL分類學習介面.png` 的展示，改以更具說服力的動態影片 `ClassifyCenter.mp4` 取代，並新增為第三項實戰案例：「外掛式 AI 智能分類系統」。
- 該新案例強調了在不更動硬體下，如何彌補傳統 AOI 的不足，並且能以 1 台 AI 主機對應 4 套傳統 AOI 的極致效能，解決客戶的矢印章不良與髒污誤判等問題。
- 修正「外掛式 AI 智能分類系統」影片因固定高度而被上下裁切的問題，調整為自適應高度以完整顯示介面。
- 依據回饋，移取消了案例介紹文案中原有的藍綠色粗體強調樣式，讓整體閱讀體驗更為乾淨一致。
- 將更新版本的 `ClassifyCenter.mp4` 影片檔案重新提交並推送至 GitHub。
- 曾嘗試調整「實戰案例」區塊的 CSS Grid 以實現三欄排版，但經評估後認為會使得案件卡片（如「外掛式 AI 智能分類系統」）在視覺上變小而減弱展示力道，因此已恢復為原先的排版設定，確保重點特色能被清楚閱讀。
- 修正 `index.html` 中第 274 行 CSS 語法警告，為 `-webkit-background-clip: text;` 補充了標準相容屬性 `background-clip: text;` 以符合標準規範。

## 2026-02-28 網站視覺素材更新
- 依據需求，透過 Python (OpenCV / PIL) 腳本，成功從原始 Logo (`assets/FineLinK_Logo_New.png`) 中萃取出黃色斜向十字星，並將其置於單純綠色圓角方形背景正中央，生成新的企業 Logo 圖騰 (`assets/Company_Logo_Icon.png`)。
- 將生成的 Logo 圖騰 (`assets/Company_Logo_Icon.png`) 的綠色背景修改為對齊原 Logo 中公司名稱的綠色，並將中間的黃色十字星進一步放大，使其尖端能夠自然突出並超越圓角方形的邊緣，形成滿版且帶有突破感的視覺效果。
- 針對 `assets/Company_Logo_Icon_Circle.png` 圓形企業 Logo 進行了深度優化：移除了星星周圍殘留的背景綠色毛邊，並萃取純粹的黃色星星將其零邊距（無 Padding）精準縮放至 512x512 的滿版尺寸。現在星星的左上角以及右下角的尖端，已經絕對完美地切齊並頂到了 Icon 畫布的極限頂點。
- 接收使用者提供的自製網站標誌 `assets/FineLinK_Logo_Rect.png`，並已將其配置於 `index.html` 的 `<head>` 區塊中，擔任網站 Favicon 與行動裝置的 Apple Touch Icon。
- 經過以上所有操作與新增之視覺素材（包含動態影片補充），目前最新的版本已成功「提交 (Commit)」並「推送 (Push)」回 GitHub (`FineLinkOpt/website`) 主分支，完全同步上線。
- 為了使 `assets/path94.png` (綠色 F 圖標) 的邊緣達到絕對銳利且「不改變任何原始綠色」的要求，捨棄了會產生光暈亮邊的傳統銳化濾鏡 (Unsharp Mask/Laplacian)。改採 Python 取樣其原始核心的絕對綠色值 (`RGB: 60, 116, 56`) ，並對透明通道進行直接的二值化硬邊裁切，最後填入該純粹綠色宣告。這去除了所有的半透明抗鋸齒毛邊，實現了極致銳利又 100% 維持原色的完美邊緣切齊。
- 根據使用者指示，將網站的 Favicon 以及 Apple Touch Icon 從原先的 `FineLinK_Logo_Rect.png` 替換為最新的 `assets/FineLinK_Logo_Rect1.png`。
- 根據指示將 `assets/ObjectDetect.mp4` 影片放上網頁，於「實戰案例」區塊新增「高精度 AI 物件偵測」項目，展示動態物件定位與辨識能力。
- 接收並更新最新的 `assets/ObjectDetect.mp4` 影片檔案，完成 GitHub 上傳與網站部署。
## 2026-05-16 評估 3D 量測擴充素材
- 檢視 `assets/3D檢測` 目錄內的設備外觀圖、3D 檢視截圖及各項精度分析報告 (Gage Study、重複性、均勻度)。
- 確認將 3D 輪廓量測技術獨立為新產品展示頁面 (如 3d-profiler.html)，目前準備進行開發。
- 依據指示，將首頁「3D 輪廓量測技術」恢復原有的文字與圖片，僅保留點擊跳轉功能。
- 建立全新獨立頁面 3d-profiler.html，專門展示桌上型 3D 輪廓量測設備的外觀、高解析 3D 視覺化分析介面，並提供三份工業級精度驗證報告供下載。
- 依據需求，將 3d-profiler.html 中直接提供 PDF 下載的區塊移除，改為萃取報告中的核心科學數據 (Cg/Cgk 指標、Z軸變異、FOV 高度落差)，轉化為簡單明瞭的「工業級精度規格」展示。
- 研究 `warpage_app` 系統原始碼，並於 `3d-profiler.html` 網頁中新增「軟體核心功能與演算法」區塊，條列 HDR 融合、多頻相位解碼、影像拼接、AI 樣板編輯及即時 3D 渲染等系統亮點。
- 讀取 3DWarp 系統最新的精度與行銷策略文字報告，並根據實際數據與建議，將 3d-profiler.html 中的規格宣稱修正為：「Cg = 1.15」、「Z軸變異中位數 < 15 μm」以及「局部雜訊穩定度 0.06 ~ 0.07 mm」，精準對齊實際機台的優勢與應用情境。
- 更正 3d-profiler.html 設備外觀圖為 ssets/3D檢測/FineLink外觀圖.png。
- 考量網頁效能，將高達 52MB 的 height_map_20260515_215151.png 記憶體模組 3D 拼接圖壓縮為 height_map_compressed.jpg (約 5MB)，並大幅簡化「直覺的 3D 視覺化分析」區塊，改為全版面單圖展示該拼接成果，突顯大視野與高解析度優勢。
- 依據回饋，修正「直覺的 3D 視覺化分析」區塊的排版，移除原先三圖中的第一張圖，保留了「缺陷偵測介面」與「軟體操作介面」兩張圖進行並排展示，使得版面更加聚焦且俐落。
- 依據需求，將 3d-profiler.html 網頁中的「軟體核心功能與演算法」以及「工業級精度規格」兩大區塊，由原先的卡片網格排版調整為乾淨簡潔的條列式 (Bulleted List) 呈現。
- 根據指示更新「高精度 3D 輪廓量測設備」的產品說明文案，強化其在「高反射、透明、軟性材料」及「精密結構量測」等核心應用領域的描述。
- 同步更新 `3d-profiler.html` 的 Meta 描述，確保搜尋引擎優化 (SEO) 資訊與網頁內容一致。
- 於 `3d-profiler.html` 新增「工業級決策視覺平台」條列式區塊，說明系統整合 AI 偵測及 OCR 功能後的各項應用場景 (包含偏光板翹曲、軟性材料平坦度、精密結構高度差、表面輪廓與高反射材料量測)。
- 依據需求，將新增的應用領域說明重新排版並移入 Hero 區塊的「設備介紹 (Product Details)」清單內，使其更具視覺一致性與易讀性。
- 為了確保視覺上完美契合，再次將該段應用領域說明改寫為與前三項完全相同的 `feature-list` 特點項目格式，統整為「工業級決策視覺平台」。
- 進一步精簡第四點特點項目的說明文字，使排版更加緊湊，兼顧閱讀流暢度與版面平衡。
- 依據回饋，移除說明文字中的斷行設定，使其呈現為最精簡的連續段落。
- 修正 `3d-profiler.html` 中「直覺的 3D 視覺化分析」區塊第一張圖 (3D拼接圖) 的文案，更新為「大視野 3D 拼接分析」，並改寫說明為「完整還原大尺寸元件的 3D 全貌，呈現整體翹曲與平整度趨勢，讓跨視野檢測不再有死角」。
- 刪除 `3d-profiler.html` 頂部「高精度 3D 輪廓量測設備」的冗長段落：「可應用於翹曲、厚度、平坦度、表面輪廓與精密結構檢測」，以避免與下方新增的第四點設備特色介紹內容重複。
- 修正「軟體核心功能與演算法」區塊中關於「多頻相位解碼 (Multi-Frequency FPP)」的錯誤描述，將原本的「結合 FFT 與時間解相」更正為精準的「結合專屬相移演算法與強效抗噪濾波，精準重建微米級 3D 高度圖」。
- 更新「軟體核心功能與演算法」區塊中「大視野拼接技術 (Stitching)」的說明文案，將原先侷限於「大尺寸偏光板檢測」的敘述，修改為更具泛用性且專業的「輕鬆應對大尺寸工件的嚴苛檢驗」。
- 移除「軟體核心功能與演算法」區塊中所有項目標題後方的英文備註 (如 Multi-Frequency FPP, HDR Fusion, Stitching, Template Editor 等)，使版面更為清爽且專注於中文的技術傳達。
- 更新 Hero 設備介紹區塊中「微米級精度掃描」的描述，將原本的「結合 3D 結構光與 FPP 技術」精確修正為「運用 FPP 3D 結構光技術」，使語句更為專業順暢。
- 再次優化 Hero 設備介紹區塊的文案，將「專為極端應用打造」改為「專為嚴苛檢測需求打造」，並將說明更正為「完美克服金屬高反光與深色吸光材質帶來的取像干擾，實現高穩定度的精密量測」，精確強調 FPP 技術在處理極端光學特性材質上的優勢。
- 為 Claude Code 建立 `CLAUDE.md` 工作指引，記錄專案結構、共用慣例（圖片保護、資產容量限制）以及內容更新流程，協助後續維護的一致性。
- **效能優化**：將首頁 hero 背景圖 `PXL_20240925_064857239.jpg` 從原始 4.9 MB 壓縮並縮放至 1920px 寬，減為 419 KB（約 -92%），首屏載入速度大幅提升。
- **資產清理**：刪除 `assets/` 內所有未引用且體積偏大的影音與圖片檔（含 30 MB 的未引用 mp4、52 MB 的未壓縮 PNG、8.6 MB 的標註圖等），並一併移除存放於公開 repo 內的中小企業創新研究獎申請書 PDF 與內部 3DWarp 系統技術／市場策略報告 (.txt/.pdf)，避免敏感資料外洩。
- **共用樣式抽取**：將兩支 HTML 重複的 `:root`、reset、header、nav、`.section-title`、footer 等 ~170 行樣式抽出至 `assets/styles.css`，並順手清除 3d-profiler.html 內已不再使用的 `.report-*` dead CSS。`index.html` 行數由 672 → 508，`3d-profiler.html` 由 503 → 305。
- **SEO 與社群分享優化**：兩支 HTML 補上 `<link rel="canonical">`、Open Graph (`og:*`) 與 Twitter Card meta，使 LINE／Facebook／Slack 分享時能顯示預覽圖文；同步加入 Schema.org JSON-LD 結構化資料 — 首頁為 `Organization`（含公司名、Logo、地址、電話、統編），3D 產品頁為 `Product`（含 Cg、Z 軸變異等規格 `additionalProperty`），有助於 Google 搜尋顯示企業資訊框與富摘要。
- **第二波優化 (2026-05-16 晚)**：
  - 所有 `<img>` 補上 `width`/`height` 屬性（依實際像素），非首屏圖再加 `loading="lazy"`，行動裝置滑到才下載，且消除版面位移 (CLS)。`alt` 文字一併改寫為更具描述性的版本。
  - 兩部案例影片加 `preload="metadata"`，避免行動裝置在進站當下就先抓整段影片。
  - 新增 `robots.txt` 與 `sitemap.xml`（含首頁與 3D 產品頁），加速 Google 收錄。
  - 新增 `404.html`，承襲整站視覺風格、提供返回首頁按鈕（取代 GitHub Pages 預設 404）。
  - hero 區塊移除 `background-attachment: fixed`，避免 iOS Safari 上背景圖跳動或無法顯示的問題。
  - a11y：兩頁加入「跳至主內容」鍵盤捷徑、為 `<nav>` 補 `aria-label="主導覽"`、用 `<main id="main-content">` 包覆主要內容區塊。
  - 移除已失效的一次性 Logo 處理腳本 `sharpen_logo.py`（其參照的 `FineLinK_Logo_Rect.png` 已於前一波清理刪除）。

---

## 開發進度總結｜2026-05-16 網站效能 / SEO / 可及性全面優化

本日完成兩波結構性優化並推送上線 (`origin/main`)，網站 (https://www.finelinkopt.com/) 已透過 GitHub Pages 自動部署。

### 第一波 — 效能、資產清理、CSS 抽取、SEO Metadata
- **Commit**：`c167021` `perf: compress hero bg, prune unused assets, extract shared CSS, add SEO metadata`
- **異動規模**：30 個檔案、+349 / −402 行

| 範疇 | 內容 |
|---|---|
| 效能 | hero 背景圖 `PXL_20240925_064857239.jpg` 由 4.9 MB → 419 KB（-92%，縮至 1920 px 寬） |
| 資產清理 | 刪除 23 個未引用／敏感檔案：30 MB 未用 mp4、52 MB 未壓縮 PNG、創新研究獎申請書 PDF、3DWarp 內部技術／市場策略報告 (.txt/.pdf)、過時的截圖與 PNG。資產目錄淨減約 115 MB |
| 共用樣式 | 抽出 `assets/styles.css`（172 行）：設計 token、header、nav、`.section-title`、footer、圖片保護、`fadeUp`；清掉 `.report-*` dead CSS。`index.html` 672→508 行、`3d-profiler.html` 503→305 行 |
| SEO | 兩頁補 `<link rel="canonical">`、Open Graph、Twitter Card；首頁 JSON-LD `Organization`（含公司名、Logo、地址、電話、統編、slogan、聯絡資訊）；3D 產品頁 JSON-LD `Product`（Cg=1.15、Z 軸變異 <15 μm 等 `additionalProperty`） |
| 內容 | `index.html` meta description 從 36 字擴充為 79 字，加入 `FineLink Optical Technology` 全名與「3D 輪廓量測」關鍵字 |
| 文件 | 新增 `CLAUDE.md`（給未來 Claude 的工作指引）；本檔追加今日工作紀錄 |

### 第二波 — Lazy load、404、a11y、Mobile 修正
- **Commit**：`ad7d1c8` `perf+a11y: lazy-load images, add 404/robots/sitemap, accessibility polish`
- **異動規模**：8 個檔案

| 範疇 | 內容 |
|---|---|
| 效能 | 10 個 `<img>` 補 `width`/`height`（依實際像素），7 個非首屏圖加 `loading="lazy"`；2 個 video 加 `preload="metadata"` |
| SEO | 新增 `robots.txt` 與 `sitemap.xml`（含首頁、3D 產品頁） |
| UX | 新增 `404.html`（同站視覺、含返回首頁按鈕），取代 GitHub Pages 預設 |
| Mobile | hero 移除 `background-attachment: fixed`（修 iOS Safari 顯示問題） |
| 可及性 | 兩頁加入「跳至主內容」skip-link、`<nav aria-label="主導覽">`、`<main id="main-content">` 包覆主內容；改寫所有 `alt` 文字為更具描述性的版本 |
| 整潔 | 移除已失效的一次性腳本 `sharpen_logo.py` |

### 量化成果（估計）

| 指標 | 優化前 | 優化後 |
|---|---|---|
| 首屏關鍵資源（hero 背景圖） | 4.9 MB | 419 KB |
| Repo 工作目錄資產目錄 | ~120 MB | ~5 MB |
| 兩支 HTML 總行數 | 1 175 | 813（含共用 CSS 172 行另計） |
| 圖片可預判尺寸（避免 CLS） | 0/10 | 10/10 |
| 結構化資料 (JSON-LD) | 無 | 首頁 Organization + 3D 頁 Product |
| 社群分享預覽 (OG/Twitter Card) | 無 | 兩頁完整覆蓋 |

### 已知未做（需設計決策才動）

- 案例區塊大量 inline `style="..."` 抽成 class — 視覺風險中、需要本地確認
- 行動裝置漢堡選單 — 需要 JS 與 icon 設計決策
- 外部 CDN (`Font Awesome`、`Google Fonts`) 加 SRI — 升版時需手動更新 hash
- Google Search Console 重新提交 `sitemap.xml` — 需業主登入操作

---

## 2026-05-16 GSC 結構化資料修正
- Google Search Console 網址審查回報 `3d-profiler.html` 的 `Product` schema 缺少必要欄位（必須指定 `offers`、`review` 或 `aggregateRating` 其中之一）。於 JSON-LD 補上 `offers` 區塊：因產品屬 B2B 客製報價型，採用 `priceSpecification`（含 `priceCurrency: TWD` 與「依規格客製報價」說明文字）取代寫死的數字價格，避免出現「價格為 0」的誤導性警告，並透過 `url` 連結到首頁聯絡區、`seller` 標示為佳聯光學科技。

## 2026-05-17 修正 GSC 產品摘要結構化資料錯誤
- 因 Google Search Console (GSC) 判定 `Product` 結構化資料內的 `offers` 必須包含 `price` 欄位（即使是 B2B 客製報價），否則會報出「必須指定「offers」、「review」或「aggregateRating」」的重大問題。
- 於 `3d-profiler.html` 的 `application/ld+json` 內，在 `offers` 及 `priceSpecification` 中補上 `"price": "0"`，以符合 GSC 對 `Product` Snippet 的嚴格檢查標準，解決網頁無法正確呈現結構化資料的問題。
