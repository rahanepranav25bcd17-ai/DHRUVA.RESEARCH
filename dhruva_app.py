import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import datetime

# 1. PAGE CONFIG
st.set_page_config(
    page_title="D.H.R.U.V.A. | National Anomaly Research",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- GOOGLE SHEETS CONNECTION ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
except Exception:
    conn = None

# --- AUTHENTICATION STATE ---
if 'auth_status' not in st.session_state: 
    st.session_state['auth_status'] = False

query_params = st.query_params
access_code = query_params.get("access", None)

# 2. IPS PREMIUM CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Raleway:wght@300;400&display=swap');
    .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Raleway', sans-serif; }
    .stTabs [data-baseweb="tab-list"] { background-color: #0A0A0A; border-bottom: 1px solid #111; justify-content: center; }
    .stTabs [data-baseweb="tab"] { color: #888 !important; font-weight: bold; font-size: 14px; letter-spacing: 1px;}
    .stTabs [aria-selected="true"] { color: #00D4FF !important; border-bottom: 2px solid #00D4FF; }
    .ips-title { font-family: 'Cinzel', serif; font-size: 55px; text-align: center; letter-spacing: 5px; margin-bottom: 0; }
    .ips-subtitle { font-family: 'Raleway', sans-serif; font-size: 14px; text-align: center; letter-spacing: 4px; color: #00D4FF; text-transform: uppercase; margin-bottom: 30px; }
    
    .green-box-container {
        background-color: #0A0A0A; border: 1px solid #1A1A1A; padding: 35px;
        max-width: 550px; margin: 20px auto; border-radius: 8px; text-align: center;
    }
    .email-text { color: #2ECC71 !important; font-weight: bold; font-size: 22px; font-family: 'Courier New', monospace; text-decoration: none; }
    .ips-block { background-color: #0A0A0A; border-left: 3px solid #00D4FF; padding: 30px; margin: 30px 0; }
    .stButton > button { background-color: #7B0000 !important; color: white; border-radius: 0; border: none; }
    
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: #121212 !important; color: white !important; border: 1px solid #222 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER
col_h1, col_h2, col_h3 = st.columns([1, 4, 1])
with col_h2:
    try: st.image("logo.png", width=150)
    except: st.markdown("<h1 style='text-align:center;'>🦅</h1>", unsafe_allow_html=True)
    st.markdown("<div class='ips-title'>D.H.R.U.V.A.</div>", unsafe_allow_html=True)
    st.markdown("<div class='ips-subtitle'>National Research & Anomaly Society</div>", unsafe_allow_html=True)

# 4. TABS
tab1, tab2, tab3, tab4, tab5 = st.tabs(["HOME", "ABOUT US", "INVESTIGATIONS", "REPORT MYSTERY", "CONTACT"])

with tab1:
    st.markdown("<h2 style='text-align:center; font-family:Cinzel;'>WE INVESTIGATE WHAT OTHERS FEAR</h2>", unsafe_allow_html=True)
    col_i1, col_i2 = st.columns([1, 2])
    with col_i1:
        try: st.image("gaurav_tiwari.png", use_container_width=True)
        except: st.info("Gaurav Tiwari Image")
    with col_i2:
        st.markdown(f"<div class='ips-block'><h3 style='font-family:Cinzel;'>OUR INSPIRATION</h3><p style='font-style:italic; font-size:18px;'>\"Fear is just missing data. Logic is the cure.\"</p><p style='color:#00D4FF; font-weight:bold;'>- Late Rev. Gaurav Tiwari</p><p>Founder, Indian Paranormal Society</p></div>", unsafe_allow_html=True)

with tab2:
    col_dir1, col_dir2 = st.columns([1, 2])
    with col_dir1:
        try: st.image("director.png", width=300)
        except: st.info("Founder Photo")
    with col_dir2:
        st.markdown("<h3 style='color:#00D4FF !important;'>Pranav Anil Rahane</h3>", unsafe_allow_html=True)
        st.caption("Founder & Chief Investigator")
        st.write("D.H.R.U.V.A. is a specialized research unit dedicated to understanding unexplained phenomena through the lens of physics, engineering, and logic. We are a team of young researchers driven by logic, not fear.")

with tab3:
    st.markdown("<h2 style='font-family:Cinzel; text-align:center;'>CASE FILES</h2>", unsafe_allow_html=True)
    if conn:
        try:
            df_inv = conn.read(worksheet="Investigations")
            for _, m in df_inv.iterrows():
                st.markdown(f"<div class='ips-block'><h4>{m['Title']}</h4><p>{m['Details']}</p><b>VERDICT: {m['Verdict']}</b></div>", unsafe_allow_html=True)
        except: st.info("No cases available yet.")
    else: st.info("Database connection pending.")

with tab4:
    with st.form("anomaly_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1: name = st.text_input("NAME"); phone = st.text_input("PHONE")
        with c2: loc = st.text_input("LOCATION"); m_type = st.selectbox("TYPE", ["Haunting", "UFO", "Shadow Figure", "Other"])
        desc = st.text_area("DESCRIPTION")
        if st.form_submit_button("TRANSMIT INTEL"):
            if conn:
                new_rep = pd.DataFrame([{"Timestamp": str(datetime.datetime.now()), "Name": name, "Phone": phone, "Loc": loc, "Type": m_type, "Desc": desc}])
                try:
                    existing = conn.read(worksheet="Reports")
                    updated = pd.concat([existing, new_rep], ignore_index=True)
                    conn.update(worksheet="Reports", data=updated)
                    st.success("INTEL SAVED PERMANENTLY.")
                except: st.error("Database connection failed.")
            else: st.warning("Database not connected.")

with tab5:
    st.markdown(f'<div class="green-box-container"><div style="color:#555; text-align:left; font-size:12px;">Email:</div><a href="mailto:team.dhruva.research@gmail.com" class="email-text">✉️ team.dhruva.research@gmail.com</a></div>', unsafe_allow_html=True)
    with st.form("contact_msg_form", clear_on_submit=True):
        st.markdown("<h4 style='text-align:center;'>SEND US A MESSAGE</h4>", unsafe_allow_html=True)
        cn = st.text_input("FULL NAME"); ce = st.text_input("EMAIL"); cm = st.text_area("MESSAGE")
        if st.form_submit_button("SEND MESSAGE"):
            if conn:
                new_msg = pd.DataFrame([{"Timestamp": str(datetime.datetime.now()), "Name": cn, "Email": ce, "Message": cm}])
                try:
                    existing = conn.read(worksheet="Messages")
                    updated = pd.concat([existing, new_msg], ignore_index=True)
                    conn.update(worksheet="Messages", data=updated)
                    st.success("MESSAGE SENT PERMANENTLY.")
                except: st.error("Storage error.")

# 5. HIDDEN ADMIN PANEL
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
            
            with st.expander("📤 PUBLISH CASE"):
                with st.form("pub_case"):
                    mt = st.text_input("Title"); ms = st.selectbox("Verdict", ["SOLVED", "UNEXPLAINED", "DEBUNKED"])
                    md = st.text_area("Details")
                    if st.form_submit_button("PUBLISH LIVE"):
                        if conn:
                            new_case = pd.DataFrame([{"Title": mt, "Verdict": ms, "Details": md, "Date": str(datetime.date.today())}])
                            try:
                                existing = conn.read(worksheet="Investigations")
                                updated = pd.concat([existing, new_case], ignore_index=True)
                                conn.update(worksheet="Investigations", data=updated)
                                st.success("Case Published.")
                            except: st.error("Database error.")

st.markdown("<div style='text-align:center; color:#333; font-size:12px; padding:40px;'>© 2026 D.H.R.U.V.A. | LOGIC OVER FEAR</div>", unsafe_allow_html=True)
