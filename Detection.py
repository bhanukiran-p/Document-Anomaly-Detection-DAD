





















# import streamlit as st 
# import pandas as pd
# import numpy as np
# from PIL import Image
# import tempfile
# import os
# from datetime import datetime
# import warnings
# warnings.filterwarnings("ignore")
# import base64

# # ----- Page config -----
# st.set_page_config(
#     page_title="Xforia DAD - Fraud Detection",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # ---------- Dashboard navigation ----------
# DASHBOARD_CANDIDATES = [
#     "pages/Dashboard.py",
#     "pages/1_Dashboard.py",
#     "pages/2_Dashboard.py",
#     "pages/DASHBOARD.py",
#     "Dashboard",
#     "DASHBOARD",
# ]

# def go_dashboard():
#     for target in DASHBOARD_CANDIDATES:
#         try:
#             st.switch_page(target)
#             return
#         except Exception:
#             continue
#     st.warning("Couldn't navigate to Dashboard.")

# # ========= SIMPLIFIED CLEAN STYLES =========
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

# :root { 
#     --brand: #1e3c72;
#     --brand2: #2a5298;
#     --brand3: #db123d;
#     --text: #0f172a;
#     --muted: #475569;
#     --card: #f8fafc;
#     --line: #e2e8f0;
#     --bg: #f5f5f5;
# }

# * { font-family: 'Inter', ui-sans-serif, system-ui, -apple-system, 'Segoe UI', sans-serif; }

# .stApp { background: var(--bg); padding-bottom: 80px !important; }

# /* Hide Streamlit Elements */
# header[data-testid="stHeader"],
# section[aria-label="sidebar"],
# [data-testid="stSidebar"],
# [data-testid="stSidebarNav"],
# [data-testid="stSidebarContent"],
# [data-testid="stSidebarCollapseButton"],
# [data-testid="collapsedControl"],
# [data-testid="stToolbar"],
# [data-testid="stDock"],
# #MainMenu,
# footer { display: none !important; }

# [data-testid="stAppViewContainer"] { padding-top: 1rem !important; }
# .main .block-container { padding-top: 1rem !important; max-width: 1200px !important; margin: 0 auto !important; }

# /* Page Title */
# .page-title { font-size: 2rem; font-weight: 700; color: var(--text); margin: 1.5rem 0 2rem 0; letter-spacing: -0.02em; }

# /* Simple Tabs */
# .stTabs [data-baseweb="tab-list"] {
#     background: transparent;
#     border-bottom: 2px solid var(--line);
#     padding: 0;
#     gap: 0;
# }

# /* HIDE ANY EMPTY/BLANK TABS (prevents blank ones from ever showing) */
# .stTabs [data-baseweb="tab"]:has(div:empty) { display: none !important; }

# .stTabs [data-baseweb="tab"] {
#     background: transparent;
#     border: none !important;
#     padding: 12px 24px;
#     font-weight: 600;
#     font-size: 1rem;
#     color: var(--muted);
#     border-bottom: 3px solid transparent;
#     margin-bottom: -2px;
# }
# .stTabs [data-baseweb="tab"]:hover { color: var(--text); }
# .stTabs [data-baseweb="tab"][aria-selected="true"] { color: var(--brand3); border-bottom: 3px solid var(--brand3); }

# /* Section Title */
# .section-title { font-size: 1.5rem; font-weight: 700; color: var(--text); margin: 2rem 0 1.5rem 0; }

# /* Simple Card */
# .simple-card {
#     background: white; border-radius: 8px; padding: 2rem;
#     box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid var(--line); margin-bottom: 2rem;
# }

# /* File Uploader */
# [data-testid="stFileUploader"] { background: #f8f9fa; border: 2px dashed #dee2e6; border-radius: 8px; padding: 2rem; text-align: center; }
# [data-testid="stFileUploader"]:hover { border-color: #adb5bd; }
# [data-testid="stFileUploader"] section { border: none !important; }
# [data-testid="stFileUploader"] label,
# [data-testid="stFileUploader"] small,
# [data-testid="stFileUploader"] [aria-live="polite"] { display: none !important; }

# /* Center Button Container */
# .center-button-wrapper { display: flex; justify-content: center; margin: 3rem 0 2rem 0; }

# /* Primary Button */
# .stButton > button {
#     background: var(--brand3) !important; color: white !important; border: none !important;
#     border-radius: 8px !important; padding: 0.875rem 3rem !important; font-weight: 700 !important;
#     font-size: 0.95rem !important; letter-spacing: 0.05em !important; text-transform: uppercase !important;
#     box-shadow: none !important; transition: all 0.2s ease !important; min-width: 300px !important;
# }
# .stButton > button:hover { filter: brightness(0.95) !important; }
# .stButton > button:active { transform: translateY(1px) !important; }

# /* Results Card */
# .results-card {
#     background: var(--card); border-radius: 16px; padding: 2rem;
#     box-shadow: 0 4px 12px rgba(15,23,42,0.05); border: 1px solid var(--line);
#     height: 100%; position: relative; overflow: hidden; transition: all 0.3s; margin-bottom: 1rem;
# }
# .results-card::before {
#     content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px;
#     background: linear-gradient(90deg, var(--brand), var(--brand2)); opacity: 0; transition: opacity 0.3s;
# }
# .results-card:hover::before { opacity: 1; }
# .results-card:hover { transform: translateY(-4px); box-shadow: 0 12px 32px rgba(15,23,42,0.12); border-color: var(--brand); }
# .results-card h3 { font-size: 1.15rem; font-weight: 800; color: var(--text); margin-bottom: 1.5rem; letter-spacing: -0.01em; }

# /* Risk Badge/Score */
# .risk-container { text-align: center; padding: 2rem; border-radius: 16px; margin-bottom: 1.5rem; background: var(--card); border: 1px solid var(--line); box-shadow: 0 4px 12px rgba(15,23,42,0.05); }
# .risk-badge { display: inline-flex; align-items: center; gap: .5rem; padding: .75rem 1.5rem; border-radius: 50px; font-weight: 800; font-size: 1rem; letter-spacing: .05em; margin-bottom: 1rem; }
# .badge-low { background:#059669; color:#fff; box-shadow:0 4px 12px rgba(5,150,105,.3); }
# .badge-medium { background:#f59e0b; color:#fff; box-shadow:0 4px 12px rgba(245,158,11,.3); }
# .badge-high { background: var(--brand3); color:#fff; box-shadow:0 4px 12px rgba(219,18,61,.3); }
# .risk-score { font-size: 3.5rem; font-weight: 900; margin: .5rem 0; line-height: 1; }
# .score-low { color:#059669 } .score-medium { color:#f59e0b } .score-high { color: var(--brand3) }
# .risk-label { font-size: .9rem; color: var(--muted); font-weight: 600; text-transform: uppercase; letter-spacing: .1em; }

# /* Info Section */
# .info-section { background: var(--card); border-radius: 16px; padding: 1.5rem; margin-bottom: 1.5rem; border: 1px solid var(--line); box-shadow: 0 4px 12px rgba(15,23,42,.05); }
# .info-section h4 { font-size: 1.1rem; font-weight: 800; color: var(--brand); margin-bottom: 1rem; display: flex; align-items: center; gap: .5rem; letter-spacing: -0.01em; }
# .info-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: .75rem; }
# .info-item { background: #fff; padding: .875rem; border-radius: 8px; border-left: 3px solid var(--brand); transition: transform .2s; }
# .info-item:hover { transform: translateX(4px); }
# .info-label { font-size: .75rem; color: var(--muted); font-weight: 600; text-transform: uppercase; letter-spacing: .05em; margin-bottom: .25rem; }
# .info-value { font-size: 1rem; color: var(--text); font-weight: 600; }

