import os
import base64

def generate_card(title, tagline, tech_stack, color_start, color_end, filename, secret=None):
    # Split tagline manually for pure SVG wrapping (approx 50 chars per line)
    words = tagline.split()
    line1 = " ".join(words[:6])
    line2 = " ".join(words[6:])
    
    secret_element = ""
    if secret:
        # Hide the secret in a desc tag (standard metadata, invisible rendered)
        encoded = base64.b64encode(secret.encode()).decode()
        secret_element = f'<desc>SECRET_KEY: {encoded}</desc>'

    svg_content = f"""<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad_{filename}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{color_start};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{color_end};stop-opacity:1" />
    </linearGradient>
    <style>
      @keyframes move_{filename} {{
        0% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(20px, -20px); }}
        100% {{ transform: translate(0, 0); }}
      }}
      .blob {{ animation: move_{filename} 8s infinite ease-in-out; }}
      .card-body {{ transition: all 0.3s ease; }}
      .card-body:hover {{ stroke: {color_end}; stroke-width: 2px; filter: drop-shadow(0 0 10px {color_start}40); }}
      .title {{ font-family: 'Segoe UI', sans-serif; font-size: 24px; font-weight: bold; fill: white; }}
      .tagline {{ font-family: 'Segoe UI', sans-serif; font-size: 14px; fill: rgba(255,255,255,0.9); }}
      .tech {{ font-family: 'Consolas', monospace; font-size: 11px; fill: {color_end}; }}
    </style>
  </defs>
  {secret_element}

  <!-- Background -->
  <rect width="100%" height="100%" fill="#0d1117" rx="10" />

  <!-- Animated Blob -->
  <circle cx="350" cy="150" r="80" fill="url(#grad_{filename})" opacity="0.4" class="blob" />
  <circle cx="50" cy="50" r="60" fill="url(#grad_{filename})" opacity="0.2" />

  <!-- Glass Card -->
  <g class="card-body">
    <rect x="10" y="10" width="380" height="180" rx="10" 
          fill="rgba(255, 255, 255, 0.05)" 
          stroke="rgba(255, 255, 255, 0.1)" 
          stroke-width="1" />
    
    <text x="30" y="50" class="title">{title}</text>
    
    <text x="30" y="80" class="tagline">{line1}</text>
    <text x="30" y="100" class="tagline">{line2}</text>

    <text x="30" y="170" class="tech">{tech_stack}</text>
  </g>
</svg>"""
    
    with open(f"assets/{filename}.svg", "w") as f:
        f.write(svg_content)
    print(f"Generated assets/{filename}.svg")

# Data for Cards
cards = [
    ("PLTM", "O(N log N) Memory Kernel with Power-Law Decay.", "Python • C • CUDA", "#FF3366", "#FFCC33", "card_pltm", None),
    ("SecuriQR", "Dual-Layer Auth: AES-256 + Visual PUF Signatures.", "OpenCV • Crypto • Python", "#33CCFF", "#3366FF", "card_securiqr", "https://github.com/Adi-Baba/Adi-Baba/blob/main/SECRET_MESSAGE.md"),
    ("FluxZero", "Thermodynamic Game AI using Fluid Tree Search.", "Physics-ML • RL", "#33CC66", "#00FF99", "card_fluxzero", None),
    ("Bhojya", "Native Hindi Systems Programming Language compiled to EXE.", "C++ • Assembly • Compiler", "#FFCC33", "#FF6600", "card_bhojya", None)
]

if __name__ == "__main__":
    if not os.path.exists("assets"):
        os.makedirs("assets")
    for c in cards:
        generate_card(*c)
