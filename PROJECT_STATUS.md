# Project Status — Humanomics

**Last Updated**: 2026-09-02

> For working conventions and structure, see [`.github/copilot-instructions.md`](.github/copilot-instructions.md).

---

## 🎯 Current Task

2026-09-03 対話セッション準備中 🔬
- `docs/dialogs/20260903/index.html` 作成済み（プレースホルダー）
- `docs/dialogs/20260903/COPILOT_MEET_INIT.md` 作成済み（2トピック構成）
  - トピック1：Medium 記事「China Officially Classifies Single Women Over 27 as "Leftovers"」
    - 記事は会員限定のため冒頭のみ閲覧、一般的背景知識（剰女・一人っ子政策・人口動態）で補完
  - トピック2：日本で頻発する大雨災害と気候変動
    - 「人類は失敗した」という傍観的・宿命論的態度への問題提起（ユーザーの問題意識）
    - 適応・緩和の両面でなお選択の余地があるという立場を整理
    - 核心的な問い（追記）：頻発する被害がCO2削減という大局的対策と結び付けて報道・議論されない「大局的なラグ」はなぜ生じるか
      → 心理的距離・因果帰属の難しさ・報道の分業・時間スケールの不一致・政治的忌避・馴化効果・抽象の質の問題、の7仮説を整理
  - いずれも「これまでの非自発性・総需要不足というテーマとの接続候補」を整理
- `docs/dialogs/20260903/nonregular_employment_data.md` を作成
  - 不本意非正規雇用の一次統計、賃金・所得、雇用者報酬・消費・GDPのデータ源を整理
  - 不本意非正規の統計上の定義と、非正規雇用全体の雇用の質を区別して分析する方針を明記
  - 次回は取得する表・期間を確定し、年次推移、属性別分布、マクロ接続の独自図表を作成する
- `docs/dialogs/index.html` の対話日・インデックスを更新（2026-08-06 / 2026-09-03 追加）

---

## 📋 Recent Work

### 2026-09-02 — 非正規雇用データ台帳の作成 🔬
- `docs/dialogs/20260903/nonregular_employment_data.md` を新規作成
  - 総務省「労働力調査（詳細集計）」を基準系列に設定
  - 就業構造基本調査、賃金構造基本統計調査、国民経済計算を分析用の中核資料として整理
  - 厚労省資料・男女共同参画白書・JILPT研究は解釈と資料探索の補助として位置付け
- `COPILOT_MEET_INIT.md` に台帳への参照と、対話で確認する分析範囲を追記

### 2026-08-28 — 2026-09-03 対話セッション準備 🔬
- `docs/dialogs/20260903/index.html` を新規作成
- `docs/dialogs/20260903/COPILOT_MEET_INIT.md` を新規作成・更新
  - トピック1：中国の「剰女」公式分類に関する Medium 記事を共有トピックとして整理
    - 人口動態・ジェンダー規範・労働経済の接点を背景知識としてまとめ
  - トピック2：日本の大雨災害頻発と気候変動を追加
    - 「人類は失敗した」という傍観的態度への批判をユーザーの問題意識として明記
    - 経済学の役割（緩和策・適応策への投資の位置づけ）を整理
  - いずれのトピックも、これまでの対話（ケインズの非自発的失業 ↔ 非自発的非正規雇用、抽象の質の議論）との接続候補を表にまとめ
- `docs/dialogs/index.html` を更新（20260806・20260903 のリンク追加、対話日を更新）

### 2026-08-06 — 対話セッション準備（本荘さん） ✅
- `docs/dialogs/20260806/index.html` を作成
- `docs/dialogs/20260806/COPILOT_MEET_INIT.md` を作成
  - テーマ：ケインズの非自発的失業 ↔ 本荘さんの非自発的非正規雇用
  - 共通の問題意識：個人の意思と市場結果の乖離、構造的な「非自発性」
  - 本荘 2019 論文の全6節を要約
  - 抽象フレームワーク追加：低レベル vs 高レベルの抽象、並列例（物理学・心理学）
- `docs/references/honjo-2019-full.html` 視覚的強化
  - CSS追加（~300行）：theory-evolution, comparison-table, section-badge, side-note, highlight styles
  - 理論進化タイムライン（古典派 → ケインズ → 本荘）追加
  - 比較表を埋め込み（6次元比較）
  - セクションバッジ追加（全6節）
  - Section 5 完全復元（表-4言及を含む9段落）
  - Section 6 完全復元（量的・質的金融緩和政策評価の結論）
  - 統計表追加（表-4～7）：
    - 表-4: 生産年齢人口推移（1995-2017）※ PDF抽出品質の問題でデータ要確認
    - 表-5: 年間収入階級別割合（2017）※ 最後2行要確認
    - 表-6: プレースホルダー（詳細はPDF参照）
    - 表-7: 年代別平均（1970年代～2010年度以降）✅

