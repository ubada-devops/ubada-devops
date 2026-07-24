import os

# Clean SVG badges with official brand paths
LOGOS = {
    "portfolio": {
        "bg": "#121013",
        "path": '<path fill="#FFFFFF" d="M12 1L24 22H0L12 1Z"/>',
        "url": "https://syed-Ubada.vercel.app"
    },
    "linkedin": {
        "bg": "#0A66C2",
        "path": '<path fill="#FFFFFF" d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/>',
        "url": "https://linkedin.com/in/ubada-devops"
    },
    "x_twitter": {
        "bg": "#000000",
        "path": '<path fill="#FFFFFF" d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>',
        "url": "https://x.com/Ubada_DevOps"
    },
    "email": {
        "bg": "#EA4335",
        "path": '<path fill="#FFFFFF" d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>',
        "url": "mailto:ubada.devops@gmail.com"
    }
}

def generate_badges():
    for name, data in LOGOS.items():
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <rect width="48" height="48" rx="10" fill="{data['bg']}"/>
  <g transform="translate(12, 12) scale(1)">
    {data['path']}
  </g>
</svg>'''
        with open(f"{name}.svg", "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"?? Generated clean OG logo badge: {name}.svg")

if __name__ == "__main__":
    generate_badges()
