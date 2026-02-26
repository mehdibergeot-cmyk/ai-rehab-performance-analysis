"""
==============================================================
 IA & Performance – Optimisation de la Rééducation LCA
 Analyse comparative : Protocole standard vs Suivi IA
==============================================================
Auteur  : [Ton Nom]
Version : 1.0.0
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
from matplotlib.lines import Line2D
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# 1. GÉNÉRATION DES DONNÉES SYNTHÉTIQUES
# ─────────────────────────────────────────────

np.random.seed(42)
SEMAINES = np.arange(0, 25)

def profil_pro(semaines):
    """Puissance explosive de référence d'un joueur pro (W/kg)."""
    baseline = 28.0
    return baseline + np.random.normal(0, 0.3, len(semaines))

def protocole_standard(semaines):
    """
    Rééducation classique basée sur des délais temporels fixes.
    Progression lente, plateau, risque de rechute vers S16.
    """
    progress = 12 + 14 * (1 - np.exp(-semaines / 9))
    noise = np.random.normal(0, 0.6, len(semaines))
    # Simulation d'une rechute légère autour de S16
    rechute = np.where((semaines >= 15) & (semaines <= 17), -2.5, 0)
    return np.clip(progress + noise + rechute, 10, 30)

def protocole_ia(semaines):
    """
    Rééducation guidée par IA (charge adaptative, bio-feedback).
    Convergence plus rapide et plus stable vers le niveau pro.
    """
    progress = 12 + 16 * (1 - np.exp(-semaines / 6.5))
    noise = np.random.normal(0, 0.35, len(semaines))
    return np.clip(progress + noise, 10, 30)

def charge_semaine(semaines, protocole="ia"):
    """Charge d'entraînement hebdomadaire (ACWR – ratio charge aiguë/chronique)."""
    if protocole == "ia":
        base = 0.6 + 0.8 * (1 - np.exp(-semaines / 5))
        return np.clip(base + np.random.normal(0, 0.05, len(semaines)), 0.5, 1.3)
    else:
        base = 0.6 + 0.9 * (1 - np.exp(-semaines / 8))
        spike = np.where((semaines >= 14) & (semaines <= 16), 0.35, 0)
        return np.clip(base + spike + np.random.normal(0, 0.08, len(semaines)), 0.5, 1.8)

def asymetrie_membre(semaines, protocole="ia"):
    """Asymétrie membre sain vs blessé (%). Idéal < 10%."""
    if protocole == "ia":
        asym = 35 * np.exp(-semaines / 7) + np.random.normal(0, 1, len(semaines))
    else:
        asym = 40 * np.exp(-semaines / 11) + np.random.normal(0, 2, len(semaines))
    return np.clip(asym, 0, 45)

# Construction du DataFrame principal
df = pd.DataFrame({
    "semaine"           : SEMAINES,
    "pro_baseline"      : profil_pro(SEMAINES),
    "standard_power"    : protocole_standard(SEMAINES),
    "ia_power"          : protocole_ia(SEMAINES),
    "acwr_standard"     : charge_semaine(SEMAINES, "standard"),
    "acwr_ia"           : charge_semaine(SEMAINES, "ia"),
    "asym_standard"     : asymetrie_membre(SEMAINES, "standard"),
    "asym_ia"           : asymetrie_membre(SEMAINES, "ia"),
})

df.to_csv("data/rehab_data_synthetique.csv", index=False)
print("✅  Dataset synthétique exporté → data/rehab_data_synthetique.csv")

# ─────────────────────────────────────────────
# 2. VISUALISATION PRINCIPALE (3 graphiques)
# ─────────────────────────────────────────────

COULEUR_PRO      = "#2ECC71"
COULEUR_IA       = "#3498DB"
COULEUR_STD      = "#E74C3C"
COULEUR_DANGER   = "#F39C12"
BG_COLOR         = "#0D1117"
GRID_COLOR       = "#21262D"
TEXT_COLOR       = "#E6EDF3"

