import streamlit as st
import os

# ─── Configuration de la page ───────────────────────────────────────────────
st.set_page_config(
    page_title="Khalifa A. NDIONE – Géomaticien",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CSS personnalisé ────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

.stApp { background: #f4f1ec; color: #1a1a2e; }

section[data-testid="stSidebar"] { background: #1a1a2e !important; color: #f4f1ec; }
section[data-testid="stSidebar"] * { color: #f4f1ec !important; }

h1, h2, h3 { font-family: 'Playfair Display', serif !important; color: #1a1a2e !important; }

.card {
    background: #ffffff; border-radius: 12px; padding: 1.4rem 1.6rem;
    margin-bottom: 1rem; border-left: 4px solid #c8963e;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.card h4 { font-family: 'Playfair Display', serif; color: #c8963e; margin: 0 0 0.4rem 0; font-size: 1rem; }
.card p  { margin: 0 0 0.3rem 0; font-size: 0.9rem; color: #444; line-height: 1.6; }

.badge {
    display: inline-block; background: #1a1a2e; color: #f4f1ec !important;
    border-radius: 20px; padding: 4px 14px; font-size: 0.78rem;
    margin: 4px 3px; font-weight: 500; letter-spacing: 0.3px;
}

.section-title { font-family: 'Playfair Display', serif; font-size: 1.7rem; color: #1a1a2e; margin-bottom: 0.2rem; }
.section-sub   { color: #c8963e; font-size: 0.85rem; font-weight: 500; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 1.2rem; }

.stTabs [data-baseweb="tab-list"] { gap: 6px; background: transparent; }
.stTabs [data-baseweb="tab"] { background: #e8e3da; border-radius: 8px; color: #1a1a2e !important; font-weight: 500; padding: 6px 18px; }
.stTabs [aria-selected="true"] { background: #1a1a2e !important; color: #f4f1ec !important; }
</style>
""", unsafe_allow_html=True)

# ─── SIDEBAR ────────────────────────────────────────────────────────────────
with st.sidebar:
    try:
        st.image("Khalifa.PNG", width=190)
    except Exception:
        st.markdown('<div style="width:160px;height:160px;border-radius:50%;background:rgba(200,150,62,0.3);display:flex;align-items:center;justify-content:center;font-size:3rem;margin:auto">🧑‍💻</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Khalifa Ababacar NDIONE")
    st.markdown("*Géomaticien · Mastérant en Géographie*")
    st.markdown("---")
    st.markdown("**📧** ndionekhalifa78@gmail.com")
    st.markdown("**📞** +221 77 688 50 51")
    st.markdown("**📍** Dakar – HLM 5, Sénégal")
    st.markdown("---")
    st.markdown("**🎓 Diplômes**")
    for d in ["Master en Géographie (en cours)", "Licence en Géographie", "BTS en Géomatique", "Baccalauréat"]:
        st.markdown(f"&nbsp;&nbsp;▸ {d}", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("**🌐 Langues**")
    st.markdown("&nbsp;&nbsp;🇫🇷 Français — Courant", unsafe_allow_html=True)
    st.markdown("&nbsp;&nbsp;🇸🇳 Wolof — Natif", unsafe_allow_html=True)
    st.markdown("&nbsp;&nbsp;🇬🇧 Anglais — Intermédiaire", unsafe_allow_html=True)
    st.markdown("---")
    st.download_button(
        label="📄 Télécharger le CV",
        data=b"CV Khalifa NDIONE",   # Remplacer par: open('CV.pdf','rb').read()
        file_name="CV_Khalifa_NDIONE.pdf",
        mime="application/pdf",
        use_container_width=True,
    )

# ─── HERO ───────────────────────────────────────────────────────────────────
st.markdown("""
<div style="background:linear-gradient(135deg,#1a1a2e 60%,#2d2d5e);border-radius:16px;padding:2.4rem 2.8rem;margin-bottom:2rem;color:#f4f1ec">
  <p style="color:#c8963e;font-size:0.8rem;letter-spacing:3px;text-transform:uppercase;margin:0 0 0.5rem">Portfolio Professionnel</p>
  <h1 style="font-family:'Playfair Display',serif;font-size:2.4rem;margin:0 0 0.7rem;color:#f4f1ec">Khalifa Ababacar NDIONE</h1>
  <p style="font-size:1rem;color:#c8c8e0;margin:0;max-width:700px;line-height:1.7">
  Étudiant en géomatique et titulaire d'une licence en Géographie, passionné par l'analyse,
  le traitement et la gestion des données géospatiales. Mon objectif est de contribuer à la
  réalisation de projets territoriaux à fort impact au Sénégal, grâce à la combinaison de la
  cartographie, du SIG et de la programmation Python.
  </p>
</div>
""", unsafe_allow_html=True)

# ─── ONGLETS ────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["🛠️ Compétences", "👨‍💻 Expériences", "🗂️ Projets", "📬 Contact"])

# ── COMPÉTENCES ─────────────────────────────────────────────────────────────
with tab1:
    st.markdown('<p class="section-sub">Savoir-faire technique</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Compétences</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("##### 🗺️ SIG & Cartographie")
        sig = ["QGIS", "ArcGIS", "Analyse spatiale", "Cartographie thématique"]
        st.markdown("".join(f'<span class="badge">{t}</span>' for t in sig), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("##### 💻 Programmation & Données")
        prog = ["Python", "Pandas", "GeoPandas", "Rasterio", "Matplotlib", "Folium", "Requêtes SQL", "Streamlit"]
        st.markdown("".join(f'<span class="badge">{t}</span>' for t in prog), unsafe_allow_html=True)

    with col2:
        st.markdown("##### 📐 DAO & Modélisation 3D")
        dao = ["AutoCAD (plans 2D)", "SketchUp (modèle 3D)"]
        st.markdown("".join(f'<span class="badge">{t}</span>' for t in dao), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("##### 📡 Acquisition de données")
        acq = ["Topographie", "Numérisation", "Mobile Topographer", "Qfield", "GeoPackage", "Géodatabase"]
        st.markdown("".join(f'<span class="badge">{t}</span>' for t in acq), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("##### 🧠 Compétences transversales")
        transv = ["Informatique bureautique", "Travail en équipe", "Rigueur & précision"]
        st.markdown("".join(f'<span class="badge">{t}</span>' for t in transv), unsafe_allow_html=True)

# ── EXPÉRIENCES ──────────────────────────────────────────────────────────────
with tab2:
    st.markdown('<p class="section-sub">Parcours professionnel</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Expériences</p>', unsafe_allow_html=True)

    experiences = [
        {"titre": "Digitalisation & Correction topologique",
         "desc": "Digitalisation des bâtis, routes et arbres sur QGIS et ArcGIS. Correction des erreurs topologiques pour garantir l'intégrité des données géographiques.",
         "outils": ["QGIS", "ArcGIS"]},
        {"titre": "Plans 2D & Modélisation 3D",
         "desc": "Réalisation de plans complets sur AutoCAD (RDC, Étage, Terrasse, Masse, Coupe, Façade), puis importation et construction 3D dans SketchUp.",
         "outils": ["AutoCAD", "SketchUp"]},
        {"titre": "Collecte de données terrain – Communes de Fass-Colobane-Gueule Tapée et Grand-Dakar",
         "desc": "Collecte d'équipements urbains (administratif, sanitaire, éducatif, lieux de cultes, lampadaires, poteaux électriques, stations, gargottes, arbres, panneaux publicitaires) via Mobile Topographer et Qfield, puis traitement et analyse sur QGIS et ArcGIS.",
         "outils": ["Mobile Topographer", "Qfield", "QGIS", "ArcGIS"]},
        {"titre": "Cartographie",
         "desc": "Réalisation de cartes de localisation et cartes thématiques.",
         "outils": ["QGIS", "ArcGIS"]},
        {"titre": "Développement d'applications web géospatiales",
         "desc": "Création d'applications web interactives avec Python et Streamlit sur JupyterLab, intégrant des visualisations cartographiques et des analyses de données.",
         "outils": ["Python", "Streamlit", "JupyterLab"]},
        {"titre": "Création de bases de données géographiques",
         "desc": "Conception et implémentation de bases de données géographiques sous QGIS (GeoPackage) et ArcGIS (File Geodatabase, Personal Geodatabase).",
         "outils": ["QGIS", "ArcGIS", "SQL"]},
    ]

    for xp in experiences:
        outils_html = "".join(
            f'<span style="background:#1a1a2e;color:#f4f1ec;border-radius:12px;padding:2px 10px;font-size:0.75rem;margin:2px 2px">{o}</span>'
            for o in xp["outils"]
        )
        st.markdown(f'<div class="card"><h4>{xp["titre"]}</h4><p>{xp["desc"]}</p><div style="margin-top:0.6rem">{outils_html}</div></div>', unsafe_allow_html=True)

# ── PROJETS (avec captures d'écran / vidéos) ─────────────────────────────────
with tab3:
    st.markdown('<p class="section-sub">Réalisations notables</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Projets</p>', unsafe_allow_html=True)

    # ╔══════════════════════════════════════════════════════════════╗
    # ║  COMMENT AJOUTER VOS MÉDIAS                                  ║
    # ║  • Créez un dossier  images/  à côté de ce fichier .py       ║
    # ║  • Créez un dossier  videos/  à côté de ce fichier .py       ║
    # ║  • Renseignez le chemin dans "image" ou "video" ci-dessous   ║
    # ║  • Laissez None si vous n'avez pas encore de média           ║
    # ╚══════════════════════════════════════════════════════════════╝
    projets = [
        {
            "emoji": "🗺️",
            "titre": "Visualisation géospatiale – Régions du Sénégal",
            "desc": "Application Streamlit interactive permettant d'explorer les régions administratives du Sénégal à partir d'un shapefile. Export GeoJSON et GeoPackage intégrés.",
            "tech": ["Python", "Streamlit", "GeoPandas", "Folium"],
            "statut": "✅ Terminé",
            "image": "images/projet_senegal.png",   # ← votre capture d'écran ici
            "video": None,
        },
        {
            "emoji": "📊",
            "titre": "Dashboard analyse données tabulaires",
            "desc": "Tableau de bord d'analyse de données étudiants (fichier Excel Geom1A.xlsx). Visualisations statistiques, filtres dynamiques et export de données.",
            "tech": ["Python", "Streamlit", "Pandas", "Plotly"],
            "statut": "✅ Terminé",
            "image": "images/projet_dashboard.png",  # ← votre capture d'écran ici
            "video": None,
        },
        {
            "emoji": "🏙️",
            "titre": "Cartographie urbaine – Fass-Colobane",
            "desc": "Carte thématique des équipements urbains de la commune avec base de données attributaires complète.",
            "tech": ["ArcGIS", "Mobile Topographer"],
            "statut": "✅ Terminé",
            "image": "images/projet_carte.png",      # ← votre carte exportée ici
            "video": None,
        },
        {
            "emoji": "🏗️",
            "titre": "Modélisation 3D de bâtiment",
            "desc": "Plans architecturaux 2D complets sur AutoCAD et reconstruction 3D sur SketchUp d'un immeuble R+2 avec toutes les vues réglementaires.",
            "tech": ["AutoCAD", "SketchUp"],
            "statut": "✅ Terminé",
            "image": "images/projet_3d.png",         # ← capture SketchUp ici
            "video": "videos/projet_3d.mp4",         # ← vidéo de la maquette 3D ici
        },
    ]

    for proj in projets:
        st.markdown("---")
        tech_html = "".join(
            f'<span style="background:#f4f1ec;color:#1a1a2e;border:1px solid #c8963e;border-radius:12px;padding:2px 10px;font-size:0.75rem;margin:2px 2px">{t}</span>'
            for t in proj["tech"]
        )
        has_image = proj.get("image") and os.path.exists(proj["image"])
        has_video = proj.get("video") and os.path.exists(proj["video"])
        has_media = has_image or has_video

        if has_media:
            col_txt, col_media = st.columns([1.2, 1])
        else:
            col_txt = st.container()

        with col_txt:
            st.markdown(
                f'<div class="card"><h4>{proj["emoji"]} {proj["titre"]}</h4>'
                f'<p>{proj["desc"]}</p>'
                f'<div style="margin-top:0.6rem">{tech_html}</div>'
                f'<p style="margin-top:0.5rem;font-size:0.8rem;color:#888">{proj["statut"]}</p></div>',
                unsafe_allow_html=True,
            )

        if has_media:
            with col_media:
                if has_image:
                    st.image(proj["apte.png"], use_column_width=True)
                elif has_video:
                    st.video(proj["video"])

    st.markdown("---")
    st.info("💡 **Astuce** : placez vos captures d'écran dans `images/` et vos vidéos dans `videos/` à côté de ce fichier Python, puis mettez à jour les chemins dans la liste `projets` ci-dessus.")

# ── CONTACT ──────────────────────────────────────────────────────────────────
with tab4:
    st.markdown('<p class="section-sub">Restons en contact</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Contact</p>', unsafe_allow_html=True)

    col_info, col_form = st.columns([1, 1.6])

    with col_info:
        st.markdown('<div class="card"><h4>Coordonnées</h4><p>📧 ndionekhalifa78@gmail.com</p><p>📞 +221 77 688 50 51</p><p>📍 Dakar – HLM 5, Sénégal</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><h4>Disponibilité</h4><p>Ouvert aux opportunités professionnelles, stages, projets collaboratifs et missions de conseil en géomatique et SIG.</p></div>', unsafe_allow_html=True)

    with col_form:
        st.markdown("##### ✉️ Envoyer un message")
        nom           = st.text_input("Votre nom")
        email_contact = st.text_input("Votre email")
        sujet         = st.selectbox("Sujet", ["Proposition de mission", "Collaboration", "Stage / Emploi", "Autre"])
        message       = st.text_area("Votre message", height=130)

        if st.button("📨 Envoyer", use_container_width=True):
            if nom and email_contact and message:
                st.success("✅ Message envoyé ! Khalifa vous répondra dans les plus brefs délais.")
            else:
                st.warning("⚠️ Merci de remplir tous les champs.")

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("<hr style='margin-top:3rem;border-color:#ddd'>", unsafe_allow_html=True)
st.markdown('<p style="text-align:center;color:#aaa;font-size:0.8rem">© 2025 Khalifa Ababacar NDIONE · Géomaticien · Dakar, Sénégal</p>', unsafe_allow_html=True)
