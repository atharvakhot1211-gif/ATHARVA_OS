import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import time

# 1. CLOUD CONNECTION SETUP
def get_gspread_client():
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    return gspread.authorize(creds)

# 2. APP CONFIG & THEME
st.set_page_config(page_title="ATHARVA OS", layout="wide")

# 3. HEADER HUD (Point 2 of Blueprint)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.metric("Live Day Score", "85%") # This will be dynamic later
with col2:
    st.markdown(f"<h1 style='text-align: center; color: #FFFFFF;'>ATHARVA OS</h1>", unsafe_allow_html=True)
with col3:
    st.write(f"🕒 **{current_time}**")
    st.write(f"📅 {now.strftime('%A, %d %b')}")

# Auto-Event Indicator (Point 2)
st.warning("⚠️ **Today's Market Status:** Nifty Expiry | No Market Holiday")

# Bhagwat Geeta Card (Point 2)
st.info("📜 **Daily Wisdom:** Focus on your action, not the fruit. (Chapter 2, Verse 47)")

# 4. MASTER NAVIGATION
tabs = st.tabs(["Checklist", "F&O Trading", "Wealth Vault", "RUDVION Agency", "Syllabus Hub"])

# --- TAB: F&O TRADING (Point 4) ---
with tabs[1]:
    st.subheader("⚡ Advanced F&O Floor")
    if 'trades' not in st.session_state: st.session_state.trades = []
    
    net_pnl = sum([t['pnl'] for t in st.session_state.trades])
    st.markdown(f"### Today's Net P&L: :green[₹{net_pnl}]" if net_pnl >= 0 else f"### Today's Net P&L: :red[₹{net_pnl}]")

    with st.expander("➕ Add Trade #", expanded=True):
        t_col1, t_col2 = st.columns(2)
        segment = t_col1.selectbox("Segment", ["Nifty", "BankNifty", "Crude Oil"])
        pnl_val = t_col2.number_input("Profit/Loss Amount", step=100.0)
        logic = st.text_area("MANDATORY: Trade Reasoning (The Logic Gate)")
        
        if st.button("Secure Trade Log"):
            if logic:
                st.session_state.trades.append({"Segment": segment, "pnl": pnl_val, "Reason": logic, "Time": now.strftime("%H:%M")})
                st.success("Trade Secured!")
            else:
                st.error("Logic Gate Locked: Enter reasoning first.")

# --- TAB: SYLLABUS HUB (Point 3) ---
with tabs[4]:
    st.subheader("📚 Infinite Syllabus Hub")
    if 'subjects' not in st.session_state: st.session_state.subjects = {}
    
    new_sub = st.text_input("Create New Subject Folder (e.g. Railway, NISM)")
    if st.button("Add Subject"):
        if new_sub: st.session_state.subjects[new_sub] = []
        
    for sub in st.session_state.subjects:
        with st.expander(f"📁 {sub}"):
            st.progress(0.4) # Subject Completion Bar
            topic = st.text_input(f"Add Topic to {sub}", key=f"in_{sub}")
            if st.button("Add Topic", key=f"btn_{sub}"):
                st.session_state.subjects[sub].append(topic)
            for t in st.session_state.subjects[sub]:
                st.checkbox(t, key=f"chk_{sub}_{t}")
                st.text_area("Session Notes", placeholder="What did you learn?", key=f"note_{sub}_{t}")

# --- TAB: RUDVION AGENCY (Point 5) ---
with tabs[3]:
    st.subheader("📁 RUDVION: Infinite Niche Vault")
    if 'niches' not in st.session_state: st.session_state.niches = ["Mughlai"]
    
    new_niche = st.text_input("Add New Niche Folder")
    if st.button("Create Folder"): st.session_state.niches.append(new_niche)
    
    sel_niche = st.selectbox("Select Niche", st.session_state.niches)
    st.write(f"### {sel_niche} Portfolio (Infinite Counter)")
    # Logic for Post #1, #2 to infinity goes here...

# --- TAB: WEALTH VAULT (Point 4) ---
with tabs[2]:
    st.subheader("💰 Infinite Wealth Folders")
    asset_cols = st.columns(4)
    with asset_cols[0]: st.number_input("SIP", min_value=0)
    with asset_cols[1]: st.number_input("Stocks/ETF", min_value=0)
    with asset_cols[2]: st.number_input("Gold", min_value=0)
    with asset_cols[3]: st.number_input("Cash", min_value=0)
    st.button("Add New Investment Category")

# --- DISCIPLINE GUARD (Point 6) ---
st.divider()
st.subheader("🔒 Midnight Lock & Plan")
col_a, col_b = st.columns(2)
with col_a:
    st.text_area("Learn-Log (Daily Lesson)")
with col_b:
    st.text_area("Plan for Tomorrow")