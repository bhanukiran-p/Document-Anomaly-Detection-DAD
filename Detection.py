# # Detection.py


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

# # ---------- Navigation functions ----------
# def go_dashboard():
#     candidates = [
#         "pages/Dashboard.py",
#         "pages/1_Dashboard.py",
#         "pages/2_Dashboard.py",
#         "pages/DASHBOARD.py",
#         "Dashboard",
#         "DASHBOARD",
#     ]
#     for target in candidates:
#         try:
#             st.switch_page(target)
#             return
#         except Exception:
#             continue
#     st.warning("Couldn't navigate to Dashboard.")

# def go_transaction_page():
#     candidates = [
#         "pages/Transaction_Analysis.py",
#         "pages/transaction_analysis.py",
#         "pages/Online_Transaction.py",
#         "pages/online_transaction.py",
#     ]
#     for target in candidates:
#         try:
#             st.switch_page(target)
#             return
#         except Exception:
#             continue
#     st.warning("Couldn't navigate to Transaction Analysis page. Please create pages/Transaction_Analysis.py")

# # ========= Styles =========
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

# :root{
#   --brand:#1e3c72; --brand2:#2a5298; --accent:#db123d;
#   --text:#0f172a; --muted:#475569; --line:#e2e8f0;
#   --bg:#f6f7fb; --card:#ffffff;
# }

# /* Base */
# *{font-family:'Inter',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;}
# .stApp{background:var(--bg);}

# /* Fixed Header */
# .app-header {
#   position: fixed;
#   top: 0;
#   left: 0;
#   right: 0;
#   height: 70px;
#   background: #ffffff;
#   border-bottom: 2px solid #e2e8f0;
#   z-index: 10000;
#   display: flex;
#   align-items: center;
#   justify-content: space-between;
#   padding: 0 32px;
#   box-shadow: 0 2px 8px rgba(15, 23, 42, 0.08);
# }

# .header-left {
#   display: flex;
#   align-items: center;
#   gap: 20px;
# }

# .header-logo {
#   height: 70px;
#   width: auto;
# }

# /* Hide default chrome */
# header[data-testid="stHeader"],
# section[aria-label="sidebar"],
# [data-testid="stSidebar"], [data-testid="stSidebarNav"],
# [data-testid="stSidebarContent"], [data-testid="stSidebarCollapseButton"],
# [data-testid="collapsedControl"], [data-testid="stToolbar"],
# [data-testid="stDock"], #MainMenu, footer {display:none !important;}

# /* Hamburger Menu */
# .hamburger-menu {
#   position: fixed;
#   top: 12px;
#   right: 32px;
#   z-index: 10001;
#   cursor: pointer;
#   display: flex;
#   flex-direction: column;
#   gap: 5px;
#   padding: 10px;
#   background: transparent;
#   border: none;
# }

# .hamburger-line {
#   width: 28px;
#   height: 3px;
#   background: #1e3c72;
#   border-radius: 3px;
#   transition: all 0.3s ease;
# }

# .hamburger-menu:hover .hamburger-line {
#   background: #db123d;
# }

# .menu-overlay {
#   position: fixed;
#   top: 0;
#   right: -100%;
#   width: 320px;
#   height: 100vh;
#   background: #ffffff;
#   box-shadow: -4px 0 20px rgba(15, 23, 42, 0.15);
#   z-index: 10002;
#   transition: right 0.3s ease;
#   padding: 80px 30px 30px;
#   overflow-y: auto;
# }

# .menu-overlay.active {
#   right: 0;
# }

# .menu-close {
#   position: absolute;
#   top: 20px;
#   right: 20px;
#   width: 32px;
#   height: 32px;
#   cursor: pointer;
#   background: transparent;
#   border: none;
#   font-size: 28px;
#   color: #475569;
#   line-height: 1;
#   transition: color 0.2s;
# }

# .menu-close:hover {
#   color: #db123d;
# }

# .menu-backdrop {
#   position: fixed;
#   top: 0;
#   left: 0;
#   right: 0;
#   bottom: 0;
#   background: rgba(15, 23, 42, 0.5);
#   z-index: 10001;
#   display: none;
#   opacity: 0;
#   transition: opacity 0.3s ease;
# }

# .menu-backdrop.active {
#   display: block;
#   opacity: 1;
# }

# .menu-title {
#   font-size: 1.5rem;
#   font-weight: 900;
#   color: #1e3c72;
#   margin: 0 0 24px 0;
#   letter-spacing: -0.02em;
# }

# .menu-item {
#   display: block;
#   padding: 16px 20px;
#   margin-bottom: 8px;
#   background: #f8fafc;
#   border: 2px solid #e2e8f0;
#   border-radius: 10px;
#   color: #0f172a;
#   text-decoration: none;
#   font-weight: 700;
#   font-size: 1rem;
#   transition: all 0.3s ease;
#   cursor: pointer;
#   border-left: 4px solid transparent;
# }

# .menu-item:hover {
#   background: #ffffff;
#   border-color: #1e3c72;
#   border-left-color: #db123d;
#   transform: translateX(8px);
#   box-shadow: 0 4px 12px rgba(15, 23, 42, 0.1);
# }

# /* Container + spacing */
# [data-testid="stAppViewContainer"]{padding-top:8px !important;}
# .main .block-container{max-width:1180px !important; padding-top:8px !important;}

# /* Title */
# .page-title{font-size:2rem; font-weight:800; color:var(--text); letter-spacing:-.02em; margin:0;}

# /* Section header */
# .section-title{font-size:1.35rem; font-weight:800; color:var(--text); margin:18px 0 12px 0;}

# /* Uploader */
# [data-testid="stFileUploader"]{
#   background:#f8fafc; border:2px dashed #d6dee8; border-radius:10px;
#   padding:22px; text-align:center;
# }
# [data-testid="stFileUploader"]:hover{border-color:#b9c5d3;}
# [data-testid="stFileUploader"] section{border:none !important;}
# [data-testid="stFileUploader"] label,
# [data-testid="stFileUploader"] small,
# [data-testid="stFileUploader"] [aria-live="polite"]{display:none !important;}

