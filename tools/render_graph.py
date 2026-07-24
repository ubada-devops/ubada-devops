# tools/render_graph.py
import json

LEVELS = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

def render_graph():
    with open("assets/contributions.json") as f:
        data = json.load(f)
        
    cols = 53
    rows = 7
    square_size = 10
    gap = 3
    
    width = cols * (square_size + gap) + 40
    height = rows * (square_size + gap) + 50
    
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <style>',
        '    .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1px; }',
        '    .title { font-family: monospace; font-size: 12px; fill: #8b949e; }',
        '  </style>',
        f'  <rect width="100%" height="100%" class="bg" rx="6" />',
        '  <text x="20" y="25" class="title">$ git log --contributions --animated</text>'
    ]
    
    for idx, day in enumerate(data):
        col = idx // rows
        row = idx % rows
        
        x = 20 + col * (square_size + gap)
        y = 40 + row * (square_size + gap)
        color = LEVELS[day["level"]]
        delay = col * 0.03
        
        svg.append(
            f'  <rect x="{x}" y="{y}" width="{square_size}" height="{square_size}" fill="{color}" rx="2">'
            f'    <animate attributeName="opacity" from="0" to="1" dur="0.2s" begin="{delay:.2f}s" fill="freeze" />'
            f'  </rect>'
        )
        
    svg.append('</svg>')
    
    with open("graph.svg", "w") as f:
        f.write("\n".join(svg))
    print("🎨 Generated graph.svg")

if __name__ == "__main__":
    render_graph()