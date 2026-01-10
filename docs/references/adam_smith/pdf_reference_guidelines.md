# Adam Smith『道徳感情論』PDF参照のガイドライン

## PDFの基本情報

- **PDF URL**: https://www.ibiblio.org/ml/libri/s/SmithA_MoralSentiments_p.pdf
- **総ページ数**: 322ページ
- **目次の位置**: PDF p.3-7
- **本文の開始**: PDF p.11（Part I, Section I）

## ページ番号の対応関係

### 基本的な考え方
- 原典目次に記載されているページ番号は、実際のPDF内の位置とは異なる
- 目次部分（PDF p.3-7）を確認して、正確なページ番号を特定する必要がある

### 判明している対応関係

| 原典ページ | PDFページ | 内容 |
|-----------|----------|------|
| - | p.11 | Part I, Section I「Of the Sense of Propriety」開始 |
| - | p.11 | Part I, Section I, Chapter 1「Of Sympathy」開始 |
| p.70 | p.77 | Part II, Section II「Of Justice and Beneficence」 |
| p.70 | p.77 | Part II, Section II, Chapter 1 |
| p.72 | p.79 | Part II, Section I冒頭（Resentment関連） |
| p.74 | p.81 | Part II, Section II, Chapter 2 |
| p.118 | p.125 | Part III, Chapter 3「Of the Influence and Authority of Conscience」|
| p.215 | p.222 | Part VI, Section III「Of Self-command」|

**注意**: 計算式（原典+7=PDF）は一般的な目安だが、目次部分（PDF p.3-7）は例外。必ず原典目次で確認すること。

## HTMLでのリンク表記ルール

### 1. 具体的なChapterへの参照
特定のChapterで論じられている概念の場合：

```html
<strong>［原典参照］</strong>
・ Impartial Spectator（公平な観察者）: Part III, Chapter 3
  「Of the Influence and Authority of Conscience」
  → <a href="https://www.ibiblio.org/ml/libri/s/SmithA_MoralSentiments_p.pdf#page=125">PDF (原典p.118, PDFp.125)</a>
```

### 2. Part/Section全体の概念への参照
Part全体またはSection全体で論じられている概念の場合：

```html
<strong>［原典参照］</strong>
・ Propriety（適切さ・固有性）: Part I全体の概念
  Part I, Section I「Of the Sense of Propriety」
  → <a href="https://www.ibiblio.org/ml/libri/s/SmithA_MoralSentiments_p.pdf#page=11">PDF (PDFp.11)</a>
```

**ポイント**: 
- 「全体の概念」と明記する
- 原典ページ番号は記載しない（Section/Part全体のため特定のページがない）
- PDFページのみを記載

### 3. 複数項目のリスト形式
Chapterの詳細を列挙する場合、各項目に必ずリンクを付ける：

```html
<strong>［原典参照］</strong>
・ Justice and Beneficence（正義と善行）: Part II, Section II全体の概念
  Section II「Of Justice and Beneficence」
  → <a href="https://www.ibiblio.org/ml/libri/s/SmithA_MoralSentiments_p.pdf#page=77">PDF (原典p.70, PDFp.77)</a>
・ Part II, Section II, Chapter 1: 「Comparison of those two virtues」
  → <a href="https://www.ibiblio.org/ml/libri/s/SmithA_MoralSentiments_p.pdf#page=77">PDF (原典p.70, PDFp.77)</a>
・ Part II, Section II, Chapter 2: 「Of the sense of Justice, of Remorse, and of the consciousness of Merit」
  → <a href="https://www.ibiblio.org/ml/libri/s/SmithA_MoralSentiments_p.pdf#page=81">PDF (原典p.74, PDFp.81)</a>
```

**ポイント**:
- 「・」で始まる各項目ごとに必ずリンクを付ける
- 形式を統一することで視認性と利便性を向上

## 作業手順

### 新しい概念への参照を追加する場合

1. **原典目次を確認**（PDF p.3-7）
   - 該当する概念がどのPart/Section/Chapterで論じられているか確認
   - 原典目次に記載されているページ番号を確認
   - **重要**: 推測せず、必ず原典目次で確認すること

2. **PDFページ番号を計算**
   - 原典目次の情報から実際のPDFページ番号を特定
   - 既知の対応関係を参照して推定
   - **計算式**: 原典ページ + 7 = PDFページ（目次部分を除く）

3. **概念の性質を判断**
   - 特定のChapterで論じられる → 具体的なChapter参照形式
   - Part/Section全体の概念 → 全体概念参照形式（「〇〇全体の概念」と明記）

4. **HTMLを記述**
   - 上記のルールに従って記述
   - 複数項目の場合は各項目にリンクを付ける

5. **moral_sentiments_toc.jsonを更新**
   - 新しく判明したページ情報を追加
   - noteフィールドに概念の性質を記録
   - **重要**: HTMLと同時に更新すること

