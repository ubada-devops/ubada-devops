# tools/render_panel.py
import os

ROWS = [
    ("user", "ubada-devops"),
    ("role", "DevOps Engineer"),
    ("focus", "CI/CD Pipelines & Cloud Automation"),
    ("stack", "Python · Docker · Kubernetes · Linux · Git"),
    ("now", "Solving DSA Blind 75 & automation workflows"),
]

BG_COLOR = "#0d1117"
BORDER_COLOR = "#30363d"
KEY_COLOR = "#79c0ff"
VALUE_COLOR = "#a5d6ff"
PING_COLOR = "#23d160"

def render_panel():
    is_preview = os.getenv("PREVIEW") == "1"
    width = 460
    height = len(ROWS) * 35 + 75
    
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <style>',
        f'    .bg {{ fill: {BG_COLOR}; stroke: {BORDER_COLOR}; stroke-width: 1px; }}',
        '    .header { font-family: monospace; font-size: 12px; fill: #8b949e; }',
        '    .status-text { font-family: monospace; font-size: 11px; font-weight: bold; fill: #23d160; }',
        '    .key { font-family: monospace; font-size: 13px; font-weight: bold; }',
        '    .val { font-family: monospace; font-size: 13px; }',
        '  </style>',
        f'  <rect width="100%" height="100%" class="bg" rx="6" />',
        
        '  <!-- Controls -->',
        '  <circle cx="20" cy="20" r="5" fill="#ff5f56" />',
        '  <circle cx="35" cy="20" r="5" fill="#ffbd2e" />',
        '  <circle cx="50" cy="20" r="5" fill="#27c93f" />',
        '  <text x="70" y="24" class="header">ubada-devops@terminal ~ sysinfo</text>',
        
        '  <!-- Live Status Ping (SMIL Animation) -->',
        f'  <circle cx="{width - 85}" cy="20" r="4" fill="{PING_COLOR}" />',
        f'  <circle cx="{width - 85}" cy="20" r="4" fill="none" stroke="{PING_COLOR}" stroke-width="1.5">',
        '    <animate attributeName="r" values="4;10;4" dur="2s" repeatCount="indefinite" />',
        '    <animate attributeName="opacity" values="1;0;1" dur="2s" repeatCount="indefinite" />',
        '  </circle>',
        f'  <text x="{width - 73}" y="24" class="status-text">ONLINE</text>',
        
        '  <line x1="0" y1="38" x2="100%" y2="38" stroke="#30363d" stroke-width="1" />'
    ]
    
    for idx, (k, v) in enumerate(ROWS):
        y = 70 + idx * 30
        delay = 0.2 + idx * 0.3 if not is_preview else 0
        
        svg.append(f'  <g class="row">')
        if not is_preview:
            svg.append(f'    <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="{delay:.1f}s" fill="freeze" />')
        svg.append(f'    <text x="20" y="{y}" class="key" fill="{KEY_COLOR}">{k.ljust(8)}:</text>')
        svg.append(f'    <text x="100" y="{y}" class="val" fill="{VALUE_COLOR}">{v}</text>')
        svg.append(f'  </g>')
        
    svg.append('</svg>')
    
    with open("sysinfo.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print("🟢 Generated valid SMIL-animated sysinfo.svg!")

if __name__ == "__main__":
    render_panel()