# /* Buttons */
# .stButton>button{
#   background:var(--accent) !important; color:#fff !important; border:none !important;
#   border-radius:10px !important; padding:12px 22px !important; font-weight:800 !important;
#   letter-spacing:.04em !important; box-shadow:none !important; transition:transform .15s ease, filter .15s ease !important;
#   width: 100% !important;
# }
# .stButton>button:hover{filter:brightness(.96) !important;}
# .stButton>button:active{transform:translateY(1px) !important;}

# /* Risk wrap */
# .risk-wrap {
#   display: flex;
#   flex-direction: column;
#   align-items: center;
#   gap: 6px;
#   padding: 16px;
#   border-radius: 14px;
#   position: relative;
#   overflow: hidden;
#   margin-bottom: 16px;
# }

# .risk-wrap-low {
#   background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
#   border: 2px solid #059669;
# }

# .risk-wrap-medium {
#   background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
#   border: 2px solid #f59e0b;
# }

# .risk-wrap-high {
#   background: linear-gradient(135deg, #fef2f2 0%, #fecaca 100%);
#   border: 2px solid #db123d;
# }

# .risk-badge {
#   font-weight: 900;
#   letter-spacing: .06em;
#   padding: 6px 14px;
#   border-radius: 999px;
#   color: #fff;
# }

# .badge-low {background: #059669;}
# .badge-medium {background: #f59e0b;}
# .badge-high {background: #db123d;}

# .risk-score {
#   font-size: 3.2rem;
#   font-weight: 900;
#   line-height: 1;
# }
            
# .login-btn {
#   display: flex;
#   align-items: center;
#   gap: 8px;
#   padding: 8px 16px;
#   background-color: #1e3c72;
#   border: 1px solid #ddd;
#   border-radius: 6px;
#   cursor: pointer;
#   font-size: 14px;
#   color: #ffffff;
#   transition: all 0.3s ease;
#   margin-right: 50px;
# }

# .login-btn:hover {
#   background-color: #344F80;
#   border-color: #999;
# }

# .login-icon {
#   width: 20px;
#   height: 20px;
# }

# .header-right {
#   display: flex;
#   align-items: center;
# }

# .score-low {color: #059669;}
# .score-medium {color: #f59e0b;}
# .score-high {color: #db123d;}

# .risk-label {
#   font-size: .8rem;
#   font-weight: 700;
#   color: var(--muted);
#   text-transform: uppercase;
# }
            
# /* Info grid */
# .grid{display:grid; grid-template-columns:repeat(2,1fr); gap:10px; margin-top:10px;}
# .item{background:#fbfdff; border-left:3px solid var(--brand); border-radius:8px; padding:10px; margin-bottom: 8px;}
# .item:hover {
#   transform:translateY(-2px) scale(1.01);
#   box-shadow:0 12px 32px rgba(15, 23, 42, 0.15);
#   border-color:var(--brand);
# }
# .lbl{font-size:.75rem; font-weight:700; color:var(--muted); text-transform:uppercase; letter-spacing:.04em;}
# .val{font-size:.95rem; font-weight:600; color:var(--text);}

# /* Factors */
# .factor{display:flex; gap:8px; align-items:center; background:#fdfdfd; border-left:3px solid var(--brand2); border-radius:8px; padding:10px; margin-bottom:6px;}
# .dot{width:22px; height:22px; border-radius:999px; display:flex; align-items:center; justify-content:center; font-weight:900; background:#fff0cc; color:#b25c00;}

# /* Recommendations */
# .rec{border-radius:12px; padding:12px; border:1px solid var(--line); margin-top:12px;}
# .rec-low{background:#eafaf2; border-color:#059669;} 
# .rec-medium{background:#fff4db; border-color:#f59e0b;}
# .rec-high{background:#ffe9ee; border-color:#db123d;}
# .rec h4{margin:0 0 6px 0; font-weight:900;}

# /* Fixed footer */
# .custom-footer{
#   position:fixed; left:0; right:0; bottom:0; height:64px; z-index:9999;
#   background:#1e3c72; color:#fff; display:flex; justify-content:center; align-items:center; gap:18px;
#   font-weight:700;
# }
# .footer-divider{opacity:.6;}

# @media (max-width:768px){
#   .grid{grid-template-columns:1fr;}
#   .risk-score{font-size:2.1rem;}
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------- SVG icons ----------
# def icon_info():
#     return """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
#     <circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>"""

# def icon_alert():
#     return """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
#     <path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>"""

# def icon_check():
#     return """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
#     <polyline points="20 6 9 17 4 12"/></svg>"""

# def add_header():
#     import pathlib
#     cwd = pathlib.Path(os.getcwd())
#     here = pathlib.Path(__file__).parent if "__file__" in globals() else cwd
#     candidates = [cwd/"FDN.png", here/"FDN.png", here/"assets"/"FDN.png", cwd/"assets"/"FDN.png"]
#     logo_path = next((p for p in candidates if p.exists()), None)
    
#     logo_html = ""
#     if logo_path:
#         encoded = base64.b64encode(logo_path.read_bytes()).decode()
#         logo_html = f'<img src="data:image/png;base64,{encoded}" alt="Logo" class="header-logo"/>'
    
#     # Header with hamburger
#     st.markdown(f"""
#     <div class="app-header">
#         <div class="header-left">
#             <a href="/" target="_self">
#             {logo_html}
#             </a>
#         </div>
#         <div class="header-right">
#             <button class="login-btn" id="loginBtn">
#                 <svg class="login-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
#                     <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path>
#                     <polyline points="10 17 15 12 10 7"></polyline>
#                     <line x1="15" y1="12" x2="3" y2="12"></line>
#                 </svg>
#                 <span>Login</span>
#             </button>
#             <div class="hamburger-menu" id="hamburgerBtn">
#                 <div class="hamburger-line"></div>
#                 <div class="hamburger-line"></div>
#                 <div class="hamburger-line"></div>
#             </div>
#         </div>
#     </div>
    