## 重要な注意事項

### 1. 原典目次の必須確認
- **絶対に推測に頼らない**: 似たようなタイトルや章構成から推測すると誤る
- 原典目次（PDF p.3-7）を開いて、直接確認する
- ページ番号が記載されていない場合（Section全体など）は、その旨を明記

### 2. 混乱しやすいポイント

#### 類似タイトルの存在
- 異なるPart/Sectionに似たタイトルが出現する可能性がある
- 例: 「Of the corruption of moral sentiments」のような表現が複数箇所に存在
- 必ず正確なPart/Section/Chapter番号とともに確認

#### Section全体とChapterの区別
- Section IのタイトルページとChapter 1の開始が同じページの場合がある
- 例: Part I, Section IとChapter 1が両方ともPDF p.11から開始

#### 無関係な項目の混入に注意
- 元の文書に誤った参照があった場合、それを引き継がないこと
- 各参照項目の内容が、対応する概念と実際に関連しているか確認

### 3. 同時更新の重要性

以下を必ず同時に更新すること：
1. HTMLファイル（garbage-collection.htmlなど）
2. moral_sentiments_toc.json
3. 対応表（このガイドライン内）

片方だけを更新すると、整合性が失われる。

### 4. 検証の方法

追加・修正後は必ず以下を確認：
1. リンクが正しいPDFページを指しているか（実際にクリックして確認）
2. 原典ページとPDFページの対応が正しいか
3. 各項目の内容が対応する概念と整合しているか
4. HTMLとJSONの情報が一致しているか

## 注意事項

- 原典ページ番号が目次に記載されていない場合（Section全体など）は、PDFページのみを記載
- 「全体の概念」であることが重要な情報の場合は、必ず明記する
- リンクのpage番号は実際のPDFページ番号を使用（#page=77など）
- 原典ページとPDFページの両方を表記する場合: `(原典p.70, PDFp.77)`
- PDFページのみの場合: `(PDFp.11)`

## よくある誤りと対処法

### 誤り1: ページ番号の推測

**問題**: 原典目次を確認せず、計算式だけでページ番号を推測
- 例: Self-commandを原典p.255（PDF p.262）としていたが、実際は原典p.215（PDF p.222）

**対処法**: 
- 必ず原典目次（PDF p.3-7）を直接確認
- 計算式（原典+7=PDF）は目安であり、目次部分など例外がある

### 誤り2: 無関係な項目の混入

**問題**: 元の文書に含まれていた誤った参照を引き継いでしまう
- 例: Self-commandの参照に「Of the corruption of our moral sentiments...」（Part Iの内容）を含めていた

**対処法**:
- 各参照項目の内容が、対応する概念と実際に関連しているか確認
- 疑わしい場合は、PDFで該当ページを開いて内容を確認

### 誤り3: HTMLとJSONの不整合

**問題**: HTMLを更新したがJSONを更新し忘れる、またはその逆

**対処法**:
- 必ず両方を同時に更新
- 更新後、両者の情報が一致しているか確認

### 誤り4: リンク形式の不統一

**問題**: 複数項目があるのに、一部の項目だけリンクがない

**対処法**:
- 「・」で始まる項目は必ず全てにリンクを付ける
- 形式を統一することを優先

### 誤り5: Section全体とChapterの混同

**問題**: Section Iのタイトルページと、その中のChapter 1を区別せずに参照

**対処法**:
- Section全体の概念として参照する場合は、「Section全体の概念」と明記
- 特定のChapterの内容として参照する場合は、Chapter番号を明記

## トラブルシューティング

### PDFページ番号が合わない場合
1. 原典目次（PDF p.3-7）を再確認
2. 既知の対応関係と比較
3. 実際にPDFでそのページを開いて内容を確認
4. 計算式（原典+7=PDF）に頼らない

### 概念が複数箇所で論じられている場合
1. 最も中心的に論じられている箇所を特定
2. 「全体の概念」なのか「特定のChapter」なのかを判断
3. 必要に応じて複数の参照を記載（主要箇所を最初に）

### 原典目次に記載がない場合
1. PDFを直接確認して該当箇所を探す
2. 前後のChapter/Sectionから推測
3. noteフィールドに「原典目次に記載なし」と明記

## 更新履歴

- 2026-01-10: 初版作成
  - Part I, Sectio
- 2026-01-10: 第2版
  - Self-commandの正しいページ番号を訂正（原典p.255→p.215）
  - 無関係な項目の削除（「Of the corruption...」の誤記載）
  - 「重要な注意事項」セクションを追加
  - 「よくある誤りと対処法」セクションを追加
  - 「トラブルシューティング」セクションを追加n IがPDF p.11から開始することを確認
  - Part II, Section IIの詳細なページ情報を追加（原典p.70, 74）
  - 「全体の概念」参照形式を確立
