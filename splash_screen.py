# splash_screen.py

import streamlit as st
from streamlit.components.v1 import html as html_comp
import base64
from pathlib import Path

LOGO_PATH = "DAD_red_black.png"

def img_to_bytes(p: str) -> str:
    return base64.b64encode(Path(p).read_bytes()).decode()

def img_tag(p: str, h: int = 250, w: int | None = None, style: str = "") -> str:
    b64 = img_to_bytes(p)
    ext = Path(p).suffix.lower()
    mime = "image/jpeg" if ext in (".jpg", ".jpeg") else "image/png"
    w_attr = f"width:{w}px;" if w else ""
    return f"<img src='data:{mime};base64,{b64}' style='height:{h}px;{w_attr}{style}' alt='DAD Logo'/>"

ICON_STYLE = "width:20px;height:20px;vertical-align:-3px;"
DOC_ICON    = f"<svg style='{ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2'><path d='M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z'/><path d='M14 2v6h6'/></svg>"
ALERT_ICON  = f"<svg style='{ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2'><circle cx='12' cy='12' r='10'/><path d='M12 8v4M12 16h.01'/></svg>"
TARGET_ICON = f"<svg style='{ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2'><circle cx='12' cy='12' r='8'/><path d='M12 2v4M12 18v4M2 12h4M18 12h4'/><circle cx='12' cy='12' r='2'/></svg>"
CARD_ICON   = f"<svg style='{ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2'><rect x='2' y='5' width='20' height='14' rx='2'/><path d='M2 10h20'/></svg>"

st.set_page_config(page_title="Xforia DAD", layout="wide")

_BASE_CSS = """
<style>
header, footer { display:none; }
.main .block-container, .block-container, .stApp { padding:0 !important; margin:0 !important; max-width:100vw !important; width:100vw !important; }
body, html { margin:0; padding:0; width:100vw; overflow-x:hidden; }

#MainMenu, [data-testid="stAppViewContainer"] > header > div[role="banner"] { display: none !important; }

/* Red Launch button styling */
.stButton > button {
  background: #ff1a1a !important;
  color: #ffffff !important;
  border: 0 !important;
  border-radius: 10px !important;
  padding: 0.8rem 1.25rem !important;
  font-weight: 800 !important;
  letter-spacing: .02em !important;
  box-shadow: 0 8px 18px rgba(255, 26, 26, .35) !important;
  cursor: pointer !important;
  margin-bottom: 20px !important;
}
.stButton > button:hover { 
  filter: brightness(0.95);
}
.stButton > button:active { 
  transform: translateY(1px);
}
.stButton > button:focus { 
  outline: 2px solid #ffd6d6; 
  outline-offset: 2px; 
}
</style>
"""