# /* Risk Factors */
# .risk-factors { background: var(--card); border-radius: 16px; padding: 1.5rem; margin-bottom: 1.5rem; border: 1px solid var(--line); box-shadow: 0 4px 12px rgba(15,23,42,.05); }
# .risk-factors h4 { font-size: 1.1rem; font-weight: 800; color: var(--brand); margin-bottom: 1rem; display: flex; align-items: center; gap: .5rem; letter-spacing: -0.01em; }
# .risk-factor-item { background: #fff; padding: 1rem; border-radius: 8px; margin-bottom: .5rem; display: flex; align-items: center; gap: .75rem; border-left: 3px solid var(--brand); font-size: .95rem; color: var(--text); box-shadow: 0 2px 8px rgba(0,0,0,.06); transition: transform .2s, box-shadow .2s; }
# .risk-factor-item:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,.1); }
# .risk-factor-icon { width: 24px; height: 24px; border-radius: 50%; background: #fef3c7; display:flex; align-items:center; justify-content:center; flex-shrink:0; font-weight:700; color:#f59e0b; }

# /* Recommendations */
# .recommendation-box { border-radius: 16px; padding: 1.5rem; margin-bottom: 1.5rem; border: 1px solid var(--line); box-shadow: 0 4px 12px rgba(15,23,42,.05); }
# .rec-low { background:#d1fae5; border-color:#059669; }
# .rec-medium { background:#fef3c7; border-color:#f59e0b; }
# .rec-high { background:#fee2e2; border-color: var(--brand3); }
# .recommendation-box h4 { font-size: 1.1rem; font-weight: 800; margin-bottom: .75rem; display:flex; align-items:center; gap:.5rem; letter-spacing:-0.01em; }
# .rec-low h4 { color:#059669 } .rec-medium h4 { color:#f59e0b } .rec-high h4 { color: var(--brand3) }
# .recommendation-list { list-style:none; padding:0; margin:0; }
# .recommendation-list li { padding:.5rem 0; color:var(--text); font-weight:500; display:flex; align-items:center; gap:.5rem; }

# /* Inputs */
# .stTextInput input, .stSelectbox select {
#     border-radius: 6px !important; border: 1px solid var(--line) !important;
#     padding: .625rem .875rem !important; font-size: .95rem !important;
# }
# .stTextInput input:focus, .stSelectbox select:focus { border-color: var(--brand) !important; box-shadow: 0 0 0 2px rgba(30,60,114,.1) !important; }
# .stTextInput label, .stSelectbox label { font-weight: 600 !important; color: var(--text) !important; font-size: .9rem !important; }

# /* Progress */
# [data-testid="stProgress"] > div { background: var(--line) !important; border-radius: 50px !important; height: 12px !important; }
# [data-testid="stProgress"] > div > div { border-radius: 50px !important; background: linear-gradient(90deg,#059669 0%,#f59e0b 50%,var(--brand3) 100%) !important; }

# /* Footer */
# .custom-footer {
#     position: fixed; bottom: 0; left: 0; right: 0; background: #2c5282; color: white;
#     padding: 1rem; display: flex; align-items: center; justify-content: center; gap: 1.5rem;
#     font-weight: 600; font-size: .95rem; height: 60px; z-index: 9999;
# }
# .footer-divider { color: white; opacity: .6; }

# /* Empty State */
# .empty-state { text-align:center; padding:3rem 2rem; color: var(--muted); }
# .empty-state h4 { font-size: 1.2rem; font-weight: 700; color: var(--text); margin-bottom: .5rem; }

# /* Icons */
# .icon-shield, .icon-alert, .icon-check, .icon-info { width: 20px; height: 20px; display: inline-block; vertical-align: middle; }

# /* Responsive */
# @media (max-width: 768px) {
#     .info-grid { grid-template-columns: 1fr; }
#     .risk-score { font-size: 2.5rem; }
# }
# </style>
# """, unsafe_allow_html=True)

# # SVG Icons
# def icon_shield():
#     return """<svg class="icon-shield" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
#         <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>"""

# def icon_alert():
#     return """<svg class="icon-alert" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
#         <circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>"""

# def icon_check():
#     return """<svg class="icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
#         <polyline points="20 6 9 17 4 12"/></svg>"""

# def icon_info():
#     return """<svg class="icon-info" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
#         <circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>"""

# # ---------- Fixed logo ----------
# def add_fixed_logo():
#     import pathlib
#     cwd = pathlib.Path(os.getcwd())
#     here = pathlib.Path(__file__).parent if "__file__" in globals() else cwd
#     candidates = [cwd / "FDN.png", here / "FDN.png", here / "assets" / "FDN.png", cwd / "assets" / "FDN.png"]
#     logo_path = next((p for p in candidates if p.exists()), None)
#     if not logo_path:
#         return
#     encoded = base64.b64encode(logo_path.read_bytes()).decode()
#     st.markdown(f"""
#     <style>
#       .fixed-logo {{ position: fixed; top: 1rem; left: 2rem; z-index: 10000; background: white; border-radius: 4px; padding: .25rem .5rem; }}
#       .fixed-logo img {{ width: 140px; height: 45px; display: block; }}
#     </style>
#     <div class="fixed-logo">
#       <a href="/" target="_self"><img src="data:image/png;base64,{encoded}" alt="Logo" /></a>
#     </div>
#     """, unsafe_allow_html=True)

# add_fixed_logo()

# # ---------- Splash screen ----------
# try:
#     from splash_screen import show_splash
# except Exception:
#     def show_splash():
#         st.markdown("""
#             <div style="display:flex;flex-direction:column;align-items:center;gap:12px;margin-top:40px;">
#                 <h1 style="margin:0;">Welcome to Fraud Detection</h1>
#                 <p style="opacity:.8;margin:0;">Your Guardian Against Fraud</p>
#             </div>
#         """, unsafe_allow_html=True)
#         if st.button("Get Started", type="primary"):
#             st.session_state.show_splash = False
#             st.rerun()

# if "show_splash" not in st.session_state:
#     st.session_state.show_splash = True

# if st.session_state.show_splash:
#     show_splash()
#     st.stop()

# # ---------- ML helpers ----------
# try:
#     from ML_Model import ml_transaction_analysis, mock_transaction_analysis
# except ImportError:
#     def ml_transaction_analysis(data):
#         import hashlib
#         h = hashlib.sha256(str(data).encode()).hexdigest()
#         return (int(h, 16) % 1000) / 1000.0
#     mock_transaction_analysis = ml_transaction_analysis

# # ===================== MINDEE CONFIG =====================
# MINDEE_API_KEY = "md_KqeDU4LG1zvPTpm7yANOMZsU5bDnb3MN"
# MINDEE_ACCOUNT_NAME = ""
# MINDEE_ENDPOINT_NAME = ""
# MINDEE_VERSION = "1"
# MINDEE_MODEL_ID = "ae8aebe3-40a8-49ec-9545-daf787b1bbe5"

# def extract_check_data(response):
#     try:
#         fields = response.inference.result.fields
#         names = ['memo','pay_to','bank_name','signature','check_date','payer_name',
#                  'word_amount','check_number','number_amount','payer_address',
#                  'account_number','routing_number']
#         return {n: (fields[n].value if n in fields else None) for n in names}
#     except Exception as e:
#         st.error(f"Error extracting check data: {e}")
#         return None

