import os
from PIL import Image, ImageDraw, ImageFont

img_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\face-of-kolkata-photography\assets\images"
os.makedirs(img_dir, exist_ok=True)

# 1. logo.svg
logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 80" width="460" height="80">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFE082" />
      <stop offset="50%" stop-color="#D4AF37" />
      <stop offset="100%" stop-color="#AA7C11" />
    </linearGradient>
    <linearGradient id="crimsonGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#B71C1C" />
      <stop offset="100%" stop-color="#4A0007" />
    </linearGradient>
  </defs>

  <!-- Circular Aperture Icon -->
  <g transform="translate(10, 8)">
    <circle cx="32" cy="32" r="30" fill="url(#crimsonGrad)" stroke="url(#goldGrad)" stroke-width="2.5" />
    <!-- Camera Aperture Blades -->
    <path d="M32 10 L44 26 L36 38 L24 22 Z" fill="none" stroke="url(#goldGrad)" stroke-width="1.8" />
    <path d="M50 26 L46 44 L32 38 L36 20 Z" fill="none" stroke="url(#goldGrad)" stroke-width="1.8" />
    <path d="M46 48 L28 52 L26 36 L44 32 Z" fill="none" stroke="url(#goldGrad)" stroke-width="1.8" />
    <path d="M26 52 L14 36 L22 24 L34 40 Z" fill="none" stroke="url(#goldGrad)" stroke-width="1.8" />
    <circle cx="32" cy="32" r="7" fill="url(#goldGrad)" />
    <!-- Sparkle Diamond -->
    <polygon points="52,14 54,19 59,21 54,23 52,28 50,23 45,21 50,19" fill="#FFF8E1" />
  </g>

  <!-- Typography -->
  <text x="88" y="38" font-family="'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif" font-size="23" font-weight="800" letter-spacing="1.5" fill="#FFFFFF">
    FACE OF KOLKATA
  </text>
  <text x="90" y="58" font-family="'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif" font-size="11" font-weight="600" letter-spacing="3" fill="url(#goldGrad)">
    PHOTOGRAPHY &amp; CINEMATOGRAPHY
  </text>
</svg>"""

with open(os.path.join(img_dir, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(logo_svg)

# 2. favicon.svg
favicon_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="favGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFE082" />
      <stop offset="100%" stop-color="#D4AF37" />
    </linearGradient>
    <linearGradient id="favCrimson" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#B71C1C" />
      <stop offset="100%" stop-color="#3E0006" />
    </linearGradient>
  </defs>
  <rect width="64" height="64" rx="16" fill="url(#favCrimson)" stroke="url(#favGold)" stroke-width="2.5"/>
  <!-- Camera Shutter Icon -->
  <circle cx="32" cy="32" r="18" fill="none" stroke="url(#favGold)" stroke-width="2.5" />
  <circle cx="32" cy="32" r="7" fill="url(#favGold)" />
  <circle cx="43" cy="21" r="3" fill="#FFF8E1" />
</svg>"""

with open(os.path.join(img_dir, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(favicon_svg)

# 3. Render raster favicons (512x512, 180x180, 32x32, favicon.ico)
size = (512, 512)
img = Image.new("RGBA", size, (20, 5, 8, 255))
draw = ImageDraw.Draw(img)

# Outer Gold Ring
draw.ellipse([32, 32, 480, 480], outline=(212, 175, 55, 255), width=16)
# Inner Crimson Fill
draw.ellipse([48, 48, 464, 464], fill=(138, 14, 28, 255))
# Shutter blades & central aperture
draw.ellipse([160, 160, 352, 352], outline=(255, 224, 130, 255), width=14)
draw.ellipse([216, 216, 296, 296], fill=(212, 175, 55, 255))
# Lens glint
draw.ellipse([330, 140, 360, 170], fill=(255, 255, 255, 220))

# Save 512x512
img.save(os.path.join(img_dir, "logo-512.png"), "PNG")

# Save Apple Touch Icon (180x180)
apple_icon = img.resize((180, 180), Image.Resampling.LANCZOS)
apple_icon.save(os.path.join(img_dir, "apple-touch-icon.png"), "PNG")

# Save 32x32
fav32 = img.resize((32, 32), Image.Resampling.LANCZOS)
fav32.save(os.path.join(img_dir, "favicon-32x32.png"), "PNG")

# Save favicon.ico
fav32.save(os.path.join(img_dir, "favicon.ico"), format="ICO", sizes=[(32, 32), (16, 16)])

print("Favicon suite successfully generated in assets/images!")
