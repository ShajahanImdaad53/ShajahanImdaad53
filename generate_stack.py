import random

svg_header = '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="320">
  <style>
    .bubble-container {
      animation: float 4s ease-in-out infinite;
    }
    .box {
      fill: #161b22;
      stroke: #30363d;
      stroke-width: 2px;
      rx: 12px;
      transition: all 0.3s ease;
    }
    .text {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      font-weight: 700;
      fill: #c9d1d9;
      font-size: 14px;
      text-anchor: middle;
    }
    @keyframes float {
      0% { transform: translateY(0px); filter: drop-shadow(0px 0px 0px rgba(0, 255, 163, 0)); }
      50% { transform: translateY(-10px); filter: drop-shadow(0px 8px 12px rgba(0, 255, 163, 0.3)); stroke: #00ffa3; }
      100% { transform: translateY(0px); filter: drop-shadow(0px 0px 0px rgba(0, 255, 163, 0)); }
    }
  </style>
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117"/>
      <stop offset="100%" stop-color="#0d1117"/>
    </linearGradient>
  </defs>
  <rect width="800" height="320" fill="url(#bg)" rx="15" stroke="#30363d" stroke-width="2"/>
'''

tools = [
    "🐍 Python", "🔥 PyTorch", "🧠 TensorFlow", "📊 Scikit-learn", 
    "🔢 NumPy", "🐼 Pandas", "📓 Jupyter", "🐘 PostgreSQL", 
    "📁 Git", "🐙 GitHub", "💻 VSCode", "🐳 Docker",
    "🌐 HTML", "🎨 CSS", "⚡ JS", "⚛️ React", "🟢 Node.js", "⚙️ C++"
]

items_per_row = 6
row_height = 80
col_width = 125

svg_content = ""
for i, tool in enumerate(tools):
    row = i // items_per_row
    col = i % items_per_row
    
    x = 25 + col * col_width
    y = 40 + row * row_height
    delay = round(random.uniform(0, 3), 2)
    
    svg_content += f'''
    <g class="bubble-container" style="animation-delay: {delay}s;" transform="translate({x}, {y})">
      <rect class="box" x="0" y="0" width="115" height="40" />
      <text class="text" x="57" y="25">{tool}</text>
    </g>'''

svg_footer = "</svg>"

with open("assets/tech_stack.svg", "w", encoding="utf-8") as f:
    f.write(svg_header + svg_content + svg_footer)
print("Generated tech_stack.svg")
