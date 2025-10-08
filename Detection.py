# Detection.py

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

st.set_page_config(page_title="AI-Powered Fraud Detection System", page_icon=None, layout="wide")

# ---------- Optional Dashboard navigation ----------
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
    st.warning("Couldn't navigate to Dashboard. Make sure a page named 'Dashboard' exists under the `pages/` folder.")

# ========= COMPACT GLOBAL STYLES & GAP FIXES =========
st.markdown("""
<style>
:root { --pad-sm: 6px; --pad-xs: 4px; }

/* Keep just enough padding so content doesn't sit under the fixed footer */
.stApp { padding-bottom: 56px !important; }

[data-testid="stAppViewContainer"] { padding-top: var(--pad-sm) !important; }
.main .block-container { padding-top: var(--pad-xs) !important; padding-bottom: 0px !important; }

/* Make header compact and invisible (reduces big top gap) */
header[data-testid="stHeader"] { height: 0 !important; min-height: 0 !important; background: transparent !important; }

/* Tabs + separators tighter */
[data-baseweb="tab-list"] { margin: var(--pad-xs) 0 !important; }
hr { margin: 6px 0 !important; }

/* Headings aligned and compact */
h1, .section-title { font-size: 32px !important; line-height: 1.15 !important; font-weight: 800 !important; margin: 2px 0 8px 0 !important; }
h2 { margin: 4px 0 6px 0 !important; }
h4, .tight-h4 { font-size: 18px !important; margin: 4px 0 6px 0 !important; font-weight: 700 !important; }

/* Trim block vertical gaps */
.block-container > div { margin-top: 0 !important; margin-bottom: 8px !important; }
.stImage, .stButton, .stMarkdown, .stTextInput, .stSelectbox, .stFileUploader { margin-top: 4px !important; margin-bottom: 6px !important; }

/* Uploader: hide label/details and tighten padding */
[data-testid="stFileUploader"] label { display: none !important; }
[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] .uploadFileDetails,
[data-testid="stFileUploader"] [aria-live="polite"] { display:none !important; }
[data-testid="stFileUploader"] [data-testid="stFileDropzone"] { padding: 8px 10px !important; min-height: auto !important; }

/* Footer fixed to bottom */
.fixed-footer {
  position: fixed !important; left: 0; right: 0; bottom: 0;
  height: 56px !important;
  background: #1e3c72 !important; color: #fff !important;
  display: flex !important; align-items: center !important; justify-content: center !important;
  gap: 10px !important; padding: 8px 12px !important;
  box-shadow: 0 -2px 10px rgba(0,0,0,.22) !important;
  font-size: 0.93em !important; font-weight: 600 !important;
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial, 'Noto Sans' !important;
  margin: 0 !important;
  z-index: 9999 !important;
}
.fixed-footer .sep { opacity: .6 !important; padding: 0 8px !important; }
.fixed-footer span { color: #fff !important; display: inline-block !important; }

/* Hide sidebar & deploy */
[data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
button[title="Deploy"], button[title*="Deploy"], a[title="Deploy"], a[title*="Deploy"],
[data-testid="ToolbarActionDeploy"], [data-testid="deployment-link"] { display:none !important; }

/* Tighten Launch Insights button spacing so it sits right above the footer */
button[key="dashboard_btn"]{ margin-bottom: 0px !important; }

/* Primary buttons styling */
[data-testid="stButton"] button[kind="primary"],
button[key="dashboard_btn"]{
    background:#db123d !important; color:#fff !important; border:0 !important;
    border-radius:12px !important; padding:12px 22px !important; font-weight:800 !important;
    font-size:15px !important; text-transform:uppercase !important; letter-spacing:.02em !important;
    box-shadow:none !important; min-width:220px !important;
}
[data-testid="stButton"] button[kind="primary"]:hover,
button[key="dashboard_btn"]:hover{ filter:brightness(1.03) !important; }
</style>

<!-- Hide any 'Limit ###MB per file' text under the uploader -->
<script>
(function() {
  const killLimit = () => {
    document.querySelectorAll('[data-testid="stFileUploader"]').forEach(u => {
      u.querySelectorAll('*').forEach(n => {
        if (!n) return;
        const txt = (n.innerText||'').trim();
        if (/^limit\\s*\\d+\\s*mb\\s*per\\s*file$/i.test(txt)) { n.style.display = 'none'; }
      });
    });
  };
  new MutationObserver(killLimit).observe(document.documentElement, {subtree:true, childList:true});
  window.addEventListener('load', killLimit);
  killLimit();

  // Extra: hide any rogue "Deploy" text nodes if they appear
  const hideDeploy = () => {
    document.querySelectorAll('a,button,span,div').forEach(el=>{
      const t=(el.innerText||'').trim(); if(/^deploy$/i.test(t)){ el.style.display='none'; const p=el.closest('a,button,div'); if(p) p.style.display='none'; }
    });
  };
  new MutationObserver(hideDeploy).observe(document.documentElement, {subtree:true, childList:true});
  hideDeploy();
})();
</script>
""", unsafe_allow_html=True)

