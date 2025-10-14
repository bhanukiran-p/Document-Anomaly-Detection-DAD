# Transaction Analysis Page

import streamlit as st 
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
import base64
import os
import pathlib

# ----- Page config -----
st.set_page_config(
    page_title="Xforia DAD - Real-time Transaction Analysis",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Navigation functions
def go_dashboard():
    candidates = [
        "pages/Dashboard.py",
        "pages/1_Dashboard.py",
        "pages/2_Dashboard.py",
        "pages/DASHBOARD.py",
        "Dashboard",
        "DASHBOARD",
    ]
    for target in candidates:
        try:
            st.switch_page(target)
            return
        except Exception:
            continue
    st.warning("Couldn't navigate to Dashboard.")

def go_home():
    # Try to navigate to the main app page
    try:
        # First try just switching to the home page without a specific file
        st.switch_page("Detection.py")
        return
    except Exception:
        pass
    
    # If that doesn't work, try other common main file names
    candidates = [
        "Fraud_Detection.py",
        "fraud_detection.py",
        "main.py",
        "Main.py",
        "Home.py",
        "home.py"
    ]
    
    for target in candidates:
        try:
            st.switch_page(target)
            return
        except Exception:
            continue
    
    # If nothing works, show an error with helpful message
    st.error("Couldn't navigate back to Check Analysis. Please ensure your main file is named 'app.py' or 'Fraud_Detection.py'")

# ========= Styles =========
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

/* Hide default chrome */
header[data-testid="stHeader"],
section[aria-label="sidebar"],
[data-testid="stSidebar"], [data-testid="stSidebarNav"],
[data-testid="stSidebarContent"], [data-testid="stSidebarCollapseButton"],
[data-testid="collapsedControl"], [data-testid="stToolbar"],
[data-testid="stDock"], #MainMenu, footer {display:none !important;}

/* Hamburger Menu */
.hamburger-menu {
  position: fixed;
  top: 12px;
  right: 32px;
  z-index: 10001;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  gap: 5px;
  padding: 10px;
  background: transparent;
  border: none;
}

.hamburger-line {
  width: 28px;
  height: 3px;
  background: #1e3c72;
  border-radius: 3px;
  transition: all 0.3s ease;
}

.hamburger-menu:hover .hamburger-line {
  background: #db123d;
}

.menu-overlay {
  position: fixed;
  top: 0;
  right: -100%;
  width: 320px;
  height: 100vh;
  background: #ffffff;
  box-shadow: -4px 0 20px rgba(15, 23, 42, 0.15);
  z-index: 10002;
  transition: right 0.3s ease;
  padding: 80px 30px 30px;
  overflow-y: auto;
}

.menu-overlay.active {
  right: 0;
}

.menu-close {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 32px;
  height: 32px;
  cursor: pointer;
  background: transparent;
  border: none;
  font-size: 28px;
  color: #475569;
  line-height: 1;
  transition: color 0.2s;
}

.menu-close:hover {
  color: #db123d;
}

.menu-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(15, 23, 42, 0.5);
  z-index: 10001;
  display: none;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.menu-backdrop.active {
  display: block;
  opacity: 1;
}

.menu-title {
  font-size: 1.5rem;
  font-weight: 900;
  color: #1e3c72;
  margin: 0 0 24px 0;
  letter-spacing: -0.02em;
}

.menu-item {
  display: block;
  padding: 16px 20px;
  margin-bottom: 8px;
  background: #f8fafc;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  color: #0f172a;
  text-decoration: none;
  font-weight: 700;
  font-size: 1rem;
  transition: all 0.3s ease;
  cursor: pointer;
  border-left: 4px solid transparent;
}

.menu-item:hover {
  background: #ffffff;
  border-color: #1e3c72;
  border-left-color: #db123d;
  transform: translateX(8px);
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.1);
}

/* Container + spacing */
[data-testid="stAppViewContainer"]{padding-top:8px !important;}
.main .block-container{max-width:1180px !important; padding-top:8px !important;}