#     <div class="menu-backdrop" id="menuBackdrop"></div>
#     <div class="menu-overlay" id="menuOverlay">
#       <button class="menu-close" id="closeBtn">×</button>
#       <h2 class="menu-title">DAD Solutions</h2>
#       <div class="menu-item" data-name="manufacturing">
#         <div style="font-size: 1.1rem; font-weight: 800; margin-bottom: 4px;">DAD for Manufacturing</div>
#         <div style="font-size: 0.85rem; color: #64748b; font-weight: 500;">Quality control & defect detection</div>
#       </div>
#       <div class="menu-item" data-name="education">
#         <div style="font-size: 1.1rem; font-weight: 800; margin-bottom: 4px;">DAD for Education</div>
#         <div style="font-size: 0.85rem; color: #64748b; font-weight: 500;">Academic integrity & assessment</div>
#       </div>
#       <div class="menu-item" data-name="healthcare">
#         <div style="font-size: 1.1rem; font-weight: 800; margin-bottom: 4px;">DAD for Healthcare</div>
#         <div style="font-size: 0.85rem; color: #64748b; font-weight: 500;">Medical records & compliance</div>
#       </div>
#     </div>
    
#     <script>
#       setTimeout(function() {{
#         const hamburger = document.getElementById('hamburgerBtn');
#         const overlay = document.getElementById('menuOverlay');
#         const backdrop = document.getElementById('menuBackdrop');
#         const closeBtn = document.getElementById('closeBtn');
        
#         function openMenu() {{
#           if (overlay && backdrop) {{
#             overlay.classList.add('active');
#             backdrop.classList.add('active');
#           }}
#         }}
        
#         function closeMenu() {{
#           if (overlay && backdrop) {{
#             overlay.classList.remove('active');
#             backdrop.classList.remove('active');
#           }}
#         }}
        
#         if (hamburger) {{
#           hamburger.addEventListener('click', function(e) {{
#             e.preventDefault();
#             e.stopPropagation();
#             openMenu();
#           }});
#         }}
        
#         if (closeBtn) {{
#           closeBtn.addEventListener('click', closeMenu);
#         }}
        
#         if (backdrop) {{
#           backdrop.addEventListener('click', closeMenu);
#         }}
        
#         const menuItems = document.querySelectorAll('.menu-item');
#         menuItems.forEach(item => {{
#           item.addEventListener('click', function() {{
#             const name = this.getAttribute('data-name');
#             alert('DAD for ' + name.charAt(0).toUpperCase() + name.slice(1) + ' - Coming Soon!');
#           }});
#         }});
#       }}, 200);
#     </script>
#     """, unsafe_allow_html=True)

# add_header()

# # ---------- Landing and Splash screens ----------
# # Initialize session states
# if "show_landing" not in st.session_state:
#     st.session_state.show_landing = True
# if "show_splash" not in st.session_state:
#     st.session_state.show_splash = False

# # Landing page (shows first)
# if st.session_state.get("show_landing", True):
#     import pathlib
#     cwd = pathlib.Path(os.getcwd())
#     here = pathlib.Path(__file__).parent if "__file__" in globals() else cwd
#     candidates = [cwd/"FD.png", here/"FD.png", here/"assets"/"FD.png", cwd/"assets"/"FD.png"]
#     logo_path = next((p for p in candidates if p.exists()), None)
    
#     logo_html = ""
#     if logo_path:
#         encoded = base64.b64encode(logo_path.read_bytes()).decode()
#         logo_html = f'<img src="data:image/png;base64,{encoded}" alt="Logo" style="max-width:400px;width:100%;height:auto; padding-bottom:40px; padding-right:50px;"/>'
    
#     st.markdown("""
#         <style>
#         .stApp {
#             background: #ffffff !important;
#         }
#         /* Responsive column layout */
#         @media (max-width: 1200px) {
#             .card-title {
#                 font-size: 1.2rem !important;
#             }
#             .card-description {
#                 font-size: 0.85rem !important;
#             }
#             .card-icon {
#                 width: 70px !important;
#                 height: 70px !important;
#             }
#         }
#         @media (max-width: 900px) {
#             .landing-card {
#                 min-height: 280px !important;
#             }
#             .card-icon {
#                 width: 60px !important;
#                 height: 60px !important;
#             }
#         }
#         .landing-card {
#             background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
#             border: 2px solid #e2e8f0;
#             border-radius: 16px;
#             padding: 32px 24px;
#             text-align: center;
#             transition: all 0.3s ease;
#             min-height: 320px;
#             display: flex;
#             flex-direction: column;
#             align-items: center;
#             justify-content: flex-start;
#             gap: 16px;
#             margin-bottom:18px;
#         }
#         .landing-card:hover {
#             transform: translateY(-8px);
#             box-shadow: 0 12px 32px rgba(30, 60, 114, 0.15);
#             border-color: #1e3c72;
#         }
#         .card-icon {
#             width: 80px;
#             height: 80px;
#             background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
#             border-radius: 50%;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             margin-bottom: 8px;
#         }
#         .card-title {
#             font-size: 1.4rem;
#             font-weight: 800;
#             color: #1e3c72;
#             margin: 0;
#             letter-spacing: -0.02em;
#         }
#         .card-description {
#             font-size: 0.95rem;
#             color: #475569;
#             font-weight: 500;
#             line-height: 1.5;
#             margin: 0;
#             min-height: 60px;
#             display: flex;
#             align-items: center;
#         }
#         .disabled-button {
#             background: #7a9cc6 !important; /* Lighter, desaturated blue */
#             color: #e8f0f8 !important; /* Very light blue-tinted text */
#             border: none !important;
#             border-radius: 10px !important;
#             padding: 12px 22px !important;
#             font-weight: 800 !important;
#             letter-spacing: 0.04em !important;
#             width: 100%;
#             text-align: center;
#             cursor: not-allowed;
#             opacity: 0.65 !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)
    
#     st.markdown(f"""
#         <div style='display:flex;flex-direction:column;align-items:center;justify-content:center;padding:40px 20px 20px 20px;'>
#             {logo_html}
#             <h1 style='font-size:clamp(1.8rem, 4vw, 2.5rem);font-weight:900;color:#1e3c72;text-align:center;letter-spacing:-0.02em;'>Choose Your DAD Solution</h1>
#             <p style='font-size:clamp(0.95rem, 2vw, 1.1rem);color:#475569;font-weight:500;margin:0 0 60px 0;text-align:center;padding-right:30px;'>Powered by Advanced AI Detection Technology</p>
#         </div>
#     """, unsafe_allow_html=True)

