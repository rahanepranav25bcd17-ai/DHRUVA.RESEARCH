import streamlit as st
import pandas as pd
import datetime
from PIL import Image

# 1. PAGE CONFIG
st.set_page_config(
    page_title="D.H.R.U.V.A. | National Anomaly Research",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- DATABASE IN MEMORY (Don't Refresh Page to keep data) ---
if 'missions' not in st.session_state: st.session_state['missions'] = [] 
if 'intel_reports' not in st.session_state: st.session_state['intel_reports'] = []
if 'contact_msgs' not in st.session_state: st.session_state['contact_msgs'] = []
if 'dir_img' not in st.session_state: st.session_state['dir_img'] = None
if 'logo_img' not in st.session_state: st.session_state['logo_img'] = None
if 'insp_img' not in st.session_state: st.session_state['insp_img'] = None
if 'about_txt' not in st.session_state: 
    st.session_state['about_txt'] = "We are the next generation of researchers, a youth-led unit driven by logic and modern physics. Our interest lies in bridging the gap between ancient folklore and verified science."
if 'auth' not in st.session_state: st.session_state['auth'] = False

query_params = st.query_params
access_code = query_params.get("access", None)

# 2. IPS PREMIUM CSS (SKY BLUE + GREEN EMAIL STYLE)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Raleway:wght@300;400&display=swap');

    .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Raleway', sans-serif; }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] { background-color: #0A0A0A; border-bottom: 1px solid #111; justify-content: center; }
    .stTabs [data-baseweb="tab"] { color: #888 !important; font-family: 'Raleway', sans-serif; font-weight: bold; font-size: 14px; letter-spacing: 1px;}
    .stTabs [aria-selected="true"] { color: #00D4FF !important; border-bottom: 2px solid #00D4FF; }

    /* IPS Headers */
    .ips-title { font-family: 'Cinzel', serif; font-size: 55px; text-align: center; letter-spacing: 5px; margin-bottom: 0; }
    .ips-subtitle { font-family: 'Raleway', sans-serif; font-size: 14px; text-align: center; letter-spacing: 4px; color: #00D4FF; text-transform: uppercase; margin-bottom: 30px; }
    
    /* Green Email Box (From your image) */
    .green-box-container {
        background-color: #0A0A0A;
        border: 1px solid #1A1A1A;
        padding: 35px;
        max-width: 550px;
        margin: 20px auto;
        border-radius: 8px;
        text-align: center;
    }
    .email-label { color: #555; font-size: 12px; text-align: left; margin-bottom: 5px; font-family: sans-serif; }
    .email-text { color: #2ECC71 !important; font-weight: bold; font-size: 22px; font-family: 'Courier New', monospace; text-decoration: none; }

    /* Inspiration Section */
    .ips-block { background-color: #0A0A0A; border-left: 3px solid #00D4FF; padding: 30px; margin: 30px 0; }
    
    /* Input Styling */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea, .stSelectbox > div > div > div {
        background-color: #121212 !important; border: 1px solid #222 !important; color: white !important; border-radius: 0px;
    }

    /* Send Message Button (IPS Red Style) */
    .stButton > button { background-color: #7B0000 !important; color: white; border-radius: 0; width: 220px; border: none; margin: 0 auto; display: block; }
    </style>
""", unsafe_allow_html=True)

# 3. PUBLIC HEADER
col_h1, col_h2, col_h3 = st.columns([1, 4, 1])
with col_h2:
    if st.session_state['logo_img']: st.image(st.session_state['logo_img'], width=150)
    else: st.markdown("<h1 style='text-align:center;'>🦅</h1>", unsafe_allow_html=True)
    st.markdown("<div class='ips-title'>D.H.R.U.V.A.</div>", unsafe_allow_html=True)
    st.markdown("<div class='ips-subtitle'>National Research & Anomaly Society</div>", unsafe_allow_html=True)

# 4. TABS (IPS NAVIGATION)
tab1, tab2, tab3, tab4, tab5 = st.tabs(["HOME", "ABOUT US", "INVESTIGATIONS", "REPORT MYSTERY", "CONTACT"])

with tab1:
    st.markdown("<h2 style='text-align:center; font-family:Cinzel;'>WE INVESTIGATE WHAT OTHERS FEAR</h2>", unsafe_allow_html=True)
    st.write("<p style='text-align:center; color:#888;'>Scientific documentation and logical assessment of unexplained phenomena across the Indian subcontinent.</p>", unsafe_allow_html=True)
    
    # --- INSPIRATION (GAURAV TIWARI SECTION) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_i1, col_i2 = st.columns([1, 2])
    with col_i1:
        if st.session_state['insp_img']: st.image(st.session_state['insp_img'], use_container_width=True)
        else: st.info("Late Rev. Gaurav Tiwari Image")
    with col_i2:
        st.markdown(f"""
            <div class='ips-block'>
                <h3 style='color:#00D4FF !important; font-family:Cinzel;'>OUR INSPIRATION</h3>
                <p style='font-style:italic; font-size:18px; color:#DDD;'>"Ghosts or consciousness survive physical death. Paranormal activity is independent of time."</p>
                <p style='color:#00D4FF; font-weight:bold; margin-bottom:0;'>- Late Rev. Gaurav Tiwari</p>
                <p style='color:#555; font-size:12px;'>Founder, Indian Paranormal Society</p>
                <p style='margin-top:15px; color:#AAA;'>His dedication to replacing fear with logic is the driving force behind D.H.R.U.V.A. We follow his scientific methods to study the unseen.</p>
            </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("<h2 style='font-family:Cinzel;'>THE DIRECTORATE</h2>", unsafe_allow_html=True)
    col_dir1, col_dir2 = st.columns([1, 2])
    with col_dir1:
        if st.session_state['dir_img']: st.image(st.session_state['dir_img'], width=300)
        else: st.info("Founder Photo")
    with col_dir2:
        st.markdown("<h3 style='color:#00D4FF !important; margin-bottom:0;'>Pranav Anil Rahane</h3>", unsafe_allow_html=True)
        st.caption("Founder & Chief Investigator")
        st.write(st.session_state['about_txt'])
        st.markdown("---")
        st.markdown("#### YOUTH IN RESEARCH\nWe represent the curiosity of India's youth. Armed with sensors and rational thinking, we aim to solve myths that have haunted generations.")

with tab3:
    st.markdown("<h2 style='font-family:Cinzel; text-align:center;'>CASE FILES</h2>", unsafe_allow_html=True)
    if not st.session_state['missions']: st.info("Active field research in progress. No declassified files yet.")
    for m in reversed(st.session_state['missions']):
        st.markdown(f"<div class='ips-block'><h4>{m['title']}</h4><p>{m['desc']}</p><b>VERDICT: {m['status']}</b></div>", unsafe_allow_html=True)

with tab4:
    st.markdown("<h2 style='font-family:Cinzel; text-align:center;'>SUBMIT REPORT</h2>", unsafe_allow_html=True)
    with st.form("anomaly_form"):
        c_a, c_b = st.columns(2)
        with c_a:
            name = st.text_input("FULL NAME *"); phone = st.text_input("CONTACT NO *")
        with c_b:
            loc = st.text_input("LOCATION *")
            m_type = st.selectbox("MYSTERY TYPE", ["Haunting", "UFO/UAP Sighting", "Poltergeist", "Shadow Figure", "Signal/Electronic Glitch", "Other"])
        desc = st.text_area("DETAILED DESCRIPTION *")
        if st.form_submit_button("TRANSMIT INTEL"):
            st.session_state['intel_reports'].append({"name": name, "phone": phone, "loc": loc, "type": m_type, "desc": desc, "time": str(datetime.datetime.now())})
            st.success("INTEL RECEIVED AT D.H.R.U.V.A. HQ.")

with tab5:
    st.markdown("<h2 style='font-family:Cinzel; text-align:center; margin-bottom:0;'>CONTACT US</h2>", unsafe_allow_html=True)
    st.write("<p style='text-align:center; color:#555;'>Reach out to our paranormal research team</p>", unsafe_allow_html=True)
    
    # GREEN EMAIL BOX (Exactly like your uploaded image style)
    st.markdown(f"""
        <div class="green-box-container">
            <div class="email-label">Email:</div>
            <div style="display: flex; align-items: center; justify-content: center; gap: 10px;">
                <span style="font-size: 24px; color: #2ECC71;">✉️</span>
                <a href="mailto:team.dhruva.research@gmail.com" class="email-text">team.dhruva.research@gmail.com</a>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align:center; font-family:Cinzel; font-size:24px; margin-top:50px;'>SEND US A MESSAGE</h3>", unsafe_allow_html=True)
    with st.form("contact_form"):
        cn = st.text_input("FULL NAME *"); ce = st.text_input("EMAIL ADDRESS *")
        cs = st.selectbox("SUBJECT *", ["Investigation Request", "Join the Team", "General Inquiry"])
        cm = st.text_area("MESSAGE *")
        if st.form_submit_button("SEND MESSAGE"):
            st.session_state['contact_msgs'].append({"name": cn, "email": ce, "sub": cs, "msg": cm, "time": str(datetime.datetime.now())})
            st.success("MESSAGE TRANSMITTED.")

# 5. HIDDEN ADMIN PANEL (HQ CONTROL)
if access_code == "classified":
    with st.sidebar:
        st.markdown("### 🔐 HQ CONTROL")
        if not st.session_state['auth']:
            u = st.text_input("ID"); p = st.text_input("KEY", type="password")
            if st.button("LOGIN"):
                if u == "Pranav" and p == "DhruvaBot": st.session_state['auth'] = True; st.rerun()
        
        if st.session_state['auth']:
            st.success("DIRECTOR ONLINE")
            
            # --- UPLOAD SECTION (All 4 Buttons) ---
            with st.expander("📤 UPLOAD & UPDATE ASSETS"):
                st.write("1. Website Logo")
                st.session_state['logo_img'] = st.file_uploader("Agency Logo", type=['png','jpg'], key="logo_up")
                
                st.write("2. Founder/Director Image")
                st.session_state['dir_img'] = st.file_uploader("Director Image", type=['png','jpg'], key="dir_up")
                
                st.write("3. Inspiration Image (GT)")
                st.session_state['insp_img'] = st.file_uploader("Gaurav Tiwari Image", type=['png','jpg'], key="insp_up")
                
                st.write("4. Investigation Case File")
                with st.form("case_form"):
                    ct = st.text_input("Title"); cv = st.selectbox("Verdict", ["SOLVED", "UNEXPLAINED", "DEBUNKED"]); cd = st.text_area("Description")
                    if st.form_submit_button("PUBLISH CASE"):
                        st.session_state['missions'].append({"title": ct, "status": cv, "desc": cd, "date": str(datetime.date.today())})
            
            # --- EDIT ABOUT SECTION ---
            with st.expander("📝 EDIT ABOUT US"):
                st.session_state['about_txt'] = st.text_area("Update Directorate Info", st.session_state['about_txt'])

            # --- INCOMING DATA (Intel & Messages) ---
            with st.expander("📨 INCOMING INTEL (Reports)"):
                for r in reversed(st.session_state['intel_reports']):
                    st.write(f"**From:** {r['name']} ({r['phone']}) - {r['type']}\n\n**Desc:** {r['desc']}")
                    st.markdown("---")

            with st.expander("💬 CONTACT MESSAGES"):
                for c in reversed(st.session_state['contact_msgs']):
                    st.write(f"**From:** {c['name']} ({c['email']})\n\n**Subject:** {c['sub']}\n\n**Msg:** {c['msg']}")
                    st.markdown("---")

st.markdown("<div style='text-align:center; color:#333; font-size:12px; padding:40px;'>© 2026 D.H.R.U.V.A. | LOGIC OVER FEAR</div>", unsafe_allow_html=True)