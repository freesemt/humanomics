# アダム・スミス『道徳感情論』PDF読み込み手順

## 概要
アダム・スミスの「道徳感情論」(The Theory of Moral Sentiments) のPDFをダウンロードして、Pythonで内容を抽出する手順です。

## 前提条件
- Python 3.x がインストールされていること
- `PyMuPDF` (fitz) パッケージがインストールされていること

## 手順

### 1. PyMuPDFのインストール
```powershell
pip install PyMuPDF
```

### 2. PDFのダウンロード
```powershell
# PowerShellの場合
Invoke-WebRequest -Uri "https://www.ibiblio.org/ml/libri/s/SmithA_MoralSentiments_p.pdf" -OutFile "SmithA_MoralSentiments.pdf"

# または curl (PowerShell 6+ / Linux / macOS)
curl -o SmithA_MoralSentiments.pdf "https://www.ibiblio.org/ml/libri/s/SmithA_MoralSentiments_p.pdf"
```

### 3. PDF抽出スクリプトの取得

スクリプトは本リポジトリの `docs/scripts/extract_moral_sentiments.py` にあります。

このスクリプトはコマンドライン引数でPDFパスを指定できます：

```python
import fitz  # PyMuPDF
import sys
import os
from pathlib import Path

# Set UTF-8 encoding for output
sys.stdout.reconfigure(encoding='utf-8')

# Get PDF path from command line argument or use default in current directory
if len(sys.argv) > 1:
    pdf_path = sys.argv[1]
else:
    pdf_path = "SmithA_MoralSentiments.pdf"

# Check if file exists
if not os.path.exists(pdf_path):
    print(f"Error: PDF file not found: {pdf_path}")
    print(f"\nUsage: python {Path(__file__).name} [pdf_path]")
    print(f"Example: python {Path(__file__).name} SmithA_MoralSentiments.pdf")
    sys.exit(1)

# Open PDF
doc = fitz.open(pdf_path)

print(f"Total pages: {len(doc)}\n")

# Extract text from first 10 pages to get an overview
print("=== First 10 pages overview ===\n")
for page_num in range(min(10, len(doc))):
    page = doc[page_num]
    text = page.get_text()
    print(f"\n--- Page {page_num + 1} ---\n{text}\n")

doc.close()
```

### 4. スクリプトの実行
```powershell
# PDFと同じディレクトリで実行する場合
python docs/scripts/extract_moral_sentiments.py SmithA_MoralSentiments.pdf

# またはカレントディレクトリにPDFがある場合
python docs/scripts/extract_moral_sentiments.py
```

## PDF情報
- **タイトル**: The Theory of Moral Sentiments
- **著者**: Adam Smith
- **版**: Sixth Edition (1790)
- **ページ数**: 322ページ
- **出典**: https://www.ibiblio.org/ml/libri/s/SmithA_MoralSentiments_p.pdf

## 書籍の構成

### Part I: 固有性（Propriety）について
- Section I: 共感の感覚について
- Section II: 様々な情念の程度について
- Section III: 繁栄と逆境が判断に及ぼす影響

### Part II: 功績と罪過（Merit and Demerit）
- Section I: 功績と罪過の感覚について
- Section II: 正義と善行について
- Section III: 運命の影響について

### Part III: 自己判断の基礎と義務の感覚
- 自己承認と自己非承認の原理
- 称賛への愛と、称賛に値することへの愛
- 良心の影響と権威

### Part IV: 効用（Utility）の影響
- 効用の外観が芸術作品に与える美しさ
- 効用が人間の性格と行動に与える美しさ

### Part V: 慣習と流行の影響
- 美と醜の概念への影響
- 道徳的感情への影響

### Part VI: 徳の性格について
- Section I: 個人の性格（慎慮 Prudence）
- Section II: 他者の幸福に影響する性格
- Section III: 自制心（Self-command）

### Part VII: 道徳哲学の諸体系
- Section I: 道徳感情の理論で検討すべき問題
- Section II: 徳の本質に関する様々な説明
- Section III: 承認の原理に関する様々な体系
- Section IV: 実践的道徳の規則の扱い方

## 応用例：全ページの抽出

全322ページを抽出してテキストファイルに保存する場合：

```python
import fitz
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Get PDF path from command line argument
if len(sys.argv) > 1:
    pdf_path = sys.argv[1]
else:
    pdf_path = "SmithA_MoralSentiments.pdf"

output_file = "moral_sentiments_full_text.txt"

if not os.path.exists(pdf_path):
    print(f"Error: PDF file not found: {pdf_path}")
    sys.exit(1)

doc = fitz.open(pdf_path)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(f"Total pages: {len(doc)}\n\n")
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        f.write(f"\n{'='*60}\n")
        f.write(f"Page {page_num + 1}\n")
        f.write(f"{'='*60}\n\n")
        f.write(text)
        f.write("\n")
        
        if (page_num + 1) % 10 == 0:
            print(f"Processed {page_num + 1} pages...")

doc.close()
print(f"\nExtraction complete! Output saved to: {output_file}")
```

## 重要な概念
- **Sympathy（共感）**: スミスの道徳理論の中心概念
- **Impartial Spectator（公平な観察者）**: 道徳的判断の基準
- **Propriety（固有性）**: 適切さ、ふさわしさ
- **Merit and Demerit（功績と罪過）**: 報酬と処罰の基礎

## トラブルシューティング

### PyMuPDFのインポートエラー
```powershell
pip install --upgrade PyMuPDF
```

### エンコーディングエラー（Windows）
スクリプトで `sys.stdout.reconfigure(encoding='utf-8')` を使用するか、
出力をファイルにリダイレクト：
```powershell
python extract_moral_sentiments.py > output.txt
```

### ダウンロードエラー
- プロキシ環境の場合、環境変数を設定
- ブラウザで手動ダウンロードも可能

## 参考資料
- [PyMuPDF Documentation](https://pymupdf.readthedocs.io/)
- [Original PDF Source](https://www.ibiblio.org/ml/libri/s/SmithA_MoralSentiments_p.pdf)
