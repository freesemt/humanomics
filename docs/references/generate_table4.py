"""表-4（生産年齢人口の推移）のHTML生成"""
import pathlib

# extracted.txt から表-4のデータを読み込む
extracted = pathlib.Path("honjo-2019-extracted.txt").read_text(encoding="utf-8")
lines = extracted.splitlines()

# 表-4は1331行目から（1-indexed → 0-indexed なので -1）
table_start = 1330  # 0-indexed
data_lines = []
for i in range(table_start, min(table_start + 100, len(lines))):
    line = lines[i].strip()
    if line.startswith("表-5"):
        break
    data_lines.append(line)

print(f"Extracted {len(data_lines)} lines from table-4")
print("First 10 lines:")
for line in data_lines[:10]:
    print(f"  {line}")

# データ構造を解析
# 表-4: 年のブロック → 人口のブロック → 年のブロック → 人口のブロック
all_lines = []
for line in data_lines[4:]:  # "表-4", "生産年齢人口...", "(万人)", "年" をスキップ
    if line and not line.startswith("表-") and not line.startswith("生産年齢") and not line.startswith("(万人") and line != "年":
        all_lines.append(line)

# ブロック分割: 年1, 人口1, 年2, 人口2
# 最初の"生産年齢人口"の出現でブロック分割
pop_index = -1
for i, line in enumerate(all_lines):
    if "生産年齢人口" in line:
        pop_index = i
        break

if pop_index == -1:
    # 別の方法: 数値パターンで判定
    years1 = []
    values1 = []
    years2 = []
    values2 = []
    
    # 年か人口かを判定（カンマがあるかで判定）
    block = 0  # 0=年1, 1=人口1, 2=年2, 3=人口2
    for line in all_lines:
        if "," in line or len(line) > 6:  # 人口データ（カンマ区切りまたは長い）
            if block == 0:
                block = 1
            if block == 1:
                values1.append(line.replace(",", ""))
            elif block == 3:
                values2.append(line.replace(",", ""))
        else:  # 年データ
            if block == 1 and len(values1) > 0:
                block = 2
            if block == 0:
                years1.append(line)
            elif block == 2:
                years2.append(line)
                if len(years2) == 1:  # 2番目の年ブロック開始
                    block = 3
                    
print(f"Parsed: years1={len(years1)}, values1={len(values1)}, years2={len(years2)}, values2={len(values2)}")

# HTML生成
html = '''<!-- 表-4: 生産年齢人口の推移（折りたたみ可能） -->
<details id="table-4" style="margin: 30px 0; border: 1px solid #444; border-radius: 8px; padding: 15px; background-color: #1a1a1a;">
<summary style="cursor: pointer; font-weight: bold; color: #e0e0e0; padding: 10px; user-select: none;">
📊 表-4：生産年齢人口の推移データを表示
</summary>

<div style="margin-top: 20px;">
<p style="text-align: center; font-weight: bold; margin-bottom: 10px; color: #e0e0e0;">表-4 生産年齢人口（15歳～64歳人口）の推移</p>
<p style="text-align: center; font-size: 0.9em; margin-bottom: 15px; color: #e0e0e0;">（万人）</p>

<table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
<thead style="background-color: #f0f0f0; color: #222;">
<tr>
  <th style="border: 1px solid #ccc; padding: 8px; text-align: center;">年</th>
  <th style="border: 1px solid #ccc; padding: 8px; text-align: center;">生産年齢人口</th>
  <th style="border: 1px solid #ccc; padding: 8px; text-align: center;">年</th>
  <th style="border: 1px solid #ccc; padding: 8px; text-align: center;">生産年齢人口</th>
</tr>
</thead>
<tbody>
'''

# データ行を追加
for i in range(max(len(years1), len(years2))):
    html += '<tr>'
    if i < len(years1):
        html += f'<td style="border: 1px solid #ccc; padding: 6px; text-align: center;">{years1[i]}</td>'
        html += f'<td style="border: 1px solid #ccc; padding: 6px; text-align: right;">{values1[i]}</td>'
    else:
        html += '<td style="border: 1px solid #ccc; padding: 6px;"></td><td style="border: 1px solid #ccc; padding: 6px;"></td>'
    
    if i < len(years2):
        html += f'<td style="border: 1px solid #ccc; padding: 6px; text-align: center;">{years2[i]}</td>'
        html += f'<td style="border: 1px solid #ccc; padding: 6px; text-align: right;">{values2[i]}</td>'
    else:
        html += '<td style="border: 1px solid #ccc; padding: 6px;"></td><td style="border: 1px solid #ccc; padding: 6px;"></td>'
    html += '</tr>\n'

html += '''</tbody>
</table>

<p style="font-size: 0.9em; margin-top: 10px; color: #aaa;">
<strong>出所：</strong><a href="https://www.stat.go.jp/data/jinsui/" target="_blank" rel="noopener" style="color: #bb86fc;">総務省統計局『人口推計』</a>
</p>
</div>
</details>
'''

# ファイルに保存
pathlib.Path("table4.html").write_text(html, encoding="utf-8")
print("表-4のHTMLを生成しました: table4.html")
print(f"年数: 1列目={len(years1)}, 2列目={len(years2)}")