# def convert_ocr_to_ml_format(check_data):
#     amount = check_data.get('number_amount', 0) or 0
#     return {
#         'account_number': str(check_data.get('account_number') or 'UNKNOWN'),
#         'amount': float(amount),
#         'type': 'Check',
#         'merchant': str(check_data.get('memo') or 'Check Payment'),
#         'location': 'Unknown',
#         'recipient': str(check_data.get('pay_to') or 'Unknown'),
#         'time': 'Morning (6AM-12PM)',
#         'device': 'Check'
#     }

# def calculate_fraud_score(check_data):
#     s = 0.1
#     if not check_data.get('pay_to'): s += 0.2
#     if not check_data.get('number_amount'): s += 0.3
#     if not check_data.get('signature'): s += 0.3
#     if not check_data.get('bank_name'): s += 0.2
#     if not check_data.get('account_number'): s += 0.2
#     if not check_data.get('routing_number'): s += 0.2
#     amt = check_data.get('number_amount', 0)
#     if amt and amt > 10000: s += 0.2
#     elif amt and amt > 5000: s += 0.1
#     words = check_data.get('word_amount', '')
#     if words and amt and len(words.split()) < 3: s += 0.1
#     cd = check_data.get('check_date')
#     if cd:
#         try:
#             d = datetime.strptime(str(cd), '%Y-%m-%d')
#             days = (datetime.now() - d).days
#             if days > 180: s += 0.2
#             elif days > 90: s += 0.1
#         except:
#             s += 0.1
#     return min(s, 0.95)

# def mindee_ocr_analysis_with_ml(image_file):
#     try:
#         try:
#             from mindee import ClientV2, InferenceParameters
#         except ImportError:
#             st.error("Mindee SDK not installed.")
#             return (None,)*6

#         if not MINDEE_API_KEY:
#             st.error("MINDEE_API_KEY is not set.")
#             return (None,)*6

#         try:
#             client = ClientV2(MINDEE_API_KEY, region="us")
#         except TypeError:
#             client = ClientV2(MINDEE_API_KEY)

#         with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp:
#             tmp.write(image_file.read())
#             path = tmp.name

#         try:
#             src = client.source_from_path(path)

#             if MINDEE_ACCOUNT_NAME and MINDEE_ENDPOINT_NAME:
#                 params = InferenceParameters(
#                     account_name=MINDEE_ACCOUNT_NAME,
#                     endpoint_name=MINDEE_ENDPOINT_NAME,
#                     version=MINDEE_VERSION or "1",
#                 )
#             elif MINDEE_MODEL_ID:
#                 params = InferenceParameters(model_id=MINDEE_MODEL_ID)
#             else:
#                 st.error("Mindee not configured.")
#                 return (None,)*6

#             resp = client.enqueue_and_get_inference(src, params)
#             check_data = extract_check_data(resp)
            
#             if not check_data:
#                 return (None,)*6

#             extracted = {
#                 "Pay To": check_data.get('pay_to', 'N/A'),
#                 "Bank Name": check_data.get('bank_name', 'N/A'),
#                 "Check Date": check_data.get('check_date', 'N/A'),
#                 "Payer Name": check_data.get('payer_name', 'N/A'),
#                 "Amount (Words)": check_data.get('word_amount', 'N/A'),
#                 "Amount (Number)": f"${check_data.get('number_amount', 0):,.2f}" if check_data.get('number_amount') else 'N/A',
#                 "Check Number": check_data.get('check_number', 'N/A'),
#                 "Account Number": check_data.get('account_number', 'N/A'),
#                 "Routing Number": check_data.get('routing_number', 'N/A'),
#                 "Payer Address": check_data.get('payer_address', 'N/A'),
#                 "Memo": check_data.get('memo', 'N/A'),
#                 "Signature Present": "Yes" if check_data.get('signature') else "No"
#             }

#             tx = convert_ocr_to_ml_format(check_data)
#             ml_res = ml_transaction_analysis(tx)
            
#             if isinstance(ml_res, dict):
#                 ml_score = float(ml_res.get('ensemble_probability', 0.0))
#                 ml_ens = ml_res
#             else:
#                 ml_score = float(ml_res or 0.0)
#                 ml_ens = None

#             rule_score = calculate_fraud_score(check_data)
#             combined = ml_score * 0.7 + rule_score * 0.3
#             return extracted, combined, check_data, ml_score, rule_score, ml_ens

#         finally:
#             try:
#                 os.unlink(path)
#             except Exception:
#                 pass

#     except Exception as e:
#         st.error(f"Error processing check: {e}")
#         return (None,)*6

# def get_risk_level(score):
#     if score >= 0.7: return "HIGH RISK", "high"
#     elif score >= 0.4: return "MEDIUM RISK", "medium"
#     else: return "LOW RISK", "low"

# def get_check_risk_factors(check_data, ml_score, rule_score):
#     f = []
#     if not check_data.get('signature'): f.append("Missing signature")
#     if not check_data.get('number_amount'): f.append("Missing amount")
#     if not check_data.get('pay_to'): f.append("Missing payee")
#     if not check_data.get('bank_name'): f.append("Missing bank information")
#     amt = check_data.get('number_amount', 0)
#     if amt and amt > 10000: f.append("Very high check amount")
#     elif amt and amt > 5000: f.append("High check amount")
#     cd = check_data.get('check_date')
#     if cd:
#         try:
#             days = (datetime.now() - datetime.strptime(str(cd), '%Y-%m-%d')).days
#             if days > 180: f.append("Check is over 6 months old")
#             elif days > 90: f.append("Check is over 3 months old")
#         except:
#             f.append("Invalid check date")
#     if ml_score > 0.8: f.append("AI detected very high fraud risk")
#     elif ml_score > 0.6: f.append("AI detected elevated fraud risk")
#     words = check_data.get('word_amount', '')
#     if words and amt and len(words.split()) < 3: f.append("Incomplete written amount")
#     return f if f else ["No significant risk factors detected"]

# def get_detailed_risk_factors(transaction_data, fraud_score):
#     f = []
#     amount = float(transaction_data.get('amount', 0))
#     if amount > 10000: f.append(f"Very high transaction amount (${amount:,.2f})")
#     elif amount > 5000: f.append(f"High transaction amount (${amount:,.2f})")
#     elif amount > 1000: f.append(f"Moderate transaction amount (${amount:,.2f})")
    
#     tod = transaction_data.get('time', '')
#     if "Night" in tod: f.append("Unusual transaction time (night hours)")
    
#     device = transaction_data.get('device', '')
#     if device == "ATM" and amount > 1000: f.append("Large ATM withdrawal")
    
#     loc = (transaction_data.get('location') or '').strip().lower()
#     if not loc or loc == 'unknown': f.append("Unknown transaction location")
    
#     rec = transaction_data.get('recipient', '')
#     if not rec or rec.lower() == 'unknown': f.append("Unverified recipient")
    
#     if fraud_score > 0.8: f.append("AI model shows very high fraud confidence")
#     elif fraud_score > 0.6: f.append("AI model shows elevated fraud risk")
#     elif fraud_score > 0.4: f.append("AI model shows moderate fraud risk")
    
#     return f if f else ["No significant risk factors detected"]

# # ===================== PAGE TITLE =====================
# st.markdown("<h1 class='page-title'>AI-Powered Fraud Detection System</h1>", unsafe_allow_html=True)

# # ===================== TABS (EXPLICITLY ONLY TWO) =====================
# tab_labels = ["Check Analysis", "Online Transaction Analysis"]  # no blanks allowed
# tab1, tab2 = st.tabs(tab_labels)

# # ===== CHECK ANALYSIS TAB =====
# with tab1:
#     st.markdown("<h2 class='section-title'>Enhanced Check Analysis with AI</h2>", unsafe_allow_html=True)
#     col1, col2 = st.columns([1, 1], gap="large")
    
