#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
本荘2019論文の表-1をHTMLテーブルに変換
"""

from pathlib import Path
import re

html_path = Path(__file__).parent.parent / "docs" / "references" / "honjo-2019-full.html"

with html_path.open("r", encoding="utf-8") as f:
    html = f.read()

# 表-1の開始位置を探す（既存の長いテキストブロック）
table_start = "表-1 わが国の主要経済指標の推移"
table_end_pattern = r'<a href="https://www\.stat\.go\.jp/data/cpi/" target="_blank" rel="noopener">総務省統計局（消費者物価指数）</a> \. 2'

# 表の範囲を抽出
start_idx = html.find(table_start)
if start_idx == -1:
    print("❌ 表-1が見つかりませんでした")
    exit(1)

# 表の終わりを見つける
match = re.search(table_end_pattern, html[start_idx:])
if not match:
    print("❌ 表の終わりが見つかりませんでした")
    exit(1)

end_idx = start_idx + match.end()

# 元のテキストを取得
old_table_text = html[start_idx:end_idx]

# HTMLテーブルを作成
new_table_html = """<div id="table-1" style="margin: 30px 0;">
<p style="text-align: center; font-weight: bold; margin-bottom: 10px;">表-1 わが国の主要経済指標の推移</p>
<p style="text-align: center; font-size: 0.9em; margin-bottom: 15px;">［GDP評価：平成23年基準。消費者物価指数（コアCPI）は2015年=100］</p>

<table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
<thead style="background-color: #f0f0f0;">
<tr>
  <th style="border: 1px solid #ccc; padding: 8px; text-align: center;">年度</th>
  <th colspan="2" style="border: 1px solid #ccc; padding: 8px; text-align: center;">名目GDP</th>
  <th colspan="2" style="border: 1px solid #ccc; padding: 8px; text-align: center;">実質GDP</th>
  <th style="border: 1px solid #ccc; padding: 8px; text-align: center;">完全失業率</th>
  <th style="border: 1px solid #ccc; padding: 8px; text-align: center;">消費者物価指数</th>
</tr>
<tr>
  <th style="border: 1px solid #ccc; padding: 8px; text-align: center;"></th>
  <th style="border: 1px solid #ccc; padding: 8px; text-align: center;">兆円</th>
  <th style="border: 1px solid #ccc; padding: 8px; text-align: center;">対前年度<br>増加率（%）</th>
  <th style="border: 1px solid #ccc; padding: 8px; text-align: center;">兆円</th>
  <th style="border: 1px solid #ccc; padding: 8px; text-align: center;">対前年度<br>増加率（%）</th>
  <th style="border: 1px solid #ccc; padding: 8px; text-align: center;">年度平均（%）</th>
  <th style="border: 1px solid #ccc; padding: 8px; text-align: center;">前年比（%）</th>
</tr>
</thead>
<tbody>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">1996</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">528.8</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">2.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">453.7</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">2.9</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">3.3</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.3</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">1997</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">533.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.9</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">453.8</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.0</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">3.5</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">2.1</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">1998</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">526.0</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-1.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">449.8</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-0.9</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">4.3</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-0.2</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">1999</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">521.9</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-0.8</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">452.9</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.7</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">4.7</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-0.1</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2000</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">528.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">1.2</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">464.2</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">2.5</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">4.7</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-0.4</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2001</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">519.2</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-1.8</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">461.7</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-0.5</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">5.2</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-0.8</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2002</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">514.9</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-0.8</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">465.8</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.9</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">5.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-0.8</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2003</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">517.7</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.6</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">474.9</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">2.0</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">5.1</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-0.2</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2004</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">521.3</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.7</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">483.0</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">1.7</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">4.6</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-0.2</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2005</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">525.7</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.8</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">492.5</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">2.0</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">4.3</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.1</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2006</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">529.0</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.6</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">499.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">1.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">4.1</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.1</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2007</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">530.9</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">505.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">1.2</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">3.8</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.3</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2008</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">509.5</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-4.0</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">488.1</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-3.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">4.1</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">1.2</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2009</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">492.0</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-3.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">477.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-2.2</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">5.2</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-1.6</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2010</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">499.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">1.5</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">493.0</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">3.3</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">4.9</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-0.8</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2011</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">494.0</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-1.1</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">495.3</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.5</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">4.5</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.0</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2012</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">494.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.1</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">499.3</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.8</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">4.3</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-0.2</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2013</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">507.3</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">2.6</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">512.5</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">2.6</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">3.9</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.8</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2014</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">518.2</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">2.2</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">510.7</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-0.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">3.5</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">2.8</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2015</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">533.0</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">2.8</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">517.4</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">1.3</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">3.3</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.0</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2016</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">536.8</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.7</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">522.0</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.9</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">3.0</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">-0.2</td></tr>
<tr><td style="border: 1px solid #ccc; padding: 6px; text-align: center;">2017</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">547.8</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">2.0</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">531.7</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">1.9</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">2.7</td><td style="border: 1px solid #ccc; padding: 6px; text-align: right;">0.7</td></tr>
</tbody>
</table>

<p style="font-size: 0.9em; margin-top: 10px;">
<strong>出所：</strong>GDPは<a href="https://www.esri.cao.go.jp/jp/sna/menu.html" target="_blank" rel="noopener">内閣府（国民経済計算）</a>。完全失業率：<a href="https://www.stat.go.jp/data/roudou/" target="_blank" rel="noopener">総務省統計局『労働力調査年報 平成29年』</a>（平成30年5月）。消費者物価指数は<a href="https://www.stat.go.jp/data/cpi/" target="_blank" rel="noopener">総務省統計局</a>。
</p>
</div>"""

# 置換実行
html = html[:start_idx] + new_table_html + html[end_idx:]

# [表データ - 後で整形] というプレースホルダーがあれば削除
html = html.replace('<p><em>[表データ - 後で整形]</em></p>', '')

# 保存
with html_path.open("w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ 表-1をHTMLテーブルに変換完了: {html_path}")