#     # Responsive column layout based on screen size
#     col1, col2, col3, col4 = st.columns(4, gap="medium")

#     with col1:
#         st.markdown("""
#             <div class='landing-card'>
#                 <div class='card-icon'>
#                     <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2">
#                         <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
#                         <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
#                     </svg>
#                 </div>
#                 <h3 class='card-title'>Education</h3>
#                 <p class='card-description'>Ensure academic integrity and verify educational documents and assessments</p>
#             </div>
#         """, unsafe_allow_html=True)
#         st.markdown("<div class='disabled-button'>COMING SOON</div>", unsafe_allow_html=True)

#     with col2:
#         st.markdown("""
#             <div class='landing-card'>
#                 <div class='card-icon'>
#                     <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2">
#                         <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
#                         <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
#                     </svg>
#                 </div>
#                 <h3 class='card-title'>Finance</h3>
#                 <p class='card-description'>Detect fraud in financial documents, checks, and transactions with real-time analysis</p>
#             </div>
#         """, unsafe_allow_html=True)
#         if st.button("ENTER FINANCE", type="primary", use_container_width=True, key="enter_btn"):
#             st.session_state.show_landing = False
#             st.session_state.show_splash = True
#             st.rerun()
    
#     with col3:
#         st.markdown("""
#             <div class='landing-card'>
#                 <div class='card-icon'>
#                     <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2">
#                         <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
#                     </svg>
#                 </div>
#                 <h3 class='card-title'>Healthcare</h3>
#                 <p class='card-description'>Verify medical records and ensure compliance with healthcare regulations</p>
#             </div>
#         """, unsafe_allow_html=True)
#         st.markdown("<div class='disabled-button'>COMING SOON</div>", unsafe_allow_html=True)

#     with col4:
#         st.markdown("""
#             <div class='landing-card'>
#                 <div class='card-icon'>
#                     <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2">
#                         <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
#                         <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
#                     </svg>
#                 </div>
#                 <h3 class='card-title'>Federal Services</h3>
#                 <p class='card-description'>Secure government document verification and identity authentication for federal agencies</p>
#             </div>
#         """, unsafe_allow_html=True)
#         st.markdown("<div class='disabled-button'>COMING SOON</div>", unsafe_allow_html=True)

#     st.stop()

# # Splash screen (shows after landing)
# if st.session_state.get("show_splash", False):
#     try:
#         from splash_screen import show_splash
#         show_splash()
#         st.stop()
#     except ImportError:
#         # Fallback to simple splash if splash_screen.py doesn't exist
#         st.markdown("""
#             <div style='display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;margin-top:80px;'>
#                 <h1 style='margin:0;font-size:3rem;font-weight:900;color:#1e3c72;'>Welcome to Fraud Detection</h1>
#                 <p style='opacity:.7;margin:0;font-size:1.2rem;font-weight:500;'>Your Guardian Against Fraud</p>
#             </div>
#         """, unsafe_allow_html=True)
        
#         col1, col2, col3 = st.columns([1, 1, 1])
#         with col2:
#             if st.button("Get Started", type="primary", use_container_width=True):
#                 st.session_state.show_splash = False
#                 st.rerun()
#         st.stop()


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
#             try: os.unlink(path)
#             except Exception: pass

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

# # ===================== PAGE HEADER WITH NAVIGATION BUTTONS =====================
# col_title, col_btn1 = st.columns([4, 1])
# with col_title:
#     st.markdown("<h1 class='page-title'>Document Anomaly For Finance</h1>", unsafe_allow_html=True)
# with col_btn1:
#     if st.button("Real-time Transaction", key="transaction_btn", type="secondary", use_container_width=True):
#         go_transaction_page()

# # ===================== CHECK ANALYSIS (MAIN PAGE) =====================
# st.markdown("<h2 class='section-title'>Enhanced Check Analysis with AI</h2>", unsafe_allow_html=True)

# c1, c2 = st.columns([2,3], gap="large")

# with c1:
#     st.markdown("#### Upload Check Image")
#     uploaded_file = st.file_uploader("Drop your check image here", type=['jpg','jpeg','png'], label_visibility="collapsed", key="check_uploader")
    
#     if uploaded_file:
#         try:
#             uploaded_file.seek(0)
#             img = Image.open(uploaded_file)
#             st.image(img, use_container_width=True)
            
#             st.markdown("<br>", unsafe_allow_html=True)
#             if st.button("Analyze Check", type="primary", key="analyze_check_btn", use_container_width=True):
#                 with st.spinner("Analyzing your check..."):
#                     uploaded_file.seek(0)
#                     extracted, combined, raw, ml_s, rule_s, ml_ens = mindee_ocr_analysis_with_ml(uploaded_file)
                
#                 if extracted and combined is not None:
#                     st.success("Check processed successfully!")
#                     st.session_state.check_results = {
#                         'extracted_data': extracted,
#                         'fraud_score': combined,
#                         'ml_score': ml_s,
#                         'rule_score': rule_s,
#                         'raw_data': raw,
#                         'ml_ensemble': ml_ens
#                     }
#                     st.rerun()
#                 else:
#                     st.error("Unable to process the check. Please try again.")
#         except Exception as e:
#             st.error(f"Error: {e}")
    

# with c2:
#     if 'check_results' in st.session_state:
#         res = st.session_state.check_results
#         fs = float(res['fraud_score'])
#         ml_score = float(res.get('ml_score', 0))
#         rule_score = float(res.get('rule_score', 0))
#         level, risk_class = get_risk_level(fs)

#         # RESULTS AT TOP
#         st.markdown(f"""
#             <div class="risk-wrap risk-wrap-{risk_class}">
#                 <div class="risk-badge badge-{risk_class}">{level}</div>
#                 <div class="risk-score score-{risk_class}">{fs*100:.0f}%</div>
#                 <div class="risk-label">Fraud Risk Score</div>
#             </div>
#         """, unsafe_allow_html=True)
        
#         # Risk Factors
#         factors = get_check_risk_factors(res.get('raw_data', {}), ml_score, rule_score)
#         st.markdown(f"<h4 style='display:flex;align-items:center;gap:8px;margin:0 0 8px 0;'>{icon_alert()} Risk Factors</h4>", unsafe_allow_html=True)
#         for fct in factors:
#             st.markdown(f"<div class='factor'><div class='dot'>!</div><span>{fct}</span></div>", unsafe_allow_html=True)
        
