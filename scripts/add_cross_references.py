#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
本荘2019論文のHTML版に相互参照リンクとデータソースURLを追加
"""

import re
from pathlib import Path

html_path = Path(__file__).parent.parent / "docs" / "references" / "honjo-2019-full.html"

with html_path.open("r", encoding="utf-8") as f:
    html = f.read()

# 1. 節への参照をリンク化
html = re.sub(r'第([1-6])節(?=で)', r'<a href="#sec\1">第\1節</a>', html)

# 2. 表への参照をリンク化
html = re.sub(r'表-([123])(?=に示されているように)', r'<a href="#table-\1">表-\1</a>', html)

# 3. 図への参照をリンク化
html = re.sub(r'図-([12])(?=に示されて|の |と )', r'<a href="#fig-\1">図-\1</a>', html)

# 4. 表のキャプションにid属性を追加
html = html.replace(
    '<p>表-1\nわが国の主要経済指標の推移',
    '<div id="table-1" style="margin: 30px 0;">\n<p style="text-align: center; font-weight: bold; margin-bottom: 10px;">表-1 わが国の主要経済指標の推移'
)

# 5. データソースをURL化
html = html.replace(
    '内鷲府ホームヘ‐―シ゛',
    '<a href="https://www.esri.cao.go.jp/jp/sna/menu.html" target="_blank" rel="noopener">内閣府（国民経済計算）</a>'
)
html = html.replace(
    '総務省続計局『労働力調査年報 平成29生』',
    '<a href="https://www.stat.go.jp/data/roudou/" target="_blank" rel="noopener">総務省統計局『労働力調査年報 平成29年』</a>'
)
html = html.replace(
    '総務省疑計局ホームヘ |―シ°',
    '<a href="https://www.stat.go.jp/data/cpi/" target="_blank" rel="noopener">総務省統計局（消費者物価指数）</a>'
)

# 6. 図のキャプションを<div>でラップしてid追加
html = html.replace(
    '図-1\n〃/′\n古典派の労働需要曲線と労働供給曲線',
    '<div id="fig-1" style="margin: 20px 0; padding: 10px; border: 1px solid #ddd; background: #fafafa;">\n<strong>図-1</strong> 古典派の労働需要曲線と労働供給曲線\n<pre style="margin: 10px 0;">\n〃/′'
)
html = html.replace(
    '0\nゴV 、 プV',
    '0\nゴV 、 プV\n</pre>\n</div>'
)

html = html.replace(
    '図-2\nケインズの労働需要曲線と労働供給曲線',
    '<div id="fig-2" style="margin: 20px 0; padding: 10px; border: 1px solid #ddd; background: #fafafa;">\n<strong>図-2</strong> ケインズの労働需要曲線と労働供給曲線\n<pre style="margin: 10px 0;">'
)
html = html.replace(
    '0\nAr: Ar* ⅣクNS',
    '0\nAr: Ar* ⅣクNS\n</pre>\n</div>'
)

# 保存
with html_path.open("w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ 相互参照リンクとデータソースURL追加完了: {html_path}")
