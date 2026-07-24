# tools/render_portrait.py
import numpy as np
from PIL import Image

GLYPHS = " '.,:;~+*xXO#" 
ACCENT_COLOR = "#58a6ff" # Cyan/Blue accent
BG_COLOR = "#0d1117"     # Dark GitHub background

def render_ascii_svg(input_path, output_path, cols=60):
    img = Image.open(input_path).convert("L")
    w, h = img.size
    aspect_ratio = h / w
    rows = int(cols * aspect_ratio * 0.55)
    
    img = img.resize((cols, rows), Image.Resampling.LANCZOS)
    pixels = np.array(img)
    
    num_glyphs = len(GLYPHS)
    indices = (pixels / 255.0 * (num_glyphs - 1)).astype(int)
    
    ascii_rows = []
    for r in range(rows):
        row_str = "".join([GLYPHS[idx] for idx in indices[r]])
        row_str = row_str.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        ascii_rows.append(row_str)
        
    char_w, char_h = 7, 12
    svg_w = cols * char_w + 20
    svg_h = rows * char_h + 20
    
    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">',
        '  <style>',
        f'    .bg {{ fill: {BG_COLOR}; }}',
        f'    .ascii {{ font-family: monospace; font-size: 10px; fill: {ACCENT_COLOR}; white-space: pre; }}',
        '  </style>',
        f'  <rect width="100%" height="100%" class="bg" rx="6" />',
        '  <defs>'
    ]
    
    for i in range(rows):
        delay = i * 0.04
        svg_lines.append(f'    <clipPath id="clip-{i}">')
        svg_lines.append(f'      <rect x="0" y="{10 + i * char_h}" height="{char_h}" width="0">')
        svg_lines.append(f'        <animate attributeName="width" to="{svg_w}" dur="0.2s" begin="{delay:.2f}s" fill="freeze" />')
        svg_lines.append('      </rect>')
        svg_lines.append('    </clipPath>')
        
    svg_lines.append('  </defs>')
    
    for i, line in enumerate(ascii_rows):
        y_pos = 20 + i * char_h
        svg_lines.append(f'  <text x="10" y="{y_pos}" class="ascii" clip-path="url(#clip-{i})">{line}</text>')
        
    svg_lines.append('</svg>')
    
    with open(output_path, "w") as f:
        f.write("\n".join(svg_lines))
    print(f"✨ Generated portrait SVG: {output_path}")

if __name__ == "__main__":
    render_ascii_svg("assets/photo-ready.png", "portrait.svg")