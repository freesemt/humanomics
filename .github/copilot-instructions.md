<!-- AI Context Standard v0.9.2 - Adopted: 2026-04-02, Updated: 2026-05-05 -->
# AI Assistant Initialization Guide — Humanomics

**Purpose**: Initialize AI context for working with this repository

> **On every session start**: Before responding to ANY first message, read [`PROJECT_STATUS.md`](../PROJECT_STATUS.md) first, then output exactly this line at the top of your response:
> `✅ Initialized (humanomics) — [現在のタスクを一言で]`
> Then respond to the user's message.

---

## 📚 Core Documents to Read at Initialization

1. **This file** — working conventions and repository structure
2. **PROJECT_STATUS.md** — current focus and recent work
3. **README.md** — project overview

---

## 🎯 Repository Context

**Project**: Humanomics Study Group — Economics for the Climate Change Problem  
**Website**: https://freesemt.github.io/humanomics/  
**Repository**: https://github.com/freesemt/humanomics  

**Mission**: A study group exploring economic approaches to climate change, centering on Keynesian economics, employment theory, and monetary policy. Monthly dialogue sessions with Professor Y.H. are recorded and published here.

**Primary language**: Japanese (content), English (some references and UI)

**Key academic themes**:
- Keynesian economics and employment theory (本荘 2019 paper as primary reference)
- Adam Smith's *The Theory of Moral Sentiments* (ongoing study)
- Climate change policy and economics
- Japanese and international politics

---

## 📂 Repository Structure

```
humanomics/
├── docs/                           # GitHub Pages root (static site)
│   ├── index.html                  # Top page (Papers / Thoughts / Dialogs)
│   ├── styles.css                  # Shared stylesheet
│   ├── dialogs/
│   │   ├── index.html              # Dialog index (password-protected)
│   │   └── YYYYMMDD/               # Per-session directory
│   │       ├── index.html          # Session notes
│   │       ├── honjo-2019.html     # 本荘2019解読メモ (if present)
│   │       ├── keynes.html         # ケインズ研究メモ (if present)
│   │       └── figs/               # Figures for that session
│   └── references/
│       ├── honjo-2019.html         # 本荘 2019 paper reference
│       └── adam_smith/             # Adam Smith TMS project
│           ├── index.html
│           ├── moral_sentiments_toc.json
│           └── applications/
├── scripts/                        # Utility scripts
│   ├── checkpw.js                  # Password protection logic
│   ├── sha256-min.js               # SHA256 library (minified)
│   ├── core-min.js                 # Core library (minified)
│   ├── extract_moral_sentiments.py # PDF extraction for TMS
│   └── extract_pdf_full.py         # General PDF extraction
├── .github/
│   └── copilot-instructions.md     # This file (STATIC conventions, auto-loaded)
├── PROJECT_STATUS.md               # Dynamic state and current work
├── AI_CONTEXT_STANDARD.md          # Source standard document
└── README.md
```

---

## 🔑 Working Conventions

### Dialog Session Directory Format

- Directory name: `YYYYMMDD` (e.g., `20260305` for March 5, 2026)
- Location: `docs/dialogs/YYYYMMDD/`
- Required file: `index.html` (session notes)
- Optional files: `honjo-2019.html`, `keynes.html`, `figs/`

### HTML Template for Dialog Session Pages

All dialog session `index.html` files follow this structure:

```html
<!DOCTYPE html>
<head>
<meta charset="utf-8">
<title>YYYY-MM-DD</title>
<link rel="stylesheet" type="text/css" href="../../styles.css">
<!-- MathJax script block (copy from existing sessions) -->
</head>
<style type="text/css">
img.middle { vertical-align: middle; }
body { line-height:1.7; }
</style>
<body>
<pre>
・ BGM Selection
  ・ <a href="URL">BGM Title</a>

・ トピック1
・ トピック2
...

・ <a href="../../dialogs/index.html">Dialogs with Professor Y. H.</a>
</pre>
</body>
</html>
```

Key points:
- `<pre>` tag for monospace text layout (core site design choice)
- MathJax included for LaTeX math rendering (`$...$` inline, `$$...$$` display)
- Relative path `../../styles.css` from `dialogs/YYYYMMDD/`
- Navigation link back to dialog index at bottom

### Password Protection (Dialog Index)

`docs/dialogs/index.html` is password-protected via SHA256 hash comparison.  
The password hash is stored in the `checkPassword()` call in the `<body onload>` attribute.  
**Do not expose or guess the password.** The protection mechanism is client-side only.

