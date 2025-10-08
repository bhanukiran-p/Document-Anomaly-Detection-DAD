
# # Detection.py

# import streamlit as st
# import pandas as pd
# import numpy as np
# from PIL import Image
# import tempfile
# import os
# from datetime import datetime
# import pytz
# import warnings
# warnings.filterwarnings("ignore")
# import base64

# st.set_page_config(
#     page_title="AI-Powered Fraud Detection System",
#     page_icon=None,
#     layout="wide"
# )

# # ====== CONFIG: list all possible Dashboard targets ======
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
#     st.warning("Couldn't navigate to Dashboard. Make sure a page named 'Dashboard' exists under the `pages/` folder.")

# # ---------- Header / UI tweaks ----------
# st.markdown("""
# <style>
# .main .block-container { padding-top: 0 !important; margin-top: 0 !important; }
# [data-testid="stAppViewBlockContainer"] { z-index: 100 !important; }

# /* HIDE SIDEBAR AND TOGGLE BUTTON */
# [data-testid="stSidebar"] { display: none !important; }
# button[title*="sidebar"] { display: none !important; }
# section[data-testid="stSidebar"] { display: none !important; }

# [data-testid="stFileUploader"] small,
# [data-testid="stFileUploader"] .uploadFileDetails,
# [data-testid="stFileUploader"] [aria-live="polite"] { display:none !important; }

# .stApp { z-index: 100 !important; }
# </style>
# """, unsafe_allow_html=True)

# # --- Hide Deploy ---
# st.markdown("""
# <style>
#     [data-testid="stSidebar"] {{
#         display: none;
#     }}
#     [data-testid="stSidebarNav"] {{
#         display: none;
#     }}
#     [data-testid="stSidebarCollapseButton"] {{
#         display: none;
#     }}

# button[title="Deploy"], button[title*="Deploy"],
# a[title="Deploy"], a[title*="Deploy"],
# [data-testid="ToolbarActionDeploy"],
# [data-testid="deployment-link"] { display:none !important; }
# </style>
# <script>
# (function() {
#   const hideDeploy = () => {
#     const hdr = document.querySelector('header') || document.body;
#     if (!hdr) return;
#     hdr.querySelectorAll('*').forEach(el => {
#       const txt = (el.innerText || '').trim();
#       if (/^deploy$/i.test(txt)) {
#         el.style.display = 'none';
#         const p = el.closest('a,button,div'); if (p) p.style.display = 'none';
#       }
#     });
#   };
#   new MutationObserver(hideDeploy).observe(document.documentElement, {childList:true, subtree:true});
#   hideDeploy();
# })();
# </script>
# """, unsafe_allow_html=True)

# # ---------- Fixed logo ----------
# def add_fixed_logo():
#     import pathlib
#     cwd = pathlib.Path(os.getcwd())
#     here = pathlib.Path(__file__).parent if "__file__" in globals() else cwd
#     candidates = [cwd / "FDN.png", here / "FDN.png", here / "assets" / "FDN.png", cwd / "assets" / "FDN.png"]
#     logo_path = next((p for p in candidates if p.exists()), None)
    
#     if not logo_path:
#         st.warning("Logo file 'FDN.png' not found.")
#         return

#     encoded = base64.b64encode(logo_path.read_bytes()).decode()

#     st.markdown(f"""
#     <style>
#     .fixed-logo {{
#         position: fixed;
#         top: 12px;
#         left: 20px;
#         z-index: 2147482000;
#         background: rgba(255,255,255,0.95);
#         border-radius: 6px;
#         padding: 4px 6px;
#     }}
#     .fixed-logo img {{
#         width: 150px;
#         height: 50px;
#         display: block;
#         cursor: pointer;
#     }}
#     @media (max-width: 768px) {{
#         .fixed-logo {{ left: 20px; top: 10px; }}
#     }}
#     </style>
#     <div class="fixed-logo">
#         <a href="/" target="_self">
#             <img src="data:image/png;base64,{encoded}" alt="FDN Logo" />
#         </a>
#     </div>
#     """, unsafe_allow_html=True)

# add_fixed_logo()

# # ---------- Splash screen ----------
# try:
#     from splash_screen import show_splash
# except ImportError:
#     def show_splash():
#         st.title("Welcome to the Fraud Detection System")
#         st.write("Please run the app with the 'splash_screen.py' module available to see the full splash.")
#         if st.button("Launch Dashboard", type="primary"):
#             st.session_state.show_splash = False
#             st.rerun()

# if 'show_splash' not in st.session_state:
#     st.session_state.show_splash = True
# if st.session_state.show_splash:
#     st.markdown("""
#     <style>
#       .dad-pill {
#         position: relative;
#         display: inline-flex;
#         align-items: center; justify-content: center;
#         gap: 8px;
#         background: #D32F2F;
#         color: #fff !important;
#         border: 0;
#         border-radius: 12px;
#         padding: 12px 22px;
#         font-weight: 800 !important;
#         font-size: 15px !important;
#         text-transform: uppercase;
#         letter-spacing: .02em;
#         box-shadow: 0 10px 20px rgba(211,47,47,.45), 0 2px 6px rgba(0,0,0,.18);
#         cursor: pointer;
#         user-select: none; -webkit-user-select: none; text-decoration: none;
#         transition: transform .08s ease, box-shadow .15s ease, filter .15s ease;
#       }
#       .dad-pill:hover { filter: brightness(1.1); box-shadow: 0 14px 28px rgba(211,47,47,.55), 0 3px 8px rgba(0,0,0,.22); }
#       .dad-pill:active { transform: translateY(1px) scale(0.99); }

#       .dad-halo {
#         position: absolute; inset: -18px -28px -18px -28px;
#         background: radial-gradient(ellipse at center, rgba(255,255,255,.55), rgba(255,255,255,0));
#         border-radius: 24px; filter: blur(2px);
#         z-index: -1; pointer-events: none;
#       }
#     </style>

#     <script>
#       (function() {
#         function normalize() {
#           const all = Array.from(document.querySelectorAll('button, a'));
#           const btn = all.find(el => {
#             const t = (el.innerText || '').trim().toLowerCase();
#             return t === 'launch dad' || t === 'launch' || t === 'launch dashboard';
#           });
#           if (btn) {
#             btn.classList.add('dad-pill');
#             if (!btn.previousElementSibling || !btn.previousElementSibling.classList || !btn.previousElementSibling.classList.contains('dad-halo')) {
#               const halo = document.createElement('span');
#               halo.className = 'dad-halo';
#               btn.parentNode.insertBefore(halo, btn);
#             }
#           }
#         }
#         normalize();
#         new MutationObserver(normalize).observe(document.documentElement, {childList: true, subtree: true});
#       })();
#     </script>
#     """, unsafe_allow_html=True)

#     show_splash()
#     st.stop()

# # ---------- Check for dashboard navigation trigger ----------
# if 'navigate_to_dashboard' in st.session_state and st.session_state.navigate_to_dashboard:
#     st.session_state.navigate_to_dashboard = False
#     go_dashboard()

# # ---------- Footer styles ----------
# st.markdown("""
#     <style>
#     /* Hide default Streamlit footer */
#     footer {visibility: hidden;}
    
#     /* Remove all bottom padding/margins from page */
#     body, html {
#         margin-bottom: 0 !important;
#         padding-bottom: 0 !important;
#         overflow-x: hidden !important;
#     }
    
