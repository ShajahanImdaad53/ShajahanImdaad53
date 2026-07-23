import os

def create_button(filename, text, color1, color2, delay="0s"):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="220" height="60">
  <style>
    .btn {{
      fill: url(#grad);
      rx: 8px;
      transform-origin: center;
      animation: pulse 2s infinite {delay};
    }}
    .text {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      font-size: 16px;
      font-weight: 800;
      fill: white;
      text-anchor: middle;
      dominant-baseline: middle;
      pointer-events: none;
      transform-origin: center;
      animation: pulse-text 2s infinite {delay};
      letter-spacing: 1px;
    }}
    @keyframes pulse {{
      0% {{ filter: drop-shadow(0 0 5px {color1}); transform: scale(1); }}
      50% {{ filter: drop-shadow(0 0 15px {color1}); transform: scale(1.03); }}
      100% {{ filter: drop-shadow(0 0 5px {color1}); transform: scale(1); }}
    }}
    @keyframes pulse-text {{
      0% {{ transform: scale(1); }}
      50% {{ transform: scale(1.03); }}
      100% {{ transform: scale(1); }}
    }}
  </style>
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{color1};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{color2};stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect class="btn" x="10" y="10" width="200" height="40" />
  <text class="text" x="110" y="32">{text}</text>
</svg>"""
    with open(f"assets/{filename}", "w", encoding="utf-8") as f:
        f.write(svg)

# Create Buttons
create_button("portfolio.svg", "🚀 PORTFOLIO", "#FF007A", "#7928CA", "0s")
create_button("github.svg", "🐙 GITHUB", "#24292e", "#000000", "0.2s")
create_button("linkedin.svg", "💼 LINKEDIN", "#0077b5", "#005582", "0.4s")
create_button("email.svg", "📧 EMAIL ME", "#EA4335", "#B31412", "0.6s")

# For the Tech Stack, we can't easily animate external images in SVG on github due to CSP.
# But we can use an animated glowing container for the tech stack text!
print("Generated SVGs successfully.")