#     with col1:
#         st.markdown('<div class="simple-card">', unsafe_allow_html=True)
#         uploaded_file = st.file_uploader(
#             "Drop your check image here",
#             type=['jpg', 'jpeg', 'png'],
#             help="Upload a clear photo of your check",
#             label_visibility="collapsed"
#         )
#         if uploaded_file:
#             try:
#                 uploaded_file.seek(0)
#                 img = Image.open(uploaded_file)
#                 st.image(img, use_container_width=True)
#                 st.markdown("</div>", unsafe_allow_html=True)
#                 if st.button("Analyze Check", type="primary"):
#                     with st.spinner("Analyzing your check..."):
#                         uploaded_file.seek(0)
#                         extracted, combined, raw, ml_s, rule_s, ml_ens = mindee_ocr_analysis_with_ml(uploaded_file)
#                     if extracted and combined is not None:
#                         st.success("Check processed successfully!")
#                         st.session_state.check_results = {
#                             'extracted_data': extracted,
#                             'fraud_score': combined,
#                             'ml_score': ml_s,
#                             'rule_score': rule_s,
#                             'raw_data': raw,
#                             'ml_ensemble': ml_ens
#                         }
#                         st.rerun()
#                     else:
#                         st.error("Unable to process the check. Please try again.")
#             except Exception as e:
#                 st.error(f"Error: {e}")
#         else:
#             st.markdown("</div>", unsafe_allow_html=True)
    
#     with col2:
#         if 'check_results' in st.session_state:
#             res = st.session_state.check_results
#             fs = res['fraud_score']
#             ml_score = res.get('ml_score', 0)
#             rule_score = res.get('rule_score', 0)
#             level, risk_class = get_risk_level(fs)
            
#             st.markdown('<div class="results-card">', unsafe_allow_html=True)
#             st.markdown("<h3>Enhanced Analysis Results</h3>", unsafe_allow_html=True)
#             st.markdown(f"""
#                 <div class="risk-container">
#                     <div class="risk-badge badge-{risk_class}">{level}</div>
#                     <div class="risk-score score-{risk_class}">{fs*100:.0f}%</div>
#                     <div class="risk-label">Fraud Risk Score</div>
#                 </div>
#             """, unsafe_allow_html=True)
#             st.progress(float(fs))
#             st.markdown('<div class="info-section">', unsafe_allow_html=True)
#             st.markdown(f"<h4>{icon_info()} Extracted Information</h4>", unsafe_allow_html=True)
#             st.markdown('<div class="info-grid">', unsafe_allow_html=True)
#             for k, v in res['extracted_data'].items():
#                 st.markdown(f"""
#                     <div class="info-item">
#                         <div class="info-label">{k}</div>
#                         <div class="info-value">{v}</div>
#                     </div>
#                 """, unsafe_allow_html=True)
#             st.markdown('</div></div>', unsafe_allow_html=True)
#             factors = get_check_risk_factors(res.get('raw_data', {}), ml_score, rule_score)
#             st.markdown('<div class="risk-factors">', unsafe_allow_html=True)
#             st.markdown(f"<h4>{icon_alert()} Risk Factors</h4>", unsafe_allow_html=True)
#             for factor in factors:
#                 st.markdown(f"""
#                     <div class="risk-factor-item">
#                         <div class="risk-factor-icon">!</div>
#                         <span>{factor}</span>
#                     </div>
#                 """, unsafe_allow_html=True)
#             st.markdown('</div>', unsafe_allow_html=True)
#             if fs >= 0.7:
#                 st.markdown(f"""
#                     <div class="recommendation-box rec-high">
#                         <h4>{icon_shield()} Recommendations</h4>
#                         <ul class="recommendation-list">
#                             <li>{icon_check()} High fraud risk detected - Recommend manual verification and additional authentication</li>
#                         </ul>
#                     </div>
#                 """, unsafe_allow_html=True)
#             elif fs >= 0.4:
#                 st.markdown(f"""
#                     <div class="recommendation-box rec-medium">
#                         <h4>{icon_shield()} Recommendations</h4>
#                         <ul class="recommendation-list">
#                             <li>{icon_check()} Medium risk - Additional verification suggested before processing</li>
#                         </ul>
#                     </div>
#                 """, unsafe_allow_html=True)
#             else:
#                 st.markdown(f"""
#                     <div class="recommendation-box rec-low">
#                         <h4>{icon_shield()} Recommendations</h4>
#                         <ul class="recommendation-list">
#                             <li>{icon_check()} Low risk - Transaction appears legitimate and can be processed</li>
#                         </ul>
#                     </div>
#                 """, unsafe_allow_html=True)
#             st.markdown('</div>', unsafe_allow_html=True)

# # ===== TRANSACTION ANALYSIS TAB =====
# with tab2:
#     st.markdown("<h2 class='section-title'>Online Transaction Analysis</h2>", unsafe_allow_html=True)
#     now = datetime.now().hour
#     if 6 <= now < 12: tod = "Morning (6AM-12PM)"
#     elif 12 <= now < 18: tod = "Afternoon (12PM-6PM)"
#     elif 18 <= now < 24: tod = "Evening (6PM-12AM)"
#     else: tod = "Night (12AM-6AM)"

#     col1, col2 = st.columns([1, 1], gap="large")
#     with col1:
#         st.markdown('<div class="simple-card">', unsafe_allow_html=True)
#         with st.form("transaction_form"):
#             acct = st.text_input("Account Number", placeholder="Enter account number")
#             amt_in = st.text_input("Transaction Amount ($)", placeholder="0.00")
#             recip = st.text_input("Recipient Name", placeholder="Enter recipient name")
#             ttype = st.selectbox("Transaction Type", ["Transfer", "Payment", "Withdrawal", "Deposit"])
#             merch = st.text_input("Merchant", placeholder="Enter merchant name")
#             loc = st.text_input("Transaction Location", placeholder="City, State")
#             device = st.selectbox("Device Used", options=["Web Browser", "Mobile App", "ATM", "Phone"])
#             submitted = st.form_submit_button("Analyze Transaction", type="primary")
#             amount = 0.0
#             if amt_in:
#                 try:
#                     amount = float(amt_in.replace(',', '').replace('$', ''))
#                 except ValueError:
#                     st.error("Please enter a valid amount"); amount = 0.0
#             if submitted and acct and amount > 0:
#                 exact = datetime.now().strftime("%I:%M:%S %p on %B %d, %Y")
#                 data = {
#                     "account_number": acct, "amount": amount, "recipient": recip, "type": ttype,
#                     "merchant": merch, "location": loc, "time": tod, "exact_time": exact, "device": device
#                 }
#                 with st.spinner("Analyzing transaction..."):
#                     res = ml_transaction_analysis(data)
#                 if isinstance(res, dict):
#                     score = res['ensemble_probability']
#                     st.session_state.transaction_results = {'data': data, 'fraud_score': score, 'ensemble_result': res}
#                 else:
#                     st.session_state.transaction_results = {'data': data, 'fraud_score': res, 'ensemble_result': None}
#                 st.rerun()
#         st.markdown('</div>', unsafe_allow_html=True)

