import streamlit as st
import random

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

if mood == "Gen Z":
    imgs = [
        "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f",
        "https://images.unsplash.com/photo-1496747611176-843222e1e57c",
        "https://images.unsplash.com/photo-1529139574466-a303027c1d8b"
    ]

elif mood == "Luxury Chic":
    imgs = [
        "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c",
        "https://images.unsplash.com/photo-1492707892479-7bc8d5a4ee93",
        "https://images.unsplash.com/photo-1521572267360-ee0c2909d518"
    ]

elif mood == "Soft Girl":
    imgs = [
        "https://images.unsplash.com/photo-1524504388940-b1c1722653e1",
        "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
        "https://images.unsplash.com/photo-1483985988355-763728e1935b"
    ]

else:
    imgs = [
        "https://images.unsplash.com/photo-1441986300917-64674bd600d8",
        "https://images.unsplash.com/photo-1490481651871-ab68de25d43d",
        "https://images.unsplash.com/photo-1514996937319-344454492b37"
    ]

st.image(imgs, width="stretch")