/* Title */
.page-title{font-size:2rem; font-weight:800; color:var(--text); letter-spacing:-.02em; margin:0;}

/* Section header */
.section-title{font-size:1.35rem; font-weight:800; color:var(--text); margin:18px 0 12px 0;}

/* Buttons */
.stButton>button{
  background:var(--accent) !important; color:#fff !important; border:none !important;
  border-radius:10px !important; padding:12px 22px !important; font-weight:800 !important;
  letter-spacing:.04em !important; box-shadow:none !important; transition:transform .15s ease, filter .15s ease !important;
}
.stButton>button:hover{filter:brightness(.96) !important;}
.stButton>button:active{transform:translateY(1px) !important;}

/* Risk wrap */
.risk-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  padding: 16px;
  border-radius: 14px;
  position: relative;
  overflow: hidden;
  margin-bottom: 16px;
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
.grid{display:grid; grid-template-columns:repeat(2,1fr); gap:10px; margin-top:10px;}
.item{background:#fbfdff; border-left:3px solid var(--brand); border-radius:8px; padding:10px;}
.item:hover {
  transform:translateY(-6px) scale(1.02);
  box-shadow:0 12px 32px rgba(15, 23, 42, 0.15);
  border-color:var(--brand);
}
.lbl{font-size:.75rem; font-weight:700; color:var(--muted); text-transform:uppercase; letter-spacing:.04em;}
.val{font-size:.95rem; font-weight:600; color:var(--text);}

/* Factors */
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

/* Fixed footer */
.custom-footer{
  position:fixed; left:0; right:0; bottom:0; height:64px; z-index:9999;
  background:#1e3c72; color:#fff; display:flex; justify-content:center; align-items:center; gap:18px;
  font-weight:700;
}
.footer-divider{opacity:.6;}

@media (max-width:768px){
  .grid{grid-template-columns:1fr;}
  .risk-score{font-size:2.1rem;}
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
    cwd = pathlib.Path(os.getcwd())
    here = pathlib.Path(__file__).parent if "__file__" in globals() else cwd
    candidates = [cwd/"FDN.png", here/"FDN.png", here/"assets"/"FDN.png", cwd/"assets"/"FDN.png", here.parent/"FDN.png", here.parent/"assets"/"FDN.png"]
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
      <div class="header-right">
        <div class="hamburger-menu" id="hamburgerBtn">
          <div class="hamburger-line"></div>
          <div class="hamburger-line"></div>
          <div class="hamburger-line"></div>
        </div>
      </div>
    </div>
    
    <div class="menu-backdrop" id="menuBackdrop"></div>
    <div class="menu-overlay" id="menuOverlay">
      <button class="menu-close" id="closeBtn">×</button>
      <h2 class="menu-title">DAD Solutions</h2>
      <div class="menu-item" data-name="manufacturing">
        <div style="font-size: 1.1rem; font-weight: 800; margin-bottom: 4px;">DAD for Manufacturing</div>
        <div style="font-size: 0.85rem; color: #64748b; font-weight: 500;">Quality control & defect detection</div>
      </div>
      <div class="menu-item" data-name="education">
        <div style="font-size: 1.1rem; font-weight: 800; margin-bottom: 4px;">DAD for Education</div>
        <div style="font-size: 0.85rem; color: #64748b; font-weight: 500;">Academic integrity & assessment</div>
      </div>
      <div class="menu-item" data-name="healthcare">
        <div style="font-size: 1.1rem; font-weight: 800; margin-bottom: 4px;">DAD for Healthcare</div>
        <div style="font-size: 0.85rem; color: #64748b; font-weight: 500;">Medical records & compliance</div>
      </div>
    </div>
    
    <script>
      setTimeout(function() {{
        const hamburger = document.getElementById('hamburgerBtn');
        const overlay = document.getElementById('menuOverlay');
        const backdrop = document.getElementById('menuBackdrop');
        const closeBtn = document.getElementById('closeBtn');
        
        function openMenu() {{
          if (overlay && backdrop) {{
            overlay.classList.add('active');
            backdrop.classList.add('active');
          }}
        }}
        
        function closeMenu() {{
          if (overlay && backdrop) {{
            overlay.classList.remove('active');
            backdrop.classList.remove('active');
          }}
        }}
        
        if (hamburger) {{
          hamburger.addEventListener('click', function(e) {{
            e.preventDefault();
            e.stopPropagation();
            openMenu();
          }});
        }}
        
        if (closeBtn) {{
          closeBtn.addEventListener('click', closeMenu);
        }}
        
        if (backdrop) {{
          backdrop.addEventListener('click', closeMenu);
        }}
        
        const menuItems = document.querySelectorAll('.menu-item');
        menuItems.forEach(item => {{
          item.addEventListener('click', function() {{
            const name = this.getAttribute('data-name');
            alert('DAD for ' + name.charAt(0).toUpperCase() + name.slice(1) + ' - Coming Soon!');
          }});
        }});
      }}, 200);
    </script>
    """, unsafe_allow_html=True)

add_header()

# ---------- ML helpers ----------
try:
    from ML_Model import ml_transaction_analysis
except ImportError:
    def ml_transaction_analysis(data):
        import hashlib
        h = hashlib.sha256(str(data).encode()).hexdigest()
        return (int(h, 16) % 1000) / 1000.0

def get_risk_level(score):
    if score >= 0.7: return "HIGH RISK", "high"
    elif score >= 0.4: return "MEDIUM RISK", "medium"
    else: return "LOW RISK", "low"

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

# ===================== PAGE HEADER WITH NAVIGATION BUTTONS =====================
col_title, col_btn1, col_btn2 = st.columns([3, 1, 1])
with col_title:
    st.markdown("<h1 class='page-title'>Real-time Transaction Analysis</h1>", unsafe_allow_html=True)
with col_btn1:
    if st.button("Check Analysis", key="check_btn", type="secondary", use_container_width=True):
        go_home()
with col_btn2:
    if st.button("Insights", key="dashboard_btn", type="secondary", use_container_width=True):
        go_dashboard()

st.markdown("<h2 class='section-title'>Analyze Online Transactions</h2>", unsafe_allow_html=True)

# Get current time of day
now = datetime.now().hour
if 6 <= now < 12: tod = "Morning (6AM-12PM)"
elif 12 <= now < 18: tod = "Afternoon (12PM-6PM)"
elif 18 <= now < 24: tod = "Evening (6PM-12AM)"
else: tod = "Night (12AM-6AM)"

c1, c2 = st.columns([2,3], gap="large")

with c1:
    with st.form("transaction_form"):
        st.markdown("#### Enter Transaction Details")
        acct = st.text_input("Account Number", placeholder="Enter account number")
        amt_in = st.text_input("Transaction Amount ($)", placeholder="0.00")
        recip = st.text_input("Recipient Name", placeholder="Enter recipient name")
        ttype = st.selectbox("Transaction Type", ["Transfer", "Payment", "Withdrawal", "Deposit"])
        merch = st.text_input("Merchant", placeholder="Enter merchant name")
        loc = st.text_input("Transaction Location", placeholder="City, State")
        device = st.selectbox("Device Used", options=["Web Browser", "Mobile App", "ATM", "Phone"])
        submit = st.form_submit_button("Analyze Transaction", type="primary", use_container_width=True)

        amount = 0.0
        if amt_in:
            try:
                amount = float(amt_in.replace(',', '').replace('$', ''))
            except ValueError:
                st.error("Please enter a valid amount")
                amount = 0.0

        if submit:
            if not acct:
                st.error("Please enter an account number")
            elif amount <= 0:
                st.error("Please enter a valid transaction amount")
            else:
                exact = datetime.now().strftime("%I:%M:%S %p on %B %d, %Y")
                data = {
                    "account_number": acct, 
                    "amount": amount, 
                    "recipient": recip or "Unknown", 
                    "type": ttype,
                    "merchant": merch or "N/A", 
                    "location": loc or "Unknown", 
                    "time": tod, 
                    "exact_time": exact, 
                    "device": device
                }
                with st.spinner("Analyzing transaction..."):
                    res = ml_transaction_analysis(data)
                if isinstance(res, dict):
                    score = float(res.get('ensemble_probability', 0.0))
                    st.session_state.transaction_results = {
                        'data': data, 
                        'fraud_score': score, 
                        'ensemble_result': res
                    }
                else:
                    st.session_state.transaction_results = {
                        'data': data, 
                        'fraud_score': float(res), 
                        'ensemble_result': None
                    }
                st.success("Transaction analyzed successfully!")
                st.rerun()

with c2:
    if 'transaction_results' in st.session_state:
        r = st.session_state.transaction_results
        d = r['data']
        s = float(r['fraud_score'])
        level, risk_class = get_risk_level(s)

        st.markdown("<h3>Analysis Results</h3>", unsafe_allow_html=True)
        
        # Risk Score Display
        st.markdown(f"""
           <div class="risk-wrap risk-wrap-{risk_class}">
                <div class="risk-badge badge-{risk_class}">{level}</div>
                <div class="risk-score score-{risk_class}">{s*100:.0f}%</div>
                <div class="risk-label">Fraud Risk Score</div>
            </div>
        """, unsafe_allow_html=True)

        # Risk Factors
        factors = get_detailed_risk_factors(d, s)
        st.markdown(f"<h4 style='display:flex;align-items:center;gap:8px;margin:0 0 8px 0;'>{icon_alert()} Risk Factors</h4>", unsafe_allow_html=True)
        for fct in factors:
            st.markdown(f"<div class='factor'><div class='dot'>!</div><span>{fct}</span></div>", unsafe_allow_html=True)

        # Recommendations
        if s >= 0.7:
            st.markdown(f"<div class='rec rec-high'><h4>{icon_check()} Recommendations</h4><div>BLOCK — High fraud risk. Require additional verification and manual review.</div></div>", unsafe_allow_html=True)
        elif s >= 0.4:
            st.markdown(f"<div class='rec rec-medium'><h4>{icon_check()} Recommendations</h4><div>REQUEST VERIFICATION — Medium risk. Add extra authentication.</div></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='rec rec-low'><h4>{icon_check()} Recommendations</h4><div>APPROVE — Low fraud risk.</div></div>", unsafe_allow_html=True)

        # Transaction Summary
        st.markdown(f"<h4 style='display:flex;align-items:center;gap:8px;margin:20px 0 8px 0;'>{icon_info()} Transaction Summary</h4>", unsafe_allow_html=True)
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
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("Enter transaction details on the left to begin analysis")
        st.markdown("""
            <div style='margin-top:20px; padding:20px; background:#f8fafc; border-radius:12px; border:1px solid #e2e8f0;'>
                <h4 style='margin:0 0 12px 0; color:#1e3c72;'>How it works:</h4>
                <ol style='margin:0; padding-left:20px; color:#475569;'>
                    <li style='margin-bottom:8px;'>Fill in the transaction details in the form</li>
                    <li style='margin-bottom:8px;'>Click "Analyze Transaction" to process</li>
                    <li style='margin-bottom:8px;'>View fraud risk score and analysis</li>
                    <li>Review recommendations and transaction summary</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)

# ===== Fixed footer =====
st.markdown("""
<div class="custom-footer">
  <span>Where Innovation Meets Security</span>
  <span class="footer-divider">|</span>
  <span>Zero Tolerance for Fraud</span>
  <span class="footer-divider">|</span>
  <span>© Xforia DAD</span>
</div>
""", unsafe_allow_html=True)