# ---------- Fixed logo ----------
def add_fixed_logo():
    import pathlib
    cwd = pathlib.Path(os.getcwd())
    here = pathlib.Path(__file__).parent if "__file__" in globals() else cwd
    candidates = [cwd / "FDN.png", here / "FDN.png", here / "assets" / "FDN.png", cwd / "assets" / "FDN.png"]
    logo_path = next((p for p in candidates if p.exists()), None)
    if not logo_path:
        return
    encoded = base64.b64encode(logo_path.read_bytes()).decode()
    st.markdown(f"""
    <style>
      .fixed-logo {{
        position: fixed; top: 10px; left: 20px; z-index: 2147482000;
        background: rgba(255,255,255,0.95); border-radius: 6px; padding: 2px 6px;
      }}
      .fixed-logo img {{ width: 150px; height: 50px; display: block; cursor: pointer; }}
      @media (max-width: 768px) {{ .fixed-logo {{ left: 16px; top: 8px; }} }}
    </style>
    <div class="fixed-logo">
      <a href="/" target="_self"><img src="data:image/png;base64,{encoded}" alt="FDN Logo" /></a>
    </div>
    """, unsafe_allow_html=True)

add_fixed_logo()

# ---------- Splash screen gate ----------
try:
    from splash_screen import show_splash  # optional module; if missing, fallback below
