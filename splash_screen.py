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

# Function to display image outside HTML component (like first file)
def img_to_html(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    ext = Path(img_path).suffix.lower()
    mime = "image/jpeg" if ext in (".jpg", ".jpeg") else "image/png"
    return f"<img src='data:{mime};base64,{encoded}' style='height: 120px; width: 120px; border-radius: 8px;' alt='FDN Tag'/>"

ICON_STYLE = "width:20px;height:20px;vertical-align:-3px;"
DOC_ICON    = f"<svg style='{ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2'><path d='M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z'/><path d='M14 2v6h6'/></svg>"
ALERT_ICON  = f"<svg style='{ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2'><circle cx='12' cy='12' r='10'/><path d='M12 8v4M12 16h.01'/></svg>"
TARGET_ICON = f"<svg style='{ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2'><circle cx='12' cy='12' r='8'/><path d='M12 2v4M12 18v4M2 12h4M18 12h4'/><circle cx='12' cy='12' r='2'/></svg>"
CARD_ICON   = f"<svg style='{ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2'><rect x='2' y='5' width='20' height='14' rx='2'/><path d='M2 10h20'/></svg>"

# Business Impact Icons
IMPACT_ICON_STYLE = "width:22px;height:22px;vertical-align:-4px;margin-right:8px;"
LOSS_ICON = f"<svg style='{IMPACT_ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='#1e3c72' stroke-width='2.5'><path d='M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6'/></svg>"
SHIELD_ICON = f"<svg style='{IMPACT_ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='#1e3c72' stroke-width='2.5'><path d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'/></svg>"
REVENUE_ICON = f"<svg style='{IMPACT_ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='#1e3c72' stroke-width='2.5'><polyline points='23 6 13.5 15.5 8.5 10.5 1 18'/><polyline points='17 6 23 6 23 12'/></svg>"
SPEED_ICON = f"<svg style='{IMPACT_ICON_STYLE}' viewBox='0 0 24 24' fill='none' stroke='#1e3c72' stroke-width='2.5'><circle cx='12' cy='12' r='10'/><polyline points='12 6 12 12 16 14'/></svg>"

st.set_page_config(page_title="Xforia DAD", layout="wide")

_BASE_CSS = """
<style>
header, footer { display:none; }
.main .block-container, .block-container, .stApp { padding:0 !important; margin:0 !important; max-width:100vw !important; width:100vw !important; }
body, html { margin:0; padding:0; width:100vw; overflow-x:hidden; }

#MainMenu, [data-testid="stAppViewContainer"] > header > div[role="banner"] { display: none !important; }

/* Red Launch button styling */
.stButton > button {
  background: #db123d !important;
  color: #ffffff !important;
  border: 0 !important;
  border-radius: 10px !important;
  padding: 0.8rem 1.25rem !important;
  font-weight: 800 !important;
  letter-spacing: .02em !important;
  box-shadow: 0 8px 18px rgba(219, 18, 61, .35) !important;
  cursor: pointer !important;
  margin-bottom: 20px !important;
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
  --brand:#1e3c72; --brand2:#2a5298; --accent:#2e7d32; --brand3:#db123d;
}}
.container {{
  background:var(--bg);
  font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,'Noto Sans';
  color:var(--text);
}}
.hero {{ max-width:1060px; margin:0px auto 4px; display:flex; align-items:center; justify-content:center; margin-bottom:20px; }}
.hero-logo {{ display:flex; align-items:center; justify-content:center; transform: scale(1.3); margin-bottom:30px; }}

.hero-sub {{
  font-size:20px;
  color:#0b2a6f !important;
  font-weight:600 !important;
  margin-top:10px;
  text-align:center;
}}

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
  position: absolute; top: 0; left: 0; right: 0; height: 4px;
  background: linear-gradient(90deg, var(--brand), var(--brand2));
  opacity: 0; transition: opacity 0.3s ease;
}}
.card:hover {{ transform: translateY(-4px); box-shadow: 0 12px 32px rgba(15, 23, 42, 0.12); border-color: var(--brand); }}
.card:hover::before {{ opacity: 1; }}

.card .top {{ display:flex; align-items:center; justify-content:center; gap:12px; margin-bottom:12px; }}
.word-with-first {{ display:inline-flex; align-items:flex-end; font-weight:700; text-transform:uppercase; font-size:1.25rem; letter-spacing:.05em; color:var(--text); }}
.first-letter {{ font-size:2rem; color:var(--brand3); line-height:1; }}
.card h3 {{ margin:0 0 12px; font-size:1.35rem; font-weight:700; letter-spacing:-0.01em; color:var(--text); line-height:1.3; white-space:nowrap; }}
.card p {{ margin:0; line-height:1.6; color:var(--muted); font-size:.95rem; }}

.section-title {{ max-width:1060px; margin:32px auto 14px; font-size:32px; font-weight:900; text-align:center; color:var(--text); letter-spacing:.02em; }}

/* FEATURES - 3-column grid layout */
.features-wrapper {{ max-width:1060px; margin:32px auto 20px; }}
.features-title {{ font-size:32px; font-weight:900; text-align:center; color:var(--text); letter-spacing:.02em; margin-bottom:24px; }}
.features {{ display:grid; grid-template-columns:repeat(3,minmax(280px,1fr)); gap:20px; }}
.feature {{
  background:var(--card);
  border:1px solid var(--line);
  border-radius:16px;
  padding:28px 24px;
  box-shadow:0 4px 12px rgba(15,23,42,0.05);
  transition:transform .2s ease, box-shadow .2s ease, border-color .2s ease;
  position:relative;
  overflow:hidden;
}}
.feature::before {{
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 4px;
  background: linear-gradient(90deg, var(--brand), var(--brand2));
  opacity: 0; transition: opacity 0.3s ease;
}}
.feature:hover {{
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(15, 23, 42, 0.12);
  border-color: var(--brand);
}}
.feature:hover::before {{ opacity: 1; }}
.feature .title {{
  font-size:22px; font-weight:900; letter-spacing:.01em;
  color:#1e3c72; margin-bottom:14px; text-align:center; line-height:1.3;
  white-space:nowrap;
}}
.feature ul {{
  margin:0; padding-left:20px; list-style:disc;
  text-align:left; line-height:1.7; color:var(--muted);
}}
.feature ul li {{ margin-bottom:8px; }}
.feature p {{
  margin:0; line-height:1.7; color:var(--text); text-align:left;
}}

.metrics {{ max-width:1060px; margin:24px auto 20px; display:grid; grid-template-columns:repeat(3,minmax(220px,1fr)); gap:18px; }}
.metric {{ background:var(--card); border:1px solid var(--line); border-radius:16px; padding:18px; text-align:center; }}
.metric .title {{ font-size:22px; font-weight:900; letter-spacing:.01em; color:#1e3c72; margin-bottom:14px; line-height:1.3; }}
.metric .label {{ color:var(--muted); margin-top:4px; }}
.metric:hover {{ transform: translateY(-4px); box-shadow: 0 12px 32px rgba(15, 23, 42, 0.12); border-color: var(--brand); }}

/* Impacts */
.impacts-section {{ padding:50px 0; margin-top:40px; }}
.impacts-section h2 {{ text-align:center; margin-bottom:24px; font-size:32px; font-weight:900; letter-spacing:.02em; }}
.impacts-alt {{ display:grid; gap:16px; max-width:920px; margin:0 auto; padding:0 16px; }}
.impact-line {{
  background:var(--card); padding:16px 20px; border-radius:12px; display:flex; align-items:center;
  border:1px solid var(--line); box-shadow:0 2px 8px rgba(0,0,0,0.06);
  transition:transform .2s ease, box-shadow .2s ease; margin-bottom:10px;
  border-left:none; position:relative; white-space:nowrap; overflow:hidden;
}}
.impact-line::before {{ content:""; position:absolute; left:0; top:0; width:5px; height:100%; background:#1e3c72; border-radius:12px 0 0 12px; }}
.impact-line:hover {{ transform:translateY(-3px); box-shadow:0 6px 16px rgba(0,0,0,0.1); }}
.impact-line strong {{ color:#1e3c72; }}
.impact-line span {{ white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }}

.fixed-footer {{
  position:fixed; left:0; right:0; bottom:0; height:64px; background:#1e3c72; color:#fff;
  display:flex; align-items:center; justify-content:center; gap:10px;
  padding:10px 16px; z-index:1000; box-shadow:0 -2px 10px rgba(0,0,0,.22);
  font-size:.95em; font-weight:600;
}}
.fixed-footer .sep {{ opacity:.6; padding:0 8px; }}

[data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="stSidebarCollapseButton"] {{ display:none; }}

@media (max-width:900px) {{ .block,.features,.metrics {{ grid-template-columns:1fr; }} }}
</style>

<div class="container">
  <!-- HERO -->
  <div class="hero">
    <div class="hero-logo">{logo_html}</div>
  </div>
  <div class="hero-sub">The Intelligence That Safeguards Your Next Move</div>

  <!-- 3 CARDS -->
  <div class="block">
    <div class="card">
      <div class="top">
        <span class="word-with-first"><span class="first-letter">D</span>ocument</span>
      </div>
      <h3>Trusted document screening</h3>
      <p>Automatically screen every document and validate both its format and content to ensure compliance and authenticity.</p>
    </div>

    <div class="card">
      <div class="top">
        <span class="word-with-first"><span class="first-letter">A</span>nomaly</span>
      </div>
      <h3>Behavior-aware risk detection</h3>
      <p>The anomaly engine detects suspicious patterns and applies behavioral analysis to surface risks that humans might miss.</p>
    </div>

    <div class="card">
      <div class="top">
        <span class="word-with-first"><span class="first-letter">D</span>etection</span>
      </div>
      <h3>Real-time fraud scoring</h3>
      <p>Provides accurate, real-time monitoring with instant scoring so threats are flagged before they cause damage.</p>
    </div>
  </div>

  <!-- FEATURES -->
  <div class="features-wrapper">
    <h2 class="features-title">FEATURES</h2>
    <div class="features">
      <div class="feature">
        <div class="title">Adaptive Risk Models</div>
        <p>Adapts quickly to emerging fraud and behavior patterns.</p>
      </div>
      <div class="feature">
        <div class="title">Explainable Decisions</div>
        <p>Clear, visual reasons for every alert.</p>
      </div>
      <div class="feature">
        <div class="title">Seamless Integration</div>
        <p>Effortless setup with plug-and-play APIs.</p>
      </div>
    </div>
  </div>

  <!-- METRICS -->
  <div class="metrics">
    <div class="metric">
      <div class="title">Maximum Impact</div>
      <div style="margin-top:6px;">Consistently high precision across cheque and online flows.</div>
    </div>
    <div class="metric">
      <div class="title">Swift</div>
      <div style="margin-top:6px;">From raw image to decision in moments.</div>
    </div>
    <div class="metric">
      <div class="title">AI-powered vision</div>
      <div style="margin-top:6px;">Sharp detection with clear, explainable reasons.</div>
    </div>
  </div>

  <!-- BUSINESS IMPACTS -->
  <section class="impacts-section">
    <h2>BUSINESS IMPACTS</h2>
    <div class="impacts-alt">
      <div class="impact-line"><span>{LOSS_ICON}<strong>Reduce losses</strong> and approve faster with intelligent fraud detection. Earn customer trust while running operations smoothly.</span></div>
      <div class="impact-line"><span>{SHIELD_ICON}<strong>Stop fraud</strong> before it impacts your bottom line. Deliver fast approvals and seamless experiences that customers can trust.</span></div>
      <div class="impact-line"><span>{REVENUE_ICON}<strong>Protect revenue</strong> with smarter, quicker decisions. Build confidence and minimize disruptions across your business.</span></div>
      <div class="impact-line"><span>{SPEED_ICON}<strong>Cut financial risks</strong> and speed up approvals. Keep customers happy while ensuring uninterrupted operations.</span></div>
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
            logo_html = img_tag(LOGO_PATH, h=220)
        except Exception:
            pass

        with st.session_state.splash_ph.container():
            html_comp(_splash_html(logo_html), height=1600, scrolling=False)

            st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)

            col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
            with col3:
                if st.button("LAUNCH DAD", key="enter_app", use_container_width=True):
                    st.session_state.show_splash = False
                    st.session_state.splash_ph.empty()
                    st.rerun()

            # Tagline between button and footer
            st.markdown("""
            <div style="text-align:center; font-size:18px; color:#0b2a6f; font-weight:600; margin:30px auto 30px; padding:0 20px; font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,'Noto Sans'; font-style:italic;">
              "Just like Dad protects the home, DAD keeps fraud from going prone"
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="padding:10px 16px; color:#fff; background:#1e3c72; display:flex; align-items:center; justify-content:center; gap:10px; box-shadow:0 -2px 10px rgba(0,0,0,.22); font-weight:600; margin-top:30px; height:64px; font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,'Noto Sans';">
              <span>Where Innovation Meets Security</span>
              <span style="opacity:.6; padding:0 8px;">|</span>
              <span>Zero Tolerance for Fraud</span>
              <span style="opacity:.6; padding:0 8px;">|</span>
              <span>© Xforia DAD </span>
            </div>
            """, unsafe_allow_html=True)

        st.stop()