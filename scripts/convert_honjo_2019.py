"""
本荘2019論文のPDF抽出テキストをHTMLに変換するスクリプト
"""
from pathlib import Path
import re

def convert_to_html():
    # 抽出済みテキストを読み込み
    extracted = Path(r"c:\Users\takahashi\GitHub\humanomics\docs\references\honjo-2019-extracted.txt").read_text(encoding='utf-8')
    
    # テンプレート読み込み
    template = Path(r"c:\Users\takahashi\GitHub\humanomics\docs\references\honjo-2019-full.html").read_text(encoding='utf-8')
    
    # セクション境界を検出
    sections = {
        'sec1': extract_section(extracted, '1.はじめに', '2.『一般理論』における労働市場の分析'),
        'sec2': extract_section(extracted, '2.『一般理論』における労働市場の分析', '3.金融政策とトランスミッション・メカニズム'),
        'sec3': extract_section(extracted, '3.金融政策とトランスミッション・メカニズム', '4.『一般理論』における労働市場の分析とトランスミッション・メカニズム'),
        'sec4': extract_section(extracted, '4.『一般理論』における労働市場の分析とトランスミッション・メカニズム', '5.雇用形態の変化と総需要'),
        'sec5': extract_section(extracted, '5.雇用形態の変化と総需要', '6'),
        'sec6': extract_section(extracted, '6', None, is_last=True)
    }
    
    # HTMLに埋め込み
    for sec_id, content in sections.items():
        placeholder = f'<h2 id="{sec_id}">'
        if placeholder in template:
            # セクションタイトルの後の<p>タグを見つけて内容を挿入
            pattern = f'(<h2 id="{sec_id}">.*?</h2>\\s*)<p>\\s*（.*?）\\s*</p>'
            replacement = f'\\1\n{format_content(content)}\n'
            template = re.sub(pattern, replacement, template, flags=re.DOTALL)
    
    # 出力
    output_path = Path(r"c:\Users\takahashi\GitHub\humanomics\docs\references\honjo-2019-full.html")
    output_path.write_text(template, encoding='utf-8')
    print(f"HTML生成完了: {output_path}")

def extract_section(text, start_marker, end_marker=None, is_last=False):
    """セクションを抽出"""
    # start_markerの2回目の出現を探す（目次の後）
    first_pos = text.find(start_marker)
    if first_pos == -1:
        return ""
    second_pos = text.find(start_marker, first_pos + 1)
    if second_pos == -1:
        return ""
    
    if is_last:
        # 最後のセクション
        content = text[second_pos:]
        # 脚注や参考文献の前で切る
        for marker in ['参考文献', '注:', '(脚注)', '出所:']:
            if marker in content:
                # 最後の段落まで
                pass
        return content[len(start_marker):].strip()
    
    if end_marker:
        end_pos = text.find(end_marker, second_pos)
        if end_pos == -1:
            return text[second_pos + len(start_marker):].strip()
        return text[second_pos + len(start_marker):end_pos].strip()
    
    return ""

def format_content(content):
    """テキストをHTML段落に整形"""
    if not content:
        return "<p>（内容抽出中）</p>"
    
    # 段落分割（空行で分割）
    paragraphs = []
    current_para = []
    
    for line in content.split('\n'):
        line = line.strip()
        if not line:
            if current_para:
                paragraphs.append(' '.join(current_para))
                current_para = []
        else:
            current_para.append(line)
    
    if current_para:
        paragraphs.append(' '.join(current_para))
    
    # HTML化
    html_parts = []
    for para in paragraphs:
        # 表の検出（簡易）
        if '表-' in para and '出所:' in para:
            # 表は後で手動整形
            html_parts.append('<p><em>[表データ - 後で整形]</em></p>')
        else:
            # 段落
            # 数式の簡易検出とMathJax化
            para = re.sub(r'(?<![a-zA-Z])([A-Z])/([A-Z])(?![a-zA-Z])', r'$\1/\2$', para)  # W/P -> $W/P$
            html_parts.append(f'<p>{para}</p>')
    
    return '\n'.join(html_parts)

if __name__ == '__main__':
    convert_to_html()