### 2026-06-04 — 対話セッション ✅
- AI データセンターの隠れたコストについて議論
- コスト外部化の構造を深化

### 2026-05-05 — AI Context Standard v0.9.2 適用 ✅
- `copilot-instructions.md` の標準バージョンコメントを v0.8.8 → v0.9.2 に更新
- `PROJECT_STATUS.md` の Current Task をクリア・最新化
- 関連: ステータスバー表示機能（`ai-context-vscode` v0.3.2）の動作確認済み

### 2026-03-24 — AI Context Standard v0.7 適用 ✅
- `COPILOT-INIT.md` → `.github/copilot-instructions.md` に移行（auto-loaded）
- 旧 `COPILOT-INIT.md` を削除
- `PROJECT_STATUS.md` / `README.md` の参照先を更新
- Standard v0.5 → v0.7 にアップグレード

### 2026-03-05（昼） — 対話準備仕上げ・COPILOT_MEET_INIT.md 完成 ✅
- `docs/dialogs/20260305/COPILOT_MEET_INIT.md` を新規作成（AIの対話参加初期化ファイル）
  - イラン軍事衝突速報（The Guardian 2026-03-04）を組み込み
  - フクヤマ記事要約・TMS キーワード・通奏低音表を整備
  - 「sympathy がグローバル規模で機能しない構造的理由」の洞察を追記
- `.github/copilot-instructions.md` に3つのセクションを追加：
  - PDF 参照時の AI アシスタントルール
  - 最新時事情報へのアクセス方法（The Guardian ✅ / NHK ONE ❌）
  - "Copilot's Good Judgment" の定義（jichikai-2-priv 正典から転記）
- AI Context Standard v0.5 準拠チェック完了（README.md / COPILOT-INIT.md）
  - `README.md` に Why/Who/What's here を追加

### 2026-03-04（夕） — 2026-03-05 対話準備 ✅
- `docs/dialogs/20260305/index.html` 既存確認（別セッションで作成済み）
- 対話テーマ整理：フクヤマ記事、民主主義の危機、「政治と日常の切り離し」問題
- 関連メモを `jichikai-2-priv/docs/philosophy/` に整理（非公開管理）

### 2026-03-04（朝） — AI Context Standard 適用 ✅
- `COPILOT-INIT.md` を新規作成（STATIC: リポジトリ規約・構造）
- `PROJECT_STATUS.md` を新規作成（DYNAMIC: 現在の状態）
- `README.md` に初期化フレーズへの参照を追加

### 2026-02-05 — Dialog Session 準備中 🔬
- `docs/dialogs/20260205/index.html` を作成（プレースホルダー状態）
- トピック: 気候変動、日本の政治（内容は対話後に追記予定）

### 2026-01-09 — Dialog Session 完了 ✅
- `docs/dialogs/20260109/index.html` に対話内容を記録
- トピック: 気候変動、日本の政治、国際政治（One China Principle、台湾問題）、ウクライナ情勢、AI、Adam Smith

### 2025-12-04 — Dialog Session 完了 ✅
- `docs/dialogs/20251204/index.html` に対話内容を記録

### 2025-11-06 — Dialog Session 完了 ✅
- `docs/dialogs/20251106/index.html` に対話内容を記録

---

## ⏳ Next Steps

1. **2026-03-05 対話セッション（明日）**: 本荘さんとのオンライン対話を実施
2. **対話内容の記録**: 終了後に `docs/dialogs/20260305/index.html` へ追記
3. **dialog index 更新**: `docs/dialogs/index.html` に 20260305 のエントリを確認・公開
4. **2026-02-05 セッション内容の追記**: 対話後のメモを `docs/dialogs/20260205/index.html` に追記

---

## 📊 Status Summary

| Section | Status |
|---------|--------|
| Dialog sessions (〜2026-01-09) | ✅ 公開済み |
| Dialog session 2026-02-05 | 🔬 準備中 |
| Dialog session 2026-03-05 | � 本日実施予定（準備完了） |
| COPILOT_MEET_INIT.md パターン | ✅ 新規確立 |
| Adam Smith TMS project | 🔬 進行中 |
| Honjo 2019 paper reference | ✅ 公開済み |
| AI Context Standard 適用 | ✅ 完了（v0.5） |
