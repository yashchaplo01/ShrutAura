import re

with open('css/sections.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the start and end markers of the new hero section in the current CSS
start_marker = "/* ── Hero Section ── */"
end_marker = "/* ── Trust / Tech Partners Section ── */"

old_hero_css = """/* ── Hero Section ── */
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  position: relative;
  background-color: var(--color-navy);
  overflow: hidden;
  padding-top: var(--nav-height);
}

.hero__bg {
  position: absolute;
  inset: 0;
  overflow: hidden;
}

/* Subtle grid pattern */
.hero__grid {
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 60px 60px;
  animation: gridFade 8s ease-in-out infinite;
}

/* Gradient orbs */
.hero__orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.15;
}

.hero__orb--1 {
  width: 600px;
  height: 600px;
  background: var(--color-accent);
  top: -200px;
  right: -100px;
  animation: float1 20s ease-in-out infinite;
}

.hero__orb--2 {
  width: 400px;
  height: 400px;
  background: var(--color-emerald);
  bottom: -100px;
  left: -50px;
  animation: float2 25s ease-in-out infinite;
}

.hero__orb--3 {
  width: 300px;
  height: 300px;
  background: var(--color-accent-light);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  animation: float3 18s ease-in-out infinite;
}

/* Geometric shapes */
.hero__shape {
  position: absolute;
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-xl);
}

.hero__shape--1 {
  width: 200px;
  height: 200px;
  top: 15%;
  right: 10%;
  transform: rotate(15deg);
  animation: float1 15s ease-in-out infinite;
}

.hero__shape--2 {
  width: 120px;
  height: 120px;
  bottom: 20%;
  left: 15%;
  transform: rotate(-10deg);
  animation: float2 20s ease-in-out infinite;
  border-radius: 50%;
}

.hero__shape--3 {
  width: 80px;
  height: 80px;
  top: 40%;
  right: 30%;
  animation: float3 12s ease-in-out infinite;
}

.hero__content {
  position: relative;
  z-index: 2;
  max-width: 780px;
  padding: var(--space-16) 0;
}

.hero__badge {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-5);
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-full);
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: var(--space-8);
  backdrop-filter: blur(10px);
}

.hero__badge-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: var(--color-emerald);
  animation: pulse-ring 2s ease-in-out infinite;
}

.hero__headline {
  font-family: var(--font-heading);
  font-size: var(--text-7xl);
  font-weight: var(--weight-extrabold);
  color: var(--color-white);
  letter-spacing: var(--tracking-tight);
  line-height: var(--leading-tight);
  margin-bottom: var(--space-6);
}

.hero__headline-accent {
  background: linear-gradient(135deg, var(--color-accent-light), var(--color-emerald));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero__subtext {
  font-size: var(--text-xl);
  line-height: var(--leading-relaxed);
  color: rgba(255, 255, 255, 0.6);
  max-width: 600px;
  margin-bottom: var(--space-10);
}

.hero__actions {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  flex-wrap: wrap;
}

@media (max-width: 768px) {
  .hero {
    min-height: auto;
    padding-top: calc(var(--nav-height) + var(--space-12));
    padding-bottom: var(--space-16);
  }
  .hero__content {
    padding: var(--space-8) 0;
  }
  .hero__actions {
    flex-direction: column;
    align-items: flex-start;
  }
}
"""

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + old_hero_css + "\n\n" + content[end_idx:]
    with open('css/sections.css', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully replaced.")
else:
    print("Markers not found.")