def _splash_html(logo_html: str) -> str:
    return f"""
<style>
:root {{
  --bg:#ffffff; --text:#0f172a; --muted:#475569; --card:#f8fafc; --line:#e2e8f0;
  --brand:#1e3c72; --brand2:#2a5298; --accent:#2e7d32; --brand3:#D32F2F;
}}
.container {{
  background:var(--bg);
  font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,'Noto Sans';
  color:var(--text);
}}
.hero {{ max-width:1060px; margin:0px auto 4px; display:flex; align-items:center; justify-content:center; }}
.hero-logo {{ display:flex; align-items:center; justify-content:center; }}
.hero-sub {{ font-size:18px; color:var(--muted); margin-top:10px; text-align:center; }}

.block {{ max-width:1060px; margin:24px auto 20px; display:grid; grid-template-columns: repeat(3, minmax(260px,1fr)); gap:24px; }}

.card {{
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 28px 24px;
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}}

.card::before {{
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--brand), var(--brand2));
  opacity: 0;
  transition: opacity 0.3s ease;
}}

.card:hover {{
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(15, 23, 42, 0.12);
  border-color: var(--brand);
}}

.card:hover::before {{
  opacity: 1;
}}

.card .top {{
  display: flex;
  align-items: center; /* bottom-align icon and text */
  justify-content:center;
  gap: 12px;
  margin-bottom: 12px;
}}


.word-with-first {{
  display: inline-flex;
  align-items: flex-end; /* bottom-align rest of word with first letter */
  font-weight: 700;
  text-transform: uppercase;
  font-size: 1.25rem;
  letter-spacing: 0.05em;
  color: var(--text);
}}

.first-letter {{
  font-size: 2rem;
  color: var(--brand3);
  line-height: 1;
}}
  
.card h3 {{
  margin: 0 0 12px;
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--text);
  line-height: 1.3;
  white-space: nowrap; 
}}

.card p {{
  margin: 0;
  line-height: 1.6;
  color: var(--muted);
  font-size: 0.95rem;
}}
.section-title {{ max-width:1060px; margin:32px auto 14px; font-size:32px; font-weight:900; text-align:center; color:var(--text); letter-spacing:.02em; }}

.features {{ max-width:1060px; margin:0 auto 4px; display:grid; grid-template-columns:repeat(2,minmax(320px,1fr)); gap:24px; }}
.feature {{ background:var(--card); border:1px solid var(--line); border-radius:16px; padding:18px; }}
.feature .title {{ font-weight:800; margin-bottom:8px; }}
.feature ul {{ margin:0; padding-left:18px; line-height:1.5em; }}
.feature:hover {{
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(15, 23, 42, 0.12);
  border-color: var(--brand);
}}
.features h2 {{
  grid-column: 1 / -1;
  padding-top:60px;
  text-align: center;
  margin-bottom: 12px;
}}


.metrics {{ max-width:1060px; margin:24px auto 20px; display:grid; grid-template-columns:repeat(3,minmax(220px,1fr)); gap:18px; }}
.metric {{ background:var(--card); border:1px solid var(--line); border-radius:16px; padding:18px; text-align:center; }}
.metric .kpi {{ font-size:28px; font-weight:900; color:var(--brand); }}
.metric .label {{ color:var(--muted); margin-top:4px; }}
.metric:hover {{
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(15, 23, 42, 0.12);
  border-color: var(--brand);
}}

/* Section background */
.impacts-section {{
  padding: 50px 0;
  margin-top: 40px;
}}

/* Section title */
.impacts-section h2 {{
  grid-column: 1 / -1;
  text-align: center;
  margin-bottom: 6px;
  font-size: 1.5rem;
  font-weight: bold;
  letter-spacing: .02em;
  text-transform: uppercase;
}}

.section-subtitle {{
  text-align: center;
  color: #555;
  font-size: 16px;
  margin-bottom: 28px;
}}

/* Impacts container */
.impacts-alt {{
  display: grid;
  gap: 16px;
  max-width: 920px;
  margin: 0 auto;
  padding: 0 16px;
}}

.impacts-section h2 {{
  margin-bottom: 30px;
}}

/* Individual impact card */
.impact-line {{
  background: var(--card);
  padding: 16px 20px;          /* equal spacing */
  border-radius: 12px;
  display: flex;
  align-items: center;         /* vertical center */
  border: 1px solid var(--line);
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  margin-bottom: 10px;

  /* single line text */
  white-space: nowrap;
  overflow-x: auto;            /* scroll if too long */
  scrollbar-width: thin;       /* optional: thin scrollbar */
  border-left: none;           /* remove visual shift from left border */
  position: relative;          /* for pseudo-element */
}}

/* Left colored border as pseudo-element so it doesn’t affect spacing */
.impact-line::before {{
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  width: 5px;
  height: 100%;
  background: #1e3c72;
  border-radius: 12px 0 0 12px;
}}

.impact-line:hover {{
  transform: translateY(-3px);
  box-shadow: 0 6px 16px rgba(0,0,0,0.1);
}}

.impact-line span {{
  flex: 1;                     /* take remaining space */
  display: inline-block;
  padding-left: 5px;           /* spacing from pseudo-border */
  white-space: nowrap;  
}}

/* Icons */
.impact-line .icon {{
  font-size: 20px;
  flex-shrink: 0;
}}

/* Bold text highlight */
.impact-line strong {{
  color: #1e3c72;
}}

 .fixed-footer {{
        position: fixed; left: 0; right: 0; bottom: 0;
        height: 64px;
        background:#1e3c72;
        color:#fff;
        display: flex; align-items: center; justify-content: center; gap: 10px;
        padding: 10px 16px;
        z-index: 1000;
        box-shadow: 0 -2px 10px rgba(0,0,0,.22);
        font-size: 0.95em;
        font-weight: 600;
    }}
  .fixed-footer .sep {{ opacity: .6; padding: 0 8px; }}

   [data-testid="stSidebar"] {{
            display: none;
        }}
        [data-testid="stSidebarNav"] {{
            display: none;
        }}
        [data-testid="stSidebarCollapseButton"] {{
            display: none;
        }}

@media (max-width:900px) {{
  .block,.features,.metrics {{ grid-template-columns:1fr; }}
}}
</style>

<div class="container">
  <div class="hero">
    <div class="hero-logo">{logo_html}</div>
  </div>
  <div class="hero-sub">Document Anomaly Detection — The Intelligence That Safeguards Your Next Move</div>

<div class="block">
  <div class="card">
    <div class="top">
      <span class="word-with-first">
        <span class="first-letter">D</span>ocument
      </span>
    </div>
    <h3>Trusted document screening</h3>
    <p>We automatically screen every document and validate both its format and content to ensure compliance and authenticity.</p>
  </div>

  <div class="card">
    <div class="top">
      <span class="word-with-first">
        <span class="first-letter">A</span>nomaly
      </span>
    </div>
    <h3>Behavior-aware risk detection</h3>
    <p>The anomaly engine detects suspicious patterns and applies behavioral analysis to surface risks that humans might miss.</p>
  </div>

  <div class="card">
    <div class="top">
      <span class="word-with-first">
        <span class="first-letter">D</span>etection
      </span>
    </div>
    <h3>Real-time fraud scoring</h3>
    <p>We provide accurate, real-time monitoring with instant scoring so threats are flagged before they cause damage.</p>
  </div>
</div>


  <div class="features">
   <h2>FEATURES</h2>
    <div class="feature">
      <div class="title">{DOC_ICON} SMART CHECK ANALYSIS</div>
      <ul>
        <li>Ai-Vision data extraction</li>
        <li>Amount validation</li>
        <li>Document authentication</li>
        <li>Record verification</li>
      </ul>
    </div>
    <div class="feature">
      <div class="title">{CARD_ICON} TRANSACTION MONITORING</div>
      <ul>
        <li>Real-time risk assessment</li>
        <li>Behavioral pattern analysis</li>
        <li>Customer verification</li>
        <li>Fast action</li>
      </ul>
    </div>
  </div>

  <div class="metrics">
    <div class="metric">
      <div class="kpi">Maximum Impact</div>
      <div style="margin-top:6px;">Consistently high precision across cheque and online flows.</div>
    </div>
    <div class="metric">
      <div class="kpi">Swift</div>
      <div style="margin-top:6px;">From start to finish, your data moves at lightning speed, going from raw image to final decision before you can blink.</div>
    </div>
    <div class="metric">
      <div class="kpi">AI-powered vision</div>
      <div style="margin-top:6px;">A smart team of models with sharp eyes for details and clear explanations for every decision (explainability).</div>
    </div>
  </div>


<section class="impacts-section">
  <h2>BUSINESS IMPACTS</h2>
  <div class="impacts-alt">
    <div class="impact-line">
      <span><strong>Reduce losses</strong> and approve faster with intelligent fraud detection. Earn customer trust while running operations smoothly. </span>
    </div>
    <div class="impact-line">
      <span><strong>Stop fraud</strong> before it impacts your bottom line. Deliver fast approvals and seamless experiences that customers can trust. </span>
    </div>
    <div class="impact-line">
      <span><strong>Protect revenue</strong> with smarter, quicker decisions. Build confidence and minimize disruptions across your business. </span>
    </div>
    <div class="impact-line">
      <span><strong>Cut financial risks </strong> and speed up approvals. Keep customers happy while ensuring uninterrupted operations.</span>
    </div>
  </div>
</section>


</div>
"""