#         # Recommendations
#         if fs >= 0.7:
#             st.markdown(f"<div class='rec rec-high'><h4>{icon_check()} Recommendations</h4><div>High fraud risk detected — manual verification & additional auth recommended.</div></div>", unsafe_allow_html=True)
#         elif fs >= 0.4:
#             st.markdown(f"<div class='rec rec-medium'><h4>{icon_check()} Recommendations</h4><div>Medium risk — perform extra verification before processing.</div></div>", unsafe_allow_html=True)
#         else:
#             st.markdown(f"<div class='rec rec-low'><h4>{icon_check()} Recommendations</h4><div>Low risk — transaction appears legitimate.</div></div>", unsafe_allow_html=True)

#         # EXTRACTED INFORMATION AT BOTTOM
#         st.markdown(f"<h4 style='display:flex;align-items:center;gap:8px;margin:20px 0 0 0;'>{icon_info()} Extracted Information</h4>", unsafe_allow_html=True)
#         st.markdown("<div class='grid'>", unsafe_allow_html=True)
#         for k, v in res['extracted_data'].items():
#             st.markdown(f"<div class='item'><div class='lbl'>{k}</div><div class='val'>{v}</div></div>", unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)
#     else:
#         st.info("Upload a check image on the left to begin analysis")
#         st.markdown("""
#             <div style='margin-top:20px; padding:20px; background:#f8fafc; border-radius:12px; border:1px solid #e2e8f0;'>
#                 <h4 style='margin:0 0 12px 0; color:#1e3c72;'>How it works:</h4>
#                 <ol style='margin:0; padding-left:20px; color:#475569;'>
#                     <li style='margin-bottom:8px;'>Upload a check image (JPG, JPEG, or PNG)</li>
#                     <li style='margin-bottom:8px;'>Click "Analyze Check" to process</li>
#                     <li style='margin-bottom:8px;'>View fraud risk score and detailed analysis</li>
#                     <li>Review recommendations and extracted check data</li>
#                 </ol>
#             </div>
#         """, unsafe_allow_html=True)

# # ===== Fixed footer =====
# st.markdown("""
# <div class="custom-footer">
#   <span>Where Innovation Meets Security</span>
#   <span class="footer-divider">|</span>
#   <span>Zero Tolerance for Fraud</span>
#   <span class="footer-divider">|</span>
#   <span>© Xforia DAD</span>
# </div>
# """, unsafe_allow_html=True)



































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

st.set_page_config(page_title="Xforia DAD - Fraud Detection", layout="wide", initial_sidebar_state="collapsed")

def go_dashboard():
    candidates = ["pages/Dashboard.py", "pages/1_Dashboard.py", "pages/2_Dashboard.py", "pages/DASHBOARD.py", "Dashboard", "DASHBOARD"]
    for target in candidates:
        try:
            st.switch_page(target)
            return
        except Exception:
            continue
    st.warning("Couldn't navigate to Dashboard.")

def go_transaction_page():
    candidates = ["pages/Transaction_Analysis.py", "pages/transaction_analysis.py", "pages/Online_Transaction.py", "pages/online_transaction.py"]
    for target in candidates:
        try:
            st.switch_page(target)
            return
        except Exception:
            continue
    st.warning("Couldn't navigate to Transaction Analysis page. Please create pages/Transaction_Analysis.py")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