### Updating the Dialog Index

When adding a new session, update `docs/dialogs/index.html`:
1. Update "次回の対話" (next dialog) date inside `#protected-content`
2. Add new entry to the Index list: `・ <a href="YYYYMMDD/index.html">YYYY-MM-DD</a>`
3. Add `（準備中）` if the session page is a placeholder

### Sitemap

After adding new pages, consider updating `docs/sitemap.xml` for SEO.

### 最新時事情報へのアクセス方法

対話準備や議論の背景調査に使える公開ニュースソース（認証不要・直接取得可能）：

| サービス | URL | 備考 |
|---------|-----|------|
| **The Guardian** | `https://www.theguardian.com/world/[topic]` | ✅ 最も信頼性高い。トピック別ページで最新記事一覧を取得可能 |
| **BBC News** | `https://www.bbc.com/news/topics/[topic-id]` | ✅ 取得可能 |
| **Reuters** | `https://www.reuters.com/world/` | △ 取得できない場合あり |
| **AP News** | `https://apnews.com/hub/[topic]` | △ 接続リセットされる場合あり |

**❌ アクセス不可（ログイン必須）**:
- NHK ONE (`news.web.nhk/newsweb/`) — NHK の全記事がここにリダイレクトされる（2026-03時点）
- 日本経済新聞 (`nikkei.com`) — 有料会員制

**使い方**:
- トピック例: `https://www.theguardian.com/world/iran`, `/world/ukraine`, `/world/donald-trump`
- 取得したページから主要見出しを抽出→ 要点を箇条書きにして COPILOT_MEET_INIT.md に反映する
- 日本語翻訳が必要な場合は取得と同時に翻訳して提示する

**確認済み実績（2026-03-05）**:
- The Guardian の `/world/iran` から米・イスラエル vs イラン軍事衝突（第5日目）の速報を取得成功

---

### Python Scripts for PDF Extraction

- `scripts/extract_moral_sentiments.py` — extracts text from Adam Smith TMS PDF
- `scripts/extract_pdf_full.py` — general PDF full-text extraction
- Usage: `python scripts/extract_pdf_full.py <path-to-pdf>`

**AI Assistant Rule**: When asked to reference or quote from a PDF (e.g., Adam Smith TMS, 本荘 2019), run the appropriate extraction script first rather than attempting to `read_file` the binary directly. Extracted text can then be searched and quoted normally.

---

## 💡 Quick Tips for AI Assistants

- **Primary task type**: Adding new dialog session pages, updating the dialog index, editing reference materials
- **Site is static HTML**: No build system, no framework — edit HTML files directly
- **Math rendering**: MathJax is loaded via CDN; use `$...$` for inline, `$$...$$` for display math in HTML
- **Character encoding**: Always UTF-8; Japanese content is common
- **No CMS**: All content is hand-written HTML — maintain the `<pre>` layout style
- **Dialog frequency**: Monthly, typically first Thursday of the month
- **Next session**: Check PROJECT_STATUS.md for upcoming session date

### Understanding "Copilot's Good Judgment"

<!-- 正典は jichikai-2-priv/COPILOT-INIT.md の同名セクション。内容が乖離した場合はそちらを優先。 -->

ユーザーが期待する「良識」:
- **判断の主体性**: 自ら考え、判断し、提案する（選択を丸投げしない）
- **同調リスクへの警戒**: ユーザーの期待に同調するだけでなく、批判的思考を保持
- **知的謙虚さ**: 簡単にまとめられない時は、その複雑さを認める
- **哲学的洞察の質**: 表面的な接続ではなく、本質的な関係を見抜く

対話セッション（COPILOT_MEET_INIT.md 参照）での良識の発揮:
- 話題の転換点や新情報が出た時、必要と判断したら「調べましょうか？」と自発的に提案する
- 情報源の信頼性についても批判的視点を添える
- 議論の流れを単に追うのではなく、論点の深化に貢献する

---

## 🤖 AI Operating Conventions (from AI Context Standard v0.8.8)

### Failure Recovery

When the same operation fails 3+ times, stop and explain to the user. Propose alternatives. Do not silently retry 15+ times.

### PowerShell Multi-repo Git

Always use `git -C <path>` instead of `cd <path>; git ...`.  
The terminal tool may silently strip `cd` from chained commands.

```powershell
# ❌ Unreliable
cd C:\path\to\repo; git commit -m "..."

# ✅ Reliable
git -C C:\path\to\repo commit -m "..."
```