plt.rcParams.update({
    "figure.facecolor"  : BG_COLOR,
    "axes.facecolor"    : "#161B22",
    "axes.edgecolor"    : GRID_COLOR,
    "axes.labelcolor"   : TEXT_COLOR,
    "xtick.color"       : TEXT_COLOR,
    "ytick.color"       : TEXT_COLOR,
    "text.color"        : TEXT_COLOR,
    "grid.color"        : GRID_COLOR,
    "grid.linewidth"    : 0.6,
    "font.family"       : "DejaVu Sans",
})

fig = plt.figure(figsize=(18, 12), facecolor=BG_COLOR)
fig.suptitle(
    "IA & Performance — Optimisation de la Rééducation LCA\nAnalyse comparative : Protocole standard vs Suivi IA",
    fontsize=16, fontweight="bold", color=TEXT_COLOR, y=0.98
)

gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.45, wspace=0.35)

# ── Graphique 1 : Puissance explosive ──
ax1 = fig.add_subplot(gs[0, :])  # pleine largeur

ax1.fill_between(df.semaine, df.pro_baseline - 1.5, df.pro_baseline + 1.5,
                 alpha=0.12, color=COULEUR_PRO, label="_nolegend_")
ax1.plot(df.semaine, df.pro_baseline, "--", color=COULEUR_PRO,
         linewidth=1.8, alpha=0.7, label="Niveau Pro (référence)")

ax1.plot(df.semaine, df.standard_power, "-o", color=COULEUR_STD,
         linewidth=2, markersize=4, label="Protocole standard")
ax1.plot(df.semaine, df.ia_power, "-o", color=COULEUR_IA,
         linewidth=2.5, markersize=4, label="Protocole IA")

# Zone de danger (rechute)
ax1.axvspan(14.5, 17.5, alpha=0.08, color=COULEUR_DANGER)
ax1.annotate("⚠ Risque rechute\n(protocole standard)",
             xy=(16, 20), fontsize=8.5, color=COULEUR_DANGER,
             ha="center",
             bbox=dict(boxstyle="round,pad=0.3", fc="#161B22", ec=COULEUR_DANGER, alpha=0.8))

# Zone "Return to Play"
rtp_semaine = 19
ax1.axvline(x=rtp_semaine, color=COULEUR_IA, linestyle=":", linewidth=1.5, alpha=0.7)
ax1.annotate(f"Return to Play (IA) ≈ S{rtp_semaine}",
             xy=(rtp_semaine + 0.3, 14), fontsize=8.5, color=COULEUR_IA)

ax1.set_xlabel("Semaine post-opératoire", fontsize=10)
ax1.set_ylabel("Puissance explosive (W/kg)", fontsize=10)
ax1.set_title("Évolution de la Puissance Explosive au cours de la Rééducation", fontsize=12, pad=10)
ax1.legend(fontsize=9, framealpha=0.2, loc="lower right")
ax1.grid(True, axis="both")
ax1.set_xlim(0, 24)
ax1.set_ylim(8, 32)

# ── Graphique 2 : Ratio de charge (ACWR) ──
ax2 = fig.add_subplot(gs[1, 0])

ax2.fill_between(df.semaine, 0.8, 1.3, alpha=0.08, color=COULEUR_PRO,
                 label="Zone optimale (0.8–1.3)")
ax2.plot(df.semaine, df.acwr_standard, color=COULEUR_STD,
         linewidth=2, label="Standard")
ax2.plot(df.semaine, df.acwr_ia, color=COULEUR_IA,
         linewidth=2, label="IA")
ax2.axhline(1.3, color=COULEUR_DANGER, linestyle="--", linewidth=1, alpha=0.6)
ax2.text(0.5, 1.32, "Seuil surcharge", color=COULEUR_DANGER, fontsize=8, alpha=0.8)

ax2.set_xlabel("Semaine post-opératoire", fontsize=10)
ax2.set_ylabel("ACWR (Ratio Charge Aiguë/Chronique)", fontsize=9)
ax2.set_title("Gestion de la Charge d'Entraînement", fontsize=11, pad=8)
ax2.legend(fontsize=8.5, framealpha=0.2)
ax2.grid(True)
ax2.set_xlim(0, 24)
ax2.set_ylim(0.4, 2.0)