def show_splash():
    st.markdown(_BASE_CSS, unsafe_allow_html=True)

    if "splash_ph" not in st.session_state:
        st.session_state.splash_ph = st.empty()
    if "show_splash" not in st.session_state:
        st.session_state.show_splash = True

    if st.session_state.show_splash:
        logo_html = ""
        try:
            logo_html = img_tag(LOGO_PATH, h=250)
        except Exception:
            pass

        with st.session_state.splash_ph.container():
            html_comp(_splash_html(logo_html), height=1500, scrolling=False)
            
            # Add spacing before button
            st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)
            
            # Center button using columns
            col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
            with col3:
                if st.button("LAUNCH DAD", key="enter_app", use_container_width=True):
                    st.session_state.show_splash = False
                    st.session_state.splash_ph.empty()
                    st.rerun()
            
            # Footer
            st.markdown("""
            <div style="padding:10px 16px; color:#fff; background:#1e3c72; display:flex; align-items:center; justify-content:center; gap:10px; box-shadow:0 -2px 10px rgba(0,0,0,.22); font-weight:600; margin-top:30px; height: 64px; font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,'Noto Sans';">
              <span>Where Innovation Meets Security</span>
              <span style="opacity:.6; padding:0 8px;">|</span>
              <span>Zero Tolerance for Fraud</span>
              <span style="opacity:.6; padding:0 8px;">|</span>
              <span>© Xforia DAD </span>
            </div>
            """, unsafe_allow_html=True)