#     /* Remove bottom padding from main container */
#     .main {
#         padding-bottom: 0 !important;
#         margin-bottom: 0 !important;
#     }
    
#     [data-testid="stAppViewContainer"] {
#         padding-bottom: 0 !important;
#         margin-bottom: 0 !important;
#         overflow-x: hidden !important;
#     }
    
#     section[data-testid="stAppViewBlockContainer"] {
#         padding-bottom: 0 !important;
#         margin-bottom: 0 !important;
#     }
    
#     .block-container {
#         padding-bottom: 0 !important;
#         margin-bottom: 0 !important;
#     }
    
#     /* Ensure no space after footer */
#     .fixed-footer ~ * {
#         margin-bottom: 0 !important;
#         padding-bottom: 0 !important;
#     }
    
#     /* Footer at the end of content - Full width edge-to-edge, no gap below */
#     .fixed-footer {
#         position: relative !important;
#         width: 100vw !important;
#         height: 64px !important;
#         background: #1e3c72 !important;
#         color: #fff !important;
#         display: flex !important;
#         align-items: center !important;
#         justify-content: center !important;
#         gap: 10px !important;
#         padding: 10px 16px !important;
#         box-shadow: 0 -2px 10px rgba(0,0,0,.22) !important;
#         font-size: 0.95em !important;
#         font-weight: 600 !important;
#         font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial, 'Noto Sans' !important;
#         margin-left: calc(-50vw + 50%) !important;
#         margin-right: calc(-50vw + 50%) !important;
#         margin-top: 20px !important;
#         margin-bottom: -20px !important;
#         padding-bottom: 20px !important;
#         box-sizing: border-box !important;
#     }
    
#     .fixed-footer .sep { 
#         opacity: .6 !important; 
#         padding: 0 8px !important; 
#     }
    
#     .fixed-footer span {
#         color: #fff !important;
#         display: inline-block !important;
#     }
    
