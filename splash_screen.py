



























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

IMPACT_ICON_STYLE = "width:28px;height:28px;margin-right:12px;flex-shrink:0;"
LOSS_ICON    = f"<svg style='{IMPACT_ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='#db123d' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'><path d='M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6'/></svg>"
SHIELD_ICON  = f"<svg style='{IMPACT_ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='#1e3c72' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'><path d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'/></svg>"
REVENUE_ICON = f"<svg style='{IMPACT_ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='#059669' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'><polyline points='23 6 13.5 15.5 8.5 10.5 1 18'/><polyline points='17 6 23 6 23 12'/></svg>"
SPEED_ICON   = f"<svg style='{IMPACT_ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='#7c3aed' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'><circle cx='12' cy='12' r='10'/><polyline points='12 6 12 12 16 14'/></svg>"

st.set_page_config(page_title="Xforia DAD", layout="wide")

_BASE_CSS = """
<style>
header, footer { display:none; }
.main .block-container, .block-container, .stApp { padding:0 !important; margin:0 !important; max-width:100vw !important; width:100vw !important; }
body, html { margin:0; padding:0; width:100vw; overflow-x:hidden; }
#MainMenu, [data-testid="stAppViewContainer"] > header > div[role="banner"] { display: none !important; }

/* Unified vertical rhythm */
:root {
  --section-gap: 28px;
  --gap-sm: 12px;
}

/* Keep the same visual gap between impacts and button */
.after-splash { margin-top:-86px; }
@media (max-width:1200px){ .after-splash{ margin-top:-74px; } }
@media (max-width:900px){  .after-splash{ margin-top:-62px; } }
@media (max-width:700px){  .after-splash{ margin-top:-50px; } }

/* Button styling */
.stButton > button {
  background: #db123d !important;
  color: #ffffff !important;
  border: 0 !important;
  border-radius: 10px !important;
  padding: 0.8rem 1.25rem !important;
  font-weight: 800 !important;
  letter-spacing: .02em !important;
  box-shadow: none !important;
  cursor: pointer !important;
  margin-bottom: 8px !important;
}
.stButton > button:hover { filter: brightness(0.95); }
.stButton > button:active { transform: translateY(1px); }
.stButton > button:focus { outline: 2px solid #ffd6d6; outline-offset: 2px; }
</style>
"""

