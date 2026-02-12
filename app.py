import streamlit as st
import requests
import random
from datetime import date
import base64
import streamlit.components.v1 as components



st.set_page_config(page_title="This Day in History", page_icon="📜")

st.markdown("""
<style>
.stApp {
    background-color: transparent;
}
</style>
""", unsafe_allow_html=True)



st.title("📜 This Day in History")
st.subheader("Pick any day and explore history")
st.markdown("### 🎂 Made with love for Anjana ❤️")

def autoplay_music(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
        <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)


def fireworks():
    components.html("""
    <style>
    #fireworks-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -1000;
        pointer-events: none;
    }
    </style>

    <canvas id="fireworks-bg"></canvas>

    <script>
    const canvas = document.getElementById("fireworks-bg");
    const ctx = canvas.getContext("2d");

    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    resize();
    window.onresize = resize;

    let particles = [];

    function random(min, max) {
        return Math.random() * (max - min) + min;
    }

    function createFirework() {
        const x = random(100, canvas.width - 100);
        const y = random(50, canvas.height / 2);
        for (let i = 0; i < 60; i++) {
            particles.push({
                x: x,
                y: y,
                speedX: random(-5, 5),
                speedY: random(-5, 5),
                radius: 2,
                life: 80,
                color: "hsl(" + random(0,360) + ",100%,50%)"
            });
        }
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach((p, i) => {
            p.x += p.speedX;
            p.y += p.speedY;
            p.life--;
            ctx.fillStyle = p.color;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fill();
            if (p.life <= 0) particles.splice(i, 1);
        });
        requestAnimationFrame(animate);
    }

    setInterval(createFirework, 900);
    animate();
    </script>
    """, height=0)

# Default date → Feb 21 (birthday)
default_date = date(2026, 2, 21)

selected_date = st.date_input(
    "📅 Choose a day",
    default_date,
    format="DD/MM/YYYY"
)

month = selected_date.month
day = selected_date.day

# Special birthday message
if month == 2 and day == 21:
    fireworks()
    st.markdown("## 🎉Happy Birthday from your brother!! ")
    st.success("🎂 Birthday of Anjana — 21st February 2007")
    
    st.audio("music/bg.mp3")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("images/anjana2.jpg", caption="Anjana 💖")

    with col2:
        st.image("images/anjana1.jpg", caption="Birthday Queen 👑")

    with col3:
        st.image("images/anjana3.jpg", caption="World Explorer 🌍")


url = f"https://history.muffinlabs.com/date/{month}/{day}"

if month == 9 and day == 4:
    st.markdown("## 🎉Happy Birthday from your brother!! ")
    st.success("🎂 Birthday of Chikkumanee — 04th September 2013")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("images/chikku1.jpg", caption="Attitudee 😎😏")

    with col2:
        st.image("images/chikku2.jpg", caption="mmm..yummyy..👌😹")

    with col3:
        st.image("images/chikku3.jpg", caption="angryyy😡🥵")

url = f"https://history.muffinlabs.com/date/{month}/{day}"

if month == 12 and day == 1:
    st.markdown("## 🎉Happy Birthday Mammoojjii ")
    st.success("🎂 Birthday of Mammoojjii — 1st Decemeber 1987")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/mom1.jpg", caption="with chikkumaneei")

    with col2:
        st.image("images/mom2.jpg", caption="again manee!!😹 ")

    with col3:
        st.image("images/mom3.jpg", caption="together without mee!!🥲")

url = f"https://history.muffinlabs.com/date/{month}/{day}"

if month == 6 and day == 4:
    st.markdown("## 🎉Happy Birthday from Myself ")
    st.success("🎂 Birthday of Mee — 04th June 2011")
        
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/me1.jpg", caption="styleeii!!🕶🙈")

    with col2:
        st.image("images/me2.jpg", caption="mudi vettatee.! ✂🪮 ")

    with col3:
        st.image("images/me3.jpg", caption="Posingg..✌🤞")


url = f"https://history.muffinlabs.com/date/{month}/{day}"


try:
    response = requests.get(url, timeout=10)
    data = response.json()

    events = data["data"]["Events"]

    st.write(f"## 🗓️ {selected_date.strftime('%B %d')}")

    selected = random.sample(events, min(5, len(events)))

    for event in selected:
        st.markdown("---")
        st.write(f"### {event['year']}")
        st.write(event["text"])

except:
    st.error("Internet problem or API not responding. Please try again later.")