# ── Graphique 3 : Asymétrie membres ──
ax3 = fig.add_subplot(gs[1, 1])

ax3.fill_between(df.semaine, 0, 10, alpha=0.08, color=COULEUR_PRO,
                 label="Zone cible (<10%)")
ax3.plot(df.semaine, df.asym_standard, color=COULEUR_STD,
         linewidth=2, label="Standard")
ax3.plot(df.semaine, df.asym_ia, color=COULEUR_IA,
         linewidth=2, label="IA")
ax3.axhline(10, color=COULEUR_PRO, linestyle="--", linewidth=1, alpha=0.6)
ax3.text(0.5, 10.5, "Seuil clinique (10%)", color=COULEUR_PRO, fontsize=8, alpha=0.8)

# Annoter la semaine de passage sous 10% pour le protocole IA
semaine_ok_ia  = df[df.asym_ia  < 10].semaine.min()
semaine_ok_std = df[df.asym_std  < 10].semaine.min() if "asym_std" in df else None
ax3.annotate(f"IA : < 10% à S{semaine_ok_ia}",
             xy=(semaine_ok_ia, 10), xytext=(semaine_ok_ia + 1, 16),
             arrowprops=dict(arrowstyle="->", color=COULEUR_IA, lw=1.2),
             fontsize=8, color=COULEUR_IA)

ax3.set_xlabel("Semaine post-opératoire", fontsize=10)
ax3.set_ylabel("Asymétrie membre sain/blessé (%)", fontsize=9)
ax3.set_title("Réduction des Asymétries Biomécaniques", fontsize=11, pad=8)
ax3.legend(fontsize=8.5, framealpha=0.2)
ax3.grid(True)
ax3.set_xlim(0, 24)
ax3.set_ylim(0, 48)

plt.savefig("outputs/comparaison_reeducation.png",
            dpi=180, bbox_inches="tight", facecolor=BG_COLOR)
print("✅  Graphique exporté → outputs/comparaison_reeducation.png")
plt.close()

# ─────────────────────────────────────────────
# 3. RAPPORT STATISTIQUE SYNTHÉTIQUE
# ─────────────────────────────────────────────

semaine_rtp_ia  = int(df[df.ia_power >= 26].semaine.min())
semaine_rtp_std = int(df[df.standard_power >= 26].semaine.min()) if df[df.standard_power >= 26].shape[0] > 0 else ">24"
gain_semaines   = semaine_rtp_std - semaine_rtp_ia if isinstance(semaine_rtp_std, int) else "N/A"

asym_finale_ia  = round(df.asym_ia.iloc[-1], 1)
asym_finale_std = round(df.asym_standard.iloc[-1], 1)

acwr_max_ia  = round(df.acwr_ia.max(), 2)
acwr_max_std = round(df.acwr_standard.max(), 2)

rapport = f"""
╔══════════════════════════════════════════════════════════════╗
║        RAPPORT STATISTIQUE — RÉÉDUCATION LCA               ║
╠══════════════════════════════════════════════════════════════╣
║  Return to Play (niveau ≥ 26 W/kg)                         ║
║    → Protocole IA       : Semaine {semaine_rtp_ia:<5}                      ║
║    → Protocole standard : Semaine {semaine_rtp_std:<5}                      ║
║    → Gain estimé        : {gain_semaines} semaines                     ║
╠══════════════════════════════════════════════════════════════╣
║  Asymétrie finale (S24)                                     ║
║    → Protocole IA       : {asym_finale_ia:>5} %                         ║
║    → Protocole standard : {asym_finale_std:>5} %                         ║
╠══════════════════════════════════════════════════════════════╣
║  Pic de charge (ACWR max)                                   ║
║    → Protocole IA       : {acwr_max_ia:<5}  (zone sûre < 1.3)         ║
║    → Protocole standard : {acwr_max_std:<5}  (surcharge détectée)      ║
╚══════════════════════════════════════════════════════════════╝
"""
print(rapport)

with open("outputs/rapport_statistique.txt", "w", encoding="utf-8") as f:
    f.write(rapport)
print("✅  Rapport exporté → outputs/rapport_statistique.txt")