:root{--brand:#1e3c72; --brand2:#2a5298; --accent:#db123d; --text:#0f172a; --muted:#475569; --line:#e2e8f0; --bg:#f6f7fb; --card:#ffffff;}
*{font-family:'Inter',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;}
.stApp{background:var(--bg);}
.app-header {position: fixed; top: 0; left: 0; right: 0; height: 70px; background: #ffffff; border-bottom: 2px solid #e2e8f0; z-index: 10000; display: flex; align-items: center; justify-content: space-between; padding: 0 32px; box-shadow: 0 2px 8px rgba(15, 23, 42, 0.08);}
.header-left {display: flex; align-items: center; gap: 20px;}
.header-logo {height: 70px; width: auto;}
header[data-testid="stHeader"], section[aria-label="sidebar"], [data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="stSidebarContent"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"], [data-testid="stToolbar"], [data-testid="stDock"], #MainMenu, footer {display:none !important;}
[data-testid="stAppViewContainer"]{padding-top:8px !important;}
.main .block-container{max-width:1180px !important; padding-top:8px !important;}
.page-title{font-size:2rem; font-weight:800; color:var(--text); letter-spacing:-.02em; margin:0;}
.section-title{font-size:1.35rem; font-weight:800; color:var(--text); margin:18px 0 12px 0;}
[data-testid="stFileUploader"]{background:#f8fafc; border:2px dashed #d6dee8; border-radius:10px; padding:22px; text-align:center;}
[data-testid="stFileUploader"]:hover{border-color:#b9c5d3;}
[data-testid="stFileUploader"] section{border:none !important;}
[data-testid="stFileUploader"] label, [data-testid="stFileUploader"] small, [data-testid="stFileUploader"] [aria-live="polite"]{display:none !important;}
.stButton>button{background:var(--accent) !important; color:#fff !important; border:none !important; border-radius:10px !important; padding:12px 22px !important; font-weight:800 !important; letter-spacing:.04em !important; box-shadow:none !important; transition:transform .15s ease, filter .15s ease !important; width: 100% !important;}
.stButton>button:hover{filter:brightness(.96) !important;}
.stButton>button:active{transform:translateY(1px) !important;}
.risk-wrap {display: flex; flex-direction: column; align-items: center; gap: 6px; padding: 16px; border-radius: 14px; position: relative; overflow: hidden; margin-bottom: 16px;}
.risk-wrap-low {background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%); border: 2px solid #059669;}
.risk-wrap-medium {background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%); border: 2px solid #f59e0b;}
.risk-wrap-high {background: linear-gradient(135deg, #fef2f2 0%, #fecaca 100%); border: 2px solid #db123d;}
.risk-badge {font-weight: 900; letter-spacing: .06em; padding: 6px 14px; border-radius: 999px; color: #fff;}
.badge-low {background: #059669;} .badge-medium {background: #f59e0b;} .badge-high {background: #db123d;}
.risk-score {font-size: 3.2rem; font-weight: 900; line-height: 1;}
.login-btn {display: flex; align-items: center; gap: 8px; padding: 8px 16px; background-color: #1e3c72; border: 1px solid #ddd; border-radius: 6px; cursor: pointer; font-size: 14px; color: #ffffff; transition: all 0.3s ease;}
.login-btn:hover {background-color: #344F80; border-color: #999;}
.login-icon {width: 20px; height: 20px;}
.header-right {display: flex; align-items: center; margin-right: 0;}
.score-low {color: #059669;} .score-medium {color: #f59e0b;} .score-high {color: #db123d;}
.risk-label {font-size: .8rem; font-weight: 700; color: var(--muted); text-transform: uppercase;}
.grid{display:grid; grid-template-columns:repeat(2,1fr); gap:10px; margin-top:10px;}
.item{background:#fbfdff; border-left:3px solid var(--brand); border-radius:8px; padding:10px; margin-bottom: 8px;}
.item:hover {transform:translateY(-2px) scale(1.01); box-shadow:0 12px 32px rgba(15, 23, 42, 0.15); border-color:var(--brand);}
.lbl{font-size:.75rem; font-weight:700; color:var(--muted); text-transform:uppercase; letter-spacing:.04em;}
.val{font-size:.95rem; font-weight:600; color:var(--text);}
.factor{display:flex; gap:8px; align-items:center; background:#fdfdfd; border-left:3px solid var(--brand2); border-radius:8px; padding:10px; margin-bottom:6px;}
.dot{width:22px; height:22px; border-radius:999px; display:flex; align-items:center; justify-content:center; font-weight:900; background:#fff0cc; color:#b25c00;}
.rec{border-radius:12px; padding:12px; border:1px solid var(--line); margin-top:12px;}
.rec-low{background:#eafaf2; border-color:#059669;} .rec-medium{background:#fff4db; border-color:#f59e0b;} .rec-high{background:#ffe9ee; border-color:#db123d;}
.rec h4{margin:0 0 6px 0; font-weight:900;}
.custom-footer{position:fixed; left:0; right:0; bottom:0; height:64px; z-index:9999; background:#1e3c72; color:#fff; display:flex; justify-content:center; align-items:center; gap:18px; font-weight:700;}
.footer-divider{opacity:.6;}
@media (max-width:768px){.grid{grid-template-columns:1fr;} .risk-score{font-size:2.1rem;}}
</style>
""", unsafe_allow_html=True)

def icon_info():
    return """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>"""

def icon_alert():
    return """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>"""

def icon_check():
    return """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>"""

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
            <a href="/" target="_self">{logo_html}</a>
        </div>
        <div class="header-right">
            <button class="login-btn" id="loginBtn">
                <svg class="login-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path>
                    <polyline points="10 17 15 12 10 7"></polyline>
                    <line x1="15" y1="12" x2="3" y2="12"></line>
                </svg>
                <span>Login</span>
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

add_header()

if "show_landing" not in st.session_state:
    st.session_state.show_landing = True
if "show_splash" not in st.session_state:
    st.session_state.show_splash = False
if "show_choice_page" not in st.session_state:
    st.session_state.show_choice_page = False

if st.session_state.get("show_landing", True):
    import pathlib
    cwd = pathlib.Path(os.getcwd())
    here = pathlib.Path(__file__).parent if "__file__" in globals() else cwd
    candidates = [cwd/"FD.png", here/"FD.png", here/"assets"/"FD.png", cwd/"assets"/"FD.png"]
    logo_path = next((p for p in candidates if p.exists()), None)
    
    logo_html = ""
    if logo_path:
        encoded = base64.b64encode(logo_path.read_bytes()).decode()
        logo_html = f'<img src="data:image/png;base64,{encoded}" alt="Logo" style="max-width:400px;width:100%;height:auto; padding-bottom:40px; padding-right:50px;"/>'
    
    st.markdown("""
        <style>
        .stApp {background: #ffffff !important;}
        @media (max-width: 1200px) {.card-title {font-size: 1.2rem !important;} .card-description {font-size: 0.85rem !important;} .card-icon {width: 70px !important; height: 70px !important;}}
        @media (max-width: 900px) {.landing-card {min-height: 280px !important;} .card-icon {width: 60px !important; height: 60px !important;}}
        .landing-card {background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%); border: 2px solid #e2e8f0; border-radius: 16px; padding: 32px 24px; text-align: center; transition: all 0.3s ease; min-height: 320px; display: flex; flex-direction: column; align-items: center; justify-content: flex-start; gap: 16px; margin-bottom:18px;}
        .landing-card:hover {transform: translateY(-8px); box-shadow: 0 12px 32px rgba(30, 60, 114, 0.15); border-color: #1e3c72;}
        .card-icon {width: 80px; height: 80px; background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 8px;}
        .card-title {font-size: 1.4rem; font-weight: 800; color: #1e3c72; margin: 0; letter-spacing: -0.02em;}
        .card-description {font-size: 0.95rem; color: #475569; font-weight: 500; line-height: 1.5; margin: 0; min-height: 60px; display: flex; align-items: center;}
        .disabled-button {background: #7a9cc6 !important; color: #e8f0f8 !important; border: none !important; border-radius: 10px !important; padding: 12px 22px !important; font-weight: 800 !important; letter-spacing: 0.04em !important; width: 100%; text-align: center; cursor: not-allowed; opacity: 0.65 !important;}
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style='display:flex;flex-direction:column;align-items:center;justify-content:center;padding:40px 20px 20px 20px;'>
            {logo_html}
            <h1 style='font-size:clamp(1.8rem, 4vw, 2.5rem);font-weight:900;color:#1e3c72;text-align:center;letter-spacing:-0.02em;'>Choose Your DAD Solution</h1>
            <p style='font-size:clamp(0.95rem, 2vw, 1.1rem);color:#475569;font-weight:500;margin:0 0 60px 0;text-align:center;padding-right:30px;'>Powered by Advanced AI Detection Technology</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4, gap="medium")

    with col1:
        st.markdown("""
            <div class='landing-card'>
                <div class='card-icon'><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg></div>
                <h3 class='card-title'>Education</h3>
                <p class='card-description'>Ensure academic integrity and verify educational documents and assessments</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<div class='disabled-button'>COMING SOON</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class='landing-card'>
                <div class='card-icon'><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg></div>
                <h3 class='card-title'>Finance</h3>
                <p class='card-description'>Detect fraud in financial documents, checks, and transactions with real-time analysis</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ENTER FINANCE", type="primary", use_container_width=True, key="enter_btn"):
            st.session_state.show_landing = False
            st.session_state.show_splash = True
            st.rerun()
    
    with col3:
        st.markdown("""
            <div class='landing-card'>
                <div class='card-icon'><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></div>
                <h3 class='card-title'>Healthcare</h3>
                <p class='card-description'>Verify medical records and ensure compliance with healthcare regulations</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<div class='disabled-button'>COMING SOON</div>", unsafe_allow_html=True)

    with col4:
        st.markdown("""
            <div class='landing-card'>
                <div class='card-icon'><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg></div>
                <h3 class='card-title'>Federal Services</h3>
                <p class='card-description'>Secure government document verification and identity authentication for federal agencies</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<div class='disabled-button'>COMING SOON</div>", unsafe_allow_html=True)

    st.stop()

if st.session_state.get("show_splash", False):
    try:
        from splash_screen import show_splash
        show_splash()
        st.stop()
    except ImportError:
        st.markdown("""
            <div style='display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;margin-top:80px;'>
                <h1 style='margin:0;font-size:3rem;font-weight:900;color:#1e3c72;'>Welcome to Fraud Detection</h1>
                <p style='opacity:.7;margin:0;font-size:1.2rem;font-weight:500;'>Your Guardian Against Fraud</p>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Get Started", type="primary", use_container_width=True):
                st.session_state.show_splash = False
                st.rerun()
        st.stop()

# Choice Page - 2-button selection between Real Time and On Demand
if st.session_state.get("show_choice_page", False):
    import pathlib
    cwd = pathlib.Path(os.getcwd())
    here = pathlib.Path(__file__).parent if "__file__" in globals() else cwd
    candidates = [cwd/"DAD_red_black.png", here/"DAD_red_black.png", here/"assets"/"DAD_red_black.png", cwd/"assets"/"DAD_red_black.png"]
    logo_path = next((p for p in candidates if p.exists()), None)
    
    logo_html = ""
    if logo_path:
        encoded = base64.b64encode(logo_path.read_bytes()).decode()
        logo_html = f'<img src="data:image/png;base64,{encoded}" alt="Logo" style="max-width:300px;width:100%;height:auto; margin-bottom:20px;"/>'
    
    st.markdown("""
        <style>
        .stApp {background: #ffffff !important;}
        .choice-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 60px 20px 20px 20px;
            min-height: 70vh;
        }
        .choice-cards {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 40px;
            max-width: 900px;
            width: 100%;
            margin-top: 40px;
        }
        .choice-card {
            background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
            border: 2px solid #e2e8f0;
            border-radius: 20px;
            padding: 40px 32px;
            text-align: center;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }
        .choice-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #1e3c72, #2a5298);
            opacity: 0;
            transition: opacity 0.3s;
        }
        .choice-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 32px rgba(30, 60, 114, 0.15);
            border-color: #1e3c72;
        }
        .choice-card:hover::before {
            opacity: 1;
        }
        .choice-icon {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
        }
        .choice-title {
            font-size: 1.5rem;
            font-weight: 800;
            color: #1e3c72;
            margin: 0 0 12px 0;
            letter-spacing: -0.02em;
        }
        .choice-description {
            font-size: 1rem;
            color: #475569;
            font-weight: 500;
            line-height: 1.6;
            margin: 0;
        }
        .choice-button {
            width: 100%;
            margin-top: 20px;
            padding: 14px 24px;
            background: #db123d;
            color: #ffffff;
            border: none;
            border-radius: 10px;
            font-weight: 800;
            font-size: 1rem;
            letter-spacing: 0.04em;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .choice-button:hover {
            filter: brightness(0.95);
            transform: translateY(-2px);
        }
        @media (max-width: 900px) {
            .choice-cards { grid-template-columns: 1fr; gap: 20px; }
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class='choice-container'>
            {logo_html}
            <h1 style='font-size:clamp(2rem, 4vw, 2.5rem);font-weight:900;color:#1e3c72;text-align:center;letter-spacing:-0.02em;margin-bottom:10px;'>Choose Transaction Type</h1>
            <p style='font-size:clamp(0.95rem, 2vw, 1.1rem);color:#475569;font-weight:500;margin:0 0 40px 0;text-align:center;'>Select your preferred fraud detection method</p>
            <div class='choice-cards'>
                <div class='choice-card'>
                    <div class='choice-icon'>
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2">
                            <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline>
                            <polyline points="17 6 23 6 23 12"></polyline>
                        </svg>
                    </div>
                    <h3 class='choice-title'>Real Time Transaction</h3>
                    <p class='choice-description'>Analyze online transactions instantly with real-time fraud detection and instant scoring</p>
                </div>
                <div class='choice-card'>
                    <div class='choice-icon'>
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                            <line x1="16" y1="13" x2="8" y2="13"></line>
                            <line x1="16" y1="17" x2="8" y2="17"></line>
                            <polyline points="10 9 9 9 8 9"></polyline>
                        </svg>
                    </div>
                    <h3 class='choice-title'>On Demand Transactions</h3>
                    <p class='choice-description'>Upload and analyze check images with OCR extraction and comprehensive fraud assessment</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Buttons positioned under their respective cards
    col1, col2, col3, col4 = st.columns(4, gap="large")
    with col2:
        if st.button("Real Time Transaction", type="primary", use_container_width=True, key="realtime_btn"):
            st.switch_page("pages/Transaction_Analysis.py")
    
    with col3:
        if st.button("On Demand Transactions", type="primary", use_container_width=True, key="ondemand_btn"):
            st.session_state.show_choice_page = False
            st.rerun()
    
    st.markdown("""
        <div style="position:fixed;left:0;right:0;bottom:0;height:64px;z-index:9999;background:#1e3c72;color:#fff;display:flex;justify-content:center;align-items:center;gap:18px;font-weight:700;">
            <span>Where Innovation Meets Security</span>
            <span style="opacity:.6;">|</span>
            <span>Zero Tolerance for Fraud</span>
            <span style="opacity:.6;">|</span>
            <span>© Xforia DAD</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.stop()

try:
    from ML_Model import ml_transaction_analysis, mock_transaction_analysis
except ImportError:
    def ml_transaction_analysis(data):
        import hashlib
        h = hashlib.sha256(str(data).encode()).hexdigest()
        return (int(h, 16) % 1000) / 1000.0
    mock_transaction_analysis = ml_transaction_analysis

MINDEE_API_KEY = "md_IdbyoMF3oVF18w3TquR1ivHmMufgzgG4"
MINDEE_ACCOUNT_NAME = ""
MINDEE_ENDPOINT_NAME = ""
MINDEE_VERSION = "1"
MINDEE_MODEL_ID = "c25da62c-dad8-4858-93b9-be97c1d50277"

def extract_check_data(response):
    try:
        fields = response.inference.result.fields
        names = ['memo','pay_to','bank_name','signature','check_date','payer_name','word_amount','check_number','number_amount','payer_address','account_number','routing_number']
        return {n: (fields[n].value if n in fields else None) for n in names}
    except Exception as e:
        st.error(f"Error extracting check data: {e}")
        return None

def convert_ocr_to_ml_format(check_data):
    amount = check_data.get('number_amount', 0) or 0
    return {'account_number': str(check_data.get('account_number') or 'UNKNOWN'), 'amount': float(amount), 'type': 'Check', 'merchant': str(check_data.get('memo') or 'Check Payment'), 'location': 'Unknown', 'recipient': str(check_data.get('pay_to') or 'Unknown'), 'time': 'Morning (6AM-12PM)', 'device': 'Check'}

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
                params = InferenceParameters(account_name=MINDEE_ACCOUNT_NAME, endpoint_name=MINDEE_ENDPOINT_NAME, version=MINDEE_VERSION or "1")
            elif MINDEE_MODEL_ID:
                params = InferenceParameters(model_id=MINDEE_MODEL_ID)
            else:
                st.error("Mindee not configured.")
                return (None,)*6
            resp = client.enqueue_and_get_inference(src, params)
            check_data = extract_check_data(resp)
            if not check_data:
                return (None,)*6
            extracted = {"Pay To": check_data.get('pay_to', 'N/A'), "Bank Name": check_data.get('bank_name', 'N/A'), "Check Date": check_data.get('check_date', 'N/A'), "Payer Name": check_data.get('payer_name', 'N/A'), "Amount (Words)": check_data.get('word_amount', 'N/A'), "Amount (Number)": f"${check_data.get('number_amount', 0):,.2f}" if check_data.get('number_amount') else 'N/A', "Check Number": check_data.get('check_number', 'N/A'), "Account Number": check_data.get('account_number', 'N/A'), "Routing Number": check_data.get('routing_number', 'N/A'), "Payer Address": check_data.get('payer_address', 'N/A'), "Memo": check_data.get('memo', 'N/A'), "Signature Present": "Yes" if check_data.get('signature') else "No"}
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

col_title, col_btn1 = st.columns([4, 1])
with col_title:
    st.markdown("<h1 class='page-title'>Document Anomaly For Finance</h1>", unsafe_allow_html=True)
with col_btn1:
    if st.button("Real-time Transaction", key="transaction_btn", type="secondary", use_container_width=True):
        go_transaction_page()

st.markdown("<h2 class='section-title'>Enhanced Check Analysis with AI</h2>", unsafe_allow_html=True)

c1, c2 = st.columns([2,3], gap="large")

with c1:
    st.markdown("#### Upload Check Image")
    uploaded_file = st.file_uploader("Drop your check image here", type=['jpg','jpeg','png'], label_visibility="collapsed", key="check_uploader")
    
    if uploaded_file:
        try:
            uploaded_file.seek(0)
            img = Image.open(uploaded_file)
            st.image(img, use_container_width=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Analyze Check", type="primary", key="analyze_check_btn", use_container_width=True):
                with st.spinner("Analyzing your check..."):
                    uploaded_file.seek(0)
                    extracted, combined, raw, ml_s, rule_s, ml_ens = mindee_ocr_analysis_with_ml(uploaded_file)
                
                if extracted and combined is not None:
                    st.success("Check processed successfully!")
                    st.session_state.check_results = {'extracted_data': extracted, 'fraud_score': combined, 'ml_score': ml_s, 'rule_score': rule_s, 'raw_data': raw, 'ml_ensemble': ml_ens}
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

        # st.markdown(f"<h4 style='display:flex;align-items:center;gap:8px;margin:20px 0 0 0;'>{icon_info()} Extracted Information</h4>", unsafe_allow_html=True)
        # st.markdown("<div class='grid'>", unsafe_allow_html=True)
        # for k, v in res['extracted_data'].items():
        #     st.markdown(f"<div class='item'><div class='lbl'>{k}</div><div class='val'>{v}</div></div>", unsafe_allow_html=True)
        # st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("Upload a check image on the left to begin analysis")
        st.markdown("""
            <div style='margin-top:20px; padding:20px; background:#f8fafc; border-radius:12px; border:1px solid #e2e8f0;'>
                <h4 style='margin:0 0 12px 0; color:#1e3c72;'>How it works:</h4>
                <ol style='margin:0; padding-left:20px; color:#475569;'>
                    <li style='margin-bottom:8px;'>Upload a check image (JPG, JPEG, or PNG)</li>
                    <li style='margin-bottom:8px;'>Click "Analyze Check" to process</li>
                    <li style='margin-bottom:8px;'>View fraud risk score and detailed analysis</li>
                    <li>Review recommendations and extracted check data</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)

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
            <div class="custom-footer">
                <span>Where Innovation Meets Security</span>
                <span class="footer-divider">|</span>
                <span>Zero Tolerance for Fraud</span>
                <span class="footer-divider">|</span>
                <span>© Xforia DAD</span>
            </div>
            """, unsafe_allow_html=True)