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
.main .block-container, .block-container, .stApp { padding:0 !important; margin:0 !important; max-width:100vw !important; width:100vw !important; background:#ffffff !important; }
body, html { margin:0; padding:0; width:100vw; overflow-x:hidden; background:#ffffff !important; }
.main, [data-testid="stAppViewContainer"], [data-testid="stApp"] { background:#ffffff !important; }
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

def _splash_html(logo_html: str, impact_image_html: str = "") -> str:
    return f"""
<style>
:root {{
  --bg:#ffffff; --text:#0f172a; --muted:#475569; --card:#f8fafc; --line:#e2e8f0;
  --brand:#1e3c72; --brand2:#2a5298; --brand3:#db123d;
  --section-gap: 28px;
  --gap-sm: 12px;
  main-section-gap: 80px;
}}
.container {{
  background:var(--bg);
  font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,'Noto Sans';
  color:var(--text);
  margin:0;
  padding:0 0 100px 0;
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
  max-width:1060px; margin:0 auto var(--section-gap); margin-bottom: 80px;
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
.metrics {{ max-width:1060px; margin:0 auto var(--section-gap); display:grid; grid-template-columns:repeat(3,minmax(220px,1fr)); gap:12px; margin-bottom: 80px;}}
.metric {{ background:var(--card); border:1px solid var(--line); border-radius:16px; padding:18px 18px; box-shadow:0 4px 12px rgba(15,23,42,0.05); transition:transform .2s, box-shadow .2s, border-color .2s; position:relative; overflow:hidden; margin:0; }}
.metric::before {{ content:''; position:absolute; top:0; left:0; right:0; height:4px; background:linear-gradient(90deg, var(--brand), var(--brand2)); opacity:0; transition:opacity .3s; }}
.metric:hover {{ transform:translateY(-4px); box-shadow:0 12px 32px rgba(15, 23, 42, 0.12); border-color:var(--brand); }}
.metric:hover::before {{ opacity:1; }}
.metric .title {{ font-size:19px; font-weight:900; letter-spacing:.01em; color:#1e3c72; margin-bottom:8px; text-align:center; line-height:1.2; white-space:nowrap; }}
.metric p {{ margin:0; line-height:1.5; color:var(--text); text-align:left; }}


/* BUSINESS IMPACTS - Left impacts, right image */
.impacts-section {{ margin:0 0 0 0; padding:0; }}
.impacts-section h2 {{ text-align:center; margin:0 0 20px 0; font-size:26px; font-weight:900; letter-spacing:.02em; color:var(--text); }}
.impacts-container {{ 
  display:grid; 
  grid-template-columns:1fr 400px; 
  gap:24px; 
  max-width:1100px; 
  margin:0 auto; 
  padding:0 16px;
  align-items:stretch;
}}
.impacts-list {{
  display:flex;
  flex-direction:column;
  gap:16px;
  justify-content:space-between;
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
.impact-image-card {{
  background:transparent;
  border-radius:16px;
  padding:0;
  box-shadow:0 4px 16px rgba(15, 23, 42, 0.08);
  border:none;
  display:flex;
  align-items:center;
  justify-content:center;
  height:100%;
}}
.impact-image-placeholder {{
  width:100%;
  height:100%;
  display:flex;
  align-items:center;
  justify-content:center;
  color:#1e3c72;
  font-size:18px;
  font-weight:700;
  text-align:center;
  flex-direction:column;
  gap:12px;
  background:linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  border-radius:16px;
  border:2px solid #e2e8f0;
}}
.impact-image-placeholder svg {{
  stroke:#1e3c72;
}}

@media (max-width:1100px) {{ 
  .impacts-container {{ grid-template-columns:1fr; }}
  .impact-image-card {{ position:relative; min-height:300px; }}
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
      <p>Automatically screen every document to ensure regulatory compliance and authenticity — vital for KYC, AML, CDD, and account integrity.</p>
    </div>
    <div class="card">
      <div class="top"><span class="word-with-first"><span class="first-letter">A</span>nomaly</span></div>
      <h3>Behavior-aware risk detection</h3>
      <p>Detect suspicious patterns to surface risks that indicate sophisticated fraud and potential compliance breaches.</p>
    </div>
    <div class="card">
      <div class="top"><span class="word-with-first"><span class="first-letter">D</span>etection</span></div>
      <h3>Real-time fraud scoring</h3>
      <p>Provide accurate, instant monitoring so threats are flagged before they cause damage.</p>
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
    <div class="impacts-container">
      <div class="impacts-list">
        <div class="impact-card">
          {LOSS_ICON}
          <div class="impact-content">
            <div class="impact-title">Sustain Financial Health</div>
            <p class="impact-desc">Make smarter decisions faster to protect savings and prevent fraud early.</p>
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
      <div class="impact-image-card">
        <div class="impact-image-placeholder">
          {impact_image_html if impact_image_html else '''
          <svg width="120" height="120" viewBox="0 0 24 24" fill="none" stroke-width="1.5">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
            <path d="M9 12l2 2 4-4"/>
          </svg>
          <div>Protected & Secure</div>
          '''}
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
        impact_image_html = ""
        try:
            logo_html = img_tag(LOGO_PATH, h=140)
            # Add your impact image here - example:
            impact_image_html = img_tag("flow.png", h=428,w=400,  style="border-radius:12px;")
        except Exception:
            pass

        with st.session_state.splash_ph.container():
            html_comp(_splash_html(logo_html, impact_image_html), height=1400, scrolling=False)

            st.markdown("<div class='after-splash'>", unsafe_allow_html=True)
            col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
            with col3:
                if st.button("LAUNCH DAD", key="enter_app", use_container_width=True):
                    st.session_state.show_splash = False
                    st.session_state.show_choice_page = True
                    st.session_state.splash_ph.empty()
                    st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown(
                "<div style='text-align:center; font-size:18px; color:#0b2a6f; font-weight:600; margin:24px auto 120px; padding:0 20px; font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,\"Noto Sans\"; font-style:italic; position:relative; background:#ffffff;'>"
                "\"Just like Dad protects the home, Xforia's DAD keeps fraud from going prone\""
                "</div>",
                unsafe_allow_html=True
            )


            # Footer with hover effect - Fixed at bottom
            # FAB Button and Footer
            st.markdown("""
            <style>
            /* FAB Button */
            .fab-button {
                position: fixed;
                right: 32px;
                bottom: 96px;
                width: 60px;
                height: 60px;
                background: #1e3c72;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 4px 16px rgba(30, 60, 114, 0.4);
                cursor: pointer;
                z-index: 10000;
                transition: all 0.3s ease;
            }
            .fab-button:hover {
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                box-shadow: 0 6px 24px rgba(30, 60, 114, 0.6);
                transform: scale(1.1) translateY(-2px);
            }
            .fab-button:active {
                transform: scale(1.05) translateY(0px);
            }
            .fab-button svg {
                width: 28px;
                height: 28px;
                stroke: white;
                stroke-width: 2;
                fill: none;
            }
            
            /* Footer */
            .splash-footer {
                position: fixed;
                left: 0;
                right: 0;
                bottom: 0;
                height: 64px;
                z-index: 9999;
                padding:10px 16px; 
                color:#fff; 
                background:#1e3c72; 
                display:flex; 
                align-items:center; 
                justify-content:center; 
                gap:18px; 
                box-shadow:0 -2px 10px rgba(0,0,0,.22); 
                font-weight:700; 
                font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,'Noto Sans';
                transition: all 0.3s ease;
                overflow: hidden;
            }
            .splash-footer::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
                transition: left 0.5s ease;
            }
            .splash-footer:hover {
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                box-shadow: 0 -4px 20px rgba(0,0,0,.3);
                transform: translateY(-2px);
            }
            .splash-footer:hover::before {
                left: 100%;
            }
            .footer-divider {
                opacity: .6;
            }
            </style>
            
            <!-- FAB Button -->
            <div class="fab-button" onclick="alert('Message feature coming soon!')">
                <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                </svg>
            </div>
            
            <!-- Footer -->
            <div class="splash-footer">
              <span>Where Innovation Meets Security</span>
              <span class="footer-divider">|</span>
              <span>Zero Tolerance for Fraud</span>
              <span class="footer-divider">|</span>
              <span>© Xforia DAD</span>
            </div>
            """, unsafe_allow_html=True)

        st.stop()