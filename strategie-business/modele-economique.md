# 💰 Stratégie Commerciale & Modèle Économique
## Lancement de la Genouillère Connectée **Active-Sense**

> Transformer un concept MedTech en leader du marché de la réathlétisation d'élite — de la R&D au premier euro de revenus récurrents.

---

## 1. Business Model — Hardware-as-a-Service (HaaS)

La stratégie repose sur un modèle hybride : **vente d'équipement premium + revenus SaaS récurrents**. Trois segments adressés simultanément pour maximiser la couverture marché.

| Segment | Modèle | Offre | Prix Cible |
| :--- | :--- | :--- | ---: |
| 🏟️ **B2B Élite** — Clubs Pro, Fédérations | Vente + Abonnement SaaS | Genouillère + Dashboard Staff Médical (données équipe) | 1 500€/unité + 5 000€/an |
| 🏥 **B2B Kiné** — Cliniques, Cabinets | Location / Leasing | Matériel mis à disposition, facturable comme acte technique | 150€/mois/unité |
| 🧑‍⚕️ **B2C** — Sportif individuel post-op | Location courte durée | Location sur la durée critique de rééducation (3–6 mois) + app mobile | 80€/semaine |

**Pourquoi ce modèle ?**
Le HaaS génère de la **prévisibilité financière** (ARR stable) tout en abaissant la barrière à l'entrée pour les kinés indépendants qui ne peuvent pas investir 1 500€ en une seule fois.

---

## 2. Structure des Coûts

### 🔵 Capex — Investissements Initiaux

| Poste | Description | Priorité |
| :--- | :--- | :---: |
| **R&D & Prototypage** | IA embarquée (Edge Computing), capteurs IMU 1000Hz, itérations textiles | 🔴 Critique |
| **Certification Médicale** | ISO 13485 + Marquage CE — dossier technique + tests cliniques | 🔴 Critique |
| **Propriété Intellectuelle** | Brevet algorithme bio-feedback haptique + protection marque | 🟠 Élevée |

> ⚠️ Le Marquage CE n'est pas optionnel —  pour accéder au marché médical européen.

### 🟢 Opex — Coûts Annuels (Phase de Lancement)

- **Masse salariale :** Ingénieurs IA/Hardware, Biomécanicien référent, Technico-Commerciaux Santé
- **Production & Logistique :** COGS (fabrication), stockage, expédition
- **Marketing B2B :** Salons (Medica, congrès orthopédie), démos en clubs, comptes stratégiques

---

## 3. Financement — Levée de Fonds Seed

**Besoin total estimé : 1,2 M€** pour couvrir les Capex + 18 mois d'Opex.

```
┌─────────────────────────────────────────────────────────┐
│  Financement Public (30%)          →   360 000€         │
│  BPI France DeepTech, French Tech, Concours Innovation  │
├─────────────────────────────────────────────────────────┤
│  Levée Seed (70%)                  →   840 000€         │
│  Business Angels Santé/Sport + VCs Early-Stage          │
└─────────────────────────────────────────────────────────┘
```

**Conditions de la levée :**
- Valorisation pré-money cible : **4M€ – 6M€**
- Utilisation des fonds : finalisation Marquage CE · recrutement équipe commerciale · production des **100 premières unités pilotes**

---

## 4. Écosystème de Partenariats

Un produit MedTech ne se lance pas seul — la crédibilité clinique est un actif aussi important que le produit lui-même.

```
                    ┌──────────────────┐
                    │   Active-Sense   │
                    └────────┬─────────┘
           ┌─────────────────┼─────────────────┐
           ▼                 ▼                 ▼
   🏥 Cliniques          ⚙️ Fabricants      📦 Distributeurs
   CERS Capbreton        Textiles médicaux   Kiné / Orthopédie
   INSEP                 ISO 13485           (marché libéral)
   (validation + data)   (production)        (couverture B2B)
           │
           ▼
   👨‍⚕️ Prescripteurs Clés
   Chirurgiens orthopédiques LCA
   → Si convaincus, le patient loue la genouillère
```

---

## 5. KPIs & Objectifs de Croissance (Y1 → Y3)

