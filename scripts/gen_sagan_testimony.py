"""
Carl Sagan 1985 Congressional Testimony
YouTube transcript -> HTML page generator
"""
import re
from youtube_transcript_api import YouTubeTranscriptApi

VIDEO_ID = "Wp-WiNXH6hI"
OUTPUT_PATH = r"C:\Users\takahashi\GitHub\humanomics\docs\climate-change\sagan-1985-testimony.html"

# -------- 1. Fetch transcript --------
api = YouTubeTranscriptApi()
result = api.fetch(VIDEO_ID)
snippets = list(result)

# -------- 2. Combine into full text --------
full_text = " ".join(s.text for s in snippets)

# -------- 3. Light cleanup --------
# Remove newline chars within entries
full_text = full_text.replace("\n", " ")
# Collapse multiple spaces
full_text = re.sub(r" {2,}", " ", full_text)

# -------- 4. Split into paragraphs --------
# Strategy: break at sentence-ending punctuation followed by space + lowercase
# (YouTube auto-captions rarely use caps after sentences, so we split on "." or "?" near natural breaks)
# We'll use a fixed-length chunking as fallback: ~400 chars per paragraph.

def split_paragraphs(text, target_len=400):
    """Split text into paragraphs at sentence boundaries near target_len."""
    paragraphs = []
    start = 0
    while start < len(text):
        end = start + target_len
        if end >= len(text):
            paragraphs.append(text[start:].strip())
            break
        # Look for a period/question mark near the target length
        search_window = text[start:start + target_len + 100]
        # Find last sentence boundary in the window
        best = -1
        for m in re.finditer(r'[.?!] ', search_window):
            if m.start() <= target_len + 50:
                best = m.end()
        if best > 0:
            paragraphs.append(text[start:start + best].strip())
            start += best
        else:
            # No sentence boundary found, break at space
            space = text.rfind(" ", start, start + target_len + 50)
            if space > start:
                paragraphs.append(text[start:space].strip())
                start = space + 1
            else:
                paragraphs.append(text[start:start + target_len].strip())
                start += target_len
    return paragraphs

paragraphs = split_paragraphs(full_text, target_len=450)
print(f"Generated {len(paragraphs)} paragraphs")

# -------- 5. Capitalize and lightly fix text --------
PROPER_NOUNS = {
    r'\bcarl sagan\b': 'Carl Sagan',
    r'\bdr carl sagan\b': 'Dr. Carl Sagan',
    r'\bsagan\b': 'Sagan',
    r'\bsenator gore\b': 'Senator Gore',
    r'\bsenator dernberger\b': 'Senator Dernberger',
    r'\bsenator burdick\b': 'Senator Burdick',
    r'\bcornell university\b': 'Cornell University',
    r'\bnasa\b': 'NASA',
    r'\bunited states\b': 'United States',
    r'\bsoviet union\b': 'Soviet Union',
    r'\bsoviet\b': 'Soviet',
    r'\bchinese\b': 'Chinese',
    r'\bchina\b': 'China',
    r'\bvenus\b': 'Venus',
    r'\bmars\b': 'Mars',
    r'\bjupiter\b': 'Jupiter',
    r'\btitan\b': 'Titan',
    r'\bsaturn\b': 'Saturn',
    r'\bearth\b': 'Earth',
    r'\blos angeles\b': 'Los Angeles',
    r'\bwest antarctic\b': 'West Antarctic',
    r'\broman empire\b': 'Roman Empire',
    r'\begypt\b': 'Egypt',
    r'\bcalifornia\b': 'California',
    r'\bco2\b': 'CO₂',
}

def fix_paragraph(p):
    # Capitalize first letter
    p = p[0].upper() + p[1:] if p else p
    # Ensure ends with punctuation
    if p and p[-1] not in ".?!,":
        p += "."
    # Remove filler words
    p = re.sub(r"\buh\b", "", p)
    p = re.sub(r"\bum\b", "", p)
    p = re.sub(r" {2,}", " ", p)
    # Capitalize after period/question mark
    p = re.sub(r'([.?!]) ([a-z])', lambda m: m.group(1) + ' ' + m.group(2).upper(), p)
    # Apply proper noun capitalization
    for pattern, replacement in PROPER_NOUNS.items():
        p = re.sub(pattern, replacement, p, flags=re.IGNORECASE)
    # Fix standalone pronoun "i" -> "I"
    p = re.sub(r'(?<= )i(?= )', 'I', p)
    p = re.sub(r"(?<= )i(?=')", 'I', p)   # i'm, i've, i'd etc.
    return p.strip()

paragraphs = [fix_paragraph(p) for p in paragraphs if p.strip()]
# Remove trailing fragments (very short last paragraph)
if paragraphs and len(paragraphs[-1]) < 30:
    paragraphs.pop()

# -------- 6. Build YouTube timestamp links --------
# Create a list of major time anchors for navigation
def fmt_time(secs):
    m = int(secs) // 60
    s = int(secs) % 60
    return f"{m}:{s:02d}"

# -------- 7. Generate HTML --------
yt_url = f"https://www.youtube.com/watch?v={VIDEO_ID}"

para_html = "\n".join(f"    <p>{p}</p>" for p in paragraphs)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Carl Sagan: Senate Testimony on Climate Change (1985)</title>
<style>
  body {{
    font-family: Georgia, 'Times New Roman', serif;
    max-width: 800px;
    margin: 2em auto;
    padding: 0 1.5em;
    line-height: 1.8;
    color: #222;
    background: #fafaf8;
  }}
  h1 {{ font-size: 1.5em; margin-bottom: 0.3em; }}
  .meta {{ color: #666; font-size: 0.9em; margin-bottom: 2em; border-bottom: 1px solid #ccc; padding-bottom: 1em; }}
  .meta a {{ color: #444; }}
  p {{ margin: 1em 0; text-align: justify; }}
  blockquote {{
    border-left: 4px solid #888;
    margin: 1.5em 0;
    padding: 0.5em 1em;
    background: #f0ede8;
    font-style: italic;
  }}
  .note {{
    background: #e8f0e8;
    border: 1px solid #aac;
    padding: 0.8em 1em;
    font-size: 0.88em;
    margin-bottom: 2em;
  }}
  .back {{ margin-top: 3em; font-size: 0.9em; }}
</style>
</head>
<body>

<h1>Carl Sagan: Senate Testimony on Climate Change (1985)</h1>
<div class="meta">
  Senate Subcommittee on Science, Technology and Space (Commerce Committee)<br>
  December 10, 1985 &nbsp;|&nbsp;
  <a href="{yt_url}" target="_blank">Watch on YouTube &#x25B6;</a>
</div>

<div class="note">
  <strong>Note:</strong> This text is derived from the auto-generated YouTube captions of the
  <a href="{yt_url}" target="_blank">official recording</a> (channel: carlsagandotcom).
  Filler words have been lightly removed; punctuation and capitalization have been
  auto-corrected. For the authoritative record, refer to the original video or the
  Senate hearing record (99th Congress).
</div>

<blockquote>
  "We are all in this greenhouse together."<br>
  — Carl Sagan, closing the testimony
</blockquote>

{para_html}

<div class="back">
  <a href="index.html">&#x2190; Back to Climate Change</a>
</div>

</body>
</html>
"""

import pathlib
out = pathlib.Path(OUTPUT_PATH)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(html, encoding="utf-8")
print(f"Written: {out.resolve()}")