def _splash_html(logo_html: str) -> str:
    return f"""
<style>
:root {{
  --bg:#ffffff; --text:#0f172a; --muted:#475569; --card:#f8fafc; --line:#e2e8f0;
  --brand:#1e3c72; --brand2:#2a5298; --brand3:#db123d;
  --section-gap: 28px;
  --gap-sm: 12px;
}}
.container {{
  background:var(--bg);
  font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,'Noto Sans';
  color:var(--text);
  margin:0;
  padding:0;
}}
.hero {{ max-width:1060px; margin:0 auto var(--gap-sm); display:flex; align-items:center; justify-content:center; }}
.hero-logo {{ display:flex; align-items:center; justify-content:center; transform: scale(0.85); margin:10px 0 6px; }}

/* The Intelligence... line */
.hero-sub {{
  font-size:20px; color:#0b2a6f !important; font-weight:600 !important;
  margin:2px 0 var(--section-gap); text-align:center;
}}

/* D • A • D cards block */
.block {{
  max-width:1060px; margin:0 auto var(--section-gap);
  display:grid; grid-template-columns: repeat(3, minmax(260px,1fr)); gap:18px;
}}
.card {{
  background:var(--card); border:1px solid var(--line); border-radius:16px; padding:20px 18px;
  box-shadow:0 4px 12px rgba(15, 23, 42, 0.05); transition:all .3s; position:relative; overflow:hidden; margin:0;
}}
.card::before {{ content:''; position:absolute; top:0; left:0; right:0; height:4px; background:linear-gradient(90deg, var(--brand), var(--brand2)); opacity:0; transition:opacity .3s; }}
.card:hover {{ transform:translateY(-4px); box-shadow:0 12px 32px rgba(15, 23, 42, 0.12); border-color:var(--brand); }}
.card:hover::before {{ opacity:1; }}
.card .top {{ display:flex; align-items:center; justify-content:center; gap:12px; margin-bottom:8px; }}
.word-with-first {{ display:inline-flex; align-items:flex-end; font-weight:700; text-transform:uppercase; font-size:1.1rem; letter-spacing:.05em; color:var(--text); }}
.first-letter {{ font-size:1.65rem; color:var(--brand3); line-height:1; }}
.card h3 {{ margin:0 0 6px; font-size:1.15rem; font-weight:800; letter-spacing:-0.01em; color:var(--text); line-height:1.3; white-space:nowrap; }}
.card p {{ margin:0; line-height:1.5; color:var(--muted); font-size:.95rem; }}

/* FEATURES section */
.features-wrapper {{ max-width:1060px; margin:0 auto var(--section-gap); }}
.features-title {{ font-size:26px; font-weight:900; text-align:center; color:var(--text); letter-spacing:.02em; margin:0 0 var(--gap-sm); }}
.features {{ display:grid; grid-template-columns:repeat(3,minmax(280px,1fr)); gap:14px; }}
.feature {{ background:var(--card); border:1px solid var(--line); border-radius:16px; padding:18px 18px; box-shadow:0 4px 12px rgba(15,23,42,0.05); transition:transform .2s, box-shadow .2s, border-color .2s; position:relative; overflow:hidden; margin:0; }}
.feature::before {{ content:''; position:absolute; top:0; left:0; right:0; height:4px; background:linear-gradient(90deg, var(--brand), var(--brand2)); opacity:0; transition:opacity .3s; }}
.feature:hover {{ transform:translateY(-4px); box-shadow:0 12px 32px rgba(15, 23, 42, 0.12); border-color:var(--brand); }}
.feature:hover::before {{ opacity:1; }}
.feature .title {{ font-size:19px; font-weight:900; letter-spacing:.01em; color:#1e3c72; margin-bottom:8px; text-align:center; line-height:1.2; white-space:nowrap; }}
.feature p {{ margin:0; line-height:1.5; color:var(--text); text-align:left; }}

/* Metrics */
.metrics {{ max-width:1060px; margin:0 auto var(--section-gap); display:grid; grid-template-columns:repeat(3,minmax(220px,1fr)); gap:12px; }}
.metric {{ background:var(--card); border:1px solid var(--line); border-radius:16px; padding:14px; text-align:center; }}
.metric .title {{ font-size:19px; font-weight:900; letter-spacing:.01em; color:#1e3c72; margin-bottom:8px; line-height:1.2; }}

/* BUSINESS IMPACTS - New Design */
.impacts-section {{ margin:0 0 0 0; padding:0; }}
.impacts-section h2 {{ text-align:center; margin:0 0 20px 0; font-size:26px; font-weight:900; letter-spacing:.02em; color:var(--text); }}
.impacts-grid {{ 
  display:grid; 
  grid-template-columns:repeat(2, minmax(400px, 520px)); 
  gap:16px; 
  max-width:1100px; 
  margin:0 auto; 
  padding:0 16px; 
  justify-content:center;
}}
.impact-card {{
  background:linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
  padding:20px 24px;
  border-radius:16px;
  display:flex;
  align-items:center;
  gap:16px;
  border:2px solid #e2e8f0;
  box-shadow:0 4px 16px rgba(15, 23, 42, 0.08);
  transition:all .3s ease;
  position:relative;
  overflow:hidden;
}}
.impact-card::before {{
  content:'';
  position:absolute;
  top:0;
  left:0;
  width:6px;
  height:100%;
  background:linear-gradient(180deg, var(--brand), var(--brand2));
  opacity:0;
  transition:opacity .3s;
}}
.impact-card:hover {{
  transform:translateY(-6px) scale(1.02);
  box-shadow:0 12px 32px rgba(15, 23, 42, 0.15);
  border-color:var(--brand);
}}
.impact-card:hover::before {{
  opacity:1;
}}
.impact-content {{
  flex:1;
  text-align:left;
}}
.impact-title {{
  font-size:18px;
  font-weight:800;
  color:var(--text);
  margin-bottom:6px;
  letter-spacing:0.01em;
}}
.impact-desc {{
  font-size:15px;
  color:var(--muted);
  line-height:1.6;
  margin:0;
}}

@media (max-width:1100px) {{ 
  .impacts-grid {{ grid-template-columns:1fr; max-width:540px; }}
}}
@media (max-width:900px) {{ .block,.features,.metrics {{ grid-template-columns:1fr; }} }}
</style>

<div class="container">
  <div class="hero"><div class="hero-logo">{logo_html}</div></div>
  <div class="hero-sub">The Intelligence That Safeguards Your Next Move</div>

  <div class="block">
    <div class="card">
      <div class="top"><span class="word-with-first"><span class="first-letter">D</span>ocument</span></div>
      <h3>Trusted document screening</h3>
      <p>Automatically screen every document and validate both its format and content to ensure compliance and authenticity.</p>
    </div>
    <div class="card">
      <div class="top"><span class="word-with-first"><span class="first-letter">A</span>nomaly</span></div>
      <h3>Behavior-aware risk detection</h3>
      <p>The anomaly engine detects suspicious patterns and applies behavioral analysis to surface risks that humans might miss.</p>
    </div>
    <div class="card">
      <div class="top"><span class="word-with-first"><span class="first-letter">D</span>etection</span></div>
      <h3>Real-time fraud scoring</h3>
      <p>Provides accurate, real-time monitoring with instant scoring so threats are flagged before they cause damage.</p>
    </div>
  </div>

  <div class="features-wrapper">
    <h2 class="features-title">FEATURES</h2>
    <div class="features">
      <div class="feature"><div class="title">Adaptive Risk Models</div><p>Adapts quickly to emerging fraud and behavior patterns.</p></div>
      <div class="feature"><div class="title">Explainable Decisions</div><p>Clear, visual reasons for every alert.</p></div>
      <div class="feature"><div class="title">Seamless Integration</div><p>Effortless setup with plug-and-play APIs.</p></div>
    </div>
  </div>

  <div class="metrics">
    <div class="metric"><div class="title">Maximum Impact</div><div style="margin-top:4px;">Consistently high precision across check and online flows.</div></div>
    <div class="metric"><div class="title">Real-Time</div><div style="margin-top:4px;">From raw image to decision in seconds.</div></div>
    <div class="metric"><div class="title">Secure Architecture</div><div style="margin-top:4px;">End-to-end protection with zero data leaks.</div></div>
  </div>

  <section class="impacts-section">
    <h2>BUSINESS IMPACTS</h2>
    <div class="impacts-grid">
      <div class="impact-card">
        {LOSS_ICON}
        <div class="impact-content">
          <div class="impact-title">Protect Margins</div>
          <p class="impact-desc">Make smarter decisions faster to protect margins and prevent fraud early.</p>
        </div>
      </div>
      <div class="impact-card">
        {SHIELD_ICON}
        <div class="impact-content">
          <div class="impact-title">Defend Against Smart Threats</div>
          <p class="impact-desc">Intercept threats before they impact your bottom line or customer experience.</p>
        </div>
      </div>
      <div class="impact-card">
        {REVENUE_ICON}
        <div class="impact-content">
          <div class="impact-title">Accelerate Trusted Approvals</div>
          <p class="impact-desc">Maintain approvals and cash flow while minimizing false declines.</p>
        </div>
      </div>
      <div class="impact-card">
        {SPEED_ICON}
        <div class="impact-content">
          <div class="impact-title">Stay Resilient</div>
          <p class="impact-desc">Accelerate approvals and keep operations running without disruption.</p>
        </div>
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
            logo_html = img_tag(LOGO_PATH, h=140)
        except Exception:
            pass

        with st.session_state.splash_ph.container():
            html_comp(_splash_html(logo_html), height=1100, scrolling=False)

            st.markdown("<div class='after-splash'>", unsafe_allow_html=True)
            col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
            with col3:
                if st.button("LAUNCH DAD", key="enter_app", use_container_width=True):
                    st.session_state.show_splash = False
                    st.session_state.splash_ph.empty()
                    st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown(
                "<div style='text-align:center; font-size:18px; color:#0b2a6f; font-weight:600; margin:8px auto 20px; padding:0 20px; font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,'Noto Sans'; font-style:italic;'>"
                "\"Just like Dad protects the home, Xforia's DAD keeps fraud from going prone\""
                "</div>",
                unsafe_allow_html=True
            )

            #Footer
            st.markdown("""
            <div style="padding:10px 16px; color:#fff; background:#1e3c72; display:flex; align-items:center; justify-content:center; gap:10px; box-shadow:0 -2px 10px rgba(0,0,0,.22); font-weight:600; margin-top:10px; height:64px; font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,'Noto Sans';">
              <span>Where Innovation Meets Security</span>
              <span style="opacity:.6; padding:0 8px;">|</span>
              <span>Zero Tolerance for Fraud</span>
              <span style="opacity:.6; padding:0 8px;">|</span>
              <span>© Xforia DAD</span>
            </div>
            """, unsafe_allow_html=True)

        st.stop()