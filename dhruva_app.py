import streamlit as st
import pandas as pd
import datetime

# 1. PAGE CONFIG
st.set_page_config(
    page_title="D.H.R.U.V.A. | National Anomaly Research",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- DATABASE IN MEMORY ---
if 'missions' not in st.session_state: st.session_state['missions'] = [] 
if 'intel_reports' not in st.session_state: st.session_state['intel_reports'] = []
if 'contact_msgs' not in st.session_state: st.session_state['contact_msgs'] = []
if 'dir_img' not in st.session_state: st.session_state['dir_img'] = None
if 'logo_img' not in st.session_state: st.session_state['logo_img'] = None
if 'insp_img' not in st.session_state: st.session_state['insp_img'] = None
if 'about_txt' not in st.session_state: 
    st.session_state['about_txt'] = "We are the next generation of researchers, a youth-led unit driven by logic and modern physics."
if 'auth_status' not in st.session_state: st.session_state['auth_status'] = False

query_params = st.query_params
access_code = query_params.get("access", None)

# 2. IPS PREMIUM CSS (SKY BLUE THEME + GREEN EMAIL)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Raleway:wght@300;400&display=swap');
    .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Raleway', sans-serif; }
    .stTabs [data-baseweb="tab-list"] { background-color: #0A0A0A; border-bottom: 1px solid #111; justify-content: center; }
    .stTabs [data-baseweb="tab"] { color: #888 !important; font-weight: bold; font-size: 14px; letter-spacing: 1px;}
    .stTabs [aria-selected="true"] { color: #00D4FF !important; border-bottom: 2px solid #00D4FF; }
    .ips-title { font-family: 'Cinzel', serif; font-size: 55px; text-align: center; letter-spacing: 5px; margin-bottom: 0; }
    .ips-subtitle { font-family: 'Raleway', sans-serif; font-size: 14px; text-align: center; letter-spacing: 4px; color: #00D4FF; text-transform: uppercase; margin-bottom: 30px; }
    
    /* Green Email Box Styling from Image */
    .green-box-container {
        background-color: #0A0A0A; border: 1px solid #1A1A1A; padding: 35px;
        max-width: 550px; margin: 20px auto; border-radius: 8px; text-align: center;
    }
    .email-text { color: #2ECC71 !important; font-weight: bold; font-size: 22px; font-family: 'Courier New', monospace; text-decoration: none; }
    .ips-block { background-color: #0A0A0A; border-left: 3px solid #00D4FF; padding: 30px; margin: 30px 0; }
    
    /* Form and Sidebar Buttons */
    .stButton > button { background-color: #7B0000 !important; color: white; border-radius: 0; border: none; }
    .stTextInput > div > div > input, .stTextArea > div > div > textarea { background-color: #121212 !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER
col_h1, col_h2, col_h3 = st.columns([1, 4, 1])
with col_h2:
    if st.session_state['logo_img']: st.image(st.session_state['logo_img'], width=150)
    else: st.markdown("<h1 style='text-align:center;'>🦅</h1>", unsafe_allow_html=True)
    st.markdown("<div class='ips-title'>D.H.R.U.V.A.</div>", unsafe_allow_html=True)
    st.markdown("<div class='ips-subtitle'>National Research & Anomaly Society</div>", unsafe_allow_html=True)

# 4. TABS
tab1, tab2, tab3, tab4, tab5 = st.tabs(["HOME", "ABOUT US", "INVESTIGATIONS", "REPORT MYSTERY", "CONTACT"])

with tab1:
    st.markdown("<h2 style='text-align:center; font-family:Cinzel;'>WE INVESTIGATE WHAT OTHERS FEAR</h2>", unsafe_allow_html=True)
    col_i1, col_i2 = st.columns([1, 2])
    with col_i1:
        if st.session_state['insp_img']: st.image(st.session_state['insp_img'], use_container_width=True)
        else: st.info("Gaurav Tiwari Image Placeholder")
    with col_i2:
        st.markdown(f"<div class='ips-block'><h3 style='font-family:Cinzel;'>OUR INSPIRATION</h3><p style='font-style:italic; font-size:18px;'>\"Fear is just missing data. Logic is the cure.\"</p><p style='color:#00D4FF; font-weight:bold;'>- Late Rev. Gaurav Tiwari</p><p>Founder, Indian Paranormal Society</p></div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<h2 style='font-family:Cinzel;'>THE DIRECTORATE</h2>", unsafe_allow_html=True)
    col_dir1, col_dir2 = st.columns([1, 2])
    with col_dir1:
        if st.session_state['dir_img']: st.image(st.session_state['dir_img'], width=300)
        else: st.info("Founder Photo Placeholder")
    with col_dir2:
        st.markdown("<h3 style='color:#00D4FF !important;'>Pranav Anil Rahane</h3>", unsafe_allow_html=True)
        st.caption("Founder & Lead Investigator")
        st.write(st.session_state['about_txt'])

with tab3:
    st.markdown("<h2 style='font-family:Cinzel; text-align:center;'>CASE FILES</h2>", unsafe_allow_html=True)
    if not st.session_state['missions']: st.info("No declassified investigations yet.")
    for m in reversed(st.session_state['missions']):
        st.markdown(f"<div class='ips-block'><h4>{m['title']}</h4><p>{m['desc']}</p><b>VERDICT: {m['status']}</b></div>", unsafe_allow_html=True)

with tab4:
    with st.form("anomaly_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1: name = st.text_input("NAME"); phone = st.text_input("PHONE")
        with c2: loc = st.text_input("LOCATION"); m_type = st.selectbox("MYSTERY TYPE", ["Haunting", "UFO", "Shadow", "Poltergeist", "Other"])
        desc = st.text_area("DESCRIPTION")
        if st.form_submit_button("SUBMIT REPORT"):
            st.session_state['intel_reports'].append({"name": name, "phone": phone, "loc": loc, "type": m_type, "desc": desc, "time": str(datetime.datetime.now())})
            st.success("REPORT SENT TO HQ.")

with tab5:
    st.markdown("<h2 style='font-family:Cinzel; text-align:center;'>CONTACT US</h2>", unsafe_allow_html=True)
    st.markdown(f'<div class="green-box-container"><div style="color:#555; text-align:left; font-size:12px;">Email:</div><a href="mailto:team.dhruva.research@gmail.com" class="email-text">✉️ team.dhruva.research@gmail.com</a></div>', unsafe_allow_html=True)
    with st.form("contact_msg_form", clear_on_submit=True):
        st.markdown("<h4 style='text-align:center;'>SEND US A MESSAGE</h4>", unsafe_allow_html=True)
        cn = st.text_input("FULL NAME"); ce = st.text_input("EMAIL ADDRESS"); cm = st.text_area("MESSAGE")
        if st.form_submit_button("SEND MESSAGE"):
            st.session_state['contact_msgs'].append({"name": cn, "email": ce, "msg": cm, "time": str(datetime.datetime.now())})
            st.success("MESSAGE TRANSMITTED.")

# 5. HIDDEN ADMIN PANEL (FIXED)
if access_code == "classified":
    with st.sidebar:
        st.markdown("### 🔐 HQ CONTROL")
        if not st.session_state['auth_status']:
            user_input = st.text_input("ID", key="admin_user")
            pass_input = st.text_input("KEY", type="password", key="admin_pass")
            if st.button("LOGIN"):
                if user_input == "Pranav" and pass_input == "DhruvaBot":
                    st.session_state['auth_status'] = True
                    st.rerun()
                else: st.error("ACCESS DENIED")
        
        if st.session_state['auth_status']:
            st.success("DIRECTOR ONLINE")
            if st.button("LOGOUT"):
                st.session_state['auth_status'] = False
                st.rerun()

            with st.expander("📤 UPLOAD ASSETS"):
                logo = st.file_uploader("Agency Logo", key="logo_up")
                if logo: st.session_state['logo_img'] = logo
                founder = st.file_uploader("Founder Image", key="dir_up")
                if founder: st.session_state['dir_img'] = founder
                gt = st.file_uploader("Gaurav Tiwari Image", key="gt_up")
                if gt: st.session_state['insp_img'] = gt
            
            with st.expander("📝 EDIT ABOUT"):
                st.session_state['about_txt'] = st.text_area("Update Information", st.session_state['about_txt'])
            
            with st.expander("📨 VIEW INTEL"):
                for r in reversed(st.session_state['intel_reports']):
                    st.write(f"**From:** {r['name']} ({r['phone']})\n**Desc:** {r['desc']}")
                    st.markdown("---")

            with st.expander("💬 VIEW MESSAGES"):
                for c in reversed(st.session_state['contact_msgs']):
                    st.write(f"**From:** {c['name']} ({c['email']})\n**Msg:** {c['msg']}")
                    st.markdown("---")
            
            with st.expander("📤 PUBLISH CASE"):
                with st.form("pub_case"):
                    mt = st.text_input("Case Title"); ms = st.selectbox("Verdict", ["SOLVED", "UNEXPLAINED"])
                    md = st.text_area("Investigation Summary")
                    if st.form_submit_button("PUBLISH LIVE"):
                        st.session_state['missions'].append({"title": mt, "status": ms, "desc": md})
                        st.success("Case Published.")

st.markdown("<div style='text-align:center; color:#333; font-size:12px; padding:40px;'>© 2026 D.H.R.U.V.A. | LOGIC OVER FEAR</div>", unsafe_allow_html=True)