#     /* Mobile responsive */
#     @media (max-width: 768px) {
#         .fixed-footer {
#             font-size: 0.85rem !important;
#             gap: 6px !important;
#             padding: 8px 12px !important;
#         }
#         .fixed-footer .sep {
#             padding: 0 4px !important;
#         }
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown(
#     "<h1 style='margin-bottom:10px;'>AI-Powered Fraud Detection System</h1>",
#     unsafe_allow_html=True
# )


# # ---------- Model / Analysis functions ----------
# try:
#     from ML_Model import ml_transaction_analysis, mock_transaction_analysis
# except ImportError:
#     st.error("ML_Model.py not found. Using mock analysis.")
#     def ml_transaction_analysis(data):
#         import hashlib
#         h = hashlib.sha256(str(data).encode()).hexdigest()
#         score = int(h, 16) % 1000 / 1000.0
#         return score 
#     mock_transaction_analysis = ml_transaction_analysis

# API_KEY = "md_B9aH0hoQrXrmza3p8zRuiH9FIkz9bj0a"
# MODEL_ID = "07b0e09b-f1c0-4fa9-89e4-7c00c2a9aa20"

# def extract_check_data(response):
#     try:
#         fields = response.inference.result.fields
#         check_data = {}
#         field_names = ['memo','pay_to','bank_name','signature','check_date',
#                        'payer_name','word_amount','check_number','number_amount',
#                        'payer_address','account_number','routing_number']
#         for n in field_names:
#             check_data[n] = fields[n].value if n in fields else None
#         return check_data
#     except Exception as e:
#         st.error(f"Error extracting check data: {str(e)}")
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
#     fraud_score = 0.1
#     if not check_data.get('pay_to'): fraud_score += 0.2
#     if not check_data.get('number_amount'): fraud_score += 0.3
#     if not check_data.get('signature'): fraud_score += 0.3
#     if not check_data.get('bank_name'): fraud_score += 0.2
#     if not check_data.get('account_number'): fraud_score += 0.2
#     if not check_data.get('routing_number'): fraud_score += 0.2
#     amount = check_data.get('number_amount', 0)
#     if amount and amount > 10000: fraud_score += 0.2
#     elif amount and amount > 5000: fraud_score += 0.1
#     word_amount = check_data.get('word_amount', '')
#     if word_amount and amount and len(word_amount.split()) < 3: fraud_score += 0.1
#     check_date = check_data.get('check_date')
#     if check_date:
#         try:
#             date_obj = datetime.strptime(str(check_date), '%Y-%m-%d')
#             days_old = (datetime.now() - date_obj).days
#             if days_old > 180: fraud_score += 0.2
#             elif days_old > 90: fraud_score += 0.1
#         except:
#             fraud_score += 0.1
#     return min(fraud_score, 0.95)

# def mindee_ocr_analysis_with_ml(image_file):
#     try:
#         from mindee import ClientV2, InferenceParameters
#         mindee_client = ClientV2(API_KEY)
#         params = InferenceParameters(model_id=MODEL_ID, rag=False)
#         with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
#             tmp_file.write(image_file.read())
#             tmp_file_path = tmp_file.name
#         try:
#             input_source = mindee_client.source_from_path(tmp_file_path)
#             response = mindee_client.enqueue_and_get_inference(input_source, params)
#             check_data = extract_check_data(response)
#             if check_data:
#                 extracted_data = {
#                     "Pay To": check_data.get('pay_to', 'N/A'),
#                     "Bank Name": check_data.get('bank_name', 'N/A'),
#                     "Check Date": check_data.get('check_date', 'N/A'),
#                     "Payer Name": check_data.get('payer_name', 'N/A'),
#                     "Amount (Words)": check_data.get('word_amount', 'N/A'),
#                     "Amount (Number)": f"${check_data.get('number_amount', 0):,.2f}" if check_data.get('number_amount') else 'N/A',
#                     "Check Number": check_data.get('check_number', 'N/A'),
#                     "Account Number": check_data.get('account_number', 'N/A'),
#                     "Routing Number": check_data.get('routing_number', 'N/A'),
#                     "Payer Address": check_data.get('payer_address', 'N/A'),
#                     "Memo": check_data.get('memo', 'N/A'),
#                     "Signature Present": "Yes" if check_data.get('signature') else "No"
#                 }
#                 ml_transaction_data = convert_ocr_to_ml_format(check_data)
#                 ml_result = ml_transaction_analysis(ml_transaction_data)
#                 if isinstance(ml_result, dict):
#                     ml_fraud_score = ml_result['ensemble_probability']
#                     ml_ensemble_data = ml_result
#                 else:
#                     ml_fraud_score = ml_result
#                     ml_ensemble_data = None
#                 rule_based_score = calculate_fraud_score(check_data)
#                 combined_score = (ml_fraud_score * 0.7) + (rule_based_score * 0.3)
#                 return extracted_data, combined_score, check_data, ml_fraud_score, rule_based_score, ml_ensemble_data
#             else:
#                 return None, None, None, None, None, None
#         finally:
#             if os.path.exists(tmp_file_path):
#                 os.unlink(tmp_file_path)
#     except Exception as e:
#         st.error(f"Error processing Check: {e}")
#         return None, None, None, None, None, None

# def get_risk_level(score):
#     if score >= 0.7: return "HIGH RISK", "red"
#     elif score >= 0.4: return "MEDIUM RISK", "orange"
#     else: return "LOW RISK", "green"

# def get_check_risk_factors(check_data, ml_score, rule_score):
#     factors = []
#     if not check_data.get('signature'): factors.append("• Missing signature detected")
#     if not check_data.get('number_amount'): factors.append("• Missing or invalid amount")
#     if not check_data.get('pay_to'): factors.append("• Missing payee information")
#     if not check_data.get('bank_name'): factors.append("• Missing bank information")
#     amount = check_data.get('number_amount', 0)
#     if amount and amount > 10000: factors.append("• Very high check amount")
#     elif amount and amount > 5000: factors.append("• High check amount")
#     check_date = check_data.get('check_date')
#     if check_date:
#         try:
#             days_old = (datetime.now() - datetime.strptime(str(check_date), '%Y-%m-%d')).days
#             if days_old > 180: factors.append("• Very old check (>6 months)")
#             elif days_old > 90: factors.append("• Old check (>3 months)")
#         except:
#             factors.append("• Invalid / unclear check date")
#     if ml_score > 0.8: factors.append("• ML model shows very high fraud confidence")
#     elif ml_score > 0.6: factors.append("• ML model shows elevated fraud risk")
#     word_amount = check_data.get('word_amount', '')
#     if word_amount and amount and len(word_amount.split()) < 3: factors.append("• Incomplete written amount")
#     return factors if factors else ["• No major risk factors identified"]

# def get_detailed_risk_factors(transaction_data, fraud_score):
#     factors = []
#     amount = float(transaction_data.get('amount', 0))
    
#     # Amount-based factors
#     if amount > 10000: 
#         factors.append("• Very high transaction amount (>${:,.2f}) - Exceeds normal threshold".format(amount))
#     elif amount > 5000: 
#         factors.append("• High transaction amount (>${:,.2f}) - Above average transaction size".format(amount))
#     elif amount > 1000:
#         factors.append("• Moderate transaction amount (>${:,.2f})".format(amount))
    
#     # Time-based factors
#     time_of_day = transaction_data.get('time', '')
#     if "Night" in time_of_day:
#         factors.append("• Unusual transaction time (night) - Transactions between 12AM-6AM are statistically higher risk")
#     elif "Morning" in time_of_day:
#         factors.append("• Standard transaction time (morning) - Normal business hours")
    
#     # Device-based factors
#     device = transaction_data.get('device', '')
#     if device == "ATM" and amount > 1000: 
#         factors.append("• Large ATM withdrawal - Exceeds typical ATM transaction limit")
#     elif device == "ATM":
#         factors.append("• ATM transaction - Standard withdrawal pattern")
#     elif device == "Mobile App":
#         factors.append("• Mobile transaction - Modern payment method with standard security")
#     elif device == "Phone":
#         factors.append("• Phone-based transaction - Voice or SMS authentication recommended")
    
#     # Location-based factors
#     location = transaction_data.get('location', '').lower()
#     if 'unknown' in location or not location or location.strip() == '':
#         factors.append("• Unknown transaction location - Geographic verification unavailable")
#     else:
#         factors.append(f"• Transaction location: {transaction_data.get('location')} - Location verified")
    
#     # Transaction type factors
#     trans_type = transaction_data.get('type', '')
#     if trans_type == "Transfer":
#         factors.append("• Transfer transaction - Peer-to-peer money movement")
#     elif trans_type == "Withdrawal":
#         factors.append("• Withdrawal transaction - Cash disbursement detected")
#     elif trans_type == "Payment":
#         factors.append("• Payment transaction - Merchant transaction identified")
    
#     # Recipient analysis
#     recipient = transaction_data.get('recipient', '')
#     if not recipient or recipient.lower() == 'unknown':
#         factors.append("• Unverified recipient - Payee information incomplete")
#     else:
#         factors.append(f"• Recipient verified: {recipient}")
    
#     # ML model confidence factors
#     if fraud_score > 0.8: 
#         factors.append("• ML model shows very high fraud confidence (>80%) - Multiple risk indicators detected")
#     elif fraud_score > 0.6: 
#         factors.append("• ML model shows elevated fraud risk (60-80%) - Several warning signs present")
#     elif fraud_score > 0.4:
#         factors.append("• ML model shows moderate fraud risk (40-60%) - Some concerns identified")
#     else:
#         factors.append("• ML model shows low fraud risk (<40%) - Transaction pattern appears normal")
    
#     # Account behavior (simulated based on amount and type)
#     if amount > 5000 and device == "ATM":
#         factors.append("• Unusual combination: High-value ATM transaction - Rarely seen in normal behavior")
    
#     return factors if factors else ["• No major risk factors identified - Transaction appears within normal parameters"]

# # ---------- Tabs ----------
# tab1, tab2 = st.tabs(["Check Analysis", "Online Transaction Analysis"])

# # ===== CHECK ANALYSIS TAB =====
# with tab1:
#     st.markdown("### Enhanced Check Analysis with AI", unsafe_allow_html=True)
#     col1, col2 = st.columns([1, 1])
#     with col1:
#         st.write("") 
#         st.markdown("#### Upload Check File")
#         uploaded_file = st.file_uploader("Upload File", help="Upload a clear image for processing", label_visibility="visible")
#         if uploaded_file is not None:
#             try:
#                 uploaded_file.seek(0)
#                 image = Image.open(uploaded_file)
#             except Exception:
#                 st.error("Please upload a valid image file.")
#                 image = None
#             if image is not None:
#                 st.image(image, caption="Uploaded Image", use_container_width=True)
#                 if st.button("Analyze Check", type="primary"):
#                     with st.spinner("Analyzing check for fraud..."):
#                         uploaded_file.seek(0)
#                         extracted_data, combined_score, raw_data, ml_score, rule_score, ml_ensemble = mindee_ocr_analysis_with_ml(uploaded_file)
#                     if extracted_data and combined_score is not None:
#                         st.success("Check processed successfully!")
#                         st.session_state.Check_results = {
#                             'extracted_data': extracted_data,
#                             'fraud_score': combined_score,
#                             'ml_score': ml_score,
#                             'rule_score': rule_score,
#                             'raw_data': raw_data,
#                             'ml_ensemble': ml_ensemble
#                         }
#                     else:
#                         st.error("Failed to process the Check. Please check your API configuration and try again.")
#     with col2:
#         if 'Check_results' in st.session_state:
#             st.write("") 
#             st.markdown("#### Enhanced Analysis Results")
#             results = st.session_state.Check_results
#             st.markdown("**Extracted Information:**")
#             for key, value in results['extracted_data'].items():
#                 st.text(f"{key}: {value}")
#             st.markdown("---")
#             fraud_score = results['fraud_score']
#             ml_score = results.get('ml_score', 0)
#             rule_score = results.get('rule_score', 0)
#             risk_level, color = get_risk_level(fraud_score)
#             st.markdown("**Enhanced Fraud Analysis:**")
#             st.markdown(f"**Risk Level:** :{color}[{risk_level}]")
#             st.progress(float(fraud_score))
            
#             # Display only the combined score as percentage - LARGER
#             fraud_percentage = fraud_score * 100
#             st.markdown(f"<h2 style='color: {color}; margin-top: 10px; margin-bottom: 15px;'>Fraud Detection Score: {fraud_percentage:.0f}%</h2>", unsafe_allow_html=True)
            
#             st.markdown("**Risk Factors:**")
#             raw_data = results.get('raw_data', {})
#             for factor in get_check_risk_factors(raw_data, ml_score, rule_score):
#                 st.text(factor)
#             st.markdown("**Recommendations:**")
#             if fraud_score >= 0.7:
#                 st.error("High fraud risk detected. Recommend manual verification and additional authentication.")
#             elif fraud_score >= 0.4:
#                 st.warning("Medium risk. Additional verification suggested before processing.")
#             else:
#                 st.success("Low risk. Transaction appears legitimate and can be processed.")

# # ===== ONLINE TRANSACTION TAB =====
# with tab2:
#     st.markdown("### Online Transaction Analysis", unsafe_allow_html=True)
    
#     # Get exact current time (runs in background, not displayed)
#     current_time = datetime.now()
#     exact_time_display = current_time.strftime("%I:%M:%S %p")
#     full_datetime_display = current_time.strftime("%B %d, %Y at %I:%M:%S %p")
    
#     # Determine time period for ML model
#     current_hour = current_time.hour
#     if 6 <= current_hour < 12:
#         time_period = "Morning (6AM-12PM)"
#     elif 12 <= current_hour < 18:
#         time_period = "Afternoon (12PM-6PM)"
#     elif 18 <= current_hour < 24:
#         time_period = "Evening (6PM-12AM)"
#     else:
#         time_period = "Night (12AM-6AM)"
    
#     # Default location (changeable by user)
#     default_location = "Boydton, Virginia, US"
    
#     col1, col2 = st.columns([1, 1])
#     with col1:
#         st.subheader("Transaction Details")
#         with st.form("transaction_form"):
#             account_number = st.text_input("Account Number", placeholder="Enter account number")
#             amount_input = st.text_input("Transaction Amount ($)", placeholder="Enter amount")
#             recipient_name = st.text_input("Recipient Name", placeholder="Enter recipient name")
#             transaction_type = st.selectbox("Transaction Type", ["Transfer", "Payment", "Withdrawal", "Deposit"])
#             merchant = st.text_input("Merchant", placeholder="Enter merchant")
            
#             # Auto-populated location with option to change
#             location = st.text_input("Transaction Location", value=default_location, placeholder="City, State")
            
#             # Auto-populated device
#             device_type = st.selectbox("Device Used", 
#                                       options=["Web Browser", "Mobile App", "ATM", "Phone"],
#                                       index=0)
            
#             submitted = st.form_submit_button("Analyze Transaction", type="primary")
            
#             # Convert amount input to float
#             amount = 0.0
#             if amount_input:
#                 try:
#                     amount = float(amount_input)
#                 except ValueError:
#                     st.error("Please enter a valid numeric amount")
#                     amount = 0.0
            
#             if submitted and account_number and amount > 0:
#                 # Get fresh timestamp at submission
#                 transaction_time = datetime.now()
#                 exact_time_str = transaction_time.strftime("%I:%M:%S %p on %B %d, %Y")
                
#                 transaction_data = {
#                     "account_number": account_number,
#                     "amount": amount,
#                     "recipient": recipient_name,
#                     "type": transaction_type,
#                     "merchant": merchant,
#                     "location": location,
#                     "time": time_period,
#                     "exact_time": exact_time_str,
#                     "device": device_type
#                 }
#                 with st.spinner("Analyzing transaction for fraud patterns..."):
#                     result = ml_transaction_analysis(transaction_data)
#                 if isinstance(result, dict):
#                     fraud_score = result['ensemble_probability']
#                     st.session_state.transaction_results = {
#                         'data': transaction_data,
#                         'fraud_score': fraud_score,
#                         'ensemble_result': result
#                     }
#                 else:
#                     fraud_score = result
#                     st.session_state.transaction_results = {
#                         'data': transaction_data,
#                         'fraud_score': fraud_score,
#                         'ensemble_result': None
#                     }
#     with col2:
#         if 'transaction_results' in st.session_state:
#             st.subheader("Analysis Results")
#             results = st.session_state.transaction_results
#             data = results['data']
#             fraud_score = results['fraud_score']
            
#             st.markdown("**Transaction Summary:**")
#             st.text(f"Account: {data['account_number']}")
#             st.text(f"Amount: ${data['amount']:,.2f}")
#             st.text(f"Type: {data['type']}")
#             st.text(f"Recipient: {data['recipient']}")
#             st.text(f"Merchant: {data['merchant']}")
#             st.text(f"Location: {data['location']}")
#             st.text(f"Device: {data['device']}")
#             st.text(f"Transaction Time: {data.get('exact_time', 'N/A')}")
            
#             st.markdown("---")
            
#             # Fraud Analysis Section
#             st.markdown("**Fraud Analysis:**")
#             risk_level, color = get_risk_level(fraud_score)
#             st.markdown(f"**Risk Level:** :{color}[{risk_level}]")
#             st.progress(float(fraud_score))
            
#             # AI Fraud Detection Score
#             st.markdown("---")
#             st.markdown("**AI Fraud Detection Score:**")
#             fraud_percentage = fraud_score * 100
#             st.markdown(f"<h2 style='color: {color};'>{fraud_percentage:.1f}%</h2>", unsafe_allow_html=True)
            
#             # Risk Level Banner
#             if fraud_score < 0.4:
#                 st.success("LOW RISK TRANSACTION")
#                 st.info("Transaction appears legitimate!")
#             elif fraud_score < 0.7:
#                 st.warning("MEDIUM RISK TRANSACTION")
#             else:
#                 st.error("HIGH RISK TRANSACTION")
#                 st.warning("Manual review required!")
            
#             st.markdown("---")
#             st.markdown("**Risk Factors:**")
#             factors = get_detailed_risk_factors(data, fraud_score)
#             for factor in factors:
#                 st.text(factor)
            
#             st.markdown("---")
#             st.markdown("**Recommendations:**")
#             if fraud_score >= 0.7:
#                 st.error("BLOCK TRANSACTION - High fraud risk detected. Require additional verification and manual review.")
#             elif fraud_score >= 0.4:
#                 st.warning("REQUEST VERIFICATION - Medium risk. Additional authentication before processing.")
#             else:
#                 st.success("APPROVE TRANSACTION - Low fraud risk")
            
#             # Processing Status
#             st.markdown("---")
#             st.markdown("**Processing Status:**")
#             if fraud_score < 0.4:
#                 st.markdown("- ✅ Transaction approved for processing")
#                 st.markdown("- ✅ Normal monitoring applies")
#                 st.markdown("- ✅ Proceed with standard workflow")
#             elif fraud_score < 0.7:
#                 st.markdown("- ⚠️ Transaction requires additional verification")
#                 st.markdown("- ⚠️ Enhanced monitoring applied")
#                 st.markdown("- ⚠️ Waiting for authentication")
#             else:
#                 st.markdown("- ❌ Transaction blocked")
#                 st.markdown("- ❌ Manual review required")
#                 st.markdown("- ❌ Customer notification sent")

# # ---------- Floating "LAUNCH DASHBOARD" ----------
# st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)
# button_container = st.container()
# with button_container:
#     col1, col2, col3 = st.columns([1, 1, 1])
#     with col2:
#         if st.button("LAUNCH DASHBOARD", key="dashboard_btn", type="primary", use_container_width=True):
#             st.session_state.navigate_to_dashboard = True
#             st.rerun()

# st.markdown("""
# <style>
# button[key="dashboard_btn"],
# button[key="dashboard_btn"]:focus,
# button[key="dashboard_btn"]:visited {
#     background: #D32F2F !important;
#     background-color: #D32F2F !important;
#     background-image: none !important;
#     color: #fff !important;
#     border: 0 !important;
#     border-radius: 12px !important;
#     padding: 12px 22px !important;
#     font-weight: 800 !important;
#     font-size: 15px !important;
#     text-transform: uppercase !important;
#     letter-spacing: .02em !important;
#     box-shadow: 0 10px 20px rgba(211,47,47,.45), 0 2px 6px rgba(0,0,0,.18) !important;
#     cursor: pointer !important;
#     transition: transform .08s ease, box-shadow .15s ease, filter .15s ease !important;
#     min-width: 220px !important;
# }

# button[key="dashboard_btn"]:hover {
#     background: #D32F2F !important;
#     background-color: #D32F2F !important;
#     background-image: none !important;
#     filter: brightness(1.1) !important;
#     box-shadow: 0 14px 28px rgba(211,47,47,.55), 0 3px 8px rgba(0,0,0,.22) !important;
# }

# button[key="dashboard_btn"]:active {
#     background: #D32F2F !important;
#     background-color: #D32F2F !important;
#     background-image: none !important;
#     transform: translateY(1px) scale(0.99) !important;
# }

# button[key="dashboard_btn"]::before {
#     content: "";
#     position: absolute;
#     inset: -18px -28px;
#     background: radial-gradient(ellipse at center, rgba(255,255,255,.55), rgba(255,255,255,0));
#     border-radius: 24px;
#     filter: blur(2px);
#     z-index: -1;
#     pointer-events: none;
# }

# @media (max-width: 640px) {
#     button[key="dashboard_btn"] {
#         padding: 11px 18px !important;
#         font-size: 14px !important;
#         min-width: 180px !important;
#     }
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------- Footer ----------
# st.markdown("""
#     <div class='fixed-footer'>
#       <span>Where Innovation Meets Security</span>
#       <span class="sep">|</span>
#       <span>Zero Tolerance for Fraud</span>
#       <span class="sep">|</span>
#       <span>© Xforia DAD</span>
#     </div>
# """, unsafe_allow_html=True)


























# Detection.py

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import tempfile
import os
from datetime import datetime
import pytz
import warnings
warnings.filterwarnings("ignore")
import base64

st.set_page_config(
    page_title="AI-Powered Fraud Detection System",
    page_icon=None,
    layout="wide"
)

# ====== CONFIG: list all possible Dashboard targets ======
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

# ---------- Header / UI tweaks ----------
st.markdown("""
<style>
.main .block-container { padding-top: 0 !important; margin-top: 0 !important; }
[data-testid="stAppViewBlockContainer"] { z-index: 100 !important; }

/* HIDE SIDEBAR AND TOGGLE BUTTON */
[data-testid="stSidebar"] { display: none !important; }
button[title*="sidebar"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }

[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] .uploadFileDetails,
[data-testid="stFileUploader"] [aria-live="polite"] { display:none !important; }

.stApp { z-index: 100 !important; }
</style>
""", unsafe_allow_html=True)

# --- Hide Deploy ---
st.markdown("""
<style>
    [data-testid="stSidebar"] {{
        display: none;
    }}
    [data-testid="stSidebarNav"] {{
        display: none;
    }}
    [data-testid="stSidebarCollapseButton"] {{
        display: none;
    }}

button[title="Deploy"], button[title*="Deploy"],
a[title="Deploy"], a[title*="Deploy"],
[data-testid="ToolbarActionDeploy"],
[data-testid="deployment-link"] { display:none !important; }
</style>
<script>
(function() {
  const hideDeploy = () => {
    const hdr = document.querySelector('header') || document.body;
    if (!hdr) return;
    hdr.querySelectorAll('*').forEach(el => {
      const txt = (el.innerText || '').trim();
      if (/^deploy$/i.test(txt)) {
        el.style.display = 'none';
        const p = el.closest('a,button,div'); if (p) p.style.display = 'none';
      }
    });
  };
  new MutationObserver(hideDeploy).observe(document.documentElement, {childList:true, subtree:true});
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
        st.warning("Logo file 'FDN.png' not found.")
        return

    encoded = base64.b64encode(logo_path.read_bytes()).decode()

    st.markdown(f"""
    <style>
    .fixed-logo {{
        position: fixed;
        top: 12px;
        left: 20px;
        z-index: 2147482000;
        background: rgba(255,255,255,0.95);
        border-radius: 6px;
        padding: 4px 6px;
    }}
    .fixed-logo img {{
        width: 150px;
        height: 50px;
        display: block;
        cursor: pointer;
    }}
    @media (max-width: 768px) {{
        .fixed-logo {{ left: 20px; top: 10px; }}
    }}
    </style>
    <div class="fixed-logo">
        <a href="/" target="_self">
            <img src="data:image/png;base64,{encoded}" alt="FDN Logo" />
        </a>
    </div>
    """, unsafe_allow_html=True)

add_fixed_logo()

# ---------- Splash screen ----------
try:
    from splash_screen import show_splash
except ImportError:
    def show_splash():
        st.title("Welcome to the Fraud Detection System")
        st.write("Please run the app with the 'splash_screen.py' module available to see the full splash.")
        if st.button("Launch Dashboard", type="primary"):
            st.session_state.show_splash = False
            st.rerun()

if 'show_splash' not in st.session_state:
    st.session_state.show_splash = True
if st.session_state.show_splash:
    st.markdown("""
    <style>
      .dad-pill {
        position: relative;
        display: inline-flex;
        align-items: center; justify-content: center;
        gap: 8px;
        background: #D32F2F;
        color: #fff !important;
        border: 0;
        border-radius: 12px;
        padding: 12px 22px;
        font-weight: 800 !important;
        font-size: 15px !important;
        text-transform: uppercase;
        letter-spacing: .02em;
        box-shadow: 0 10px 20px rgba(211,47,47,.45), 0 2px 6px rgba(0,0,0,.18);
        cursor: pointer;
        user-select: none; -webkit-user-select: none; text-decoration: none;
        transition: transform .08s ease, box-shadow .15s ease, filter .15s ease;
      }
      .dad-pill:hover { filter: brightness(1.1); box-shadow: 0 14px 28px rgba(211,47,47,.55), 0 3px 8px rgba(0,0,0,.22); }
      .dad-pill:active { transform: translateY(1px) scale(0.99); }

      .dad-halo {
        position: absolute; inset: -18px -28px -18px -28px;
        background: radial-gradient(ellipse at center, rgba(255,255,255,.55), rgba(255,255,255,0));
        border-radius: 24px; filter: blur(2px);
        z-index: -1; pointer-events: none;
      }
    </style>

    <script>
      (function() {
        function normalize() {
          const all = Array.from(document.querySelectorAll('button, a'));
          const btn = all.find(el => {
            const t = (el.innerText || '').trim().toLowerCase();
            return t === 'launch dad' || t === 'launch' || t === 'launch dashboard';
          });
          if (btn) {
            btn.classList.add('dad-pill');
            if (!btn.previousElementSibling || !btn.previousElementSibling.classList || !btn.previousElementSibling.classList.contains('dad-halo')) {
              const halo = document.createElement('span');
              halo.className = 'dad-halo';
              btn.parentNode.insertBefore(halo, btn);
            }
          }
        }
        normalize();
        new MutationObserver(normalize).observe(document.documentElement, {childList: true, subtree: true});
      })();
    </script>
    """, unsafe_allow_html=True)

    show_splash()
    st.stop()

# ---------- Check for dashboard navigation trigger ----------
if 'navigate_to_dashboard' in st.session_state and st.session_state.navigate_to_dashboard:
    st.session_state.navigate_to_dashboard = False
    go_dashboard()

# ---------- Footer styles ----------
st.markdown("""
    <style>
    /* Hide default Streamlit footer */
    footer {visibility: hidden;}
    
    /* Remove all bottom padding/margins from page */
    body, html {
        margin-bottom: 0 !important;
        padding-bottom: 0 !important;
        overflow-x: hidden !important;
    }
    
    /* Remove bottom padding from main container */
    .main {
        padding-bottom: 0 !important;
        margin-bottom: 0 !important;
    }
    
    [data-testid="stAppViewContainer"] {
        padding-bottom: 0 !important;
        margin-bottom: 0 !important;
        overflow-x: hidden !important;
    }
    
    section[data-testid="stAppViewBlockContainer"] {
        padding-bottom: 0 !important;
        margin-bottom: 0 !important;
    }
    
    .block-container {
        padding-bottom: 0 !important;
        margin-bottom: 0 !important;
    }
    
    /* Ensure no space after footer */
    .fixed-footer ~ * {
        margin-bottom: 0 !important;
        padding-bottom: 0 !important;
    }
    
    /* Footer at the end of content - Full width edge-to-edge, no gap below */
    .fixed-footer {
        position: relative !important;
        width: 100vw !important;
        height: 64px !important;
        background: #1e3c72 !important;
        color: #fff !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 10px !important;
        padding: 10px 16px !important;
        box-shadow: 0 -2px 10px rgba(0,0,0,.22) !important;
        font-size: 0.95em !important;
        font-weight: 600 !important;
        font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial, 'Noto Sans' !important;
        margin-left: calc(-50vw + 50%) !important;
        margin-right: calc(-50vw + 50%) !important;
        margin-top: 20px !important;
        margin-bottom: -20px !important;
        padding-bottom: 20px !important;
        box-sizing: border-box !important;
    }
    
    .fixed-footer .sep { 
        opacity: .6 !important; 
        padding: 0 8px !important; 
    }
    
    .fixed-footer span {
        color: #fff !important;
        display: inline-block !important;
    }
    
    /* Mobile responsive */
    @media (max-width: 768px) {
        .fixed-footer {
            font-size: 0.85rem !important;
            gap: 6px !important;
            padding: 8px 12px !important;
        }
        .fixed-footer .sep {
            padding: 0 4px !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 style='margin-bottom:10px;'>AI-Powered Fraud Detection System</h1>",
    unsafe_allow_html=True
)


# ---------- Model / Analysis functions ----------
try:
    from ML_Model import ml_transaction_analysis, mock_transaction_analysis
except ImportError:
    st.error("ML_Model.py not found. Using mock analysis.")
    def ml_transaction_analysis(data):
        import hashlib
        h = hashlib.sha256(str(data).encode()).hexdigest()
        score = int(h, 16) % 1000 / 1000.0
        return score 
    mock_transaction_analysis = ml_transaction_analysis

API_KEY = "md_B9aH0hoQrXrmza3p8zRuiH9FIkz9bj0a"
MODEL_ID = "07b0e09b-f1c0-4fa9-89e4-7c00c2a9aa20"

def extract_check_data(response):
    try:
        fields = response.inference.result.fields
        check_data = {}
        field_names = ['memo','pay_to','bank_name','signature','check_date',
                       'payer_name','word_amount','check_number','number_amount',
                       'payer_address','account_number','routing_number']
        for n in field_names:
            check_data[n] = fields[n].value if n in fields else None
        return check_data
    except Exception as e:
        st.error(f"Error extracting check data: {str(e)}")
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
    fraud_score = 0.1
    if not check_data.get('pay_to'): fraud_score += 0.2
    if not check_data.get('number_amount'): fraud_score += 0.3
    if not check_data.get('signature'): fraud_score += 0.3
    if not check_data.get('bank_name'): fraud_score += 0.2
    if not check_data.get('account_number'): fraud_score += 0.2
    if not check_data.get('routing_number'): fraud_score += 0.2
    amount = check_data.get('number_amount', 0)
    if amount and amount > 10000: fraud_score += 0.2
    elif amount and amount > 5000: fraud_score += 0.1
    word_amount = check_data.get('word_amount', '')
    if word_amount and amount and len(word_amount.split()) < 3: fraud_score += 0.1
    check_date = check_data.get('check_date')
    if check_date:
        try:
            date_obj = datetime.strptime(str(check_date), '%Y-%m-%d')
            days_old = (datetime.now() - date_obj).days
            if days_old > 180: fraud_score += 0.2
            elif days_old > 90: fraud_score += 0.1
        except:
            fraud_score += 0.1
    return min(fraud_score, 0.95)

def mindee_ocr_analysis_with_ml(image_file):
    try:
        from mindee import ClientV2, InferenceParameters
        mindee_client = ClientV2(API_KEY)
        params = InferenceParameters(model_id=MODEL_ID, rag=False)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
            tmp_file.write(image_file.read())
            tmp_file_path = tmp_file.name
        try:
            input_source = mindee_client.source_from_path(tmp_file_path)
            response = mindee_client.enqueue_and_get_inference(input_source, params)
            check_data = extract_check_data(response)
            if check_data:
                extracted_data = {
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
                ml_transaction_data = convert_ocr_to_ml_format(check_data)
                ml_result = ml_transaction_analysis(ml_transaction_data)
                if isinstance(ml_result, dict):
                    ml_fraud_score = ml_result['ensemble_probability']
                    ml_ensemble_data = ml_result
                else:
                    ml_fraud_score = ml_result
                    ml_ensemble_data = None
                rule_based_score = calculate_fraud_score(check_data)
                combined_score = (ml_fraud_score * 0.7) + (rule_based_score * 0.3)
                return extracted_data, combined_score, check_data, ml_fraud_score, rule_based_score, ml_ensemble_data
            else:
                return None, None, None, None, None, None
        finally:
            if os.path.exists(tmp_file_path):
                os.unlink(tmp_file_path)
    except Exception as e:
        st.error(f"Error processing Check: {e}")
        return None, None, None, None, None, None

def get_risk_level(score):
    if score >= 0.7: return "HIGH RISK", "red"
    elif score >= 0.4: return "MEDIUM RISK", "orange"
    else: return "LOW RISK", "green"

def get_check_risk_factors(check_data, ml_score, rule_score):
    factors = []
    if not check_data.get('signature'): factors.append("• Missing signature detected")
    if not check_data.get('number_amount'): factors.append("• Missing or invalid amount")
    if not check_data.get('pay_to'): factors.append("• Missing payee information")
    if not check_data.get('bank_name'): factors.append("• Missing bank information")
    amount = check_data.get('number_amount', 0)
    if amount and amount > 10000: factors.append("• Very high check amount")
    elif amount and amount > 5000: factors.append("• High check amount")
    check_date = check_data.get('check_date')
    if check_date:
        try:
            days_old = (datetime.now() - datetime.strptime(str(check_date), '%Y-%m-%d')).days
            if days_old > 180: factors.append("• Very old check (>6 months)")
            elif days_old > 90: factors.append("• Old check (>3 months)")
        except:
            factors.append("• Invalid / unclear check date")
    if ml_score > 0.8: factors.append("• ML model shows very high fraud confidence")
    elif ml_score > 0.6: factors.append("• ML model shows elevated fraud risk")
    word_amount = check_data.get('word_amount', '')
    if word_amount and amount and len(word_amount.split()) < 3: factors.append("• Incomplete written amount")
    return factors if factors else ["• No major risk factors identified"]

def get_detailed_risk_factors(transaction_data, fraud_score):
    factors = []
    amount = float(transaction_data.get('amount', 0))
    
    # Amount-based factors
    if amount > 10000: 
        factors.append("• Very high transaction amount (>${:,.2f}) - Exceeds normal threshold".format(amount))
    elif amount > 5000: 
        factors.append("• High transaction amount (>${:,.2f}) - Above average transaction size".format(amount))
    elif amount > 1000:
        factors.append("• Moderate transaction amount (>${:,.2f})".format(amount))
    
    # Time-based factors
    time_of_day = transaction_data.get('time', '')
    if "Night" in time_of_day:
        factors.append("• Unusual transaction time (night) - Transactions between 12AM-6AM are statistically higher risk")
    elif "Morning" in time_of_day:
        factors.append("• Standard transaction time (morning) - Normal business hours")
    
    # Device-based factors
    device = transaction_data.get('device', '')
    if device == "ATM" and amount > 1000: 
        factors.append("• Large ATM withdrawal - Exceeds typical ATM transaction limit")
    elif device == "ATM":
        factors.append("• ATM transaction - Standard withdrawal pattern")
    elif device == "Mobile App":
        factors.append("• Mobile transaction - Modern payment method with standard security")
    elif device == "Phone":
        factors.append("• Phone-based transaction - Voice or SMS authentication recommended")
    
    # Location-based factors
    location = transaction_data.get('location', '').lower()
    if 'unknown' in location or not location or location.strip() == '':
        factors.append("• Unknown transaction location - Geographic verification unavailable")
    else:
        factors.append(f"• Transaction location: {transaction_data.get('location')} - Location verified")
    
    # Transaction type factors
    trans_type = transaction_data.get('type', '')
    if trans_type == "Transfer":
        factors.append("• Transfer transaction - Peer-to-peer money movement")
    elif trans_type == "Withdrawal":
        factors.append("• Withdrawal transaction - Cash disbursement detected")
    elif trans_type == "Payment":
        factors.append("• Payment transaction - Merchant transaction identified")
    
    # Recipient analysis
    recipient = transaction_data.get('recipient', '')
    if not recipient or recipient.lower() == 'unknown':
        factors.append("• Unverified recipient - Payee information incomplete")
    else:
        factors.append(f"• Recipient verified: {recipient}")
    
    # ML model confidence factors
    if fraud_score > 0.8: 
        factors.append("• ML model shows very high fraud confidence (>80%) - Multiple risk indicators detected")
    elif fraud_score > 0.6: 
        factors.append("• ML model shows elevated fraud risk (60-80%) - Several warning signs present")
    elif fraud_score > 0.4:
        factors.append("• ML model shows moderate fraud risk (40-60%) - Some concerns identified")
    else:
        factors.append("• ML model shows low fraud risk (<40%) - Transaction pattern appears normal")
    
    # Account behavior (simulated based on amount and type)
    if amount > 5000 and device == "ATM":
        factors.append("• Unusual combination: High-value ATM transaction - Rarely seen in normal behavior")
    
    return factors if factors else ["• No major risk factors identified - Transaction appears within normal parameters"]

# ---------- Tabs ----------
tab1, tab2 = st.tabs(["Check Analysis", "Online Transaction Analysis"])

# ===== CHECK ANALYSIS TAB =====
with tab1:
    st.markdown("### Enhanced Check Analysis with AI", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("") 
        st.markdown("#### Upload Check File")
        uploaded_file = st.file_uploader("Upload File", help="Upload a clear image for processing", label_visibility="visible")
        if uploaded_file is not None:
            try:
                uploaded_file.seek(0)
                image = Image.open(uploaded_file)
            except Exception:
                st.error("Please upload a valid image file.")
                image = None
            if image is not None:
                st.image(image, caption="Uploaded Image", use_container_width=True)
                if st.button("Analyze Check", type="primary"):
                    with st.spinner("Analyzing check for fraud..."):
                        uploaded_file.seek(0)
                        extracted_data, combined_score, raw_data, ml_score, rule_score, ml_ensemble = mindee_ocr_analysis_with_ml(uploaded_file)
                    if extracted_data and combined_score is not None:
                        st.success("Check processed successfully!")
                        st.session_state.Check_results = {
                            'extracted_data': extracted_data,
                            'fraud_score': combined_score,
                            'ml_score': ml_score,
                            'rule_score': rule_score,
                            'raw_data': raw_data,
                            'ml_ensemble': ml_ensemble
                        }
                    else:
                        st.error("Failed to process the Check. Please check your API configuration and try again.")
    with col2:
        if 'Check_results' in st.session_state:
            st.write("") 
            st.markdown("#### Enhanced Analysis Results")
            results = st.session_state.Check_results
            st.markdown("**Extracted Information:**")
            for key, value in results['extracted_data'].items():
                st.text(f"{key}: {value}")
            st.markdown("---")
            fraud_score = results['fraud_score']
            ml_score = results.get('ml_score', 0)
            rule_score = results.get('rule_score', 0)
            risk_level, color = get_risk_level(fraud_score)
            st.markdown("**Enhanced Fraud Analysis:**")
            st.markdown(f"**Risk Level:** :{color}[{risk_level}]")
            st.progress(float(fraud_score))
            
            # Display only the combined score as percentage - LARGER
            fraud_percentage = fraud_score * 100
            st.markdown(f"<h2 style='color: {color}; margin-top: 10px; margin-bottom: 15px;'>Fraud Detection Score: {fraud_percentage:.0f}%</h2>", unsafe_allow_html=True)
            
            st.markdown("**Risk Factors:**")
            raw_data = results.get('raw_data', {})
            for factor in get_check_risk_factors(raw_data, ml_score, rule_score):
                st.text(factor)
            st.markdown("**Recommendations:**")
            if fraud_score >= 0.7:
                st.error("High fraud risk detected. Recommend manual verification and additional authentication.")
            elif fraud_score >= 0.4:
                st.warning("Medium risk. Additional verification suggested before processing.")
            else:
                st.success("Low risk. Transaction appears legitimate and can be processed.")

# ===== ONLINE TRANSACTION TAB =====
with tab2:
    st.markdown("### Online Transaction Analysis", unsafe_allow_html=True)
    
    # Get exact current time (runs in background, not displayed)
    current_time = datetime.now()
    exact_time_display = current_time.strftime("%I:%M:%S %p")
    full_datetime_display = current_time.strftime("%B %d, %Y at %I:%M:%S %p")
    
    # Determine time period for ML model
    current_hour = current_time.hour
    if 6 <= current_hour < 12:
        time_period = "Morning (6AM-12PM)"
    elif 12 <= current_hour < 18:
        time_period = "Afternoon (12PM-6PM)"
    elif 18 <= current_hour < 24:
        time_period = "Evening (6PM-12AM)"
    else:
        time_period = "Night (12AM-6AM)"
    
    # Default location (changeable by user)
    default_location = "Boydton, Virginia, US"
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Transaction Details")
        with st.form("transaction_form"):
            account_number = st.text_input("Account Number", placeholder="Enter account number")
            amount_input = st.text_input("Transaction Amount ($)", placeholder="Enter amount")
            recipient_name = st.text_input("Recipient Name", placeholder="Enter recipient name")
            transaction_type = st.selectbox("Transaction Type", ["Transfer", "Payment", "Withdrawal", "Deposit"])
            merchant = st.text_input("Merchant", placeholder="Enter merchant")
            
            # Auto-populated location with option to change
            location = st.text_input("Transaction Location", value=default_location, placeholder="City, State")
            
            # Auto-populated device
            device_type = st.selectbox("Device Used", 
                                      options=["Web Browser", "Mobile App", "ATM", "Phone"],
                                      index=0)
            
            submitted = st.form_submit_button("Analyze Transaction", type="primary")
            
            # Convert amount input to float
            amount = 0.0
            if amount_input:
                try:
                    amount = float(amount_input)
                except ValueError:
                    st.error("Please enter a valid numeric amount")
                    amount = 0.0
            
            if submitted and account_number and amount > 0:
                # Get fresh timestamp at submission
                transaction_time = datetime.now()
                exact_time_str = transaction_time.strftime("%I:%M:%S %p on %B %d, %Y")
                
                transaction_data = {
                    "account_number": account_number,
                    "amount": amount,
                    "recipient": recipient_name,
                    "type": transaction_type,
                    "merchant": merchant,
                    "location": location,
                    "time": time_period,
                    "exact_time": exact_time_str,
                    "device": device_type
                }
                with st.spinner("Analyzing transaction for fraud patterns..."):
                    result = ml_transaction_analysis(transaction_data)
                if isinstance(result, dict):
                    fraud_score = result['ensemble_probability']
                    st.session_state.transaction_results = {
                        'data': transaction_data,
                        'fraud_score': fraud_score,
                        'ensemble_result': result
                    }
                else:
                    fraud_score = result
                    st.session_state.transaction_results = {
                        'data': transaction_data,
                        'fraud_score': fraud_score,
                        'ensemble_result': None
                    }
    with col2:
        if 'transaction_results' in st.session_state:
            st.subheader("Analysis Results")
            results = st.session_state.transaction_results
            data = results['data']
            fraud_score = results['fraud_score']
            
            st.markdown("**Transaction Summary:**")
            st.text(f"Account: {data['account_number']}")
            st.text(f"Amount: ${data['amount']:,.2f}")
            st.text(f"Type: {data['type']}")
            st.text(f"Recipient: {data['recipient']}")
            st.text(f"Merchant: {data['merchant']}")
            st.text(f"Location: {data['location']}")
            st.text(f"Device: {data['device']}")
            st.text(f"Transaction Time: {data.get('exact_time', 'N/A')}")
            
            st.markdown("---")
            
            # Fraud Analysis Section
            st.markdown("**Fraud Analysis:**")
            risk_level, color = get_risk_level(fraud_score)
            st.markdown(f"**Risk Level:** :{color}[{risk_level}]")
            st.progress(float(fraud_score))
            
            # AI Fraud Detection Score
            st.markdown("---")
            st.markdown("**AI Fraud Detection Score:**")
            fraud_percentage = fraud_score * 100
            st.markdown(f"<h2 style='color: {color};'>{fraud_percentage:.1f}%</h2>", unsafe_allow_html=True)
            
            # Risk Level Banner
            if fraud_score < 0.4:
                st.success("LOW RISK TRANSACTION")
                st.info("Transaction appears legitimate!")
            elif fraud_score < 0.7:
                st.warning("MEDIUM RISK TRANSACTION")
            else:
                st.error("HIGH RISK TRANSACTION")
                st.warning("Manual review required!")
            
            st.markdown("---")
            st.markdown("**Risk Factors:**")
            factors = get_detailed_risk_factors(data, fraud_score)
            for factor in factors:
                st.text(factor)
            
            st.markdown("---")
            st.markdown("**Recommendations:**")
            if fraud_score >= 0.7:
                st.error("BLOCK TRANSACTION - High fraud risk detected. Require additional verification and manual review.")
            elif fraud_score >= 0.4:
                st.warning("REQUEST VERIFICATION - Medium risk. Additional authentication before processing.")
            else:
                st.success("APPROVE TRANSACTION - Low fraud risk")
            
            # Processing Status
            st.markdown("---")
            st.markdown("**Processing Status:**")
            if fraud_score < 0.4:
                st.markdown("- ✅ Transaction approved for processing")
                st.markdown("- ✅ Normal monitoring applies")
                st.markdown("- ✅ Proceed with standard workflow")
            elif fraud_score < 0.7:
                st.markdown("- ⚠️ Transaction requires additional verification")
                st.markdown("- ⚠️ Enhanced monitoring applied")
                st.markdown("- ⚠️ Waiting for authentication")
            else:
                st.markdown("- ❌ Transaction blocked")
                st.markdown("- ❌ Manual review required")
                st.markdown("- ❌ Customer notification sent")

# ---------- Floating "LAUNCH INSIGHTS" ----------
st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)
button_container = st.container()
with button_container:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("LAUNCH INSIGHTS", key="dashboard_btn", type="primary", use_container_width=True):
            st.session_state.navigate_to_dashboard = True
            st.rerun()

st.markdown("""
<style>
/* Target the button more specifically */
[data-testid="stButton"] button[kind="primary"],
button[key="dashboard_btn"],
button[key="dashboard_btn"]:focus,
button[key="dashboard_btn"]:visited,
div[data-testid="stButton"] > button:first-child {
    background: #db123d !important;
    background-color: #db123d !important;
    background-image: none !important;
    color: #fff !important;
    border: 0 !important;
    border-radius: 12px !important;
    padding: 12px 22px !important;
    font-weight: 800 !important;
    font-size: 15px !important;
    text-transform: uppercase !important;
    letter-spacing: .02em !important;
    box-shadow: 0 10px 20px rgba(219,18,61,.45), 0 2px 6px rgba(0,0,0,.18) !important;
    cursor: pointer !important;
    transition: transform .08s ease, box-shadow .15s ease, filter .15s ease !important;
    min-width: 220px !important;
}

[data-testid="stButton"] button[kind="primary"]:hover,
button[key="dashboard_btn"]:hover,
div[data-testid="stButton"] > button:first-child:hover {
    background: #db123d !important;
    background-color: #db123d !important;
    background-image: none !important;
    filter: brightness(1.1) !important;
    box-shadow: 0 14px 28px rgba(219,18,61,.55), 0 3px 8px rgba(0,0,0,.22) !important;
}

[data-testid="stButton"] button[kind="primary"]:active,
button[key="dashboard_btn"]:active,
div[data-testid="stButton"] > button:first-child:active {
    background: #db123d !important;
    background-color: #db123d !important;
    background-image: none !important;
    transform: translateY(1px) scale(0.99) !important;
}

button[key="dashboard_btn"]::before {
    content: "";
    position: absolute;
    inset: -18px -28px;
    background: radial-gradient(ellipse at center, rgba(255,255,255,.55), rgba(255,255,255,0));
    border-radius: 24px;
    filter: blur(2px);
    z-index: -1;
    pointer-events: none;
}

@media (max-width: 640px) {
    button[key="dashboard_btn"] {
        padding: 11px 18px !important;
        font-size: 14px !important;
        min-width: 180px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("""
    <div class='fixed-footer'>
      <span>Where Innovation Meets Security</span>
      <span class="sep">|</span>
      <span>Zero Tolerance for Fraud</span>
      <span class="sep">|</span>
      <span>© Xforia DAD</span>
    </div>
""", unsafe_allow_html=True)