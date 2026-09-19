#!/usr/bin/env python3
"""
Generate ultra-modern, dynamic, stylized GitHub profile assets for h3n-x.
Studio Ghibli Twilight Sky & Warm Lantern theme.
Validated for XML compliance and GitHub Markdown embedding.
"""

import os
import xml.etree.ElementTree as ET

ASSETS_DIR = "/home/h3n/Portfolio/h3n-x/assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. CINEMATIC HEADERS (Dark & Light)
# -------------------------------------------------------------
def get_header_dark():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 370" width="100%" height="100%">
  <defs>
    <!-- Sky & Twilight Gradient -->
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080D14" />
      <stop offset="35%" stop-color="#0E141D" />
      <stop offset="75%" stop-color="#151F2C" />
      <stop offset="100%" stop-color="#1D2A3B" />
    </linearGradient>

    <!-- Warm Lantern Sunset Radial Glow -->
    <radialGradient id="sunsetGlow" cx="22%" cy="28%" r="60%">
      <stop offset="0%" stop-color="#F4A261" stop-opacity="0.25" />
      <stop offset="50%" stop-color="#F4A261" stop-opacity="0.06" />
      <stop offset="100%" stop-color="#0E141D" stop-opacity="0" />
    </radialGradient>

    <!-- Mint Aurora Ambient Glow -->
    <radialGradient id="auroraGlow" cx="82%" cy="35%" r="55%">
      <stop offset="0%" stop-color="#00D2B4" stop-opacity="0.18" />
      <stop offset="50%" stop-color="#2A6647" stop-opacity="0.07" />
      <stop offset="100%" stop-color="#0E141D" stop-opacity="0" />
    </radialGradient>

    <!-- Terminal Window Gradient -->
    <linearGradient id="termGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#151F2C" stop-opacity="0.96" />
      <stop offset="100%" stop-color="#0E141D" stop-opacity="0.98" />
    </linearGradient>

    <!-- Border Neon Gradient -->
    <linearGradient id="neonBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F4A261" stop-opacity="0.75" />
      <stop offset="45%" stop-color="#5EBAA0" stop-opacity="0.8" />
      <stop offset="85%" stop-color="#64B5F6" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#F4A261" stop-opacity="0.75" />
    </linearGradient>

    <!-- Grid Pattern -->
    <pattern id="headerGrid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="rgba(255,255,255,0.028)" stroke-width="1" />
    </pattern>
  </defs>

  <style>
    @keyframes pulseDot { 0%, 100% { transform: scale(1); opacity: 0.85; } 50% { transform: scale(1.35); opacity: 1; } }
    @keyframes lanternFloat1 { 0%, 100% { transform: translateY(0px) translateX(0px); opacity: 0.35; } 50% { transform: translateY(-12px) translateX(6px); opacity: 0.9; } }
    @keyframes lanternFloat2 { 0%, 100% { transform: translateY(0px) translateX(0px); opacity: 0.25; } 50% { transform: translateY(-16px) translateX(-7px); opacity: 0.85; } }
    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
    @keyframes auroraWave { 0%, 100% { opacity: 0.14; } 50% { opacity: 0.28; } }
    @keyframes shootingStar { 0% { transform: translateX(0) translateY(0); opacity: 0; } 10% { opacity: 1; } 30% { transform: translateX(180px) translateY(90px); opacity: 0; } 100% { transform: translateX(180px) translateY(90px); opacity: 0; } }

    .pulse { animation: pulseDot 2.2s ease-in-out infinite; transform-origin: 52px 42px; }
    .firefly-a { animation: lanternFloat1 5.5s ease-in-out infinite; }
    .firefly-b { animation: lanternFloat2 7s ease-in-out 1.5s infinite; }
    .firefly-c { animation: lanternFloat1 6.5s ease-in-out 3s infinite; }
    .cursor { animation: blink 1s step-end infinite; }
    .aurora-bg { animation: auroraWave 7.5s ease-in-out infinite; }
    .star-shoot { animation: shootingStar 9s linear infinite; }

    .h-title { font-family: 'Plus Jakarta Sans', -apple-system, system-ui, sans-serif; font-weight: 800; font-size: 38px; fill: #F3F6F9; letter-spacing: -1px; }
    .h-sub { font-family: 'Plus Jakarta Sans', -apple-system, system-ui, sans-serif; font-weight: 600; font-size: 15px; fill: #F4A261; letter-spacing: 0.2px; }
    .h-pitch { font-family: 'Plus Jakarta Sans', -apple-system, system-ui, sans-serif; font-weight: 400; font-size: 13px; fill: #CBD5E1; }
    .term-code { font-family: 'JetBrains Mono', 'Fira Code', monospace; font-size: 11px; }
  </style>

  <!-- Canvas Background -->
  <rect x="2" y="2" width="916" height="366" rx="20" fill="url(#skyGrad)" stroke="#1D2A3B" stroke-width="1.5" />
  <rect x="2" y="2" width="916" height="366" rx="20" fill="url(#headerGrid)" />
  <rect x="2" y="2" width="916" height="366" rx="20" fill="url(#sunsetGlow)" />
  <rect x="2" y="2" width="916" height="366" rx="20" fill="url(#auroraGlow)" class="aurora-bg" />
  <rect x="2" y="2" width="916" height="366" rx="20" fill="none" stroke="url(#neonBorder)" stroke-width="1.3" opacity="0.75" />

  <!-- Atmospheric Ghibli Horizon Hills & Wind-Turbine Silhouettes -->
  <path d="M 2 368 Q 220 315, 460 342 T 918 325 L 918 368 L 2 368 Z" fill="#0A0F16" opacity="0.85" />
  <path d="M 2 368 Q 280 332, 580 352 T 918 340 L 918 368 L 2 368 Z" fill="#151F2C" opacity="0.45" />

  <!-- Wind Turbine / Antenna silhouettes in the distant twilight -->
  <g stroke="#CBD5E1" stroke-opacity="0.15" stroke-width="1">
    <line x1="830" y1="326" x2="830" y2="295" />
    <circle cx="830" cy="295" r="1.5" fill="#F4A261" />
    <line x1="822" y1="290" x2="838" y2="300" stroke-opacity="0.2" />
    <line x1="880" y1="335" x2="880" y2="310" />
    <circle cx="880" cy="310" r="1.5" fill="#5EBAA0" />
  </g>

  <!-- Constellation Nodes & Tech Lines -->
  <g stroke="#CBD5E1" stroke-opacity="0.12" stroke-width="1" stroke-dasharray="3,3">
    <line x1="45" y1="125" x2="160" y2="72" />
    <line x1="160" y1="72" x2="280" y2="108" />
    <line x1="280" y1="108" x2="385" y2="52" />
    <line x1="385" y1="52" x2="445" y2="95" />
  </g>

  <!-- Shooting Data Star -->
  <g class="star-shoot">
    <line x1="40" y1="40" x2="70" y2="55" stroke="url(#neonBorder)" stroke-width="1.5" stroke-linecap="round" />
  </g>

  <!-- Glowing Fireflies / Twilight Spirit Sparks -->
  <g>
    <circle cx="110" cy="88" r="2.2" fill="#F4A261" class="firefly-a" />
    <circle cx="280" cy="56" r="2.8" fill="#5EBAA0" class="firefly-b" />
    <circle cx="390" cy="112" r="1.8" fill="#FFD166" class="firefly-c" />
    <circle cx="455" cy="310" r="2.5" fill="#F4A261" class="firefly-b" />
    <circle cx="870" cy="52" r="2" fill="#5EBAA0" class="firefly-a" />
    <circle cx="895" cy="265" r="2.2" fill="#64B5F6" class="firefly-c" />
    <circle cx="60" cy="245" r="1.8" fill="#5EBAA0" class="firefly-a" />
  </g>

  <!-- ================= LEFT COLUMN: HERO IDENTITY ================= -->
  <!-- Operational Status Badge -->
  <g transform="translate(38, 30)">
    <rect x="0" y="0" width="295" height="28" rx="14" fill="#151F2C" stroke="rgba(94,186,160,0.35)" stroke-width="1" />
    <circle cx="14" cy="14" r="5" fill="#5EBAA0" class="pulse" />
    <circle cx="14" cy="14" r="2" fill="#FFFFFF" />
    <text x="28" y="18" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#5EBAA0" letter-spacing="0.8px">SYSTEM RUNTIME: HARDENED</text>
    <text x="218" y="18" font-family="'JetBrains Mono', monospace" font-size="10" fill="#475569">|</text>
    <text x="230" y="18" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#F4A261">0 CVEs</text>
  </g>

  <!-- Name & Handle -->
  <g transform="translate(38, 96)">
    <text x="0" y="0" class="h-title">Henry Pacheco</text>
    <text x="312" y="-3" font-family="'JetBrains Mono', monospace" font-size="19" font-weight="500" fill="#64748B">/ h3n-x</text>
  </g>

  <!-- Role Subtitle -->
  <g transform="translate(38, 126)">
    <text x="0" y="0" class="h-sub">DevOps &amp; Linux Infrastructure Engineer</text>
    <text x="338" y="0" font-family="'JetBrains Mono', monospace" font-size="13" fill="#5EBAA0">✦ SRE &amp; DevSecOps</text>
  </g>

  <!-- Engineering Pitch -->
  <g transform="translate(38, 156)">
    <text x="0" y="0" class="h-pitch">Eliminating operational fragility through predictable Linux automation,</text>
    <text x="0" y="21" class="h-pitch">container runtime security (CIS Benchmark), and SARIF CI/CD gates.</text>
  </g>

  <!-- Tech Stack Highlights Pills -->
  <g transform="translate(38, 212)">
    <!-- Linux -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="105" height="30" rx="8" fill="#151F2C" stroke="rgba(255,255,255,0.12)" stroke-width="1" />
      <circle cx="12" cy="15" r="3.5" fill="#CBD5E1" />
      <text x="24" y="19" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600" fill="#F3F6F9">Arch Linux</text>
    </g>
    <!-- Docker -->
    <g transform="translate(113, 0)">
      <rect x="0" y="0" width="112" height="30" rx="8" fill="#151F2C" stroke="rgba(0,210,180,0.3)" stroke-width="1" />
      <circle cx="12" cy="15" r="3.5" fill="#00D2B4" />
      <text x="24" y="19" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600" fill="#00D2B4">Docker CIS</text>
    </g>
    <!-- CI/CD -->
    <g transform="translate(233, 0)">
      <rect x="0" y="0" width="108" height="30" rx="8" fill="#151F2C" stroke="rgba(244,162,97,0.3)" stroke-width="1" />
      <circle cx="12" cy="15" r="3.5" fill="#F4A261" />
      <text x="24" y="19" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600" fill="#F4A261">SARIF 2.1.0</text>
    </g>
    <!-- Python -->
    <g transform="translate(349, 0)">
      <rect x="0" y="0" width="95" height="30" rx="8" fill="#151F2C" stroke="rgba(100,181,246,0.3)" stroke-width="1" />
      <circle cx="12" cy="15" r="3.5" fill="#64B5F6" />
      <text x="24" y="19" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600" fill="#64B5F6">Python 3.12</text>
    </g>
  </g>

  <!-- Location & Coordinates -->
  <g transform="translate(38, 275)">
    <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="11" fill="#64748B">
      <tspan fill="#5EBAA0">●</tspan> Open to Global Remote Roles  ·  Bucaramanga, Colombia  ·  <tspan fill="#F4A261">h3n-x.dev</tspan>
    </text>
  </g>

  <!-- Metric Badges Row (2026 Ready) -->
  <g transform="translate(38, 316)">
    <rect x="0" y="0" width="82" height="22" rx="5" fill="#182333" stroke="#1D2A3B" stroke-width="1" />
    <text x="41" y="14" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#5EBAA0" font-weight="600" text-anchor="middle">100% Tests</text>

    <rect x="90" y="0" width="102" height="22" rx="5" fill="#182333" stroke="#1D2A3B" stroke-width="1" />
    <text x="141" y="14" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#F4A261" font-weight="600" text-anchor="middle">CIS Benchmark</text>

    <rect x="200" y="0" width="95" height="22" rx="5" fill="#182333" stroke="#1D2A3B" stroke-width="1" />
    <text x="247" y="14" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#64B5F6" font-weight="600" text-anchor="middle">CycloneDX 1.5</text>

    <rect x="303" y="0" width="105" height="22" rx="5" fill="#182333" stroke="#1D2A3B" stroke-width="1" />
    <text x="355" y="14" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#CBD5E1" font-weight="600" text-anchor="middle">Idempotent Bash</text>
  </g>

  <!-- ================= RIGHT COLUMN: INTERACTIVE HUD TERMINAL ================= -->
  <g transform="translate(465, 30)">
    <!-- Terminal Outer Frame with Glassmorphism -->
    <rect x="0" y="0" width="418" height="308" rx="12" fill="url(#termGrad)" stroke="rgba(255,255,255,0.15)" stroke-width="1.2" />
    
    <!-- Title Bar -->
    <path d="M 0 12 Q 0 0, 12 0 L 406 0 Q 418 0, 418 12 L 418 34 L 0 34 Z" fill="#182333" />
    <circle cx="18" cy="17" r="4.5" fill="#EF4444" opacity="0.85" />
    <circle cx="34" cy="17" r="4.5" fill="#F59E0B" opacity="0.85" />
    <circle cx="50" cy="17" r="4.5" fill="#10B981" opacity="0.85" />
    <text x="209" y="21" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600" fill="#94A3B8" text-anchor="middle">h3n@twilight: ~/devops-defense</text>

    <!-- Terminal Output -->
    <g transform="translate(18, 56)">
      <!-- Line 1 -->
      <text x="0" y="0" class="term-code" fill="#F4A261">$</text>
      <text x="14" y="0" class="term-code" fill="#F3F6F9">dockerward --audit live-runtime</text>
      <text x="0" y="19" class="term-code" fill="#5EBAA0">✓ Docker Engine API connected (/var/run/docker.sock)</text>
      <text x="0" y="36" class="term-code" fill="#CBD5E1">→ CIS v1.6.0: cgroups memory=512M cpu=1.0 pids=200</text>
      <text x="0" y="53" class="term-code" fill="#CBD5E1">→ Capabilities: bounding set dropped · seccomp active</text>

      <!-- Line 2 -->
      <text x="0" y="80" class="term-code" fill="#F4A261">$</text>
      <text x="14" y="80" class="term-code" fill="#F3F6F9">repo-secret-auditor --history --sbom</text>
      <text x="0" y="99" class="term-code" fill="#5EBAA0">✓ Git log -p audited: 0 leaked tokens found</text>
      <text x="0" y="116" class="term-code" fill="#CBD5E1">→ CycloneDX 1.5 SBOM generated · CVSS v3.1 checked</text>
      <text x="0" y="133" class="term-code" fill="#64B5F6">→ SARIF 2.1.0 exported to GitHub Code Scanning</text>

      <!-- Line 3 -->
      <text x="0" y="160" class="term-code" fill="#F4A261">$</text>
      <text x="14" y="160" class="term-code" fill="#F3F6F9">secuscan-api --posture-score</text>
      <text x="0" y="179" class="term-code" fill="#5EBAA0">✓ Posture Score: 98/100 (Grade A+) · Anti-SSRF Guard</text>

      <!-- Line 4 -->
      <text x="0" y="206" class="term-code" fill="#F4A261">$</text>
      <text x="14" y="206" class="term-code" fill="#F3F6F9">archforge --verify-idempotency</text>
      <text x="0" y="225" class="term-code" fill="#5EBAA0">✓ 28 modules converged · systemd &amp; nftables synced</text>

      <!-- Cursor -->
      <text x="0" y="246" class="term-code" fill="#F4A261">h3n@twilight ~ % <tspan fill="#00D2B4" class="cursor">█</tspan></text>
    </g>
  </g>
</svg>'''

def get_header_light():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 370" width="100%" height="100%">
  <defs>
    <!-- Ghibli Parchment & Watercolor Gradient -->
    <linearGradient id="skyGradL" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FBF9F4" />
      <stop offset="40%" stop-color="#FFFFFF" />
      <stop offset="80%" stop-color="#F3ECE1" />
      <stop offset="100%" stop-color="#EAE0D1" />
    </linearGradient>

    <!-- Terracotta Glow -->
    <radialGradient id="sunsetGlowL" cx="22%" cy="28%" r="60%">
      <stop offset="0%" stop-color="#B84E26" stop-opacity="0.14" />
      <stop offset="100%" stop-color="#FBF9F4" stop-opacity="0" />
    </radialGradient>

    <!-- Deep Forest Glow -->
    <radialGradient id="forestGlowL" cx="82%" cy="35%" r="55%">
      <stop offset="0%" stop-color="#2A6647" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#FBF9F4" stop-opacity="0" />
    </radialGradient>

    <!-- Terminal Window Light Gradient -->
    <linearGradient id="termGradL" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.98" />
      <stop offset="100%" stop-color="#F7F3EB" stop-opacity="0.98" />
    </linearGradient>

    <pattern id="headerGridL" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="rgba(45,55,72,0.04)" stroke-width="1" />
    </pattern>
  </defs>

  <style>
    .h-title-l { font-family: 'Plus Jakarta Sans', -apple-system, system-ui, sans-serif; font-weight: 800; font-size: 38px; fill: #1C232B; letter-spacing: -1px; }
    .h-sub-l { font-family: 'Plus Jakarta Sans', -apple-system, system-ui, sans-serif; font-weight: 600; font-size: 15px; fill: #B84E26; letter-spacing: 0.2px; }
    .h-pitch-l { font-family: 'Plus Jakarta Sans', -apple-system, system-ui, sans-serif; font-weight: 400; font-size: 13px; fill: #3B4654; }
    .term-code-l { font-family: 'JetBrains Mono', 'Fira Code', monospace; font-size: 11px; }
    .cursor-l { animation: blink 1s step-end infinite; }
    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
  </style>

  <!-- Canvas Background -->
  <rect x="2" y="2" width="916" height="366" rx="20" fill="url(#skyGradL)" stroke="#CCD2DA" stroke-width="1.5" />
  <rect x="2" y="2" width="916" height="366" rx="20" fill="url(#headerGridL)" />
  <rect x="2" y="2" width="916" height="366" rx="20" fill="url(#sunsetGlowL)" />
  <rect x="2" y="2" width="916" height="366" rx="20" fill="url(#forestGlowL)" />

  <!-- Base Landscape Silhouette -->
  <path d="M 2 368 Q 240 325, 480 348 T 918 335 L 918 368 L 2 368 Z" fill="#E8DEC9" opacity="0.6" />
  <path d="M 2 368 Q 280 340, 620 358 T 918 348 L 918 368 L 2 368 Z" fill="#DDD1B8" opacity="0.4" />

  <!-- Wind Turbine / Antenna silhouettes in the distant meadow -->
  <g stroke="#266A8C" stroke-opacity="0.2" stroke-width="1">
    <line x1="830" y1="332" x2="830" y2="305" />
    <circle cx="830" cy="305" r="1.5" fill="#B84E26" />
    <line x1="880" y1="340" x2="880" y2="318" />
    <circle cx="880" cy="318" r="1.5" fill="#2A6647" />
  </g>

  <!-- ================= LEFT COLUMN: HERO IDENTITY ================= -->
  <!-- Operational Status Badge -->
  <g transform="translate(38, 30)">
    <rect x="0" y="0" width="295" height="28" rx="14" fill="#FFFFFF" stroke="#2A6647" stroke-width="1.2" opacity="0.9" />
    <circle cx="14" cy="14" r="5" fill="#2A6647" />
    <circle cx="14" cy="14" r="2" fill="#FFFFFF" />
    <text x="28" y="18" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#2A6647" letter-spacing="0.8px">SYSTEM RUNTIME: HARDENED</text>
    <text x="218" y="18" font-family="'JetBrains Mono', monospace" font-size="10" fill="#CBD5E1">|</text>
    <text x="230" y="18" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#B84E26">0 CVEs</text>
  </g>

  <!-- Name & Handle -->
  <g transform="translate(38, 96)">
    <text x="0" y="0" class="h-title-l">Henry Pacheco</text>
    <text x="312" y="-3" font-family="'JetBrains Mono', monospace" font-size="19" font-weight="500" fill="#718096">/ h3n-x</text>
  </g>

  <!-- Role Subtitle -->
  <g transform="translate(38, 126)">
    <text x="0" y="0" class="h-sub-l">DevOps &amp; Linux Infrastructure Engineer</text>
    <text x="338" y="0" font-family="'JetBrains Mono', monospace" font-size="13" fill="#2A6647">✦ SRE &amp; DevSecOps</text>
  </g>

  <!-- Engineering Pitch -->
  <g transform="translate(38, 156)">
    <text x="0" y="0" class="h-pitch-l">Eliminating operational fragility through predictable Linux automation,</text>
    <text x="0" y="21" class="h-pitch-l">container runtime security (CIS Benchmark), and SARIF CI/CD gates.</text>
  </g>

  <!-- Tech Stack Highlights Pills -->
  <g transform="translate(38, 212)">
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="105" height="30" rx="8" fill="#FFFFFF" stroke="#CCD2DA" stroke-width="1.2" />
      <circle cx="12" cy="15" r="3.5" fill="#266A8C" />
      <text x="24" y="19" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600" fill="#1C232B">Arch Linux</text>
    </g>
    <g transform="translate(113, 0)">
      <rect x="0" y="0" width="112" height="30" rx="8" fill="#FFFFFF" stroke="#CCD2DA" stroke-width="1.2" />
      <circle cx="12" cy="15" r="3.5" fill="#2A6647" />
      <text x="24" y="19" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600" fill="#2A6647">Docker CIS</text>
    </g>
    <g transform="translate(233, 0)">
      <rect x="0" y="0" width="108" height="30" rx="8" fill="#FFFFFF" stroke="#CCD2DA" stroke-width="1.2" />
      <circle cx="12" cy="15" r="3.5" fill="#B84E26" />
      <text x="24" y="19" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600" fill="#B84E26">SARIF 2.1.0</text>
    </g>
    <g transform="translate(349, 0)">
      <rect x="0" y="0" width="95" height="30" rx="8" fill="#FFFFFF" stroke="#CCD2DA" stroke-width="1.2" />
      <circle cx="12" cy="15" r="3.5" fill="#266A8C" />
      <text x="24" y="19" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600" fill="#266A8C">Python 3.12</text>
    </g>
  </g>

  <!-- Location & Coordinates -->
  <g transform="translate(38, 275)">
    <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="11" fill="#718096">
      <tspan fill="#2A6647">●</tspan> Open to Global Remote Roles  ·  Bucaramanga, Colombia  ·  <tspan fill="#B84E26">h3n-x.dev</tspan>
    </text>
  </g>

  <!-- Metric Badges Row -->
  <g transform="translate(38, 316)">
    <rect x="0" y="0" width="82" height="22" rx="5" fill="#FFFFFF" stroke="#CCD2DA" stroke-width="1" />
    <text x="41" y="14" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#2A6647" font-weight="600" text-anchor="middle">100% Tests</text>

    <rect x="90" y="0" width="102" height="22" rx="5" fill="#FFFFFF" stroke="#CCD2DA" stroke-width="1" />
    <text x="141" y="14" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#B84E26" font-weight="600" text-anchor="middle">CIS Benchmark</text>

    <rect x="200" y="0" width="95" height="22" rx="5" fill="#FFFFFF" stroke="#CCD2DA" stroke-width="1" />
    <text x="247" y="14" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#266A8C" font-weight="600" text-anchor="middle">CycloneDX 1.5</text>

    <rect x="303" y="0" width="105" height="22" rx="5" fill="#FFFFFF" stroke="#CCD2DA" stroke-width="1" />
    <text x="355" y="14" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#5A6A80" font-weight="600" text-anchor="middle">Idempotent Bash</text>
  </g>

  <!-- ================= RIGHT COLUMN: INTERACTIVE HUD TERMINAL ================= -->
  <g transform="translate(465, 30)">
    <!-- Terminal Outer Frame -->
    <rect x="0" y="0" width="418" height="308" rx="12" fill="url(#termGradL)" stroke="#CCD2DA" stroke-width="1.2" />
    
    <!-- Title Bar -->
    <path d="M 0 12 Q 0 0, 12 0 L 406 0 Q 418 0, 418 12 L 418 34 L 0 34 Z" fill="#EAE0D1" />
    <circle cx="18" cy="17" r="4.5" fill="#DC2626" opacity="0.8" />
    <circle cx="34" cy="17" r="4.5" fill="#D97706" opacity="0.8" />
    <circle cx="50" cy="17" r="4.5" fill="#059669" opacity="0.8" />
    <text x="209" y="21" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600" fill="#4B5563" text-anchor="middle">h3n@parchment: ~/devops-defense</text>

    <!-- Terminal Output -->
    <g transform="translate(18, 56)">
      <text x="0" y="0" class="term-code-l" fill="#B84E26">$</text>
      <text x="14" y="0" class="term-code-l" fill="#1C232B">dockerward --audit live-runtime</text>
      <text x="0" y="19" class="term-code-l" fill="#2A6647">✓ Docker Engine API connected (/var/run/docker.sock)</text>
      <text x="0" y="36" class="term-code-l" fill="#4B5563">→ CIS v1.6.0: cgroups memory=512M cpu=1.0 pids=200</text>
      <text x="0" y="53" class="term-code-l" fill="#4B5563">→ Capabilities: bounding set dropped · seccomp active</text>

      <text x="0" y="80" class="term-code-l" fill="#B84E26">$</text>
      <text x="14" y="80" class="term-code-l" fill="#1C232B">repo-secret-auditor --history --sbom</text>
      <text x="0" y="99" class="term-code-l" fill="#2A6647">✓ Git log -p audited: 0 leaked tokens found</text>
      <text x="0" y="116" class="term-code-l" fill="#4B5563">→ CycloneDX 1.5 SBOM generated · CVSS v3.1 checked</text>
      <text x="0" y="133" class="term-code-l" fill="#266A8C">→ SARIF 2.1.0 exported to GitHub Code Scanning</text>

      <text x="0" y="160" class="term-code-l" fill="#B84E26">$</text>
      <text x="14" y="160" class="term-code-l" fill="#1C232B">secuscan-api --posture-score</text>
      <text x="0" y="179" class="term-code-l" fill="#2A6647">✓ Posture Score: 98/100 (Grade A+) · Anti-SSRF Guard</text>

      <text x="0" y="206" class="term-code-l" fill="#B84E26">$</text>
      <text x="14" y="206" class="term-code-l" fill="#1C232B">archforge --verify-idempotency</text>
      <text x="0" y="225" class="term-code-l" fill="#2A6647">✓ 28 modules converged · systemd &amp; nftables synced</text>

      <text x="0" y="246" class="term-code-l" fill="#B84E26">h3n@parchment ~ % <tspan fill="#2A6647" class="cursor-l">█</tspan></text>
    </g>
  </g>
</svg>'''


# -------------------------------------------------------------
# 2. ARCHITECTURE INFOGRAPHIC: 5-LAYER DEFENSE-IN-DEPTH
# -------------------------------------------------------------
def get_defense_architecture_dark():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 280" width="100%" height="100%">
  <defs>
    <linearGradient id="archBgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E141D" />
      <stop offset="100%" stop-color="#151F2C" />
    </linearGradient>
    <linearGradient id="neonLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#64B5F6" />
      <stop offset="25%" stop-color="#00D2B4" />
      <stop offset="50%" stop-color="#F4A261" />
      <stop offset="75%" stop-color="#5EBAA0" />
      <stop offset="100%" stop-color="#A78BFA" />
    </linearGradient>
  </defs>

  <rect x="2" y="2" width="916" height="276" rx="16" fill="url(#archBgDark)" stroke="#1D2A3B" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(28, 28)">
    <text font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" fill="#5EBAA0" letter-spacing="1.2px">DEFENSE-IN-DEPTH INFRASTRUCTURE ARCHITECTURE</text>
    <text y="18" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="13" font-weight="400" fill="#94A3B8">How Henry Pacheco's core engineered systems integrate to form a hardened zero-trust ecosystem</text>
  </g>

  <!-- Flow Connector Bar -->
  <path d="M 60 148 L 860 148" stroke="url(#neonLine)" stroke-width="2" stroke-dasharray="6,4" opacity="0.6" />

  <!-- 5 Layer Boxes -->
  <!-- Layer 1: Host & Kernel (archforge) -->
  <g transform="translate(24, 75)">
    <rect width="160" height="175" rx="10" fill="#182333" stroke="rgba(100,181,246,0.4)" stroke-width="1.2" />
    <rect width="160" height="4" rx="2" fill="#64B5F6" />
    <text x="12" y="24" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#64B5F6">LAYER 01: HOST</text>
    <text x="12" y="44" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="14" font-weight="800" fill="#F3F6F9">archforge</text>
    <text x="12" y="62" font-family="'JetBrains Mono', monospace" font-size="10" fill="#5EBAA0">Linux Kernel Hardening</text>
    <line x1="12" y1="72" x2="148" y2="72" stroke="#1D2A3B" stroke-width="1" />
    <text x="12" y="90" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• cgroups v1/v2 limits</text>
    <text x="12" y="108" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• systemd daemons</text>
    <text x="12" y="126" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• nftables firewall</text>
    <text x="12" y="144" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• 28 idempotent modules</text>
    <rect x="12" y="152" width="136" height="15" rx="4" fill="#0E141D" />
    <text x="80" y="163" font-family="'JetBrains Mono', monospace" font-size="8" fill="#94A3B8" text-anchor="middle">Foundational OS</text>
  </g>

  <!-- Layer 2: Container Runtime (DockerWard) -->
  <g transform="translate(199, 75)">
    <rect width="160" height="175" rx="10" fill="#182333" stroke="rgba(0,210,180,0.4)" stroke-width="1.2" />
    <rect width="160" height="4" rx="2" fill="#00D2B4" />
    <text x="12" y="24" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#00D2B4">LAYER 02: RUNTIME</text>
    <text x="12" y="44" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="14" font-weight="800" fill="#F3F6F9">DockerWard</text>
    <text x="12" y="62" font-family="'JetBrains Mono', monospace" font-size="10" fill="#5EBAA0">CIS Benchmark Audit</text>
    <line x1="12" y1="72" x2="148" y2="72" stroke="#1D2A3B" stroke-width="1" />
    <text x="12" y="90" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Docker Engine API</text>
    <text x="12" y="108" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• CIS v1.6.0 live rules</text>
    <text x="12" y="126" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• seccomp &amp; caps drops</text>
    <text x="12" y="144" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• SARIF export &amp; CLI</text>
    <rect x="12" y="152" width="136" height="15" rx="4" fill="#0E141D" />
    <text x="80" y="163" font-family="'JetBrains Mono', monospace" font-size="8" fill="#00D2B4" text-anchor="middle">Runtime Guard</text>
  </g>

  <!-- Layer 3: CI/CD & Supply Chain (repo-secret-auditor) -->
  <g transform="translate(374, 75)">
    <rect width="160" height="175" rx="10" fill="#182333" stroke="rgba(244,162,97,0.4)" stroke-width="1.2" />
    <rect width="160" height="4" rx="2" fill="#F4A261" />
    <text x="12" y="24" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#F4A261">LAYER 03: CI/CD GATE</text>
    <text x="12" y="44" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="13.5" font-weight="800" fill="#F3F6F9">secret-auditor</text>
    <text x="12" y="62" font-family="'JetBrains Mono', monospace" font-size="10" fill="#F4A261">Supply Chain Security</text>
    <line x1="12" y1="72" x2="148" y2="72" stroke="#1D2A3B" stroke-width="1" />
    <text x="12" y="90" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• GitHub Actions Gate</text>
    <text x="12" y="108" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• CycloneDX 1.5 SBOM</text>
    <text x="12" y="126" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• OASIS SARIF 2.1.0</text>
    <text x="12" y="144" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Shannon entropy</text>
    <rect x="12" y="152" width="136" height="15" rx="4" fill="#0E141D" />
    <text x="80" y="163" font-family="'JetBrains Mono', monospace" font-size="8" fill="#F4A261" text-anchor="middle">Pipeline Blocker</text>
  </g>

  <!-- Layer 4: Perimeter & Network (secuscan-api) -->
  <g transform="translate(549, 75)">
    <rect width="160" height="175" rx="10" fill="#182333" stroke="rgba(94,186,160,0.4)" stroke-width="1.2" />
    <rect width="160" height="4" rx="2" fill="#5EBAA0" />
    <text x="12" y="24" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#5EBAA0">LAYER 04: PERIMETER</text>
    <text x="12" y="44" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="14" font-weight="800" fill="#F3F6F9">secuscan-api</text>
    <text x="12" y="62" font-family="'JetBrains Mono', monospace" font-size="10" fill="#5EBAA0">EASM &amp; Anti-SSRF</text>
    <line x1="12" y1="72" x2="148" y2="72" stroke="#1D2A3B" stroke-width="1" />
    <text x="12" y="90" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• FastAPI Microservices</text>
    <text x="12" y="108" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Anti-SSRF / DNS rebinding</text>
    <text x="12" y="126" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Security posture score</text>
    <text x="12" y="144" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Celery async queue</text>
    <rect x="12" y="152" width="136" height="15" rx="4" fill="#0E141D" />
    <text x="80" y="163" font-family="'JetBrains Mono', monospace" font-size="8" fill="#5EBAA0" text-anchor="middle">Network Boundary</text>
  </g>

  <!-- Layer 5: Zero-Knowledge Comms (chat-anonimo) -->
  <g transform="translate(724, 75)">
    <rect width="172" height="175" rx="10" fill="#182333" stroke="rgba(167,139,250,0.4)" stroke-width="1.2" />
    <rect width="172" height="4" rx="2" fill="#A78BFA" />
    <text x="12" y="24" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#A78BFA">LAYER 05: PRIVACY</text>
    <text x="12" y="44" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="14" font-weight="800" fill="#F3F6F9">chat-anonimo</text>
    <text x="12" y="62" font-family="'JetBrains Mono', monospace" font-size="10" fill="#A78BFA">End-to-End Encryption</text>
    <line x1="12" y1="72" x2="160" y2="72" stroke="#1D2A3B" stroke-width="1" />
    <text x="12" y="90" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• WebCrypto AES-GCM</text>
    <text x="12" y="108" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• ECDH P-256 key ex</text>
    <text x="12" y="126" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Zero-RAM server relay</text>
    <text x="12" y="144" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Ephemeral WebSockets</text>
    <rect x="12" y="152" width="148" height="15" rx="4" fill="#0E141D" />
    <text x="86" y="163" font-family="'JetBrains Mono', monospace" font-size="8" fill="#A78BFA" text-anchor="middle">Zero-Trust Payload</text>
  </g>
</svg>'''

def get_defense_architecture_light():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 280" width="100%" height="100%">
  <defs>
    <linearGradient id="archBgLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FBF9F4" />
      <stop offset="100%" stop-color="#F3ECE1" />
    </linearGradient>
    <linearGradient id="neonLineL" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#266A8C" />
      <stop offset="25%" stop-color="#2A6647" />
      <stop offset="50%" stop-color="#B84E26" />
      <stop offset="75%" stop-color="#2A6647" />
      <stop offset="100%" stop-color="#7C3AED" />
    </linearGradient>
  </defs>

  <rect x="2" y="2" width="916" height="276" rx="16" fill="url(#archBgLight)" stroke="#CCD2DA" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(28, 28)">
    <text font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" fill="#2A6647" letter-spacing="1.2px">DEFENSE-IN-DEPTH INFRASTRUCTURE ARCHITECTURE</text>
    <text y="18" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="13" font-weight="400" fill="#5A6A80">How Henry Pacheco's core engineered systems integrate to form a hardened zero-trust ecosystem</text>
  </g>

  <!-- Flow Connector Bar -->
  <path d="M 60 148 L 860 148" stroke="url(#neonLineL)" stroke-width="2" stroke-dasharray="6,4" opacity="0.6" />

  <!-- 5 Layer Boxes -->
  <!-- Layer 1: Host & Kernel -->
  <g transform="translate(24, 75)">
    <rect width="160" height="175" rx="10" fill="#FFFFFF" stroke="#CCD2DA" stroke-width="1.2" />
    <rect width="160" height="4" rx="2" fill="#266A8C" />
    <text x="12" y="24" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#266A8C">LAYER 01: HOST</text>
    <text x="12" y="44" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="14" font-weight="800" fill="#1C232B">archforge</text>
    <text x="12" y="62" font-family="'JetBrains Mono', monospace" font-size="10" fill="#2A6647">Linux Kernel Hardening</text>
    <line x1="12" y1="72" x2="148" y2="72" stroke="#E2E8F0" stroke-width="1" />
    <text x="12" y="90" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• cgroups v1/v2 limits</text>
    <text x="12" y="108" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• systemd daemons</text>
    <text x="12" y="126" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• nftables firewall</text>
    <text x="12" y="144" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• 28 idempotent modules</text>
    <rect x="12" y="152" width="136" height="15" rx="4" fill="#F3ECE1" />
    <text x="80" y="163" font-family="'JetBrains Mono', monospace" font-size="8" fill="#475569" text-anchor="middle">Foundational OS</text>
  </g>

  <!-- Layer 2: Container Runtime -->
  <g transform="translate(199, 75)">
    <rect width="160" height="175" rx="10" fill="#FFFFFF" stroke="#CCD2DA" stroke-width="1.2" />
    <rect width="160" height="4" rx="2" fill="#2A6647" />
    <text x="12" y="24" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#2A6647">LAYER 02: RUNTIME</text>
    <text x="12" y="44" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="14" font-weight="800" fill="#1C232B">DockerWard</text>
    <text x="12" y="62" font-family="'JetBrains Mono', monospace" font-size="10" fill="#2A6647">CIS Benchmark Audit</text>
    <line x1="12" y1="72" x2="148" y2="72" stroke="#E2E8F0" stroke-width="1" />
    <text x="12" y="90" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• Docker Engine API</text>
    <text x="12" y="108" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• CIS v1.6.0 live rules</text>
    <text x="12" y="126" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• seccomp &amp; caps drops</text>
    <text x="12" y="144" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• SARIF export &amp; CLI</text>
    <rect x="12" y="152" width="136" height="15" rx="4" fill="#F3ECE1" />
    <text x="80" y="163" font-family="'JetBrains Mono', monospace" font-size="8" fill="#2A6647" text-anchor="middle">Runtime Guard</text>
  </g>

  <!-- Layer 3: CI/CD & Supply Chain -->
  <g transform="translate(374, 75)">
    <rect width="160" height="175" rx="10" fill="#FFFFFF" stroke="#CCD2DA" stroke-width="1.2" />
    <rect width="160" height="4" rx="2" fill="#B84E26" />
    <text x="12" y="24" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#B84E26">LAYER 03: CI/CD GATE</text>
    <text x="12" y="44" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="13.5" font-weight="800" fill="#1C232B">secret-auditor</text>
    <text x="12" y="62" font-family="'JetBrains Mono', monospace" font-size="10" fill="#B84E26">Supply Chain Security</text>
    <line x1="12" y1="72" x2="148" y2="72" stroke="#E2E8F0" stroke-width="1" />
    <text x="12" y="90" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• GitHub Actions Gate</text>
    <text x="12" y="108" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• CycloneDX 1.5 SBOM</text>
    <text x="12" y="126" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• OASIS SARIF 2.1.0</text>
    <text x="12" y="144" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• Shannon entropy</text>
    <rect x="12" y="152" width="136" height="15" rx="4" fill="#F3ECE1" />
    <text x="80" y="163" font-family="'JetBrains Mono', monospace" font-size="8" fill="#B84E26" text-anchor="middle">Pipeline Blocker</text>
  </g>

  <!-- Layer 4: Perimeter & Network -->
  <g transform="translate(549, 75)">
    <rect width="160" height="175" rx="10" fill="#FFFFFF" stroke="#CCD2DA" stroke-width="1.2" />
    <rect width="160" height="4" rx="2" fill="#2A6647" />
    <text x="12" y="24" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#2A6647">LAYER 04: PERIMETER</text>
    <text x="12" y="44" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="14" font-weight="800" fill="#1C232B">secuscan-api</text>
    <text x="12" y="62" font-family="'JetBrains Mono', monospace" font-size="10" fill="#2A6647">EASM &amp; Anti-SSRF</text>
    <line x1="12" y1="72" x2="148" y2="72" stroke="#E2E8F0" stroke-width="1" />
    <text x="12" y="90" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• FastAPI Microservices</text>
    <text x="12" y="108" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• Anti-SSRF / DNS rebinding</text>
    <text x="12" y="126" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• Security posture score</text>
    <text x="12" y="144" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• Celery async queue</text>
    <rect x="12" y="152" width="136" height="15" rx="4" fill="#F3ECE1" />
    <text x="80" y="163" font-family="'JetBrains Mono', monospace" font-size="8" fill="#2A6647" text-anchor="middle">Network Boundary</text>
  </g>

  <!-- Layer 5: Zero-Knowledge Comms -->
  <g transform="translate(724, 75)">
    <rect width="172" height="175" rx="10" fill="#FFFFFF" stroke="#CCD2DA" stroke-width="1.2" />
    <rect width="172" height="4" rx="2" fill="#7C3AED" />
    <text x="12" y="24" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#7C3AED">LAYER 05: PRIVACY</text>
    <text x="12" y="44" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="14" font-weight="800" fill="#1C232B">chat-anonimo</text>
    <text x="12" y="62" font-family="'JetBrains Mono', monospace" font-size="10" fill="#7C3AED">End-to-End Encryption</text>
    <line x1="12" y1="72" x2="160" y2="72" stroke="#E2E8F0" stroke-width="1" />
    <text x="12" y="90" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• WebCrypto AES-GCM</text>
    <text x="12" y="108" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• ECDH P-256 key ex</text>
    <text x="12" y="126" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• Zero-RAM server relay</text>
    <text x="12" y="144" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="10.5" fill="#475569">• Ephemeral WebSockets</text>
    <rect x="12" y="152" width="148" height="15" rx="4" fill="#F3ECE1" />
    <text x="86" y="163" font-family="'JetBrains Mono', monospace" font-size="8" fill="#7C3AED" text-anchor="middle">Zero-Trust Payload</text>
  </g>
</svg>'''


# -------------------------------------------------------------
# 3. UPGRADED 6 PINNED PROJECT CARDS (Dark & Light)
# -------------------------------------------------------------
# The 6 pinned projects in STRICT order:
# 1. DockerWard
# 2. repo-secret-auditor
# 3. secuscan-api
# 4. archforge
# 5. portfolio
# 6. chat-anonimo

PROJECTS = [
    {
        "num": "1",
        "name": "dockerward",
        "title": "DockerWard",
        "category": "CONTAINER RUNTIME AUDIT",
        "category_l": "CONTAINER RUNTIME AUDIT",
        "metric": "100% Rules Pass",
        "metric_detail": "CIS Docker v1.6.0",
        "desc_1": "Runtime security audit engine for Docker Engine API.",
        "desc_2": "Audits live containers against CIS Benchmark v1.6.0 with SARIF.",
        "tags": ["Docker Engine API", "CIS Benchmark v1.6.0", "cgroups & seccomp", "71 Tests"],
        "accent": "#00D2B4",
        "accent_l": "#2A6647",
        "icon_type": "docker"
    },
    {
        "num": "2",
        "name": "repo-secret-auditor",
        "title": "repo-secret-auditor",
        "category": "CI/CD & SUPPLY CHAIN SECURITY",
        "category_l": "CI/CD & SUPPLY CHAIN SECURITY",
        "metric": "91% Test Cov",
        "metric_detail": "SARIF 2.1.0 · SBOM",
        "desc_1": "Autonomous CI/CD secret scanner and SBOM generator.",
        "desc_2": "Audits Git commit logs for leaked credentials & FIRST CVSS v3.1.",
        "tags": ["GitHub Actions", "CycloneDX 1.5 SBOM", "SARIF 2.1.0", "74 Tests"],
        "accent": "#F4A261",
        "accent_l": "#B84E26",
        "icon_type": "shield"
    },
    {
        "num": "3",
        "name": "secuscan-api",
        "title": "secuscan-api",
        "category": "EASM & PERIMETER DEFENSE",
        "category_l": "EASM & PERIMETER DEFENSE",
        "metric": "Grade A+ (98/100)",
        "metric_detail": "Anti-SSRF Guard",
        "desc_1": "Asynchronous microservices API for External Attack Surface.",
        "desc_2": "FastAPI + Celery + PostgreSQL 16 with Anti-SSRF & DNS rebinding guard.",
        "tags": ["FastAPI Async", "PostgreSQL 16", "Celery Queue", "86 Tests"],
        "accent": "#5EBAA0",
        "accent_l": "#2A6647",
        "icon_type": "radar"
    },
    {
        "num": "4",
        "name": "archforge",
        "title": "archforge",
        "category": "LINUX KERNEL & SYSTEM HARDENING",
        "category_l": "LINUX KERNEL & SYSTEM HARDENING",
        "metric": "28 Modules",
        "metric_detail": "Idempotent Bash",
        "desc_1": "Automated post-installation & kernel hardening for Arch Linux.",
        "desc_2": "Systemd services, nftables firewall, cgroups, and modular dotfiles.",
        "tags": ["Arch Linux", "systemd daemons", "nftables firewall", "Pure Bash"],
        "accent": "#64B5F6",
        "accent_l": "#266A8C",
        "icon_type": "terminal"
    },
    {
        "num": "5",
        "name": "portfolio",
        "title": "portfolio",
        "category": "ENGINEERING BRAND & SHOWCASE",
        "category_l": "ENGINEERING BRAND & SHOWCASE",
        "metric": "WCAG AA",
        "metric_detail": "Astro 5 + Tailwind v4",
        "desc_1": "Personal engineering portfolio built with Astro 5 & TypeScript.",
        "desc_2": "Ghibli Twilight palette, Playwright tests, and zero CVE dependencies.",
        "tags": ["Astro 5", "TypeScript", "Tailwind CSS v4", "Playwright"],
        "accent": "#F4A261",
        "accent_l": "#B84E26",
        "icon_type": "globe"
    },
    {
        "num": "6",
        "name": "chat-anonimo",
        "title": "chat-anonimo",
        "category": "ZERO-KNOWLEDGE PRIVACY",
        "category_l": "ZERO-KNOWLEDGE PRIVACY",
        "metric": "Zero-RAM Relay",
        "metric_detail": "AES-256-GCM + ECDH",
        "desc_1": "Ephemeral zero-knowledge encrypted messaging system.",
        "desc_2": "WebCrypto API with AES-256-GCM, ECDH P-256 and FastAPI relay.",
        "tags": ["WebCrypto API", "AES-256-GCM", "ECDH P-256", "40 Suites"],
        "accent": "#A78BFA",
        "accent_l": "#7C3AED",
        "icon_type": "lock"
    }
]

def get_svg_icon(icon_type, color):
    if icon_type == "docker":
        return f'''<g stroke="{color}" stroke-width="1.6" fill="none">
          <rect x="0" y="6" width="6" height="5" rx="1" fill="{color}" fill-opacity="0.3" />
          <rect x="8" y="6" width="6" height="5" rx="1" fill="{color}" fill-opacity="0.3" />
          <rect x="16" y="6" width="6" height="5" rx="1" fill="{color}" fill-opacity="0.3" />
          <rect x="8" y="0" width="6" height="5" rx="1" fill="{color}" fill-opacity="0.3" />
          <path d="M -4 14 C 2 21, 24 21, 28 14 C 28 12, 26 11, 22 12" />
        </g>'''
    elif icon_type == "shield":
        return f'''<g stroke="{color}" stroke-width="1.6" fill="none">
          <path d="M 12 2 L 2 6 L 2 13 C 2 19, 12 23, 12 23 C 12 23, 22 19, 22 13 L 22 6 Z" fill="{color}" fill-opacity="0.25" />
          <path d="M 8 12 L 11 15 L 16 9" stroke-linecap="round" stroke-linejoin="round" />
        </g>'''
    elif icon_type == "radar":
        return f'''<g stroke="{color}" stroke-width="1.6" fill="none">
          <circle cx="12" cy="12" r="10" />
          <circle cx="12" cy="12" r="6" stroke-dasharray="2,2" />
          <circle cx="12" cy="12" r="2" fill="{color}" />
          <line x1="12" y1="12" x2="19" y2="5" stroke-linecap="round" />
        </g>'''
    elif icon_type == "terminal":
        return f'''<g stroke="{color}" stroke-width="1.6" fill="none">
          <rect x="2" y="3" width="20" height="17" rx="3" fill="{color}" fill-opacity="0.15" />
          <path d="M 6 8 L 10 11.5 L 6 15" stroke-linecap="round" stroke-linejoin="round" />
          <line x1="12" y1="15" x2="17" y2="15" stroke-linecap="round" />
        </g>'''
    elif icon_type == "globe":
        return f'''<g stroke="{color}" stroke-width="1.6" fill="none">
          <circle cx="12" cy="12" r="10" fill="{color}" fill-opacity="0.15" />
          <ellipse cx="12" cy="12" rx="4.5" ry="10" />
          <line x1="2" y1="12" x2="22" y2="12" />
        </g>'''
    elif icon_type == "lock":
        return f'''<g stroke="{color}" stroke-width="1.6" fill="none">
          <rect x="4" y="9" width="16" height="13" rx="3" fill="{color}" fill-opacity="0.25" />
          <path d="M 7 9 L 7 6 C 7 3.2, 17 3.2, 17 6 L 17 9" stroke-linecap="round" />
          <circle cx="12" cy="15" r="1.5" fill="{color}" />
        </g>'''
    return ""

def generate_card_dark(p):
    accent = p["accent"]
    icon_svg = get_svg_icon(p["icon_type"], accent)

    # Escape descriptions & tags
    desc1 = p["desc_1"].replace("&", "&amp;")
    desc2 = p["desc_2"].replace("&", "&amp;")
    category = p["category"].replace("&", "&amp;")
    metric = p["metric"].replace("&", "&amp;")
    metric_detail = p["metric_detail"].replace("&", "&amp;")

    # Tags layout (4 tags, neatly spaced across 430px width)
    # Available width: 440px - 44px margins = 396px
    tag_elements = []
    x_pos = 22
    for t in p["tags"]:
        escaped_t = t.replace("&", "&amp;")
        # approximate width: 8.5px per char + 16px padding
        tag_w = max(55, len(t) * 6.5 + 16)
        tag_elements.append(f'''
      <g transform="translate({x_pos}, 150)">
        <rect x="0" y="0" width="{tag_w:.1f}" height="22" rx="6" fill="#182333" stroke="rgba(255,255,255,0.08)" stroke-width="1" />
        <circle cx="8" cy="11" r="2.5" fill="{accent}" />
        <text x="16" y="14.5" font-family="'JetBrains Mono', monospace" font-size="9" fill="#CBD5E1" font-weight="500">{escaped_t}</text>
      </g>''')
        x_pos += tag_w + 8

    tags_markup = "".join(tag_elements)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 185" width="100%" height="185">
  <defs>
    <linearGradient id="cardBg_dark_{p['num']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#121A24" />
      <stop offset="100%" stop-color="#162231" />
    </linearGradient>
    <radialGradient id="cardGlow_dark_{p['num']}" cx="85%" cy="20%" r="50%">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0.14" />
      <stop offset="100%" stop-color="#121A24" stop-opacity="0" />
    </radialGradient>
    <pattern id="cardGrid_{p['num']}" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="rgba(255,255,255,0.02)" stroke-width="1" />
    </pattern>
  </defs>

  <!-- Card Surface -->
  <rect x="1.5" y="1.5" width="437" height="182" rx="14" fill="url(#cardBg_dark_{p['num']})" stroke="#1D2A3B" stroke-width="1.5" />
  <rect x="1.5" y="1.5" width="437" height="182" rx="14" fill="url(#cardGrid_{p['num']})" />
  <rect x="1.5" y="1.5" width="437" height="182" rx="14" fill="url(#cardGlow_dark_{p['num']})" />
  
  <!-- Glowing Top Accent Line -->
  <line x1="22" y1="1.5" x2="140" y2="1.5" stroke="{accent}" stroke-width="3" stroke-linecap="round" />

  <!-- Top Category & Metric Badge -->
  <g transform="translate(22, 22)">
    <text font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="{accent}" letter-spacing="0.8px">{category}</text>
  </g>
  <g transform="translate(418, 22)">
    <rect x="-115" y="-12" width="115" height="19" rx="9" fill="#182333" stroke="rgba(255,255,255,0.1)" stroke-width="1" />
    <circle cx="-105" cy="-2.5" r="3" fill="{accent}" />
    <text x="-95" y="1" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="600" fill="#F3F6F9">{metric}</text>
  </g>

  <!-- Title & Domain Icon -->
  <g transform="translate(22, 58)">
    <text x="0" y="0" font-family="'Plus Jakarta Sans', -apple-system, system-ui, sans-serif" font-size="18" font-weight="800" fill="#F3F6F9" letter-spacing="-0.3px">{p['title']}</text>
    <g transform="translate(372, -18)">
      {icon_svg}
    </g>
  </g>

  <!-- Subtitle / Metric Detail -->
  <g transform="translate(22, 76)">
    <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600" fill="{accent}">✦ {metric_detail}</text>
  </g>

  <!-- Description -->
  <g transform="translate(22, 98)">
    <text x="0" y="0" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="12" font-weight="400" fill="#CBD5E1">{desc1}</text>
    <text x="0" y="18" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="12" font-weight="400" fill="#94A3B8">{desc2}</text>
  </g>

  <!-- Tech Stack Tags -->
  {tags_markup}
</svg>'''

def generate_card_light(p):
    accent_l = p["accent_l"]
    icon_svg = get_svg_icon(p["icon_type"], accent_l)

    desc1 = p["desc_1"].replace("&", "&amp;")
    desc2 = p["desc_2"].replace("&", "&amp;")
    category = p["category_l"].replace("&", "&amp;")
    metric = p["metric"].replace("&", "&amp;")
    metric_detail = p["metric_detail"].replace("&", "&amp;")

    tag_elements = []
    x_pos = 22
    for t in p["tags"]:
        escaped_t = t.replace("&", "&amp;")
        tag_w = max(55, len(t) * 6.5 + 16)
        tag_elements.append(f'''
      <g transform="translate({x_pos}, 150)">
        <rect x="0" y="0" width="{tag_w:.1f}" height="22" rx="6" fill="#F7F3EB" stroke="#E2E8F0" stroke-width="1" />
        <circle cx="8" cy="11" r="2.5" fill="{accent_l}" />
        <text x="16" y="14.5" font-family="'JetBrains Mono', monospace" font-size="9" fill="#3B4654" font-weight="600">{escaped_t}</text>
      </g>''')
        x_pos += tag_w + 8

    tags_markup = "".join(tag_elements)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 185" width="100%" height="185">
  <defs>
    <linearGradient id="cardBg_light_{p['num']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#FBF9F4" />
    </linearGradient>
    <radialGradient id="cardGlow_light_{p['num']}" cx="85%" cy="20%" r="50%">
      <stop offset="0%" stop-color="{accent_l}" stop-opacity="0.10" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0" />
    </radialGradient>
  </defs>

  <!-- Card Surface -->
  <rect x="1.5" y="1.5" width="437" height="182" rx="14" fill="url(#cardBg_light_{p['num']})" stroke="#CCD2DA" stroke-width="1.5" />
  <rect x="1.5" y="1.5" width="437" height="182" rx="14" fill="url(#cardGlow_light_{p['num']})" />
  
  <!-- Glowing Top Accent Line -->
  <line x1="22" y1="1.5" x2="140" y2="1.5" stroke="{accent_l}" stroke-width="3" stroke-linecap="round" />

  <!-- Top Category & Metric Badge -->
  <g transform="translate(22, 22)">
    <text font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="{accent_l}" letter-spacing="0.8px">{category}</text>
  </g>
  <g transform="translate(418, 22)">
    <rect x="-115" y="-12" width="115" height="19" rx="9" fill="#F3ECE1" stroke="#E2E8F0" stroke-width="1" />
    <circle cx="-105" cy="-2.5" r="3" fill="{accent_l}" />
    <text x="-95" y="1" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="600" fill="#1C232B">{metric}</text>
  </g>

  <!-- Title & Domain Icon -->
  <g transform="translate(22, 58)">
    <text x="0" y="0" font-family="'Plus Jakarta Sans', -apple-system, system-ui, sans-serif" font-size="18" font-weight="800" fill="#1C232B" letter-spacing="-0.3px">{p['title']}</text>
    <g transform="translate(372, -18)">
      {icon_svg}
    </g>
  </g>

  <!-- Subtitle / Metric Detail -->
  <g transform="translate(22, 76)">
    <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600" fill="{accent_l}">✦ {metric_detail}</text>
  </g>

  <!-- Description -->
  <g transform="translate(22, 98)">
    <text x="0" y="0" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="12" font-weight="400" fill="#3B4654">{desc1}</text>
    <text x="0" y="18" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="12" font-weight="400" fill="#5A6A80">{desc2}</text>
  </g>

  <!-- Tech Stack Tags -->
  {tags_markup}
</svg>'''


# -------------------------------------------------------------
# 4. SLEEK DIVIDER (Dark & Light)
# -------------------------------------------------------------
def get_divider_dark():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 26" width="100%" height="26">
  <defs>
    <linearGradient id="divGradDark" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#151F2C" stop-opacity="0" />
      <stop offset="25%" stop-color="#1D2A3B" />
      <stop offset="50%" stop-color="#F4A261" stop-opacity="0.8" />
      <stop offset="75%" stop-color="#5EBAA0" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#151F2C" stop-opacity="0" />
    </linearGradient>
  </defs>
  <line x1="40" y1="13" x2="880" y2="13" stroke="url(#divGradDark)" stroke-width="1.4" stroke-linecap="round" />
  <circle cx="460" cy="13" r="3.5" fill="#F4A261" />
  <circle cx="460" cy="13" r="1.5" fill="#FFFFFF" />
</svg>'''

def get_divider_light():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 26" width="100%" height="26">
  <defs>
    <linearGradient id="divGradLight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#CCD2DA" stop-opacity="0" />
      <stop offset="25%" stop-color="#CCD2DA" />
      <stop offset="50%" stop-color="#B84E26" stop-opacity="0.7" />
      <stop offset="75%" stop-color="#2A6647" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#CCD2DA" stop-opacity="0" />
    </linearGradient>
  </defs>
  <line x1="40" y1="13" x2="880" y2="13" stroke="url(#divGradLight)" stroke-width="1.4" stroke-linecap="round" />
  <circle cx="460" cy="13" r="3.5" fill="#B84E26" />
  <circle cx="460" cy="13" r="1.5" fill="#FFFFFF" />
</svg>'''


# -------------------------------------------------------------
# MAIN EXECUTION
# -------------------------------------------------------------
def main():
    files = {
        "header-dark.svg": get_header_dark(),
        "header-light.svg": get_header_light(),
        "defense-in-depth-dark.svg": get_defense_architecture_dark(),
        "defense-in-depth-light.svg": get_defense_architecture_light(),
        "divider-dark.svg": get_divider_dark(),
        "divider-light.svg": get_divider_light(),
    }

    # Add the 6 project cards (dark and light)
    for p in PROJECTS:
        filename_dark = f"card-{p['num']}-{p['name']}-dark.svg"
        filename_light = f"card-{p['num']}-{p['name']}-light.svg"
        files[filename_dark] = generate_card_dark(p)
        files[filename_light] = generate_card_light(p)

    # Write files and validate XML
    success = True
    for fname, content in files.items():
        fpath = os.path.join(ASSETS_DIR, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        
        # XML validation check
        try:
            ET.fromstring(content)
            print(f"[VALID XML] {fname}")
        except Exception as e:
            print(f"[XML ERROR] {fname}: {e}")
            success = False

    if success:
        print("\nAll 18 profile SVG assets generated and 100% XML validated successfully!")
    else:
        print("\nSome assets failed validation.")

if __name__ == "__main__":
    main()
