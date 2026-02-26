"""
==============================================================
 IA & Performance – Analyse de Marché Concurrentiel
 Solutions de Data-Tracking dans la Rééducation Sportive
==============================================================
Auteur  : [Ton Nom]
Version : 1.0.0
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# CONFIGURATION VISUELLE
# ─────────────────────────────────────────────

BG_COLOR    = "#0D1117"
PANEL_COLOR = "#161B22"
GRID_COLOR  = "#21262D"
TEXT_COLOR  = "#E6EDF3"
MUTED_COLOR = "#8B949E"

COULEURS = {
    "Catapult"           : "#E74C3C",
    "Zone7"              : "#F39C12",
    "SkillSocks"         : "#9B59B6",
    "Genouillère IA"     : "#3498DB",
}

plt.rcParams.update({
    "figure.facecolor" : BG_COLOR,
    "axes.facecolor"   : PANEL_COLOR,
    "axes.edgecolor"   : GRID_COLOR,
    "axes.labelcolor"  : TEXT_COLOR,
    "xtick.color"      : TEXT_COLOR,
    "ytick.color"      : TEXT_COLOR,
    "text.color"       : TEXT_COLOR,
    "grid.color"       : GRID_COLOR,
    "grid.linewidth"   : 0.6,
    "font.family"      : "DejaVu Sans",
})

# ─────────────────────────────────────────────
# 1. DONNÉES
# ─────────────────────────────────────────────

# Critères d'évaluation (score /10)
criteres = [
    "Temps réel",
    "Feedback\nathlète",
    "Précision\nbiomécanique",
    "Accessibilité\nterrain",
    "IA prédictive",
    "Facilité\nd'usage",
]

scores = {
    "Catapult"       : [4, 2, 7, 6, 5, 5],
    "Zone7"          : [5, 3, 5, 4, 9, 6],
    "SkillSocks"     : [7, 4, 8, 4, 3, 6],
    "Genouillère IA" : [10, 9, 9, 9, 8, 8],
}

df_scores = pd.DataFrame(scores, index=criteres)

# Données marché
marche_annees  = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028]
marche_taille  = [1.8,  2.2,  2.7,  3.3,  4.1,  5.0,  6.1,  7.4,  9.0]   # Md USD
marche_cagr    = 22.4   # % croissance annuelle estimée

# Positionnement marché (axes : Feedback Temps Réel vs Accessibilité terrain)
positionnement = {
    "Catapult"       : {"x": 3.5, "y": 6.0, "taille": 420},
    "Zone7"          : {"x": 4.5, "y": 4.5, "taille": 280},
    "SkillSocks"     : {"x": 7.0, "y": 4.0, "taille": 160},
    "Genouillère IA" : {"x": 9.5, "y": 9.0, "taille": 220},
}

# Tableau comparatif
tableau_data = {
    "Solution"          : ["Catapult", "Zone7", "SkillSocks", "Genouillère IA (concept)"],
    "Type"              : ["Wearable GPS/IMU", "Logiciel IA", "Capteur pression", "Wearable IA temps réel"],
    "Feedback temps réel": ["❌ Post-séance", "❌ Post-séance", "⚠️ Partiel", "✅ Instantané"],
    "Alerte athlète"    : ["❌", "❌", "⚠️ Basique", "✅ Haptique + sonore"],
    "Biomécanique LCA"  : ["⚠️ Globale", "⚠️ Indirecte", "✅ Directe", "✅ Spécifique LCA"],
    "Prix estimé"       : ["~15 000€/an", "~8 000€/an", "~500€", "~800-1 200€ (cible)"],
    "Cible principale"  : ["Clubs pro", "Clubs pro", "Kiné/labo", "Kiné + Athlète"],
}
df_tableau = pd.DataFrame(tableau_data)

# ─────────────────────────────────────────────
# 2. FIGURE PRINCIPALE
# ─────────────────────────────────────────────

fig = plt.figure(figsize=(20, 22), facecolor=BG_COLOR)
fig.suptitle(
    "Analyse de Marché — Solutions IA & Data-Tracking\ndans la Rééducation Sportive de Haut Niveau",
    fontsize=17, fontweight="bold", color=TEXT_COLOR, y=0.98
)

gs = gridspec.GridSpec(3, 2, figure=fig, hspace=0.5, wspace=0.35,
                       top=0.94, bottom=0.04)

# ══════════════════════════════════════════════
# GRAPHIQUE 1 — RADAR (forces / faiblesses)
# ══════════════════════════════════════════════

ax_radar = fig.add_subplot(gs[0, 0], polar=True)

N = len(criteres)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

ax_radar.set_facecolor(PANEL_COLOR)
ax_radar.set_theta_offset(np.pi / 2)
ax_radar.set_theta_direction(-1)
ax_radar.set_rlabel_position(30)

for r in [2, 4, 6, 8, 10]:
    ax_radar.plot(angles, [r] * (N + 1), color=GRID_COLOR, linewidth=0.5, zorder=0)

ax_radar.set_xticks(angles[:-1])
ax_radar.set_xticklabels(criteres, size=8.5, color=TEXT_COLOR)
ax_radar.set_yticks([2, 4, 6, 8, 10])
ax_radar.set_yticklabels(["2", "4", "6", "8", "10"], size=7, color=MUTED_COLOR)
ax_radar.set_ylim(0, 10)
ax_radar.spines["polar"].set_color(GRID_COLOR)

for nom, vals in scores.items():
    v = vals + vals[:1]
    alpha = 0.55 if nom != "Genouillère IA" else 0.85
    lw    = 1.5  if nom != "Genouillère IA" else 2.5
    ls    = "--" if nom != "Genouillère IA" else "-"
    ax_radar.plot(angles, v, color=COULEURS[nom], linewidth=lw, linestyle=ls,
                  label=nom, alpha=alpha)
    ax_radar.fill(angles, v, color=COULEURS[nom], alpha=0.05 if nom != "Genouillère IA" else 0.12)

ax_radar.set_title("Forces & Faiblesses par Critère\n(score /10)", size=11,
                   color=TEXT_COLOR, pad=20, fontweight="bold")
ax_radar.legend(loc="upper right", bbox_to_anchor=(1.35, 1.15),
                fontsize=8.5, framealpha=0.15)

# ══════════════════════════════════════════════
# GRAPHIQUE 2 — MATRICE DE POSITIONNEMENT
# ══════════════════════════════════════════════

ax_map = fig.add_subplot(gs[0, 1])

ax_map.set_facecolor(PANEL_COLOR)

# Quadrants
ax_map.axhline(5, color=GRID_COLOR, linewidth=0.8, linestyle="--")
ax_map.axvline(5, color=GRID_COLOR, linewidth=0.8, linestyle="--")
ax_map.text(2.5, 9.5, "Accessible\nmais peu réactif",  fontsize=7.5, color=MUTED_COLOR, ha="center")
ax_map.text(7.5, 9.5, "✅ Zone idéale",                fontsize=7.5, color="#2ECC71",   ha="center")
ax_map.text(2.5, 1.0, "Peu réactif\n& peu accessible", fontsize=7.5, color=MUTED_COLOR, ha="center")
ax_map.text(7.5, 1.0, "Réactif mais\nusage limité",    fontsize=7.5, color=MUTED_COLOR, ha="center")

for nom, pos in positionnement.items():
    lw = 2.5 if nom == "Genouillère IA" else 1.2
    ec = "white" if nom == "Genouillère IA" else COULEURS[nom]
    ax_map.scatter(pos["x"], pos["y"], s=pos["taille"],
                   color=COULEURS[nom], edgecolors=ec,
                   linewidths=lw, zorder=5, alpha=0.85)
    offset_y = 0.6 if nom != "Zone7" else -0.8
    ax_map.annotate(nom, (pos["x"], pos["y"] + offset_y),
                    ha="center", fontsize=9, color=COULEURS[nom], fontweight="bold")

ax_map.set_xlim(0, 10.5)
ax_map.set_ylim(0, 10.5)
ax_map.set_xlabel("Feedback en Temps Réel →", fontsize=9)
ax_map.set_ylabel("Accessibilité Terrain →", fontsize=9)
ax_map.set_title("Positionnement Concurrentiel\n(taille = part de marché estimée)", size=11,
                 color=TEXT_COLOR, pad=10, fontweight="bold")
ax_map.grid(True, alpha=0.3)

# ══════════════════════════════════════════════
# GRAPHIQUE 3 — TAILLE DU MARCHÉ
# ══════════════════════════════════════════════

ax_mkt = fig.add_subplot(gs[1, :])

bars = ax_mkt.bar(marche_annees[:5], marche_taille[:5],
                  color="#3498DB", alpha=0.7, width=0.6, label="Données réelles (estimées)")
bars_proj = ax_mkt.bar(marche_annees[4:], marche_taille[4:],
                       color="#3498DB", alpha=0.3, width=0.6,
                       hatch="//", label="Projection")

# Courbe de tendance
ax_mkt.plot(marche_annees, marche_taille, "o-", color="#2ECC71",
            linewidth=2.5, markersize=6, zorder=5)

for i, (an, val) in enumerate(zip(marche_annees, marche_taille)):
    ax_mkt.text(an, val + 0.15, f"{val}Md$", ha="center", fontsize=8.5,
                color=TEXT_COLOR, fontweight="bold")

ax_mkt.axvline(2024.5, color=MUTED_COLOR, linestyle=":", linewidth=1.2)
ax_mkt.text(2024.6, 8.2, "Projections →", fontsize=8.5, color=MUTED_COLOR)

ax_mkt.annotate(f"CAGR : +{marche_cagr}%/an",
                xy=(2026, 6.1), xytext=(2022.5, 7.5),
                arrowprops=dict(arrowstyle="->", color="#2ECC71", lw=1.5),
                fontsize=10, color="#2ECC71", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.4", fc=PANEL_COLOR, ec="#2ECC71", alpha=0.9))

ax_mkt.set_xlabel("Année", fontsize=10)
ax_mkt.set_ylabel("Taille du marché (Milliards USD)", fontsize=10)
ax_mkt.set_title("Marché Mondial — Sports Tech & IA Rééducation (2020–2028)\nSource : estimations sectorielles Grand View Research / MarketsandMarkets",
                 size=11, color=TEXT_COLOR, pad=10, fontweight="bold")
ax_mkt.legend(fontsize=9, framealpha=0.2)
ax_mkt.set_ylim(0, 10.5)
ax_mkt.grid(True, axis="y", alpha=0.4)

# ══════════════════════════════════════════════
# GRAPHIQUE 4 — TABLEAU COMPARATIF
# ══════════════════════════════════════════════

ax_tab = fig.add_subplot(gs[2, :])
ax_tab.axis("off")
ax_tab.set_title("Tableau Comparatif des Solutions",
                 size=12, color=TEXT_COLOR, pad=15, fontweight="bold", loc="left")

cols  = list(df_tableau.columns)
vals  = df_tableau.values.tolist()

table = ax_tab.table(
    cellText=vals,
    colLabels=cols,
    cellLoc="center",
    loc="center",
    bbox=[0, 0, 1, 0.92]
)

table.auto_set_font_size(False)
table.set_fontsize(9)

# Style en-tête
for j in range(len(cols)):
    cell = table[0, j]
    cell.set_facecolor("#1F2937")
    cell.set_text_props(color=TEXT_COLOR, fontweight="bold")
    cell.set_edgecolor(GRID_COLOR)

# Style lignes
row_colors = [COULEURS["Catapult"], COULEURS["Zone7"],
              COULEURS["SkillSocks"], COULEURS["Genouillère IA"]]

for i, row_vals in enumerate(vals):
    for j in range(len(cols)):
        cell = table[i + 1, j]
        cell.set_facecolor(PANEL_COLOR)
        cell.set_edgecolor(GRID_COLOR)
        cell.set_text_props(color=TEXT_COLOR)

    # Couleur de la cellule "Solution"
    table[i + 1, 0].set_facecolor(row_colors[i])
    table[i + 1, 0].set_text_props(color="white", fontweight="bold")

    # Mettre en avant la ligne Genouillère IA
    if i == 3:
        for j in range(len(cols)):
            table[i + 1, j].set_facecolor("#1A2744")
            table[i + 1, j].set_text_props(color="#3498DB", fontweight="bold")
        table[i + 1, 0].set_facecolor(COULEURS["Genouillère IA"])
        table[i + 1, 0].set_text_props(color="white", fontweight="bold")

# ─────────────────────────────────────────────
# EXPORT
# ─────────────────────────────────────────────

plt.savefig("outputs/analyse_marche_concurrentiel.png",
            dpi=180, bbox_inches="tight", facecolor=BG_COLOR)
print("✅  Graphique exporté → outputs/analyse_marche_concurrentiel.png")
plt.close()

# ─────────────────────────────────────────────
# RAPPORT SYNTHÉTIQUE
# ─────────────────────────────────────────────

rapport = f"""
╔══════════════════════════════════════════════════════════════╗
║         ANALYSE DE MARCHÉ — SYNTHÈSE                       ║
╠══════════════════════════════════════════════════════════════╣
║  Marché Sports Tech & IA Rééducation                       ║
║    → Taille 2024       : ~4.1 Milliards USD                ║
║    → Projection 2028   : ~9.0 Milliards USD                ║
║    → CAGR              : +{marche_cagr}% / an                      ║
╠══════════════════════════════════════════════════════════════╣
║  Scores moyens par solution (sur 6 critères /10)           ║
║    → Catapult           : {np.mean(scores["Catapult"]):.1f} / 10                      ║
║    → Zone7              : {np.mean(scores["Zone7"]):.1f} / 10                      ║
║    → SkillSocks         : {np.mean(scores["SkillSocks"]):.1f} / 10                      ║
║    → Genouillère IA     : {np.mean(scores["Genouillère IA"]):.1f} / 10                      ║
╠══════════════════════════════════════════════════════════════╣
║  Opportunité identifiée                                     ║
║  Aucune solution actuelle ne combine :                      ║
║    ✅ Feedback temps réel                                   ║
║    ✅ Correction biomécanique spécifique LCA               ║
║    ✅ Accessibilité terrain (prix < 1 500€)                ║
╚══════════════════════════════════════════════════════════════╝
"""
print(rapport)
with open("outputs/rapport_marche.txt", "w", encoding="utf-8") as f:
    f.write(rapport)
print("✅  Rapport exporté → outputs/rapport_marche.txt")