except Exception:
    def show_splash():
        st.markdown("""
            <div style="display:flex;flex-direction:column;align-items:center;gap:12px;margin-top:40px;">
                <h1 style="margin:0;">Welcome to the Fraud Detection System</h1>
                <p style="opacity:.8;margin:0;">Where Innovation Meets Security</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Launch Dashboard", type="primary"):
            st.session_state.show_splash = False
            st.rerun()

if "show_splash" not in st.session_state:
    st.session_state.show_splash = True

if st.session_state.show_splash:
    show_splash()
    st.stop()

# ---------- Title ----------
st.markdown("<h1>AI-Powered Fraud Detection System</h1>", unsafe_allow_html=True)

# ---------- ML / Fraud helpers ----------
try:
    from ML_Model import ml_transaction_analysis, mock_transaction_analysis
except ImportError:
    st.error("ML_Model.py not found. Using mock analysis.")
    def ml_transaction_analysis(data):
        import hashlib
        h = hashlib.sha256(str(data).encode()).hexdigest()
        return (int(h, 16) % 1000) / 1000.0
    mock_transaction_analysis = ml_transaction_analysis

# ===================== MINDEE CONFIG =====================
MINDEE_API_KEY = "md_KqeDU4LG1zvPTpm7yANOMZsU5bDnb3MN"  # ← your key

# API Builder endpoint (preferred). Fill these if you have an endpoint.
MINDEE_ACCOUNT_NAME = ""      # e.g., "your_account_slug"
MINDEE_ENDPOINT_NAME = ""     # e.g., "check_extractor"
MINDEE_VERSION = "1"

# Legacy model UUID (fallback) – leave empty unless you truly have one.
MINDEE_MODEL_ID = "ae8aebe3-40a8-49ec-9545-daf787b1bbe5"          # e.g., "07b0e09b-f1c0-...."

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
    """
    Uses Mindee’s Python SDK.
    - If API Builder endpoint config is present -> use endpoint
    - Else if MINDEE_MODEL_ID provided -> use legacy model UUID
    Compatible with SDK versions that don't accept a 'region' kwarg.
    """
    try:
        try:
            from mindee import ClientV2, InferenceParameters
        except ImportError:
            st.error("Mindee SDK not installed. Run: pip install mindee")
            return (None,)*6

        if not MINDEE_API_KEY:
            st.error("MINDEE_API_KEY is not set.")
            return (None,)*6

        # Region kwarg compatibility handling
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
                st.error("Mindee not configured: set endpoint (account/endpoint/version) OR MINDEE_MODEL_ID.")
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
            try:
                os.unlink(path)
            except Exception:
                pass

    except Exception as e:
        st.error(f"Error processing Check: {e}")
        return (None,)*6

def get_risk_level(score):
    if score >= 0.7: return "HIGH RISK", "red"
    elif score >= 0.4: return "MEDIUM RISK", "orange"
    else: return "LOW RISK", "green"

def get_check_risk_factors(check_data, ml_score, rule_score):
    f = []
    if not check_data.get('signature'): f.append("• Missing signature detected")
    if not check_data.get('number_amount'): f.append("• Missing or invalid amount")
    if not check_data.get('pay_to'): f.append("• Missing payee information")
    if not check_data.get('bank_name'): f.append("• Missing bank information")
    amt = check_data.get('number_amount', 0)
    if amt and amt > 10000: f.append("• Very high check amount")
    elif amt and amt > 5000: f.append("• High check amount")
    cd = check_data.get('check_date')
    if cd:
        try:
            days = (datetime.now() - datetime.strptime(str(cd), '%Y-%m-%d')).days
            if days > 180: f.append("• Very old check (>6 months)")
            elif days > 90: f.append("• Old check (>3 months)")
        except:
            f.append("• Invalid / unclear check date")
    if ml_score > 0.8: f.append("• ML model shows very high fraud confidence")
    elif ml_score > 0.6: f.append("• ML model shows elevated fraud risk")
    words = check_data.get('word_amount', '')
    if words and amt and len(words.split()) < 3: f.append("• Incomplete written amount")
    return f if f else ["• No major risk factors identified"]

def get_detailed_risk_factors(transaction_data, fraud_score):
    f = []
    amount = float(transaction_data.get('amount', 0))
    if amount > 10000: f.append(f"• Very high transaction amount (>${amount:,.2f}) - Exceeds normal threshold")
    elif amount > 5000: f.append(f"• High transaction amount (>${amount:,.2f}) - Above average transaction size")
    elif amount > 1000: f.append(f"• Moderate transaction amount (>${amount:,.2f})")
    tod = transaction_data.get('time', '')
    if "Night" in tod: f.append("• Unusual transaction time (night) - 12AM–6AM higher risk")
    elif "Morning" in tod: f.append("• Standard transaction time (morning)")
    device = transaction_data.get('device', '')
    if device == "ATM" and amount > 1000: f.append("• Large ATM withdrawal")
    elif device == "ATM": f.append("• ATM transaction")
    elif device == "Mobile App": f.append("• Mobile transaction")
    elif device == "Phone": f.append("• Phone-based transaction")
    loc = (transaction_data.get('location') or '').strip().lower()
    if not loc or loc == 'unknown': f.append("• Unknown transaction location")
    else: f.append(f"• Transaction location: {transaction_data.get('location')}")
    typ = transaction_data.get('type', '')
    if typ == "Transfer": f.append("• Transfer transaction")
    elif typ == "Withdrawal": f.append("• Withdrawal transaction")
    elif typ == "Payment": f.append("• Payment transaction")
    rec = transaction_data.get('recipient', '')
    if not rec or rec.lower() == 'unknown': f.append("• Unverified recipient")
    else: f.append(f"• Recipient verified: {rec}")
    if fraud_score > 0.8: f.append("• ML model shows very high fraud confidence (>80%)")
    elif fraud_score > 0.6: f.append("• ML model shows elevated fraud risk (60–80%)")
    elif fraud_score > 0.4: f.append("• ML model shows moderate fraud risk (40–60%)")
    else: f.append("• ML model shows low fraud risk (<40%)")
    if amount > 5000 and device == "ATM": f.append("• Unusual combo: High-value ATM transaction")
    return f if f else ["• No major risk factors identified"]

# ===================== UI =====================
tab1, tab2 = st.tabs(["Check Analysis", "Online Transaction Analysis"])

# ===== CHECK ANALYSIS TAB =====
with tab1:
    st.markdown("<div class='section-title'>Enhanced Check Analysis with AI</div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1])
    with c1:
        up = st.file_uploader("Upload File", help="Upload a clear image for processing", label_visibility="collapsed")
        if up is not None:
            try:
                up.seek(0)
                img = Image.open(up)
            except Exception:
                st.error("Please upload a valid image file.")
                img = None
            if img is not None:
                st.image(img, caption="Uploaded Image", use_container_width=True)
                if st.button("Analyze Check", type="primary"):
                    with st.spinner("Analyzing check for fraud..."):
                        up.seek(0)
                        extracted, combined, raw, ml_s, rule_s, ml_ens = mindee_ocr_analysis_with_ml(up)
                    if extracted and combined is not None:
                        st.success("Check processed successfully!")
                        st.session_state.Check_results = {
                            'extracted_data': extracted,
                            'fraud_score': combined,
                            'ml_score': ml_s,
                            'rule_score': rule_s,
                            'raw_data': raw,
                            'ml_ensemble': ml_ens
                        }
                    else:
                        st.error("Failed to process the Check. Please check your Mindee configuration and try again.")
    with c2:
        if 'Check_results' in st.session_state:
            st.markdown("<h4 class='tight-h4'>Enhanced Analysis Results</h4>", unsafe_allow_html=True)
            res = st.session_state.Check_results
            st.markdown("**Extracted Information:**")
            for k, v in res['extracted_data'].items():
                st.text(f"{k}: {v}")
            st.markdown("---")
            fs = res['fraud_score']
            ml_score = res.get('ml_score', 0)
            rule_score = res.get('rule_score', 0)
            level, color = get_risk_level(fs)
            st.markdown("**Enhanced Fraud Analysis:**")
            st.markdown(f"**Risk Level:** :{color}[{level}]")
            st.progress(float(fs))
            st.markdown(f"<h2 style='color: {color}; margin: 4px 0 6px 0;'>Fraud Detection Score: {fs*100:.0f}%</h2>", unsafe_allow_html=True)
            st.markdown("**Risk Factors:**")
            for f in get_check_risk_factors(res.get('raw_data', {}), ml_score, rule_score):
                st.text(f)
            st.markdown("**Recommendations:**")
            if fs >= 0.7:
                st.error("High fraud risk detected. Recommend manual verification and additional authentication.")
            elif fs >= 0.4:
                st.warning("Medium risk. Additional verification suggested before processing.")
            else:
                st.success("Low risk. Transaction appears legitimate and can be processed.")

# ===== ONLINE TRANSACTION TAB =====
with tab2:
    st.markdown("<div class='section-title'>Online Transaction Analysis</div>", unsafe_allow_html=True)

    # Time-of-day bucket
    now = datetime.now().hour
    if 6 <= now < 12: tod = "Morning (6AM-12PM)"
    elif 12 <= now < 18: tod = "Afternoon (12PM-6PM)"
    elif 18 <= now < 24: tod = "Evening (6PM-12AM)"
    else: tod = "Night (12AM-6AM)"

    c1, c2 = st.columns([1, 1])
    with c1:
        st.subheader("Transaction Details")
        with st.form("transaction_form"):
            acct = st.text_input("Account Number", placeholder="Enter account number")
            amt_in = st.text_input("Transaction Amount ($)", placeholder="Enter amount")
            recip = st.text_input("Recipient Name", placeholder="Enter recipient name")
            ttype = st.selectbox("Transaction Type", ["Transfer", "Payment", "Withdrawal", "Deposit"])
            merch = st.text_input("Merchant", placeholder="Enter merchant")
            loc = st.text_input("Transaction Location", placeholder="City, State")
            device = st.selectbox("Device Used", options=["Web Browser", "Mobile App", "ATM", "Phone"], index=0)
            submitted = st.form_submit_button("Analyze Transaction", type="primary")

            amount = 0.0
            if amt_in:
                try:
                    amount = float(amt_in)
                except ValueError:
                    st.error("Please enter a valid numeric amount")
                    amount = 0.0

            if submitted and acct and amount > 0:
                exact = datetime.now().strftime("%I:%M:%S %p on %B %d, %Y")
                data = {
                    "account_number": acct, "amount": amount, "recipient": recip, "type": ttype,
                    "merchant": merch, "location": loc, "time": tod, "exact_time": exact, "device": device
                }
                with st.spinner("Analyzing transaction for fraud patterns..."):
                    res = ml_transaction_analysis(data)
                if isinstance(res, dict):
                    score = res['ensemble_probability']
                    st.session_state.transaction_results = {'data': data, 'fraud_score': score, 'ensemble_result': res}
                else:
                    st.session_state.transaction_results = {'data': data, 'fraud_score': res, 'ensemble_result': None}

    with c2:
        if 'transaction_results' in st.session_state:
            st.subheader("Analysis Results")
            r = st.session_state.transaction_results
            d = r['data']; s = r['fraud_score']
            st.markdown("**Transaction Summary:**")
            st.text(f"Account: {d['account_number']}")
            st.text(f"Amount: ${d['amount']:,.2f}")
            st.text(f"Type: {d['type']}")
            st.text(f"Recipient: {d['recipient']}")
            st.text(f"Merchant: {d['merchant']}")
            st.text(f"Location: {d['location']}")
            st.text(f"Device: {d['device']}")
            st.text(f"Transaction Time: {d.get('exact_time', 'N/A')}")
            st.markdown("---")
            st.markdown("**Fraud Analysis:**")
            lvl, color = get_risk_level(s)
            st.markdown(f"**Risk Level:** :{color}[{lvl}]")
            st.progress(float(s))
            st.markdown("---")
            st.markdown("**AI Fraud Detection Score:**")
            st.markdown(f"<h2 style='color: {color}; margin: 4px 0 6px 0;'>{s*100:.1f}%</h2>", unsafe_allow_html=True)
            if s < 0.4:
                st.success("LOW RISK TRANSACTION"); st.info("Transaction appears legitimate!")
            elif s < 0.7:
                st.warning("MEDIUM RISK TRANSACTION")
            else:
                st.error("HIGH RISK TRANSACTION"); st.warning("Manual review required!")
            st.markdown("---")
            st.markdown("**Risk Factors:**")
            for f in get_detailed_risk_factors(d, s): st.text(f)
            st.markdown("---")
            st.markdown("**Recommendations:**")
            if s >= 0.7: st.error("BLOCK TRANSACTION - High fraud risk detected. Require additional verification and manual review.")
            elif s >= 0.4: st.warning("REQUEST VERIFICATION - Medium risk. Additional authentication before processing.")
            else: st.success("APPROVE TRANSACTION - Low fraud risk")
            st.markdown("---")
            st.markdown("**Processing Status:**")
            if s < 0.4:
                st.markdown("- ✅ Transaction approved for processing"); st.markdown("- ✅ Normal monitoring applies"); st.markdown("- ✅ Proceed with standard workflow")
            elif s < 0.7:
                st.markdown("- ⚠️ Transaction requires additional verification"); st.markdown("- ⚠️ Enhanced monitoring applied"); st.markdown("- ⚠️ Waiting for authentication")
            else:
                st.markdown("- ❌ Transaction blocked"); st.markdown("- ❌ Manual review required"); st.markdown("- ❌ Customer notification sent")

# ---- Centered "LAUNCH INSIGHTS" (no extra spacer above footer) ----
cA, cB, cC = st.columns([1,1,1])
with cB:
    if st.button("LAUNCH INSIGHTS", key="dashboard_btn", type="primary", use_container_width=True):
        go_dashboard()  # jump straight to dashboard

# ---- Fixed footer (no visible gap) ----
st.markdown("""
<div class='fixed-footer'>
  <span>Where Innovation Meets Security</span>
  <span class="sep">|</span>
  <span>Zero Tolerance for Fraud</span>
  <span class="sep">|</span>
  <span>© Xforia DAD</span>
</div>
""", unsafe_allow_html=True)
