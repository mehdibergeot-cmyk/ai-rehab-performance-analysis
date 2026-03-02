# 📚 Sources & Références Documentaires

> Ce document recense les rapports de marché, normes réglementaires et publications scientifiques indépendantes sur lesquels reposent l'analyse financière, la modélisation concurrentielle et la conception clinique du projet **Active-Sense**.
>
> Chaque source est liée à une section précise du dossier pour garantir la traçabilité des données.

---

## 1. Données de Marché & Projections Financières

*Sources utilisées dans `STRATEGIE_COMMERCIALE.md` et `src/jcurve_investor.py` pour les projections de croissance (CAGR +22,4%) et la taille de marché (4,1 Md$ en 2024 → 9 Md$ en 2028).*

| Éditeur | Rapport | Année |
| :--- | :--- | :---: |
| **Grand View Research** | *Sports Technology Market Size, Share & Trends Analysis Report — By Technology (Device, Smart Stadium, Esports, Sports Analytics), Forecasts 2023–2030* | 2023 |
| **MarketsandMarkets** | *Sports Technology Market by Device (Wearables, Smart Fabrics), Technology (IoT, AI) — Global Forecast to 2028* | 2023 |
| **Statista** | *Digital Health & Wearable Medical Devices : Market Revenue, Penetration Rates & Projections* | 2024 |

---

## 2. Fondations Cliniques & Biomécaniques (LCA)

*Sources utilisées dans `src/rehab_analysis.py` pour justifier les indicateurs retenus : asymétrie biomécanique, ratio de charge ACWR, et seuil de retour au jeu.*

**Hewett, T. E., et al. (2005)**
> *Biomechanical Measures of Neuromuscular Control and Valgus Loading of the Knee Predict Anterior Cruciate Ligament Injury Risk.*
> The American Journal of Sports Medicine.
> → Étude de référence mondiale sur la détection du valgus dynamique — justifie le choix des capteurs IMU pour surveiller l'appui en temps réel.

**Mendiguchia, J., et al. (2017)**
> *Progression criteria for anterior cruciate ligament reconstruction rehabilitation.*
> Journal of Orthopaedic & Sports Physical Therapy (JOSPT).
> → Fonde les seuils de progression utilisés dans la modélisation de la courbe de rééducation (puissance explosive, semaine de Return to Play).

**Gokeler, A., et al. (2019)**
> *Return to Sports after ACL injury 5 years from now : 10 things we must do.*
> Journal of Experimental Orthopaedics.
> → Démontre l'efficacité du bio-feedback externe dans la rééducation post-LCA — socle scientifique du concept de genouillère Active-Sense.

---

## 3. Cadre Réglementaire — Dispositifs Médicaux

*Sources utilisées dans `STRATEGIE_COMMERCIALE.md` (Section 2 — Capex) pour justifier les étapes obligatoires de certification avant mise sur le marché européen.*

**ISO 13485:2016**
> *Dispositifs médicaux — Systèmes de management de la qualité — Exigences à des fins réglementaires.*
> Organisation Internationale de Normalisation, Genève.
> → Norme qualité obligatoire pour tout fabricant de dispositifs médicaux. Conditionne la relation avec les partenaires de production certifiés.

**Règlement (UE) 2017/745 — MDR**
> *Règlement relatif aux dispositifs médicaux.*
> Parlement européen et Conseil de l'Union européenne.
> → Cadre légal du Marquage CE en Europe. Toute commercialisation de la genouillère Active-Sense sur le marché européen est soumise à ce règlement.

---

## 4. Benchmark Concurrentiel & Modélisation Financière

*Sources utilisées dans `src/market_analysis.py` pour les scores comparatifs, et dans `src/jcurve_investor.py` pour la modélisation HaaS.*

**Fiches techniques constructeurs (2024–2025)**
Spécifications publiques analysées :
- *Catapult Vector* — GPS/IMU, données de charge et d'impact
- *Zone7 AI Platform* — algorithmes prédictifs de risque blessure
- *SkillSocks* — capteurs de pression plantaire connectés

**Modélisation HaaS (Hardware-as-a-Service)**
> Basée sur les métriques SaaS standards publiées par **David Skok (Matrix Partners)** — LTV/CAC ratio, ARR, Churn rate — adaptées à la DeepTech médicale.
> Référence : [forentrepreneurs.com/saas-metrics](https://www.forentrepreneurs.com/saas-metrics)

---

## 5. Avertissement Méthodologique

> ⚠️ Les données chiffrées utilisées dans les scripts Python (`rehab_analysis.py`, `market_analysis.py`, `jcurve_investor.py`) sont des **données synthétiques générées à des fins de démonstration**. Elles s'appuient sur les ordres de grandeur et tendances issus des sources listées ci-dessus, mais ne constituent pas des données cliniques réelles.
>
> Ce projet a une vocation de **démonstration méthodologique** dans le cadre d'une veille stratégique MedTech & Sport-Santé.

---

*Document rédigé dans le cadre d'une veille stratégique MedTech & Sport-Santé.*
*Auteur : Mehdi Bergeot — Expertise Dispositifs Médicaux & Sport-Santé*