#     with col2:
#         if 'transaction_results' in st.session_state:
#             r = st.session_state.transaction_results
#             d = r['data']; s = r['fraud_score']
#             level, risk_class = get_risk_level(s)
#             st.markdown('<div class="results-card">', unsafe_allow_html=True)
#             st.markdown("<h3>Analysis Results</h3>", unsafe_allow_html=True)
#             st.markdown(f"""
#                 <div class="risk-container">
#                     <div class="risk-badge badge-{risk_class}">{level}</div>
#                     <div class="risk-score score-{risk_class}">{s*100:.0f}%</div>
#                     <div class="risk-label">Fraud Risk Score</div>
#                 </div>
#             """, unsafe_allow_html=True)
#             st.progress(float(s))
#             st.markdown('<div class="info-section">', unsafe_allow_html=True)
#             st.markdown(f"<h4>{icon_info()} Transaction Summary</h4>", unsafe_allow_html=True)
#             st.markdown('<div class="info-grid">', unsafe_allow_html=True)
#             summary_items = [
#                 ("Account", d['account_number']),
#                 ("Amount", f"${d['amount']:,.2f}"),
#                 ("Type", d['type']),
#                 ("Recipient", d['recipient']),
#                 ("Merchant", d['merchant']),
#                 ("Location", d['location']),
#                 ("Device", d['device']),
#                 ("Time", d.get('exact_time', 'N/A'))
#             ]
#             for label, value in summary_items:
#                 st.markdown(f"""
#                     <div class="info-item">
#                         <div class="info-label">{label}</div>
#                         <div class="info-value">{value}</div>
#                     </div>
#                 """, unsafe_allow_html=True)
#             st.markdown('</div></div>', unsafe_allow_html=True)
#             factors = get_detailed_risk_factors(d, s)
#             st.markdown('<div class="risk-factors">', unsafe_allow_html=True)
#             st.markdown(f"<h4>{icon_alert()} Risk Factors</h4>", unsafe_allow_html=True)
#             for factor in factors:
#                 st.markdown(f"""
#                     <div class="risk-factor-item">
#                         <div class="risk-factor-icon">!</div>
#                         <span>{factor}</span>
#                     </div>
#                 """, unsafe_allow_html=True)
#             st.markdown('</div>', unsafe_allow_html=True)
#             if s >= 0.7:
#                 st.markdown(f"""
#                     <div class="recommendation-box rec-high">
#                         <h4>{icon_shield()} Recommendations</h4>
#                         <ul class="recommendation-list">
#                             <li>{icon_check()} BLOCK TRANSACTION - High fraud risk detected. Require additional verification and manual review</li>
#                         </ul>
#                     </div>
#                 """, unsafe_allow_html=True)
#             elif s >= 0.4:
#                 st.markdown(f"""
#                     <div class="recommendation-box rec-medium">
#                         <h4>{icon_shield()} Recommendations</h4>
#                         <ul class="recommendation-list">
#                             <li>{icon_check()} REQUEST VERIFICATION - Medium risk. Additional authentication before processing</li>
#                         </ul>
#                     </div>
#                 """, unsafe_allow_html=True)
#             else:
#                 st.markdown(f"""
#                     <div class="recommendation-box rec-low">
#                         <h4>{icon_shield()} Recommendations</h4>
#                         <ul class="recommendation-list">
#                             <li>{icon_check()} APPROVE TRANSACTION - Low fraud risk</li>
#                         </ul>
#                     </div>
#                 """, unsafe_allow_html=True)
#             st.markdown('</div>', unsafe_allow_html=True)

# # ===== CENTERED LAUNCH INSIGHTS BUTTON =====
# st.markdown('<div class="center-button-wrapper">', unsafe_allow_html=True)
# _, c, _ = st.columns([1, 1, 1])
# with c:
#     if st.button("LAUNCH INSIGHTS", type="primary", use_container_width=True):
#         go_dashboard()
# st.markdown('</div>', unsafe_allow_html=True)

# # ===== FOOTER =====
# st.markdown("""
#     <div class="custom-footer">
#         <span>Where Innovation Meets Security</span>
#         <span class="footer-divider">|</span>
#         <span>Zero Tolerance for Fraud</span>
#         <span class="footer-divider">|</span>
#         <span>© Xforia DAD</span>
#     </div>
# """, unsafe_allow_html=True)






























































import streamlit as st 
import pandas as pd
import numpy as np
from PIL import Image
import tempfile
import os
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
import base64

# ----- Page config -----
st.set_page_config(
    page_title="Xforia DAD - Fraud Detection",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- Dashboard navigation ----------
DASHBOARD_CANDIDATES = [
    "pages/Dashboard.py",
    "pages/1_Dashboard.py",
    "pages/2_Dashboard.py",
    "pages/DASHBOARD.py",
    "Dashboard",
    "DASHBOARD",
]

def go_dashboard():
    for target in DASHBOARD_CANDIDATES:
        try:
            st.switch_page(target)
            return
        except Exception:
            continue
    st.warning("Couldn't navigate to Dashboard.")

# ========= Tidy, consistent styles (no extra UI elements) =========
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root{
  --brand:#1e3c72; --brand2:#2a5298; --accent:#db123d;
  --text:#0f172a; --muted:#475569; --line:#e2e8f0;
  --bg:#f6f7fb; --card:#ffffff;
}

/* Base */
*{font-family:'Inter',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;}
.stApp{background:var(--bg);}
/* Fixed Header */
.app-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 70px;
  background: #ffffff;
  border-bottom: 2px solid #e2e8f0;
  z-index: 10000;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
  box-shadow: 0 2px 8px rgba(15, 23, 42, 0.08);
}

.header-left {
  display: flex;
  align-items: center;
  gap: 20px;
}

.header-logo {
  height: 45px;
  width: auto;
}

.header-title {
  color: #1e3c72;
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  margin: 0;
}

