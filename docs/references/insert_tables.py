"""honjo-2019-full.htmlに4つの表を挿入"""
import pathlib

# ファイル読み込み
html_lines = pathlib.Path("honjo-2019-full.html").read_text(encoding="utf-8").splitlines(keepends=True)
table4 = pathlib.Path("table4.html").read_text(encoding="utf-8")
table5 = pathlib.Path("table5.html").read_text(encoding="utf-8")
table6 = pathlib.Path("table6.html").read_text(encoding="utf-8")
table7 = pathlib.Path("table7.html").read_text(encoding="utf-8")

# 挿入位置を特定（0-indexed）
# line 668の後（表-4の言及の後）= index 668
# line 672の後（表-5の言及の後）= index 672
# line 674の後（表-6/7の言及の後）= index 674

# 逆順で挿入（行番号がずれないように）
# 1. line 674の後に table6 + table7
# 2. line 672の後に table5
# 3. line 668の後に table4

# まず line 674 の後に table6 + table7 を挿入
insert_pos_6_7 = 674
html_lines.insert(insert_pos_6_7, "\n" + table6 + "\n" + table7 + "\n")

# 次に line 672 の後に table5 を挿入
insert_pos_5 = 672
html_lines.insert(insert_pos_5, "\n" + table5 + "\n")

# 最後に line 668 の後に table4 を挿入
insert_pos_4 = 668
html_lines.insert(insert_pos_4, "\n" + table4 + "\n")

# ファイル書き込み
output = "".join(html_lines)
pathlib.Path("honjo-2019-full.html").write_text(output, encoding="utf-8")

print(f"✓ 4つの表を挿入しました")
print(f"  - 表-4: line {insert_pos_4 + 1}付近")
print(f"  - 表-5: line {insert_pos_5 + 1}付近")
print(f"  - 表-6/7: line {insert_pos_6_7 + 1}付近")
print(f"  - 新しい行数: {len(html_lines)}")