| KPI | Année 1 | Année 3 | Ce que ça mesure |
| :--- | :---: | :---: | :--- |
| 📦 Unités en circulation | 50 *(pilotes)* | 1 000 | Pénétration marché |
| 💶 Revenu Récurrent (ARR) | 50k€ | 1,2 M€ | Part SaaS dans le CA |
| 🔄 Taux de fidélité B2B | — | > 90% | LTV clubs & cliniques |
| 🦵 Impact clinique | Symétrie validée à 95% | − 40% re-ruptures (prouvé) | Valeur médicale brute |

---

## 6. Mon Rôle : Technico-Commercial Santé

> En tant que futur **Technico-Commercial Santé**, mon objectif est de maximiser la **Lifetime Value (LTV)** des comptes B2B en assurant :
>
> - La **formation** des équipes médicales à l'outil
> - Le **suivi technique** post-déploiement
> - L'**évangélisation** auprès des prescripteurs clés (chirurgiens, kinés référents)
>
> Le commercial est le pont entre la technologie et l'adoption clinique réelle.

---
"""
==============================================================
 Active-Sense — Graphique J-Curve (Modèle HaaS)
 Visualisation investisseur : Hardware vs SaaS Récurrent
==============================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker

# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────

BG_COLOR    = "#0D1117"
PANEL_COLOR = "#161B22"
GRID_COLOR  = "#21262D"
TEXT_COLOR  = "#E6EDF3"
MUTED_COLOR = "#8B949E"
ROUGE       = "#E74C3C"
BLEU        = "#3498DB"
VERT        = "#2ECC71"

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
# DONNÉES
# ─────────────────────────────────────────────

trimestres     = np.linspace(0, 12, 49)   # 3 ans = 12 trimestres
labels_annuels = [f"T{int(t)}" if t % 4 == 0 else "" for t in trimestres]

# Revenus Hardware : croissance linéaire (ventes d'unités)
hardware = 5 + 8 * trimestres

# Revenus SaaS : exponentiel (chaque unité vendue ajoute un abonnement cumulatif)
saas = 2 * np.exp(0.28 * trimestres) - 2

# Coûts totaux : lourds au départ (R&D, certif), décroissants en %
couts = 80 * np.exp(-0.18 * trimestres) + 20

# Revenu total
total = hardware + saas

# Point de croisement SaaS > Hardware
idx_cross = np.argmax(saas > hardware)
t_cross   = trimestres[idx_cross]

# Point break-even (total > coûts)
idx_be = np.argmax(total > couts)
t_be   = trimestres[idx_be]

# ─────────────────────────────────────────────
# FIGURE
# ─────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(16, 9), facecolor=BG_COLOR)
ax.set_facecolor(PANEL_COLOR)

# Zone de perte (avant break-even)
ax.fill_between(trimestres, total, couts,
                where=(total < couts),
                color=ROUGE, alpha=0.07, label="_nolegend_")

# Zone de profit (après break-even)
ax.fill_between(trimestres, total, couts,
                where=(total >= couts),
                color=VERT, alpha=0.07, label="_nolegend_")

# ── Courbes principales ──
ax.plot(trimestres, couts,
        color=MUTED_COLOR, linewidth=1.8, linestyle="--",
        alpha=0.7, label="Structure de coûts totaux")

ax.plot(trimestres, hardware,
        color=ROUGE, linewidth=2.5,
        label="Revenus Hardware (ventes unités)")

ax.plot(trimestres, saas,
        color=BLEU, linewidth=3.0,
        label="Revenus SaaS récurrents (abonnements cumulés)")

ax.plot(trimestres, total,
        color=VERT, linewidth=2.0, linestyle="-.",
        alpha=0.85, label="Revenu Total combiné")

# ── Annotations clés ──

# 1. Break-even
ax.axvline(t_be, color=VERT, linewidth=1.2, linestyle=":", alpha=0.7)
ax.annotate(
    f"Break-Even\n≈ T{int(round(t_be))}",
    xy=(t_be, couts[idx_be]),
    xytext=(t_be + 0.6, couts[idx_be] + 18),
    arrowprops=dict(arrowstyle="->", color=VERT, lw=1.3),
    fontsize=9.5, color=VERT, fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.4", fc=PANEL_COLOR, ec=VERT, alpha=0.9)
)

# 2. Croisement SaaS > Hardware
ax.axvline(t_cross, color=BLEU, linewidth=1.2, linestyle=":", alpha=0.5)
ax.annotate(
    f"SaaS depasse\nle Hardware\n≈ T{int(round(t_cross))}",
    xy=(t_cross, saas[idx_cross]),
    xytext=(t_cross - 3.5, saas[idx_cross] + 25),
    arrowprops=dict(arrowstyle="->", color=BLEU, lw=1.3),
    fontsize=9, color=BLEU, fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.4", fc=PANEL_COLOR, ec=BLEU, alpha=0.9)
)

# 3. Valeurs finales (Y3)
for valeur, couleur, label in [
    (hardware[-1], ROUGE,       f"Hardware\n{hardware[-1]:.0f}k€"),
    (saas[-1],     BLEU,        f"SaaS\n{saas[-1]:.0f}k€"),
    (total[-1],    VERT,        f"Total\n{total[-1]:.0f}k€"),
]:
    ax.annotate(
        label,
        xy=(trimestres[-1], valeur),
        xytext=(trimestres[-1] + 0.2, valeur),
        fontsize=8.5, color=couleur, fontweight="bold", va="center"
    )

# 4. Bandeau "Zone de perte" / "Zone de profit"
ax.text(1.5, 10, "[ ZONE DE PERTE ]\nR&D, Certification, Lancement",
        fontsize=8.5, color=ROUGE, alpha=0.8,
        bbox=dict(boxstyle="round,pad=0.4", fc=PANEL_COLOR, ec=ROUGE, alpha=0.5))

ax.text(8.5, 35, "[ ZONE DE PROFIT ]\nSaaS moteur de croissance",
        fontsize=8.5, color=VERT, alpha=0.9,
        bbox=dict(boxstyle="round,pad=0.4", fc=PANEL_COLOR, ec=VERT, alpha=0.5))

# 5. Argument investisseur
ax.text(
    0.5, 0.04,
    "Argument investisseur — Des l'Annee 3, la rentabilite ne depend plus de la production materielle,\n"
    "mais de la valeur recurrente de la data biomecanique hebergee.",
    transform=ax.transAxes, fontsize=9.5, color=TEXT_COLOR,
    ha="center", style="italic", alpha=0.85,
    bbox=dict(boxstyle="round,pad=0.5", fc="#1A2744", ec=BLEU, alpha=0.85)
)

# ── Axes & Titres ──
ax.set_xlim(0, 13.5)
ax.set_ylim(-5, max(total) * 1.15)

xtick_pos    = [0, 4, 8, 12]
xtick_labels = ["Lancement\n(T0)", "Année 1\n(T4)", "Année 2\n(T8)", "Année 3\n(T12)"]
ax.set_xticks(xtick_pos)
ax.set_xticklabels(xtick_labels, fontsize=10)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x)}k€"))

ax.set_xlabel("Horizon temporel", fontsize=11, labelpad=10)
ax.set_ylabel("Revenus (k€)", fontsize=11, labelpad=10)
ax.set_title(
    "J-Curve — Modèle HaaS Active-Sense\nHardware (linéaire) vs SaaS Récurrent (exponentiel)",
    fontsize=14, fontweight="bold", color=TEXT_COLOR, pad=16
)

ax.legend(fontsize=9.5, framealpha=0.2, loc="upper left",
          facecolor=PANEL_COLOR, edgecolor=GRID_COLOR)
ax.grid(True, axis="both", alpha=0.4)
ax.axhline(0, color=MUTED_COLOR, linewidth=0.8, alpha=0.5)

plt.tight_layout()
plt.savefig("outputs/jcurve_haas_activesense.png",
            dpi=180, bbox_inches="tight", facecolor=BG_COLOR)
print("✅  Graphique J-Curve exporté → outputs/jcurve_haas_activesense.png")
plt.close()
*Document rédigé dans le cadre d'une veille stratégique MedTech & Sport-Santé.*