.header-subtitle {
  color: #475569;
  font-size: 0.85rem;
  font-weight: 500;
  margin: 0;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

/* Hide default chrome */
header[data-testid="stHeader"],
section[aria-label="sidebar"],
[data-testid="stSidebar"], [data-testid="stSidebarNav"],
[data-testid="stSidebarContent"], [data-testid="stSidebarCollapseButton"],
[data-testid="collapsedControl"], [data-testid="stToolbar"],
[data-testid="stDock"], #MainMenu, footer {display:none !important;}

/* Container + spacing */
[data-testid="stAppViewContainer"]{padding-top:8px !important;}
.main .block-container{max-width:1180px !important; padding-top:8px !important;}

/* Title with button */
.title-row{display:flex; justify-content:space-between; align-items:center; margin:16px 0 10px 0; gap:20px;}
.page-title{font-size:2rem; font-weight:800; color:var(--text); letter-spacing:-.02em; margin:0; flex:1;}

/* Tabs (only two, no blanks) */
.stTabs [data-baseweb="tab-list"]{
  border-bottom:2px solid var(--line); gap:0; padding:0; background:transparent;
}
.stTabs [data-baseweb="tab"]:has(div:empty){display:none !important;}
.stTabs [data-baseweb="tab"]{
  border:none !important; margin-bottom:-2px; padding:12px 22px;
  font-weight:700; color:var(--muted); border-bottom:3px solid transparent;
}
.stTabs [data-baseweb="tab"]:hover{color:var(--text);}
.stTabs [data-baseweb="tab"][aria-selected="true"]{
  color:var(--accent); border-bottom:3px solid var(--accent);
}

/* Section header */
.section-title{font-size:1.35rem; font-weight:800; color:var(--text); margin:18px 0 12px 0;}

/* Cards */
.card{
  background:var(--card); border:1px solid var(--line); border-radius:10px;
  padding:18px; box-shadow:0 1px 3px rgba(15,23,42,.06);
}

/* Uploader (compact, centered) */
[data-testid="stFileUploader"]{
  background:#f8fafc; border:2px dashed #d6dee8; border-radius:10px;
  padding:22px; text-align:center;
}
[data-testid="stFileUploader"]:hover{border-color:#b9c5d3;}
[data-testid="stFileUploader"] section{border:none !important;}
[data-testid="stFileUploader"] label,
[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] [aria-live="polite"]{display:none !important;}

/* Buttons */
.stButton>button{
  background:var(--accent) !important; color:#fff !important; border:none !important;
  border-radius:10px !important; padding:12px 22px !important; font-weight:800 !important;
  letter-spacing:.04em !important; box-shadow:none !important; transition:transform .15s ease, filter .15s ease !important;
}
.stButton>button:hover{filter:brightness(.96) !important;}
.stButton>button:active{transform:translateY(1px) !important;}

/* Results panel */
.results{
  background:#f9fbff; border:1px solid var(--line); border-radius:14px; padding:20px;
  box-shadow:0 6px 20px rgba(15,23,42,.06);
}
.results h3{margin:0 0 10px 0; font-weight:900; font-size:1.05rem;}
.risk-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  padding: 16px;
  border-radius: 14px;
  position: relative;
  overflow: hidden;
}

.risk-wrap-low {
  background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
  border: 2px solid #059669;
}

.risk-wrap-medium {
  background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
  border: 2px solid #f59e0b;
}

.risk-wrap-high {
  background: linear-gradient(135deg, #fef2f2 0%, #fecaca 100%);
  border: 2px solid #db123d;
}

.risk-badge {
  font-weight: 900;
  letter-spacing: .06em;
  padding: 6px 14px;
  border-radius: 999px;
  color: #fff;
}

.badge-low {background: #059669;}
.badge-medium {background: #f59e0b;}
.badge-high {background: #db123d;}

.risk-score {
  font-size: 3.2rem;
  font-weight: 900;
  line-height: 1;
}

.score-low {color: #059669;}
.score-medium {color: #f59e0b;}
.score-high {color: #db123d;}

.risk-label {
  font-size: .8rem;
  font-weight: 700;
  color: var(--muted);
  text-transform: uppercase;
}
            
/* Info grid */
.info{background:#fff; border:1px solid var(--line); border-radius:12px; padding:12px; margin-top:10px;}
.grid{display:grid; grid-template-columns:repeat(2,1fr); gap:10px;}
.item{background:#fbfdff; border-left:3px solid var(--brand); border-radius:8px; padding:10px; margin-bottom:10px;}
.item:hover {{
  transform:translateY(-6px) scale(1.02);
  box-shadow:0 12px 32px rgba(15, 23, 42, 0.15);
  border-color:var(--brand);
}}
.lbl{font-size:.75rem; font-weight:700; color:var(--muted); text-transform:uppercase; letter-spacing:.04em;}
.val{font-size:.95rem; font-weight:600; color:var(--text);}

/* Factors */
.factors{background:#fff; border:1px solid var(--line); border-radius:12px; padding:12px; margin-top:12px;}
.factor{display:flex; gap:8px; align-items:center; background:#fdfdfd; border-left:3px solid var(--brand2); border-radius:8px; padding:10px; margin-bottom:6px;}
.dot{width:22px; height:22px; border-radius:999px; display:flex; align-items:center; justify-content:center; font-weight:900; background:#fff0cc; color:#b25c00;}

/* Recommendations */
.rec{border-radius:12px; padding:12px; border:1px solid var(--line); margin-top:12px;}
.rec-low{background:#eafaf2; border-color:#059669;} 
.rec-medium{background:#fff4db; border-color:#f59e0b;}
.rec-high{background:#ffe9ee; border-color:#db123d;}
.rec h4{margin:0 0 6px 0; font-weight:900;}

/* Inputs */
.stTextInput input, .stSelectbox select{
  border:1px solid var(--line) !important; border-radius:8px !important; padding:10px 12px !important; font-size:.95rem !important;
}
.stTextInput input:focus, .stSelectbox select:focus{border-color:var(--brand) !important; box-shadow:0 0 0 2px rgba(30,60,114,.12) !important;}
.stTextInput label, .stSelectbox label{font-weight:700 !important; color:var(--text) !important;}

/* Fixed logo */
.fixed-logo{position:fixed; top:10px; left:18px; z-index:10000; background:#fff; padding:2px 6px;}
.fixed-logo img{width:140px; height:45px; display:block;}

/* Fixed footer (blue bar) */
.custom-footer{
  position:fixed; left:0; right:0; bottom:0; height:64px; z-index:9999;
  background:#1e3c72; color:#fff; display:flex; justify-content:center; align-items:center; gap:18px;
  font-weight:700;
}
.footer-divider{opacity:.6;}

@media (max-width:768px){
  .grid{grid-template-columns:1fr;}
  .risk-score{font-size:2.1rem;}
  .title-row{flex-direction:column; align-items:flex-start;}
}
</style>
""", unsafe_allow_html=True)

# ---------- SVG icons ----------
def icon_info():
    return """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>"""

def icon_alert():
    return """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>"""

def icon_check():
    return """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <polyline points="20 6 9 17 4 12"/></svg>"""

def add_header():
    import pathlib
    cwd = pathlib.Path(os.getcwd())
    here = pathlib.Path(__file__).parent if "__file__" in globals() else cwd
    candidates = [cwd/"FDN.png", here/"FDN.png", here/"assets"/"FDN.png", cwd/"assets"/"FDN.png"]
    logo_path = next((p for p in candidates if p.exists()), None)
    
    logo_html = ""
    if logo_path:
        encoded = base64.b64encode(logo_path.read_bytes()).decode()
        logo_html = f'<img src="data:image/png;base64,{encoded}" alt="Logo" class="header-logo"/>'
    
    st.markdown(f"""
    <div class="app-header">
      <div class="header-left">
        <a href="/" target="_self">
        {logo_html}
        </a>
      </div>
    </div>
    """, unsafe_allow_html=True)

add_header()

# ---------- Splash screen ----------
try:
    from splash_screen import show_splash
except Exception:
    def show_splash():
        st.markdown(
            "<div style='display:flex;flex-direction:column;align-items:center;gap:8px;margin-top:40px;'>"
            "<h1 style='margin:0;'>Welcome to Fraud Detection</h1>"
            "<p style='opacity:.8;margin:0;'>Your Guardian Against Fraud</p>"
            "</div>", unsafe_allow_html=True
        )
        if st.button("Get Started", type="primary"):
            st.session_state.show_splash = False
            st.rerun()

if "show_splash" not in st.session_state:
    st.session_state.show_splash = True

if st.session_state.show_splash:
    show_splash()
    st.stop()

# ---------- ML helpers ----------
try:
    from ML_Model import ml_transaction_analysis, mock_transaction_analysis
except ImportError:
    def ml_transaction_analysis(data):
        import hashlib
        h = hashlib.sha256(str(data).encode()).hexdigest()
        return (int(h, 16) % 1000) / 1000.0
    mock_transaction_analysis = ml_transaction_analysis

# ===================== MINDEE CONFIG =====================
MINDEE_API_KEY = "md_KqeDU4LG1zvPTpm7yANOMZsU5bDnb3MN"
MINDEE_ACCOUNT_NAME = ""
MINDEE_ENDPOINT_NAME = ""
MINDEE_VERSION = "1"
MINDEE_MODEL_ID = "ae8aebe3-40a8-49ec-9545-daf787b1bbe5"

def extract_check_data(response):
    try:
        fields = response.inference.result.fields
        names = ['memo','pay_to','bank_name','signature','check_date','payer_name',
                 'word_amount','check_number','number_amount','payer_address',
                 'account_number','routing_number']
        return {n: (fields[n].value if n in fields else None) for n in names}
    except Exception as e:
        st.error(f"Error extracting check data: {e}")
        return None

def convert_ocr_to_ml_format(check_data):
    amount = check_data.get('number_amount', 0) or 0
    return {
        'account_number': str(check_data.get('account_number') or 'UNKNOWN'),
        'amount': float(amount),
        'type': 'Check',
        'merchant': str(check_data.get('memo') or 'Check Payment'),
        'location': 'Unknown',
        'recipient': str(check_data.get('pay_to') or 'Unknown'),
        'time': 'Morning (6AM-12PM)',
        'device': 'Check'
    }

def calculate_fraud_score(check_data):
    s = 0.1
    if not check_data.get('pay_to'): s += 0.2
    if not check_data.get('number_amount'): s += 0.3
    if not check_data.get('signature'): s += 0.3
    if not check_data.get('bank_name'): s += 0.2
    if not check_data.get('account_number'): s += 0.2
    if not check_data.get('routing_number'): s += 0.2
    amt = check_data.get('number_amount', 0)
    if amt and amt > 10000: s += 0.2
    elif amt and amt > 5000: s += 0.1
    words = check_data.get('word_amount', '')
    if words and amt and len(words.split()) < 3: s += 0.1
    cd = check_data.get('check_date')
    if cd:
        try:
            d = datetime.strptime(str(cd), '%Y-%m-%d')
            days = (datetime.now() - d).days
            if days > 180: s += 0.2
            elif days > 90: s += 0.1
        except:
            s += 0.1
    return min(s, 0.95)

def mindee_ocr_analysis_with_ml(image_file):
    try:
        try:
            from mindee import ClientV2, InferenceParameters
        except ImportError:
            st.error("Mindee SDK not installed.")
            return (None,)*6

        if not MINDEE_API_KEY:
            st.error("MINDEE_API_KEY is not set.")
            return (None,)*6

        try:
            client = ClientV2(MINDEE_API_KEY, region="us")
        except TypeError:
            client = ClientV2(MINDEE_API_KEY)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp:
            tmp.write(image_file.read())
            path = tmp.name

        try:
            src = client.source_from_path(path)

            if MINDEE_ACCOUNT_NAME and MINDEE_ENDPOINT_NAME:
                params = InferenceParameters(
                    account_name=MINDEE_ACCOUNT_NAME,
                    endpoint_name=MINDEE_ENDPOINT_NAME,
                    version=MINDEE_VERSION or "1",
                )
            elif MINDEE_MODEL_ID:
                params = InferenceParameters(model_id=MINDEE_MODEL_ID)
            else:
                st.error("Mindee not configured.")
                return (None,)*6

            resp = client.enqueue_and_get_inference(src, params)
            check_data = extract_check_data(resp)
            if not check_data:
                return (None,)*6

            extracted = {
                "Pay To": check_data.get('pay_to', 'N/A'),
                "Bank Name": check_data.get('bank_name', 'N/A'),
                "Check Date": check_data.get('check_date', 'N/A'),
                "Payer Name": check_data.get('payer_name', 'N/A'),
                "Amount (Words)": check_data.get('word_amount', 'N/A'),
                "Amount (Number)": f"${check_data.get('number_amount', 0):,.2f}" if check_data.get('number_amount') else 'N/A',
                "Check Number": check_data.get('check_number', 'N/A'),
                "Account Number": check_data.get('account_number', 'N/A'),
                "Routing Number": check_data.get('routing_number', 'N/A'),
                "Payer Address": check_data.get('payer_address', 'N/A'),
                "Memo": check_data.get('memo', 'N/A'),
                "Signature Present": "Yes" if check_data.get('signature') else "No"
            }

            tx = convert_ocr_to_ml_format(check_data)
            ml_res = ml_transaction_analysis(tx)
            if isinstance(ml_res, dict):
                ml_score = float(ml_res.get('ensemble_probability', 0.0))
                ml_ens = ml_res
            else:
                ml_score = float(ml_res or 0.0)
                ml_ens = None

            rule_score = calculate_fraud_score(check_data)
            combined = ml_score * 0.7 + rule_score * 0.3
            return extracted, combined, check_data, ml_score, rule_score, ml_ens

        finally:
            try: os.unlink(path)
            except Exception: pass

    except Exception as e:
        st.error(f"Error processing check: {e}")
        return (None,)*6

def get_risk_level(score):
    if score >= 0.7: return "HIGH RISK", "high"
    elif score >= 0.4: return "MEDIUM RISK", "medium"
    else: return "LOW RISK", "low"

def get_check_risk_factors(check_data, ml_score, rule_score):
    f = []
    if not check_data.get('signature'): f.append("Missing signature")
    if not check_data.get('number_amount'): f.append("Missing amount")
    if not check_data.get('pay_to'): f.append("Missing payee")
    if not check_data.get('bank_name'): f.append("Missing bank information")
    amt = check_data.get('number_amount', 0)
    if amt and amt > 10000: f.append("Very high check amount")
    elif amt and amt > 5000: f.append("High check amount")
    cd = check_data.get('check_date')
    if cd:
        try:
            days = (datetime.now() - datetime.strptime(str(cd), '%Y-%m-%d')).days
            if days > 180: f.append("Check is over 6 months old")
            elif days > 90: f.append("Check is over 3 months old")
        except:
            f.append("Invalid check date")
    if ml_score > 0.8: f.append("AI detected very high fraud risk")
    elif ml_score > 0.6: f.append("AI detected elevated fraud risk")
    words = check_data.get('word_amount', '')
    if words and amt and len(words.split()) < 3: f.append("Incomplete written amount")
    return f if f else ["No significant risk factors detected"]

def get_detailed_risk_factors(transaction_data, fraud_score):
    f = []
    amount = float(transaction_data.get('amount', 0))
    if amount > 10000: f.append(f"Very high transaction amount (${amount:,.2f})")
    elif amount > 5000: f.append(f"High transaction amount (${amount:,.2f})")
    elif amount > 1000: f.append(f"Moderate transaction amount (${amount:,.2f})")
    tod = transaction_data.get('time', '')
    if "Night" in tod: f.append("Unusual transaction time (night hours)")
    device = transaction_data.get('device', '')
    if device == "ATM" and amount > 1000: f.append("Large ATM withdrawal")
    loc = (transaction_data.get('location') or '').strip().lower()
    if not loc or loc == 'unknown': f.append("Unknown transaction location")
    rec = transaction_data.get('recipient', '')
    if not rec or rec.lower() == 'unknown': f.append("Unverified recipient")
    if fraud_score > 0.8: f.append("AI model shows very high fraud confidence")
    elif fraud_score > 0.6: f.append("AI model shows elevated fraud risk")
    elif fraud_score > 0.4: f.append("AI model shows moderate fraud risk")
    return f if f else ["No significant risk factors detected"]

# ===================== PAGE TITLE WITH DASHBOARD BUTTON =====================
col_title, col_btn = st.columns([4, 1])
with col_title:
    st.markdown("<h1 class='page-title'>AI-Powered Fraud Detection System</h1>", unsafe_allow_html=True)
with col_btn:
    if st.button("Launch Insights ", key="dashboard_btn", type="secondary", use_container_width=True):
        go_dashboard()

# ===================== TABS (EXPLICITLY ONLY TWO) =====================
tab1, tab2 = st.tabs(["Check Analysis", "Online Transaction Analysis"])

# ===== CHECK ANALYSIS TAB =====
with tab1:
    st.markdown("<h2 class='section-title'>Enhanced Check Analysis with AI</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns([2,3], gap="large")

    with c1:
        uploaded_file = st.file_uploader("Drop your check image here", type=['jpg','jpeg','png'], label_visibility="collapsed")
        if uploaded_file:
            try:
                uploaded_file.seek(0)
                img = Image.open(uploaded_file)
                st.image(img, use_container_width=True)
                if st.button("Analyze Check", type="primary", key="analyze_check_btn"):
                    with st.spinner("🔍 Analyzing your check..."):
                        uploaded_file.seek(0)
                        extracted, combined, raw, ml_s, rule_s, ml_ens = mindee_ocr_analysis_with_ml(uploaded_file)
                    if extracted and combined is not None:
                        st.success("Check processed successfully!")
                        st.session_state.check_results = {
                            'extracted_data': extracted,
                            'fraud_score': combined,
                            'ml_score': ml_s,
                            'rule_score': rule_s,
                            'raw_data': raw,
                            'ml_ensemble': ml_ens
                        }
                        st.rerun()
                    else:
                        st.error("Unable to process the check. Please try again.")
            except Exception as e:
                st.error(f"Error: {e}")

    with c2:
        if 'check_results' in st.session_state:
            res = st.session_state.check_results
            fs = float(res['fraud_score'])
            ml_score = float(res.get('ml_score', 0))
            rule_score = float(res.get('rule_score', 0))
            level, risk_class = get_risk_level(fs)

            st.markdown(f"""
                <div class="risk-wrap risk-wrap-{risk_class}">
                    <div class="risk-badge badge-{risk_class}">{level}</div>
                    <div class="risk-score score-{risk_class}">{fs*100:.0f}%</div>
                    <div class="risk-label">Fraud Risk Score</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"<h4 style='display:flex;align-items:center;gap:8px;margin:8px 0 0 0;'>{icon_info()} Extracted Information</h4>", unsafe_allow_html=True)
            st.markdown("<div class='grid'>", unsafe_allow_html=True)
            for k, v in res['extracted_data'].items():
                st.markdown(f"<div class='item'><div class='lbl'>{k}</div><div class='val'>{v}</div></div>", unsafe_allow_html=True)
            st.markdown("</div></div>", unsafe_allow_html=True)

            factors = get_check_risk_factors(res.get('raw_data', {}), ml_score, rule_score)
            st.markdown(f"<h4 style='display:flex;align-items:center;gap:8px;margin:0 0 8px 0;'>{icon_alert()} Risk Factors</h4>", unsafe_allow_html=True)
            for fct in factors:
                st.markdown(f"<div class='factor'><div class='dot'>!</div><span>{fct}</span></div>", unsafe_allow_html=True)
            if fs >= 0.7:
                st.markdown(f"<div class='rec rec-high'><h4>{icon_check()} Recommendations</h4><div>High fraud risk detected — manual verification & additional auth recommended.</div></div>", unsafe_allow_html=True)
            elif fs >= 0.4:
                st.markdown(f"<div class='rec rec-medium'><h4>{icon_check()} Recommendations</h4><div>Medium risk — perform extra verification before processing.</div></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='rec rec-low'><h4>{icon_check()} Recommendations</h4><div>Low risk — transaction appears legitimate.</div></div>", unsafe_allow_html=True)

# ===== TRANSACTION ANALYSIS TAB =====
with tab2:
    st.markdown("<h2 class='section-title'>Online Transaction Analysis</h2>", unsafe_allow_html=True)

    now = datetime.now().hour
    if 6 <= now < 12: tod = "Morning (6AM-12PM)"
    elif 12 <= now < 18: tod = "Afternoon (12PM-6PM)"
    elif 18 <= now < 24: tod = "Evening (6PM-12AM)"
    else: tod = "Night (12AM-6AM)"

    c1, c2 = st.columns([2,3], gap="large")

    with c1:
        with st.form("transaction_form"):
            acct = st.text_input("Account Number", placeholder="Enter account number")
            amt_in = st.text_input("Transaction Amount ($)", placeholder="0.00")
            recip = st.text_input("Recipient Name", placeholder="Enter recipient name")
            ttype = st.selectbox("Transaction Type", ["Transfer", "Payment", "Withdrawal", "Deposit"])
            merch = st.text_input("Merchant", placeholder="Enter merchant name")
            loc = st.text_input("Transaction Location", placeholder="City, State")
            device = st.selectbox("Device Used", options=["Web Browser", "Mobile App", "ATM", "Phone"])
            submit = st.form_submit_button("Analyze Transaction", type="primary")

            amount = 0.0
            if amt_in:
                try:
                    amount = float(amt_in.replace(',', '').replace('$', ''))
                except ValueError:
                    st.error("Please enter a valid amount"); amount = 0.0

            if submit and acct and amount > 0:
                exact = datetime.now().strftime("%I:%M:%S %p on %B %d, %Y")
                data = {
                    "account_number": acct, "amount": amount, "recipient": recip, "type": ttype,
                    "merchant": merch, "location": loc, "time": tod, "exact_time": exact, "device": device
                }
                with st.spinner("Analyzing transaction..."):
                    res = ml_transaction_analysis(data)
                if isinstance(res, dict):
                    score = float(res['ensemble_probability'])
                    st.session_state.transaction_results = {'data': data, 'fraud_score': score, 'ensemble_result': res}
                else:
                    st.session_state.transaction_results = {'data': data, 'fraud_score': float(res), 'ensemble_result': None}
                st.rerun()    

    with c2:
        if 'transaction_results' in st.session_state:
            r = st.session_state.transaction_results
            d = r['data']; s = float(r['fraud_score'])
            level, risk_class = get_risk_level(s)

            st.markdown("<h3>Analysis Results</h3>", unsafe_allow_html=True)
            st.markdown(f"""
               <div class="risk-wrap risk-wrap-{risk_class}">
                    <div class="risk-badge badge-{risk_class}">{level}</div>
                    <div class="risk-score score-{risk_class}">{s*100:.0f}%</div>
                    <div class="risk-label">Fraud Risk Score</div>
                </div>
            """, unsafe_allow_html=True)

            st.markdown(f"<h4 style='display:flex;align-items:center;gap:8px;margin:0 0 8px 0;'>{icon_info()} Transaction Summary</h4>", unsafe_allow_html=True)
            st.markdown("<div class='grid'>", unsafe_allow_html=True)
            for label, value in [
                ("Account", d['account_number']),
                ("Amount", f"${d['amount']:,.2f}"),
                ("Type", d['type']),
                ("Recipient", d['recipient']),
                ("Merchant", d['merchant']),
                ("Location", d['location']),
                ("Device", d['device']),
                ("Time", d.get('exact_time', 'N/A'))
            ]:
                st.markdown(f"<div class='item'><div class='lbl'>{label}</div><div class='val'>{value}</div></div>", unsafe_allow_html=True)
            st.markdown("</div></div>", unsafe_allow_html=True)

            factors = get_detailed_risk_factors(d, s)
            
            st.markdown(f"<h4 style='display:flex;align-items:center;gap:8px;margin:0 0 8px 0;'>{icon_alert()} Risk Factors</h4>", unsafe_allow_html=True)
            for fct in factors:
                st.markdown(f"<div class='factor'><div class='dot'>!</div><span>{fct}</span></div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            if s >= 0.7:
                st.markdown(f"<div class='rec rec-high'><h4>{icon_check()} Recommendations</h4><div>BLOCK — High fraud risk. Require additional verification and manual review.</div></div>", unsafe_allow_html=True)
            elif s >= 0.4:
                st.markdown(f"<div class='rec rec-medium'><h4>{icon_check()} Recommendations</h4><div>REQUEST VERIFICATION — Medium risk. Add extra authentication.</div></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='rec rec-low'><h4>{icon_check()} Recommendations</h4><div>APPROVE — Low fraud risk.</div></div>", unsafe_allow_html=True)

# ===== Fixed footer (kept original style) =====
st.markdown("""
<div class="custom-footer">
  <span>Where Innovation Meets Security</span>
  <span class="footer-divider">|</span>
  <span>Zero Tolerance for Fraud</span>
  <span class="footer-divider">|</span>
  <span>© Xforia DAD</span>
</div>
""", unsafe_allow_html=True)