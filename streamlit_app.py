import streamlit as st
import random

st.markdown("""
<style>

/* PAGE BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #f8dbe6 0%, #f5ebe5 45%, #f9d8e5 100%);
    font-family: 'Arial', sans-serif;
}

/* MAIN HEADINGS */
h1 {
    color: #7a2145 !important;
    font-weight: 900 !important;
    letter-spacing: -1px;
}

h2, h3 {
    color: #8d3558 !important;
    font-weight: 700 !important;
}

/* NORMAL TEXT */
p, label, span {
    color: #5a2b3f !important;
    font-weight: 500;
}

/* SELECT LABELS */
.stSelectbox label {
    color: #7a2145 !important;
    font-weight: 700 !important;
    margin-bottom: 6px;
}

/* DROPDOWN BOX CLOSED */
div[data-baseweb="select"] {
    background: #f48bb6 !important;
    border: none !important;
    border-radius: 16px !important;
    box-shadow: 0 8px 20px rgba(244,139,182,0.25);
}

/* TEXT INSIDE DROPDOWN CLOSED */
div[data-baseweb="select"] * {
    color: white !important;
    font-weight: 700 !important;
}

/* OPEN DROPDOWN MENU */
ul {
    background: #f48bb6 !important;
    border-radius: 16px !important;
}

/* OPEN MENU OPTIONS */
li {
    color: white !important;
    font-weight: 700 !important;
}

/* HOVER OPTION */
li:hover {
    background: #de5d93 !important;
}

/* BUTTON */
.stButton > button {
    background: linear-gradient(90deg,#e44f8d,#ff8eb9) !important;
    color: white !important;
    border: none !important;
    border-radius: 18px !important;
    padding: 12px 24px !important;
    font-size: 16px !important;
    font-weight: 800 !important;
    box-shadow: 0 10px 25px rgba(228,79,141,0.25);
}

/* BUTTON HOVER */
.stButton > button:hover {
    transform: scale(1.03);
}

/* SUCCESS BOX */
.stSuccess {
    background: rgba(255,255,255,0.55) !important;
    color: #7a2145 !important;
    border-radius: 18px !important;
    border: 1px solid #f3a8c7 !important;
}

/* IMAGE ROUNDED */
img {
    border-radius: 18px !important;
}

</style>
""", unsafe_allow_html=True)
st.set_page_config(page_title="Aishwarya Brand Studio")

st.title("🎀 Aishwarya Brand Studio")
st.subheader("Create your dream brand in seconds")

industry = st.selectbox(
    "Choose Industry",
    ["Fashion", "Beauty", "Luxury", "Cafe", "Streetwear"]
)

mood = st.selectbox(
    "Choose Mood",
    ["Minimal", "Bold", "Soft Girl", "Luxury Chic", "Gen Z"]
)

audience = st.selectbox(
    "Choose Audience",
    ["Students", "Women", "Premium Buyers", "Trend Lovers", "Youth"]
)

if st.button("✨ Generate Brand"):
    
    names = [
        "Veloura", "MuseHaus", "Pink Theory",
        "Noir Bloom", "Aura Lane", "Studio Vera"
    ]

    taglines = [
        "Style beyond trends",
        "Made to be remembered",
        "Luxury in motion",
        "Wear your era",
        "Built for icons"
    ]

    colors = {
        "Minimal":"#F5F0E8",
        "Bold":"#FF4B6E",
        "Soft Girl":"#F8C8DC",
        "Luxury Chic":"#1E1E1E",
        "Gen Z":"#7C3AED"
    }

    st.success("Brand Generated!")

    st.header(random.choice(names))
    st.write("**Industry:**", industry)
    st.write("**Mood:**", mood)
    st.write("**Audience:**", audience)
    st.write("**Tagline:**", random.choice(taglines))

    st.markdown("### Color Identity")
    st.color_picker("Brand Color", colors[mood], disabled=True)
    st.markdown("### ✨ Visual Identity")

if mood == "Minimal":
    st.info("Clean silhouettes • Neutral tones • Quiet luxury • Editorial minimalism")

elif mood == "Bold":
    st.info("Statement colors • Loud campaigns • Strong personality • Viral energy")

elif mood == "Soft Girl":
    st.info("Blush tones • Feminine visuals • Romantic branding • Dreamy packaging")

elif mood == "Luxury Chic":
    st.info("Black & gold • Prestige aura • Premium textures • Elite positioning")

elif mood == "Gen Z":
    st.info("Playful trends • Social-first identity • Youth culture • Internet relevance")

st.markdown("### 🖼 Moodboard")

# GOD MODE MOODBOARD

if mood == "Gen Z":
    imgs = [
        "https://images.unsplash.com/photo-1529139574466-a303027c1d8b",
        "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f",
        "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c"
    ]

elif mood == "Luxury Chic":
    imgs = [
        "https://images.unsplash.com/photo-1441986300917-64674bd600d8",
        "https://images.unsplash.com/photo-1523170335258-f5ed11844a49",
        "https://images.unsplash.com/photo-1542291026-7eec264c27ff"
    ]

elif mood == "Soft Girl":
    imgs = [
        "https://images.unsplash.com/photo-1524504388940-b1c1722653e1",
        "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
        "https://images.unsplash.com/photo-1496747611176-843222e1e57c"
    ]

else:
    imgs = [
        "https://images.unsplash.com/photo-1509631179647-0177331693ae",
        "https://images.unsplash.com/photo-1492707892479-7bc8d5a4ee93",
        "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f"
    ]


st.markdown("## ✨ Moodboard")

col1, col2 = st.columns([2,1])

with col1:
    st.image(imgs[0], width="stretch")

with col2:
    st.image(imgs[1], width="stretch")
    st.image(imgs[2], width="stretch")