

# # # DASHBOARD.py

# # import streamlit as st
# # import pandas as pd
# # import plotly.express as px
# # import plotly.graph_objects as go
# # from splash_screen import show_splash
# # import os
# # import pathlib
# # from geopy.geocoders import Nominatim
# # from top_usa_cities_f import load_usa_cities_coordinates
# # import time
# # import base64

# # try:
# #     from streamlit_plotly_events import plotly_events
# #     PLOTLY_EVENTS_AVAILABLE = True
# # except ImportError:
# #     PLOTLY_EVENTS_AVAILABLE = False
# #     st.warning("For full interactivity, install: pip install streamlit-plotly-events")

# # # Enhanced color scheme matching your theme
# # COLORS = {
# #     'primary': '#667eea',
# #     'secondary': '#764ba2',
# #     'accent': '#1e3c72',
# #     'success': '#10b981',
# #     'warning': '#f59e0b',
# #     'danger': '#ef4444',
# #     'legitimate': '#10b981',
# #     'fraud': '#ef4444',
# #     'male': '#3b82f6',
# #     'female': '#ec4899',
# #     'gradient_start': '#667eea',
# #     'gradient_end': '#764ba2'
# # }

# # def add_fixed_logo():
# #     """Add fixed logo to the dashboard with robust path finding"""
# #     cwd = pathlib.Path(os.getcwd())
# #     here = pathlib.Path(__file__).parent if "__file__" in globals() else cwd
    
# #     # Search for logo in multiple locations
# #     candidates = [
# #         cwd / "FDN.png",
# #         here / "FDN.png",
# #         here / "assets" / "FDN.png",
# #         cwd / "assets" / "FDN.png"
# #     ]
    
# #     logo_path = next((p for p in candidates if p.exists()), None)
    
# #     if not logo_path:
# #         st.warning("Logo file 'FDN.png' not found in any expected location.")
# #         return
    
# #     encoded = base64.b64encode(logo_path.read_bytes()).decode()
    
# #     st.markdown(f"""
# #         <style>
# #         .fixed-logo {{
# #             position: fixed;
# #             top: 12px;
# #             left: 60px;
# #             z-index: 2147482000;
# #             background: rgba(255,255,255,0.95);
# #             border-radius: 6px;
# #             padding: 4px 6px;
# #         }}
# #         .fixed-logo img {{
# #             width: 150px;
# #             height: 50px;
# #             display: block;
# #             cursor: pointer;
# #         }}
# #         @media (max-width: 768px) {{
# #             .fixed-logo {{
# #                 left: 56px;
# #                 top: 10px;
# #             }}
# #         }}
# #         </style>
# #         <div class="fixed-logo">
# #             <a href="/" target="_self">
# #                 <img src="data:image/png;base64,{encoded}" alt="FDN Logo" />
# #             </a>
# #         </div>
# #     """, unsafe_allow_html=True)

# # # Call the logo function
# # add_fixed_logo()

# # # Enhanced global styling
# # st.markdown("""
# #     <style>
# #     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
# #     * {
# #         font-family: 'Inter', sans-serif;
# #     }
    
# #     .main-content {
# #         padding-bottom: 100px;
# #     }
    
# #     .fixed-footer {
# #         position: fixed;
# #         bottom: 0;
# #         left: 0;
# #         right: 0;
# #         background: linear-gradient(135deg, #b91c1c 0%, #dc2626 100%);
# #         color: black;
# #         text-align: center;
# #         padding: 20px;
# #         z-index: 1000;
# #         box-shadow: 0 -4px 20px rgba(185, 28, 28, 0.4);
# #         font-size: 0.95em;
# #         font-weight: 500;
# #         letter-spacing: 0.5px;
# #     }
    
# #     .metric-card {
# #         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
# #         color: white;
# #         padding: 20px;
# #         border-radius: 12px;
# #         box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
# #         transition: all 0.3s ease;
# #         text-align: center;
# #     }
    
# #     .metric-card:hover {
# #         transform: translateY(-5px);
# #         box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
# #     }
    
# #     .stButton>button {
# #         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
# #         color: white;
# #         border: none;
# #         border-radius: 8px;
# #         padding: 12px 24px;
# #         font-weight: 600;
# #         transition: all 0.3s ease;
# #         box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
# #     }
    
# #     .stButton>button:hover {
# #         transform: translateY(-2px);
# #         box-shadow: 0 4px 15px rgba(102, 126, 234, 0.5);
# #     }
    
# #     .section-header {
# #         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
# #         -webkit-background-clip: text;
# #         -webkit-text-fill-color: transparent;
# #         font-size: 1.8em;
# #         font-weight: 700;
# #         margin: 20px 0;
# #     }
    
# #     div[data-testid="stExpander"] {
# #         background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
# #         border-radius: 10px;
# #         border: 1px solid rgba(102, 126, 234, 0.2);
# #     }
    
# #     /* Chart container hover effect */
# #     div[data-testid="stPlotlyChart"] {
# #         cursor: pointer;
# #         transition: all 0.3s ease;
# #     }
    
# #     div[data-testid="stPlotlyChart"]:hover {
# #         transform: scale(1.01);
# #         box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
# #     }
# #     </style>
# # """, unsafe_allow_html=True)

# # CSV_FILE = r"C:\Users\bhanukaranP\Desktop\DOC_AN_DET\Dataset_F_2.csv"

# # @st.cache_data
# # def get_city_coordinates(cities):
# #     geolocator = Nominatim(user_agent="fraud_dashboard")
# #     coordinates = {}
    
# #     for city in cities:
# #         try:
# #             location = geolocator.geocode(f"{city}, USA")
# #             if location:
# #                 coordinates[city] = {
# #                     'lat': location.latitude,
# #                     'lon': location.longitude
# #                 }
# #             time.sleep(0.1)
# #         except:
# #             continue
    
# #     return coordinates

# # def load_csv_data():
# #     try:
# #         if os.path.exists(CSV_FILE):
# #             df = pd.read_csv(CSV_FILE)
# #             df['DateTime'] = pd.to_datetime(df['DateTime'])
# #             df['Month-Year'] = df['DateTime'].dt.to_period('M').astype(str)
# #             return df
# #         else:
# #             st.warning(f"CSV file '{CSV_FILE}' not found.")
# #             return pd.DataFrame()
# #     except Exception as e:
# #         st.error(f"Error loading CSV: {str(e)}")
# #         return pd.DataFrame()

# # # Enhanced pie chart function
# # def create_modern_pie(values, names, title, color_map=None):
# #     fig = go.Figure(data=[go.Pie(
# #         labels=names,
# #         values=values,
# #         hole=0.4,
# #         marker=dict(
# #             colors=[color_map.get(n, COLORS['primary']) for n in names] if color_map else None,
# #             line=dict(color='white', width=2)
# #         ),
# #         textposition='auto',
# #         textinfo='percent+label',
# #         textfont=dict(size=11, color='white', family='Inter'),
# #         hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>'
# #     )])
    
# #     fig.update_layout(
# #         title=dict(text=title, font=dict(size=14, color='#1e3c72', family='Inter', weight=600)),
# #         showlegend=True,
# #         height=320,
# #         margin=dict(t=30, b=0, l=0, r=0),
# #         legend=dict(
# #             orientation="v",
# #             yanchor="middle",
# #             y=0.5,
# #             xanchor="left",
# #             x=1.02,
# #             font=dict(size=10, family='Inter')
# #         ),
# #         paper_bgcolor='rgba(0,0,0,0)',
# #         plot_bgcolor='rgba(0,0,0,0)',
# #         hovermode='closest'
# #     )
    
# #     return fig

# # # Enhanced bar chart function
# # def create_modern_bar(data, x, y, title, orientation='h', color=COLORS['primary']):
# #     fig = go.Figure(data=[go.Bar(
# #         x=data[x] if orientation == 'h' else data.index,
# #         y=data[y] if orientation == 'h' else data.values,
# #         orientation=orientation,
# #         marker=dict(
# #             color=color,
# #             line=dict(color='rgba(102, 126, 234, 0.8)', width=1.5),
# #             gradient=dict(
# #                 type='linear',
# #                 color=[COLORS['gradient_start'], COLORS['gradient_end']]
# #             )
# #         ),
# #         hovertemplate='<b>%{y if orientation == "h" else x}</b><br>Count: %{x if orientation == "h" else y}<extra></extra>',
# #         text=data[x] if orientation == 'h' else data.values,
# #         textposition='auto',
# #         textfont=dict(color='white', size=10, family='Inter', weight='bold')
# #     )])
    
# #     fig.update_layout(
# #         title=dict(text=title, font=dict(size=14, color='#1e3c72', family='Inter', weight=600)),
# #         xaxis_title=x if orientation == 'h' else '',
# #         yaxis_title=y if orientation == 'h' else '',
# #         height=320,
# #         margin=dict(t=30, b=30, l=60, r=20),
# #         paper_bgcolor='rgba(0,0,0,0)',
# #         plot_bgcolor='rgba(0,0,0,0)',
# #         xaxis=dict(gridcolor='rgba(102, 126, 234, 0.1)', showgrid=True, fixedrange=False),
# #         yaxis=dict(gridcolor='rgba(102, 126, 234, 0.1)', showgrid=True, categoryorder='total ascending' if orientation == 'h' else None, fixedrange=False),
# #         dragmode='pan',
# #         hovermode='closest'
# #     )
    
# #     return fig

# # # Plot configuration for better interactivity
# # def get_plot_config():
# #     return {
# #         'displayModeBar': True,
# #         'displaylogo': False,
# #         'scrollZoom': True,
# #         'modeBarButtonsToRemove': ['select2d', 'lasso2d', 'autoScale2d'],
# #         'toImageButtonOptions': {
# #             'format': 'png',
# #             'filename': 'fraud_analysis_chart',
# #             'height': 1080,
# #             'width': 1920,
# #             'scale': 2
# #         }
# #     }

# # # Session state initialization
# # for key in ['selected_detail', 'show_customer_details', 'show_transaction_details',
# #             'show_male_details', 'show_female_details', 'show_transfer_details',
# #             'show_legitimate_details', 'show_fraud_details',
# #             'show_2024_details', 'show_2025_details', 'show_debit_details', 'show_credit_details']:
# #     if key not in st.session_state:
# #         st.session_state[key] = False

# # # Toggle functions
# # def toggle_debit():
# #     st.session_state.show_debit_details = not st.session_state.show_debit_details

# # def toggle_credit():
# #     st.session_state.show_credit_details = not st.session_state.show_credit_details

# # def toggle_transfer():
# #     st.session_state.show_transfer_details = not st.session_state.show_transfer_details

# # def toggle_male():
# #     st.session_state.show_male_details = not st.session_state.show_male_details

# # def toggle_female():
# #     st.session_state.show_female_details = not st.session_state.show_female_details

# # def toggle_2024():
# #     st.session_state.show_2024_details = not st.session_state.show_2024_details

# # def toggle_2025():
# #     st.session_state.show_2025_details = not st.session_state.show_2025_details

# # def toggle_legitimate():
# #     st.session_state.show_legitimate_details = not st.session_state.show_legitimate_details

# # def toggle_fraud():
# #     st.session_state.show_fraud_details = not st.session_state.show_fraud_details

# # if st.session_state.show_splash:
# #     show_splash()
# #     st.stop()

# # st.sidebar.markdown("---")
# # if st.sidebar.button("Home Page"):
# #     st.session_state.show_splash = True
# #     st.rerun()

# # st.title("AI Anomaly Detection Dashboard")

# # df = load_csv_data()

# # if not df.empty:
# #     st.sidebar.header("Filters")
    
# #     available_months = sorted(df['Month-Year'].unique())
# #     if 'month_multiselect' not in st.session_state:
# #         st.session_state.month_multiselect = available_months
    
# #     def select_all_months():
# #         st.session_state.month_multiselect = available_months
    
# #     def clear_all_months():
# #         st.session_state.month_multiselect = []
    
# #     col1, col2 = st.sidebar.columns(2)
# #     with col1:
# #         st.button("Select All", key="select_all", on_click=select_all_months)
# #     with col2:
# #         st.button("Clear All", key="clear_all", on_click=clear_all_months)
    
# #     selected_months = st.sidebar.multiselect(
# #         "Month-Year",
# #         options=available_months,
# #         key="month_multiselect",
# #         help="Select one or more months to analyze"
# #     )
    
# #     st.sidebar.markdown("---")
# #     st.sidebar.subheader("Interactive Analysis")
    
# #     analysis_type = st.sidebar.selectbox(
# #         "Choose Analysis Mode:",
# #         ["Overview", "Customer Deep Dive", "Geographic Analysis", "Temporal Analysis", "Fraud Pattern Analysis"]
# #     )
    
# #     if selected_months:
# #         filtered_df = df[df['Month-Year'].isin(selected_months)]
# #         fraud_df = filtered_df[filtered_df['Legitimate'] == 0]
        
# #         st.markdown("<h2 class='section-header'>Dashboard Metrics</h2>", unsafe_allow_html=True)
# #         col1, col2, col3, col4 = st.columns(4)
        
# #         with col1:
# #             total_users = filtered_df['CustomerID'].nunique()
# #             if st.button(f"Customers: {total_users:,}", key="customers_btn", help="Click for customer details"):
# #                 st.session_state.show_customer_details = not st.session_state.show_customer_details

# #         with col2:
# #             total_transactions = len(filtered_df)
# #             if st.button(f"Transactions: {total_transactions:,}", key="trans_btn", help="Click for transaction timeline"):
# #                 st.session_state.show_transaction_details = not st.session_state.show_transaction_details
        
# #         with col3:
# #             legit_count = filtered_df['Legitimate'].sum()
# #             st.metric(label="Legitimate", value=legit_count, help="Number of legitimate transactions")
        
# #         with col4:
# #             fraud_count = len(fraud_df)
# #             st.metric(label="Fraud Detected", value=fraud_count, help="Number of fraudulent transactions")
        
# #         if st.session_state.show_customer_details:
# #             with st.expander("Customer Analysis Details", expanded=True):
# #                 customer_stats = filtered_df.groupby('CustomerID').agg({
# #                     'Amount': ['count', 'sum', 'mean'],
# #                     'Legitimate': lambda x: (x == 0).sum(),
# #                     'TransactionLocationCity': 'nunique'
# #                 }).round(2)
# #                 customer_stats.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Fraud_Count', 'Cities']
# #                 customer_stats['Fraud_Rate'] = (customer_stats['Fraud_Count'] / customer_stats['Transactions'] * 100).round(1)
# #                 customer_stats = customer_stats.sort_values('Total_Amount', ascending=False).head(20)
                
# #                 st.write("**Top 20 Customers by Transaction Volume:**")
# #                 st.dataframe(customer_stats, use_container_width=True)
                
# #                 col1, col2, col3 = st.columns(3)
# #                 with col1:
# #                     st.metric("Highest Spender", f"${customer_stats['Total_Amount'].max():,.2f}")
# #                 with col2:
# #                     st.metric("Most Active", f"{customer_stats['Transactions'].max()} transactions")
# #                 with col3:
# #                     avg_fraud_rate = customer_stats['Fraud_Rate'].mean()
# #                     st.metric("Avg Fraud Rate", f"{avg_fraud_rate:.1f}%")

# #         if st.session_state.show_transaction_details:
# #             with st.expander("Transaction Timeline Analysis", expanded=True):
# #                 daily_stats = filtered_df.groupby(filtered_df['DateTime'].dt.date).agg({
# #                     'Amount': ['count', 'sum'],
# #                     'Legitimate': lambda x: (x == 0).sum()
# #                 }).round(2)
# #                 daily_stats.columns = ['Transaction_Count', 'Total_Amount', 'Fraud_Count']
# #                 daily_stats['Fraud_Rate'] = (daily_stats['Fraud_Count'] / daily_stats['Transaction_Count'] * 100).round(1)
                
# #                 col1, col2 = st.columns(2)
# #                 with col1:
# #                     fig = go.Figure()
# #                     fig.add_trace(go.Scatter(
# #                         x=daily_stats.index,
# #                         y=daily_stats['Transaction_Count'],
# #                         mode='lines+markers',
# #                         name='Transactions',
# #                         line=dict(color=COLORS['primary'], width=3),
# #                         marker=dict(size=6, color=COLORS['secondary']),
# #                         fill='tozeroy',
# #                         fillcolor='rgba(102, 126, 234, 0.2)'
# #                     ))
# #                     fig.update_layout(
# #                         title="Daily Transaction Volume",
# #                         height=250,
# #                         margin=dict(t=30, b=20, l=20, r=20),
# #                         paper_bgcolor='rgba(0,0,0,0)',
# #                         plot_bgcolor='rgba(0,0,0,0)',
# #                         dragmode='zoom',
# #                         title_font=dict(size=13)
# #                     )
# #                     st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
                
# #                 with col2:
# #                     fig = go.Figure()
# #                     fig.add_trace(go.Scatter(
# #                         x=daily_stats.index,
# #                         y=daily_stats['Fraud_Rate'],
# #                         mode='lines+markers',
# #                         name='Fraud Rate',
# #                         line=dict(color=COLORS['danger'], width=3),
# #                         marker=dict(size=6, color='#dc2626'),
# #                         fill='tozeroy',
# #                         fillcolor='rgba(239, 68, 68, 0.2)'
# #                     ))
# #                     fig.update_layout(
# #                         title="Daily Fraud Rate (%)",
# #                         height=250,
# #                         margin=dict(t=30, b=20, l=20, r=20),
# #                         paper_bgcolor='rgba(0,0,0,0)',
# #                         plot_bgcolor='rgba(0,0,0,0)',
# #                         dragmode='zoom',
# #                         title_font=dict(size=13)
# #                     )
# #                     st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
        
# #         st.markdown("---")

# #         col1, col2 = st.columns(2)
        
# #         with col1:
# #             st.subheader("Count by Transaction Type")
# #             status_counts = filtered_df['Legitimate'].value_counts()
# #             status_labels = ['Fraud', 'Legitimate']
            
# #             color_map = {'Legitimate': COLORS['legitimate'], 'Fraud': COLORS['fraud']}
# #             fig1 = create_modern_pie(
# #                 [status_counts.get(0, 0), status_counts.get(1, 0)],
# #                 status_labels,
# #                 "",
# #                 color_map
# #             )
# #             st.plotly_chart(fig1, use_container_width=True, config=get_plot_config())

# #             col_i, col_j = st.columns(2)
# #             with col_i:
# #                 legitimate_count = status_counts.get(1, 0)
# #                 if legitimate_count > 0:
# #                     if st.button(f"Legitimate ({legitimate_count})", key='legitimate_btn', on_click=toggle_legitimate):
# #                         pass

# #             with col_j:
# #                 fraud_count = status_counts.get(0, 0)
# #                 if fraud_count > 0:
# #                     if st.button(f"Fraud ({fraud_count})", key='fraud_btn', on_click=toggle_fraud):
# #                         pass

# #             if st.session_state.show_legitimate_details:
# #                 with st.expander("Top 5 Legitimate Transaction Customers", expanded=True):
# #                     legitimate_df = filtered_df[filtered_df['Legitimate'] == 1]
# #                     if not legitimate_df.empty:
# #                         top5_legitimate = legitimate_df.groupby('CustomerID').agg({
# #                             'Amount': ['count', 'sum', 'mean'],
# #                             'TransactionLocationCity': 'nunique'
# #                         }).round(2)
# #                         top5_legitimate.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Cities']
# #                         top5_legitimate = top5_legitimate.sort_values('Total_Amount', ascending=False).head(5)
# #                         st.dataframe(top5_legitimate, use_container_width=True)

# #             if st.session_state.show_fraud_details:
# #                 with st.expander("Top 5 Fraud Transaction Customers", expanded=True):
# #                     fraud_only_df = filtered_df[filtered_df['Legitimate'] == 0]
# #                     if not fraud_only_df.empty:
# #                         top5_fraud = fraud_only_df.groupby('CustomerID').agg({
# #                             'Amount': ['count', 'sum', 'mean'],
# #                             'TransactionLocationCity': 'nunique'
# #                         }).round(2)
# #                         top5_fraud.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Cities']
# #                         top5_fraud = top5_fraud.sort_values('Total_Amount', ascending=False).head(5)
# #                         st.dataframe(top5_fraud, use_container_width=True)
            
# #             st.subheader("Fraud Transaction by Gender")
# #             if not fraud_df.empty:
# #                 fraud_by_gender = fraud_df['Gender'].value_counts()
# #                 if not fraud_by_gender.empty:
# #                     # Create horizontal bar chart
# #                     total_gender = fraud_by_gender.sum()
# #                     percentages = (fraud_by_gender / total_gender * 100).round(1)
                    
# #                     fig3 = go.Figure()
# #                     colors_list = [COLORS['male'] if g == 'Male' else COLORS['female'] for g in fraud_by_gender.index]
                    
# #                     fig3.add_trace(go.Bar(
# #                         y=fraud_by_gender.index,
# #                         x=fraud_by_gender.values,
# #                         orientation='h',
# #                         marker=dict(
# #                             color=colors_list,
# #                             line=dict(color='white', width=2)
# #                         ),
# #                         text=[f"{count} ({percentages[gender]}%)" for gender, count in fraud_by_gender.items()],
# #                         textposition='inside',
# #                         textfont=dict(color='white', size=13, family='Inter', weight='bold'),
# #                         hovertemplate='<b>%{y}</b><br>Count: %{x}<br>Percentage: %{customdata}%<extra></extra>',
# #                         customdata=percentages.values,
# #                         showlegend=False
# #                     ))
                    
# #                     fig3.update_layout(
# #                         height=280,
# #                         margin=dict(t=20, b=30, l=80, r=20),
# #                         paper_bgcolor='rgba(0,0,0,0)',
# #                         plot_bgcolor='rgba(0,0,0,0)',
# #                         xaxis=dict(
# #                             title=dict(text="Number of Fraud Transactions", font=dict(size=11)),
# #                             gridcolor='rgba(102, 126, 234, 0.1)',
# #                             showgrid=True,
# #                             fixedrange=False
# #                         ),
# #                         yaxis=dict(
# #                             title="",
# #                             gridcolor='rgba(102, 126, 234, 0.1)',
# #                             showgrid=False,
# #                             fixedrange=False
# #                         ),
# #                         dragmode='pan',
# #                         hovermode='closest'
# #                     )
# #                     st.plotly_chart(fig3, use_container_width=True, config=get_plot_config())
                    
# #                     cola, colb = st.columns(2)
# #                     with cola:
# #                         if 'Male' in fraud_by_gender.index:
# #                             if st.button(f"Male Details ({fraud_by_gender['Male']})", key='male_btn', on_click=toggle_male):
# #                                 pass
# #                     with colb:
# #                         if 'Female' in fraud_by_gender.index:
# #                             if st.button(f"Female Details ({fraud_by_gender['Female']})", key='female_btn', on_click=toggle_female):
# #                                 pass
                    
# #                     if st.session_state.show_male_details and 'Male' in fraud_by_gender.index:
# #                         with st.expander("Top 5 Male Fraud Customers", expanded=True):
# #                             male_df = fraud_df[fraud_df['Gender'] == 'Male']
# #                             if not male_df.empty:
# #                                 top5_male = male_df.groupby('CustomerID').agg({
# #                                     'Amount': ['count', 'sum', 'mean'],
# #                                     'TransactionLocationCity': 'nunique'
# #                                 }).round(2)
# #                                 top5_male.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Cities']
# #                                 top5_male = top5_male.sort_values('Total_Amount', ascending=False).head(5)
# #                                 st.dataframe(top5_male, use_container_width=True)
            
# #                     if st.session_state.show_female_details and 'Female' in fraud_by_gender.index:
# #                         with st.expander("Top 5 Female Fraud Customers", expanded=True):
# #                             female_df = fraud_df[fraud_df['Gender'] == 'Female']
# #                             if not female_df.empty:
# #                                 top5_female = female_df.groupby('CustomerID').agg({
# #                                     'Amount': ['count', 'sum', 'mean'],
# #                                     'TransactionLocationCity': 'nunique'
# #                                 }).round(2)
# #                                 top5_female.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Cities']
# #                                 top5_female = top5_female.sort_values('Total_Amount', ascending=False).head(5)
# #                                 st.dataframe(top5_female, use_container_width=True)

# #         with col2:
# #             st.subheader("Fraud Transaction by Year")
# #             if not fraud_df.empty:
# #                 fraud_by_year = fraud_df['DateTime'].dt.year.value_counts()
# #                 # Filter out 2023
# #                 fraud_by_year = fraud_by_year[fraud_by_year.index != 2023]
                
# #                 if not fraud_by_year.empty:
# #                     fig2 = create_modern_pie(
# #                         fraud_by_year.values,
# #                         fraud_by_year.index,
# #                         ""
# #                     )
# #                     st.plotly_chart(fig2, use_container_width=True, config=get_plot_config())
            
# #                     col_g, col_h = st.columns(2)
# #                     with col_g:
# #                         if 2024 in fraud_by_year.index:
# #                             if st.button(f"2024 ({fraud_by_year[2024]})", key='year_2024_btn', on_click=toggle_2024):
# #                                 pass
# #                     with col_h:
# #                         if 2025 in fraud_by_year.index:
# #                             if st.button(f"2025 ({fraud_by_year[2025]})", key='year_2025_btn', on_click=toggle_2025):
# #                                 pass
                    
# #                     # Year details sections
# #                     for year, state_key in [(2024, 'show_2024_details'), (2025, 'show_2025_details')]:
# #                         if st.session_state[state_key] and year in fraud_by_year.index:
# #                             with st.expander(f"Top 5 Fraud Customers from {year}", expanded=True):
# #                                 year_df = fraud_df[fraud_df['DateTime'].dt.year == year]
# #                                 if not year_df.empty:
# #                                     top5_year = year_df.groupby('CustomerID').agg({
# #                                         'Amount': ['count', 'sum', 'mean'],
# #                                         'TransactionLocationCity': 'nunique'
# #                                     }).round(2)
# #                                     top5_year.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Cities']
# #                                     top5_year = top5_year.sort_values('Total_Amount', ascending=False).head(5)
# #                                     st.dataframe(top5_year, use_container_width=True)

# #             st.subheader("Fraud Transaction by Type")
# #             if not fraud_df.empty:
# #                 fraud_by_type = fraud_df['Type'].value_counts()
# #                 if not fraud_by_type.empty:
# #                     # Create horizontal bar chart
# #                     total_type = fraud_by_type.sum()
# #                     percentages = (fraud_by_type / total_type * 100).round(1)
                    
# #                     # Define colors for each type
# #                     color_mapping = {
# #                         'Debit': '#0066cc',
# #                         'Credit': '#4dabf7',
# #                         'Transfer': '#e74c3c'
# #                     }
# #                     colors_list = [color_mapping.get(t, COLORS['primary']) for t in fraud_by_type.index]
                    
# #                     fig4 = go.Figure()
# #                     fig4.add_trace(go.Bar(
# #                         y=fraud_by_type.index,
# #                         x=fraud_by_type.values,
# #                         orientation='h',
# #                         marker=dict(
# #                             color=colors_list,
# #                             line=dict(color='white', width=2)
# #                         ),
# #                         text=[f"{count} ({percentages[t_type]}%)" for t_type, count in fraud_by_type.items()],
# #                         textposition='inside',
# #                         textfont=dict(color='white', size=13, family='Inter', weight='bold'),
# #                         hovertemplate='<b>%{y}</b><br>Count: %{x}<br>Percentage: %{customdata}%<extra></extra>',
# #                         customdata=percentages.values,
# #                         showlegend=False
# #                     ))
                    
# #                     fig4.update_layout(
# #                         height=280,
# #                         margin=dict(t=20, b=30, l=80, r=20),
# #                         paper_bgcolor='rgba(0,0,0,0)',
# #                         plot_bgcolor='rgba(0,0,0,0)',
# #                         xaxis=dict(
# #                             title=dict(text="Number of Fraud Transactions", font=dict(size=11)),
# #                             gridcolor='rgba(102, 126, 234, 0.1)',
# #                             showgrid=True,
# #                             fixedrange=False
# #                         ),
# #                         yaxis=dict(
# #                             title="",
# #                             gridcolor='rgba(102, 126, 234, 0.1)',
# #                             showgrid=False,
# #                             fixedrange=False,
# #                             categoryorder='total ascending'
# #                         ),
# #                         dragmode='pan',
# #                         hovermode='closest'
# #                     )
# #                     st.plotly_chart(fig4, use_container_width=True, config=get_plot_config())
                    
# #                     col_c, col_d, col_e = st.columns(3)
# #                     with col_c:
# #                         if 'Debit' in fraud_by_type.index:
# #                             if st.button(f"Debit ({fraud_by_type['Debit']})", key='debit_btn', on_click=toggle_debit):
# #                                 pass
# #                     with col_d:
# #                         if 'Credit' in fraud_by_type.index:
# #                             if st.button(f"Credit ({fraud_by_type['Credit']})", key='credit_btn', on_click=toggle_credit):
# #                                 pass
# #                     with col_e:
# #                         if 'Transfer' in fraud_by_type.index:
# #                             if st.button(f"Transfer ({fraud_by_type['Transfer']})", key='transfer_btn', on_click=toggle_transfer):
# #                                 pass
                    
# #                     # Type details sections
# #                     for trans_type, state_key in [('Debit', 'show_debit_details'), ('Credit', 'show_credit_details'), ('Transfer', 'show_transfer_details')]:
# #                         if st.session_state[state_key] and trans_type in fraud_by_type.index:
# #                             with st.expander(f"Top 5 {trans_type} Fraud Customers", expanded=True):
# #                                 type_df = fraud_df[fraud_df['Type'] == trans_type]
# #                                 if not type_df.empty:
# #                                     top5_type = type_df.groupby('CustomerID').agg({
# #                                         'Amount': ['count', 'sum', 'mean'],
# #                                         'TransactionLocationCity': 'nunique'
# #                                     }).round(2)
# #                                     top5_type.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Cities']
# #                                     top5_type = top5_type.sort_values('Total_Amount', ascending=False).head(5)
# #                                     st.dataframe(top5_type, use_container_width=True)

# #         col1, col2 = st.columns(2)

# #         with col1:
# #             st.subheader("Fraud Transactions by Cities")
# #             if not fraud_df.empty:
# #                 usa_cities = load_usa_cities_coordinates()
# #                 city_counts = fraud_df['TransactionLocationCity'].value_counts()
# #                 map_data = []
# #                 for city, count in city_counts.items():
# #                     if city in usa_cities:
# #                         lat, lon = usa_cities[city]
# #                         map_data.append({'City': city, 'Count': count, 'lat': lat, 'lon': lon})
                
# #                 if map_data:
# #                     df_map = pd.DataFrame(map_data)
# #                     fig5 = px.scatter_mapbox(
# #                         df_map,
# #                         lat='lat',
# #                         lon='lon',
# #                         size='Count',
# #                         color='Count',
# #                         hover_name='City',
# #                         hover_data={'Count': True, 'lat': False, 'lon': False},
# #                         color_continuous_scale=[[0, '#fee2e2'], [0.5, '#fca5a5'], [1, '#ef4444']],
# #                         size_max=25,
# #                         zoom=2.2,
# #                         center={'lat': 39.5, 'lon': -98.35},
# #                         mapbox_style='open-street-map'
# #                     )
# #                     fig5.update_layout(
# #                         height=320,
# #                         margin={"r":0,"t":0,"l":0,"b":0},
# #                         coloraxis_colorbar=dict(
# #                             title=dict(text="Fraud Count", font=dict(size=11)),
# #                             thicknessmode="pixels",
# #                             thickness=12,
# #                             lenmode="pixels",
# #                             len=150
# #                         ),
# #                         dragmode='zoom'
# #                     )
# #                     st.plotly_chart(fig5, use_container_width=True, config=get_plot_config())
                    
# #                     top_5_cities = city_counts.head(5)
# #                     st.write("**Top 5 Cities by Fraud Count:**")
# #                     for i, (city, count) in enumerate(top_5_cities.items(), 1):
# #                         st.write(f"{i}. {city}: {count:,}")
        
# #         with col2:
# #             st.subheader("Count by Fraud Reason")
# #             if not fraud_df.empty:
# #                 fraud_reasons = fraud_df['FraudReason'].value_counts().head(10)
# #                 if not fraud_reasons.empty:
# #                     fraud_df_plot = pd.DataFrame({
# #                         'FraudReason': fraud_reasons.index,
# #                         'Count': fraud_reasons.values
# #                     })
# #                     fraud_df_plot['ShortReason'] = fraud_df_plot['FraudReason'].apply(
# #                         lambda x: x if len(x) <= 25 else x[:22] + '...'
# #                     )
                    
# #                     fig6 = go.Figure(data=[go.Bar(
# #                         x=fraud_df_plot['Count'],
# #                         y=fraud_df_plot['ShortReason'],
# #                         orientation='h',
# #                         marker=dict(
# #                             color=fraud_df_plot['Count'],
# #                             colorscale=[[0, COLORS['gradient_start']], [1, COLORS['gradient_end']]],
# #                             line=dict(color='rgba(102, 126, 234, 0.8)', width=1.5)
# #                         ),
# #                         text=fraud_df_plot['Count'],
# #                         textposition='auto',
# #                         textfont=dict(color='white', size=11, family='Inter', weight='bold'),
# #                         hovertext=fraud_df_plot['FraudReason'],
# #                         hovertemplate='<b>%{hovertext}</b><br>Count: %{x}<extra></extra>'
# #                     )])
                    
# #                     fig6.update_layout(
# #                         xaxis_title="Count (Log Scale)",
# #                         yaxis_title="Fraud Reason",
# #                         height=320,
# #                         margin=dict(t=20, b=30, l=140, r=20),
# #                         yaxis={'categoryorder': 'total ascending'},
# #                         xaxis_type='log',
# #                         paper_bgcolor='rgba(0,0,0,0)',
# #                         plot_bgcolor='rgba(0,0,0,0)',
# #                         xaxis=dict(
# #                             title=dict(text="Count (Log Scale)", font=dict(size=11)),
# #                             gridcolor='rgba(102, 126, 234, 0.1)',
# #                             showgrid=True,
# #                             type='log'
# #                         ),
# #                         yaxis_tickfont=dict(size=9, family='Inter'),
# #                         dragmode='zoom'
# #                     )
# #                     st.plotly_chart(fig6, use_container_width=True, config=get_plot_config())
               
# #         if analysis_type != "Overview":
# #             st.markdown("---")
            
# #         if analysis_type == "Customer Deep Dive":
# #             st.markdown("<h2 class='section-header'>Customer Deep Dive Analysis</h2>", unsafe_allow_html=True)
# #             top_customers = filtered_df.groupby('CustomerID')['Amount'].sum().sort_values(ascending=False).head(50)
# #             selected_customer = st.selectbox("Select Customer ID for Analysis:", [""] + list(top_customers.index))
            
# #             if selected_customer:
# #                 customer_data = filtered_df[filtered_df['CustomerID'] == selected_customer]
# #                 col1, col2, col3, col4 = st.columns(4)
# #                 with col1:
# #                     st.metric("Total Transactions", len(customer_data))
# #                 with col2:
# #                     st.metric("Total Amount", f"${customer_data['Amount'].sum():.2f}")
# #                 with col3:
# #                     fraud_rate = (1 - customer_data['Legitimate'].mean()) * 100
# #                     st.metric("Fraud Rate", f"{fraud_rate:.1f}%")
# #                 with col4:
# #                     st.metric("Unique Cities", customer_data['TransactionLocationCity'].nunique())
               
# #                 col1, col2 = st.columns(2)
# #                 with col1:
# #                     timeline = customer_data.set_index('DateTime').resample('D')['Amount'].sum()
# #                     fig = go.Figure()
# #                     fig.add_trace(go.Scatter(
# #                         x=timeline.index,
# #                         y=timeline.values,
# #                         mode='lines+markers',
# #                         line=dict(color=COLORS['primary'], width=2),
# #                         fill='tozeroy',
# #                         fillcolor='rgba(102, 126, 234, 0.2)'
# #                     ))
# #                     fig.update_layout(
# #                         title="Transaction Timeline",
# #                         height=250,
# #                         paper_bgcolor='rgba(0,0,0,0)',
# #                         plot_bgcolor='rgba(0,0,0,0)',
# #                         dragmode='zoom',
# #                         title_font=dict(size=13),
# #                         margin=dict(t=30, b=20, l=40, r=20)
# #                     )
# #                     st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
                
# #                 with col2:
# #                     type_dist = customer_data['Type'].value_counts()
# #                     fig = create_modern_pie(type_dist.values, type_dist.index, "Transaction Types")
# #                     st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
                
# #                 st.write("**All Transactions:**")
# #                 display_data = customer_data[['DateTime', 'Type', 'Amount', 'TransactionLocationCity', 'Legitimate', 'FraudReason']].copy()
# #                 display_data['Status'] = display_data['Legitimate'].map({1: 'Legitimate', 0: 'Fraud'})
# #                 st.dataframe(display_data.drop('Legitimate', axis=1), use_container_width=True)
        
# #         elif analysis_type == "Geographic Analysis":
# #             st.markdown("<h2 class='section-header'>Geographic Analysis</h2>", unsafe_allow_html=True)
            
# #             if 'State' in fraud_df.columns:
# #                 state_analysis = fraud_df.groupby('State').agg({
# #                     'Amount': ['count', 'sum', 'mean'],
# #                     'CustomerID': 'nunique'
# #                 }).round(2)
# #                 state_analysis.columns = ['Fraud_Cases', 'Total_Amount', 'Avg_Amount', 'Customers']
# #                 state_analysis = state_analysis.sort_values('Fraud_Cases', ascending=False)
                
# #                 col1, col2 = st.columns(2)
# #                 with col1:
# #                     st.write("**Fraud Cases by State:**")
# #                     top_states = state_analysis['Fraud_Cases'].head(10)
# #                     fig = go.Figure(data=[go.Bar(
# #                         x=top_states.values,
# #                         y=top_states.index,
# #                         orientation='h',
# #                         marker=dict(
# #                             color=COLORS['primary'],
# #                             line=dict(color='rgba(102, 126, 234, 0.8)', width=1.5)
# #                         )
# #                     )])
# #                     fig.update_layout(
# #                         height=320,
# #                         paper_bgcolor='rgba(0,0,0,0)',
# #                         plot_bgcolor='rgba(0,0,0,0)',
# #                         dragmode='zoom',
# #                         margin=dict(t=20, b=30, l=40, r=20)
# #                     )
# #                     st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
                
# #                 with col2:
# #                     st.write("**Average Fraud Amount by State:**")
# #                     top_avg = state_analysis['Avg_Amount'].head(10)
# #                     fig = go.Figure(data=[go.Bar(
# #                         x=top_avg.values,
# #                         y=top_avg.index,
# #                         orientation='h',
# #                         marker=dict(
# #                             color=COLORS['danger'],
# #                             line=dict(color='rgba(239, 68, 68, 0.8)', width=1.5)
# #                         )
# #                     )])
# #                     fig.update_layout(
# #                         height=320,
# #                         paper_bgcolor='rgba(0,0,0,0)',
# #                         plot_bgcolor='rgba(0,0,0,0)',
# #                         dragmode='zoom',
# #                         margin=dict(t=20, b=30, l=40, r=20)
# #                     )
# #                     st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
        
# #         elif analysis_type == "Temporal Analysis":
# #             st.markdown("<h2 class='section-header'>Temporal Analysis</h2>", unsafe_allow_html=True)
# #             fraud_df['Hour'] = fraud_df['DateTime'].dt.hour
# #             fraud_df['DayOfWeek'] = fraud_df['DateTime'].dt.day_name()
# #             fraud_df['Month'] = fraud_df['DateTime'].dt.month_name()
            
# #             col1, col2, col3 = st.columns(3)
# #             with col1:
# #                 hourly_fraud = fraud_df['Hour'].value_counts().sort_index()
# #                 fig = go.Figure(data=[go.Bar(
# #                     x=hourly_fraud.index,
# #                     y=hourly_fraud.values,
# #                     marker=dict(
# #                         color=COLORS['primary'],
# #                         line=dict(color='rgba(102, 126, 234, 0.8)', width=1.5)
# #                     )
# #                 )])
# #                 fig.update_layout(
# #                     title="Fraud by Hour of Day",
# #                     height=250,
# #                     paper_bgcolor='rgba(0,0,0,0)',
# #                     plot_bgcolor='rgba(0,0,0,0)',
# #                     dragmode='zoom',
# #                     title_font=dict(size=13),
# #                     margin=dict(t=30, b=30, l=40, r=20)
# #                 )
# #                 st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
            
# #             with col2:
# #                 daily_fraud = fraud_df['DayOfWeek'].value_counts()
# #                 fig = go.Figure(data=[go.Bar(
# #                     x=daily_fraud.index,
# #                     y=daily_fraud.values,
# #                     marker=dict(
# #                         color=COLORS['secondary'],
# #                         line=dict(color='rgba(118, 75, 162, 0.8)', width=1.5)
# #                     )
# #                 )])
# #                 fig.update_layout(
# #                     title="Fraud by Day of Week",
# #                     height=250,
# #                     paper_bgcolor='rgba(0,0,0,0)',
# #                     plot_bgcolor='rgba(0,0,0,0)',
# #                     dragmode='zoom',
# #                     title_font=dict(size=13),
# #                     margin=dict(t=30, b=30, l=40, r=20)
# #                 )
# #                 st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
            
# #             with col3:
# #                 monthly_fraud = fraud_df['Month'].value_counts()
# #                 fig = go.Figure(data=[go.Bar(
# #                     x=monthly_fraud.index,
# #                     y=monthly_fraud.values,
# #                     marker=dict(
# #                         color=COLORS['accent'],
# #                         line=dict(color='rgba(30, 60, 114, 0.8)', width=1.5)
# #                     )
# #                 )])
# #                 fig.update_layout(
# #                     title="Fraud by Month",
# #                     height=250,
# #                     paper_bgcolor='rgba(0,0,0,0)',
# #                     plot_bgcolor='rgba(0,0,0,0)',
# #                     dragmode='zoom',
# #                     title_font=dict(size=13),
# #                     margin=dict(t=30, b=30, l=40, r=20)
# #                 )
# #                 st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
        
# #         elif analysis_type == "Fraud Pattern Analysis":
# #             st.markdown("<h2 class='section-header'>Fraud Pattern Analysis</h2>", unsafe_allow_html=True)
            
# #             fraud_df['Amount_Range'] = pd.cut(fraud_df['Amount'], 
# #                                             bins=[0, 100, 500, 1000, 5000, float('inf')], 
# #                                             labels=['$0-100', '$100-500', '$500-1K', '$1K-5K', '$5K+'])
            
# #             col1, col2 = st.columns(2)
            
# #             with col1:
# #                 st.write("**Fraud by Amount Range:**")
# #                 amount_dist = fraud_df['Amount_Range'].value_counts()
# #                 fig = go.Figure(data=[go.Bar(
# #                     x=amount_dist.index,
# #                     y=amount_dist.values,
# #                     marker=dict(
# #                         color=COLORS['primary'],
# #                         line=dict(color='rgba(102, 126, 234, 0.8)', width=1.5)
# #                     )
# #                 )])
# #                 fig.update_layout(
# #                     height=320,
# #                     paper_bgcolor='rgba(0,0,0,0)',
# #                     plot_bgcolor='rgba(0,0,0,0)',
# #                     dragmode='zoom',
# #                     margin=dict(t=20, b=30, l=40, r=20)
# #                 )
# #                 st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
            
# #             with col2:
# #                 st.write("**Correlation Analysis:**")
# #                 if len(fraud_df) > 1:
# #                     corr_data = fraud_df[['Amount']].copy()
# #                     corr_data['Hour'] = fraud_df['Hour']
# #                     corr_data['Month_Num'] = fraud_df['DateTime'].dt.month
                    
# #                     correlation_matrix = corr_data.corr()
# #                     st.dataframe(correlation_matrix, use_container_width=True)
    
# #     else:
# #         st.sidebar.warning("No months selected. Please select at least one month.")
# #         st.info("Please select at least one month from the sidebar to view the analysis.")

# # else:
# #     st.warning("No data available. Please upload your CSV file.")
# #     uploaded_file = st.file_uploader("Upload your fraud detection CSV file", type=['csv'])
# #     if uploaded_file is not None:
# #         with open(CSV_FILE, "wb") as f:
# #             f.write(uploaded_file.getbuffer())
# #         st.success("CSV file uploaded successfully!")
# #         st.rerun()

# # st.markdown("""
# #     <div class='fixed-footer'>
# #         Where Innovation Meets Security  |  Zero Tolerance for Fraud  |  © Xforia DAD 
# #     </div>
# # """, unsafe_allow_html=True)



























# # DASHBOARD.py

# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from splash_screen import show_splash
# import os
# import pathlib
# from geopy.geocoders import Nominatim
# from top_usa_cities_f import load_usa_cities_coordinates
# import time
# import base64

# try:
#     from streamlit_plotly_events import plotly_events
#     PLOTLY_EVENTS_AVAILABLE = True
# except ImportError:
#     PLOTLY_EVENTS_AVAILABLE = False
#     st.warning("For full interactivity, install: pip install streamlit-plotly-events")

# # Enhanced color scheme matching your theme
# COLORS = {
#     'primary': '#667eea',
#     'secondary': '#764ba2',
#     'accent': '#1e3c72',
#     'success': '#10b981',
#     'warning': '#f59e0b',
#     'danger': '#ef4444',
#     'legitimate': '#10b981',
#     'fraud': '#ef4444',
#     'male': '#3b82f6',
#     'female': '#ec4899',
#     'gradient_start': '#667eea',
#     'gradient_end': '#764ba2'
# }

# def add_fixed_logo():
#     """Add fixed logo to the dashboard with robust path finding"""
#     cwd = pathlib.Path(os.getcwd())
#     here = pathlib.Path(__file__).parent if "__file__" in globals() else cwd
    
#     # Search for logo in multiple locations
#     candidates = [
#         cwd / "FDN.png",
#         here / "FDN.png",
#         here / "assets" / "FDN.png",
#         cwd / "assets" / "FDN.png"
#     ]
    
#     logo_path = next((p for p in candidates if p.exists()), None)
    
#     if not logo_path:
#         st.warning("Logo file 'FDN.png' not found in any expected location.")
#         return
    
#     encoded = base64.b64encode(logo_path.read_bytes()).decode()
    
#     st.markdown(f"""
#         <style>
#         .fixed-logo {{
#             position: fixed;
#             top: 12px;
#             left: 60px;
#             z-index: 2147482000;
#             background: rgba(255,255,255,0.95);
#             border-radius: 6px;
#             padding: 4px 6px;
#         }}
#         .fixed-logo img {{
#             width: 150px;
#             height: 50px;
#             display: block;
#             cursor: pointer;
#         }}
                
#         [data-testid="stSidebar"] {{
#             display: none;
#         }}
#         [data-testid="stSidebarNav"] {{
#             display: none;
#         }}
#         [data-testid="stSidebarCollapseButton"] {{
#             display: none;
#         }}

#         @media (max-width: 768px) {{
#             .fixed-logo {{
#                 left: 56px;
#                 top: 10px;
#             }}
#         }}
#         </style>
#         <div class="fixed-logo">
#             <a href="/" target="_self">
#                 <img src="data:image/png;base64,{encoded}" alt="FDN Logo" />
#             </a>
#         </div>
#     """, unsafe_allow_html=True)

# # Call the logo function
# add_fixed_logo()

# # Enhanced global styling
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
#     * {
#         font-family: 'Inter', sans-serif;
#     }
    
#     .main-content {
#     }
    
#     .fixed-footer {
#         position: fixed;
#         bottom: 0;
#         left: 0;
#         right: 0;
#         background:#1e3c72;
#         color:#fff;
#         text-align: center;
#         padding: 20px;
#         z-index: 1000;
#         font-size: 1rem;
#         box-shadow: 0 -2px 10px rgba(0,0,0,.22);
#         font-weight: 600;
#         letter-spacing: 0.5px;
#     }
    
#     .metric-card {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         color: white;
#         padding: 20px;
#         border-radius: 12px;
#         box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
#         transition: all 0.3s ease;
#         text-align: center;
#     }
    
#     .metric-card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
#     }
    
#      .stButton>button {
#         background: linear-gradient(90deg, #2a5298, #1e3c72);;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 12px 24px;
#         font-weight: 600;
#         transition: all 0.3s ease;
#         box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
#     }
    
#     .stButton>button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 4px 15px rgba(102, 126, 234, 0.5);
#     }
    
#     .section-header {
#         background: #1e3c72;
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         font-size: 1.8em;
#         font-weight: 700;
#         margin: 20px 0;
#     }
    
#     div[data-testid="stExpander"] {
#         background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
#         border-radius: 10px;
#         border: 1px solid rgba(102, 126, 234, 0.2);
#     }
    
#     /* Chart container hover effect */
#     div[data-testid="stPlotlyChart"] {
#         cursor: pointer;
#         transition: all 0.3s ease;
#     }
    
#     div[data-testid="stPlotlyChart"]:hover {
#         transform: scale(1.01);
#         box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
#     }
#     </style>
# """, unsafe_allow_html=True)

# CSV_FILE = r"C:\Users\bhanukaranP\Desktop\DOC_AN_DET\Dataset_F_2.csv"

# @st.cache_data
# def get_city_coordinates(cities):
#     geolocator = Nominatim(user_agent="fraud_dashboard")
#     coordinates = {}
    
#     for city in cities:
#         try:
#             location = geolocator.geocode(f"{city}, USA")
#             if location:
#                 coordinates[city] = {
#                     'lat': location.latitude,
#                     'lon': location.longitude
#                 }
#             time.sleep(0.1)
#         except:
#             continue
    
#     return coordinates

# def load_csv_data():
#     try:
#         if os.path.exists(CSV_FILE):
#             df = pd.read_csv(CSV_FILE)
#             df['DateTime'] = pd.to_datetime(df['DateTime'])
#             df['Month-Year'] = df['DateTime'].dt.to_period('M').astype(str)
#             return df
#         else:
#             st.warning(f"CSV file '{CSV_FILE}' not found.")
#             return pd.DataFrame()
#     except Exception as e:
#         st.error(f"Error loading CSV: {str(e)}")
#         return pd.DataFrame()

# # Enhanced pie chart function
# def create_modern_pie(values, names, title, color_map=None):
#     fig = go.Figure(data=[go.Pie(
#         labels=names,
#         values=values,
#         hole=0.4,
#         marker=dict(
#             colors=[color_map.get(n, COLORS['primary']) for n in names] if color_map else None,
#             line=dict(color='white', width=2)
#         ),
#         textposition='auto',
#         textinfo='percent+label',
#         textfont=dict(size=11, color='white', family='Inter'),
#         hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>'
#     )])
    
#     fig.update_layout(
#         title=dict(text=title, font=dict(size=14, color='#1e3c72', family='Inter', weight=600)),
#         showlegend=True,
#         height=320,
#         margin=dict(t=30, b=0, l=0, r=0),
#         legend=dict(
#             orientation="v",
#             yanchor="middle",
#             y=0.5,
#             xanchor="left",
#             x=1.02,
#             font=dict(size=10, family='Inter')
#         ),
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)',
#         hovermode='closest'
#     )
    
#     return fig

# # Enhanced bar chart function
# def create_modern_bar(data, x, y, title, orientation='h', color=COLORS['primary']):
#     fig = go.Figure(data=[go.Bar(
#         x=data[x] if orientation == 'h' else data.index,
#         y=data[y] if orientation == 'h' else data.values,
#         orientation=orientation,
#         marker=dict(
#             color=color,
#             line=dict(color='rgba(102, 126, 234, 0.8)', width=1.5),
#             gradient=dict(
#                 type='linear',
#                 color=[COLORS['gradient_start'], COLORS['gradient_end']]
#             )
#         ),
#         hovertemplate='<b>%{y if orientation == "h" else x}</b><br>Count: %{x if orientation == "h" else y}<extra></extra>',
#         text=data[x] if orientation == 'h' else data.values,
#         textposition='auto',
#         textfont=dict(color='white', size=10, family='Inter', weight='bold')
#     )])
    
#     fig.update_layout(
#         title=dict(text=title, font=dict(size=14, color='#1e3c72', family='Inter', weight=600)),
#         xaxis_title=x if orientation == 'h' else '',
#         yaxis_title=y if orientation == 'h' else '',
#         height=320,
#         margin=dict(t=30, b=30, l=60, r=20),
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)',
#         xaxis=dict(gridcolor='rgba(102, 126, 234, 0.1)', showgrid=True, fixedrange=False),
#         yaxis=dict(gridcolor='rgba(102, 126, 234, 0.1)', showgrid=True, categoryorder='total ascending' if orientation == 'h' else None, fixedrange=False),
#         dragmode='pan',
#         hovermode='closest'
#     )
    
#     return fig

# # Plot configuration for better interactivity
# def get_plot_config():
#     return {
#         'displayModeBar': True,
#         'displaylogo': False,
#         'scrollZoom': True,
#         'modeBarButtonsToRemove': ['select2d', 'lasso2d', 'autoScale2d'],
#         'toImageButtonOptions': {
#             'format': 'png',
#             'filename': 'fraud_analysis_chart',
#             'height': 1080,
#             'width': 1920,
#             'scale': 2
#         }
#     }

# # Session state initialization
# for key in ['selected_detail', 'show_customer_details', 'show_transaction_details',
#             'show_male_details', 'show_female_details', 'show_transfer_details',
#             'show_legitimate_details', 'show_fraud_details',
#             'show_2024_details', 'show_2025_details', 'show_debit_details', 'show_credit_details']:
#     if key not in st.session_state:
#         st.session_state[key] = False

# # Toggle functions
# def toggle_debit():
#     st.session_state.show_debit_details = not st.session_state.show_debit_details

# def toggle_credit():
#     st.session_state.show_credit_details = not st.session_state.show_credit_details

# def toggle_transfer():
#     st.session_state.show_transfer_details = not st.session_state.show_transfer_details

# def toggle_male():
#     st.session_state.show_male_details = not st.session_state.show_male_details

# def toggle_female():
#     st.session_state.show_female_details = not st.session_state.show_female_details

# def toggle_2024():
#     st.session_state.show_2024_details = not st.session_state.show_2024_details

# def toggle_2025():
#     st.session_state.show_2025_details = not st.session_state.show_2025_details

# def toggle_legitimate():
#     st.session_state.show_legitimate_details = not st.session_state.show_legitimate_details

# def toggle_fraud():
#     st.session_state.show_fraud_details = not st.session_state.show_fraud_details

# if st.session_state.show_splash:
#     show_splash()
#     st.stop()


# st.title("AI Anomaly Detection Dashboard")

# df = load_csv_data()

# if not df.empty:
    
#     available_months = sorted(df['Month-Year'].unique())
#     if 'month_multiselect' not in st.session_state:
#         st.session_state.month_multiselect = available_months
    
#     def select_all_months():
#         st.session_state.month_multiselect = available_months
    
#     def clear_all_months():
#         st.session_state.month_multiselect = []
    
#     st.html('''
#     <style>
#     div[data-testid="stMultiSelect"] [data-baseweb="select"] > div > div {
#     max-height: 40px !important; /* Fix the height */
#     overflow: auto !important;
#     }
#     </style>
#     ''')

#     st.markdown("""
#     <style>
#     [data-testid="stMultiselect"] > div { margin-top: 0px; }
#     [data-testid="stSelectbox"] > div { margin-top: 0px; }
#     .section-header { margin: 0; }
#     </style>
#     """, unsafe_allow_html=True)

#     st.markdown("""
# <style>
# /* Select All button */
# [data-testid="stButton"] button[key="select_all"] {
#     background: #28a745;
#     color: white;
#     border-radius: 8px;
#     padding: 12px 20px;
#     font-weight: 600;
#     box-shadow: 0 2px 8px rgba(40, 167, 69, 0.3);
#     transition: all 0.3s ease;
# }

# /* Clear All button */
# [data-testid="stButton"] button[key="clear_all"] {
#     background: #dc3545;
#     color: white;
#     border-radius: 8px;
#     padding: 12px 24px;
#     font-weight: 600;
#     box-shadow: 0 2px 8px rgba(220, 53, 69, 0.3);
#     transition: all 0.3s ease;
# }

# </style>
# """, unsafe_allow_html=True)


#     # Wrap header in a div for bottom alignment
#     st.markdown("""
#     <div style="display: flex; align-items: flex-end; height: 100%; margin-bottom: 20px;">
#         <h2 class='section-header'>Dashboard Metrics</h2>
#     </div>
#     """, unsafe_allow_html=True)

#     filter_col1, filter_col2 = st.columns([4, 4])

#     with filter_col1:
#         selected_months = st.multiselect(
#         "Month-Year",
#         options=available_months,
#         key="month_multiselect",
#         help="Select one or more months to analyze"
#     )

#     with filter_col2:
#         c1, c2, c3 = st.columns([8,3,3])
#         with c1:
#             analysis_type = st.selectbox(
#             "Choose Analysis Mode:",
#             ["Overview", "Customer Deep Dive", "Geographic Analysis", "Temporal Analysis", "Fraud Pattern Analysis"]
#             )

#         with c2:
#             st.markdown("<div style='margin-top:23px; margin-right: 0px;'>", unsafe_allow_html=True)
#             st.button("Select All", key="select_all", on_click=select_all_months)
#             st.markdown("</div>", unsafe_allow_html=True)
#         with c3:
#             st.markdown("<div style='margin-top:23px;'>", unsafe_allow_html=True)
#             st.button("Clear All", key="clear_all", on_click=clear_all_months)
#             st.markdown("</div>", unsafe_allow_html=True)
#     st.write("") 

    
#     if selected_months:
#         filtered_df = df[df['Month-Year'].isin(selected_months)]
#         fraud_df = filtered_df[filtered_df['Legitimate'] == 0]

#         col1, col2, col3, col4 = st.columns(4)
        
#         with col1:
#             total_users = filtered_df['CustomerID'].nunique()
#             if st.button(f"Customers: {total_users:,}", key="customers_btn", help="Click for customer details"):
#                 st.session_state.show_customer_details = not st.session_state.show_customer_details

#         with col2:
#             total_transactions = len(filtered_df)
#             if st.button(f"Transactions: {total_transactions:,}", key="trans_btn", help="Click for transaction timeline"):
#                 st.session_state.show_transaction_details = not st.session_state.show_transaction_details
        
#         with col3:
#             legit_count = filtered_df['Legitimate'].sum()
#             st.metric(label="Legitimate", value=legit_count, help="Number of legitimate transactions")
        
#         with col4:
#             fraud_count = len(fraud_df)
#             st.metric(label="Fraud Detected", value=fraud_count, help="Number of fraudulent transactions")
        
#         if st.session_state.show_customer_details:
#             with st.expander("Customer Analysis Details", expanded=True):
#                 customer_stats = filtered_df.groupby('CustomerID').agg({
#                     'Amount': ['count', 'sum', 'mean'],
#                     'Legitimate': lambda x: (x == 0).sum(),
#                     'TransactionLocationCity': 'nunique'
#                 }).round(2)
#                 customer_stats.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Fraud_Count', 'Cities']
#                 customer_stats['Fraud_Rate'] = (customer_stats['Fraud_Count'] / customer_stats['Transactions'] * 100).round(1)
#                 customer_stats = customer_stats.sort_values('Total_Amount', ascending=False).head(20)
                
#                 st.write("**Top 20 Customers by Transaction Volume:**")
#                 st.dataframe(customer_stats, use_container_width=True)
                
#                 col1, col2, col3 = st.columns(3)
#                 with col1:
#                     st.metric("Highest Spender", f"${customer_stats['Total_Amount'].max():,.2f}")
#                 with col2:
#                     st.metric("Most Active", f"{customer_stats['Transactions'].max()} transactions")
#                 with col3:
#                     avg_fraud_rate = customer_stats['Fraud_Rate'].mean()
#                     st.metric("Avg Fraud Rate", f"{avg_fraud_rate:.1f}%")

#         if st.session_state.show_transaction_details:
#             with st.expander("Transaction Timeline Analysis", expanded=True):
#                 daily_stats = filtered_df.groupby(filtered_df['DateTime'].dt.date).agg({
#                     'Amount': ['count', 'sum'],
#                     'Legitimate': lambda x: (x == 0).sum()
#                 }).round(2)
#                 daily_stats.columns = ['Transaction_Count', 'Total_Amount', 'Fraud_Count']
#                 daily_stats['Fraud_Rate'] = (daily_stats['Fraud_Count'] / daily_stats['Transaction_Count'] * 100).round(1)
                
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     fig = go.Figure()
#                     fig.add_trace(go.Scatter(
#                         x=daily_stats.index,
#                         y=daily_stats['Transaction_Count'],
#                         mode='lines+markers',
#                         name='Transactions',
#                         line=dict(color=COLORS['primary'], width=3),
#                         marker=dict(size=6, color=COLORS['secondary']),
#                         fill='tozeroy',
#                         fillcolor='rgba(102, 126, 234, 0.2)'
#                     ))
#                     fig.update_layout(
#                         title="Daily Transaction Volume",
#                         height=250,
#                         margin=dict(t=30, b=20, l=20, r=20),
#                         paper_bgcolor='rgba(0,0,0,0)',
#                         plot_bgcolor='rgba(0,0,0,0)',
#                         dragmode='zoom',
#                         title_font=dict(size=13)
#                     )
#                     st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
                
#                 with col2:
#                     fig = go.Figure()
#                     fig.add_trace(go.Scatter(
#                         x=daily_stats.index,
#                         y=daily_stats['Fraud_Rate'],
#                         mode='lines+markers',
#                         name='Fraud Rate',
#                         line=dict(color=COLORS['danger'], width=3),
#                         marker=dict(size=6, color='#dc2626'),
#                         fill='tozeroy',
#                         fillcolor='rgba(239, 68, 68, 0.2)'
#                     ))
#                     fig.update_layout(
#                         title="Daily Fraud Rate (%)",
#                         height=250,
#                         margin=dict(t=30, b=20, l=20, r=20),
#                         paper_bgcolor='rgba(0,0,0,0)',
#                         plot_bgcolor='rgba(0,0,0,0)',
#                         dragmode='zoom',
#                         title_font=dict(size=13)
#                     )
#                     st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
        
#         st.markdown("---")
#         col1, col2 = st.columns(2, gap="large")
        
#         with col1:
#             st.subheader("Count by Transaction Type")
#             status_counts = filtered_df['Legitimate'].value_counts()
#             status_labels = ['Fraud', 'Legitimate']
            
#             color_map = {'Legitimate': COLORS['legitimate'], 'Fraud': COLORS['fraud']}
#             fig1 = create_modern_pie(
#                 [status_counts.get(0, 0), status_counts.get(1, 0)],
#                 status_labels,
#                 "",
#                 color_map
#             )
#             st.plotly_chart(fig1, use_container_width=True, config=get_plot_config())

#             col_i, col_j = st.columns(2)
#             with col_i:
#                 legitimate_count = status_counts.get(1, 0)
#                 if legitimate_count > 0:
#                     if st.button(f"Legitimate ({legitimate_count})", key='legitimate_btn', on_click=toggle_legitimate):
#                         pass

#             with col_j:
#                 fraud_count = status_counts.get(0, 0)
#                 if fraud_count > 0:
#                     if st.button(f"Fraud ({fraud_count})", key='fraud_btn', on_click=toggle_fraud):
#                         pass

#             if st.session_state.show_legitimate_details:
#                 with st.expander("Top 5 Legitimate Transaction Customers", expanded=True):
#                     legitimate_df = filtered_df[filtered_df['Legitimate'] == 1]
#                     if not legitimate_df.empty:
#                         top5_legitimate = legitimate_df.groupby('CustomerID').agg({
#                             'Amount': ['count', 'sum', 'mean'],
#                             'TransactionLocationCity': 'nunique'
#                         }).round(2)
#                         top5_legitimate.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Cities']
#                         top5_legitimate = top5_legitimate.sort_values('Total_Amount', ascending=False).head(5)
#                         st.dataframe(top5_legitimate, use_container_width=True)

#             if st.session_state.show_fraud_details:
#                 with st.expander("Top 5 Fraud Transaction Customers", expanded=True):
#                     fraud_only_df = filtered_df[filtered_df['Legitimate'] == 0]
#                     if not fraud_only_df.empty:
#                         top5_fraud = fraud_only_df.groupby('CustomerID').agg({
#                             'Amount': ['count', 'sum', 'mean'],
#                             'TransactionLocationCity': 'nunique'
#                         }).round(2)
#                         top5_fraud.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Cities']
#                         top5_fraud = top5_fraud.sort_values('Total_Amount', ascending=False).head(5)
#                         st.dataframe(top5_fraud, use_container_width=True)


#         with col2:
#             st.subheader("Fraud Transaction by Year")
#             if not fraud_df.empty:
#                 fraud_by_year = fraud_df['DateTime'].dt.year.value_counts()
#                 # Filter out 2023
#                 fraud_by_year = fraud_by_year[fraud_by_year.index != 2023]
                
#                 if not fraud_by_year.empty:
#                     fig2 = create_modern_pie(
#                         fraud_by_year.values,
#                         fraud_by_year.index,
#                         ""
#                     )
#                     st.plotly_chart(fig2, use_container_width=True, config=get_plot_config())
            
#                     col_g, col_h = st.columns(2)
#                     with col_g:
#                         if 2024 in fraud_by_year.index:
#                             if st.button(f"2024 ({fraud_by_year[2024]})", key='year_2024_btn', on_click=toggle_2024):
#                                 pass
#                     with col_h:
#                         if 2025 in fraud_by_year.index:
#                             if st.button(f"2025 ({fraud_by_year[2025]})", key='year_2025_btn', on_click=toggle_2025):
#                                 pass
                    
#                     # Year details sections
#                     for year, state_key in [(2024, 'show_2024_details'), (2025, 'show_2025_details')]:
#                         if st.session_state[state_key] and year in fraud_by_year.index:
#                             with st.expander(f"Top 5 Fraud Customers from {year}", expanded=True):
#                                 year_df = fraud_df[fraud_df['DateTime'].dt.year == year]
#                                 if not year_df.empty:
#                                     top5_year = year_df.groupby('CustomerID').agg({
#                                         'Amount': ['count', 'sum', 'mean'],
#                                         'TransactionLocationCity': 'nunique'
#                                     }).round(2)
#                                     top5_year.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Cities']
#                                     top5_year = top5_year.sort_values('Total_Amount', ascending=False).head(5)
#                                     st.dataframe(top5_year, use_container_width=True)


#         st.markdown("---")
#         col1, col2 = st.columns(2, gap="large")
#         with col1:
#             st.subheader("Fraud Transaction by Gender")
#             if not fraud_df.empty:
#                 fraud_by_gender = fraud_df['Gender'].value_counts()
#                 if not fraud_by_gender.empty:
#                     # Create horizontal bar chart
#                     total_gender = fraud_by_gender.sum()
#                     percentages = (fraud_by_gender / total_gender * 100).round(1)
                    
#                     fig3 = go.Figure()
#                     colors_list = [COLORS['male'] if g == 'Male' else COLORS['female'] for g in fraud_by_gender.index]
                    
#                     fig3.add_trace(go.Bar(
#                         y=fraud_by_gender.index,
#                         x=fraud_by_gender.values,
#                         orientation='h',
#                         marker=dict(
#                             color=colors_list,
#                             line=dict(color='white', width=2)
#                         ),
#                         text=[f"{count} ({percentages[gender]}%)" for gender, count in fraud_by_gender.items()],
#                         textposition='inside',
#                         textfont=dict(color='white', size=13, family='Inter', weight='bold'),
#                         hovertemplate='<b>%{y}</b><br>Count: %{x}<br>Percentage: %{customdata}%<extra></extra>',
#                         customdata=percentages.values,
#                         showlegend=False
#                     ))
                    
#                     fig3.update_layout(
#                         height=280,
#                         margin=dict(t=20, b=30, l=80, r=20),
#                         paper_bgcolor='rgba(0,0,0,0)',
#                         plot_bgcolor='rgba(0,0,0,0)',
#                         xaxis=dict(
#                             title=dict(text="Number of Fraud Transactions", font=dict(size=11)),
#                             gridcolor='rgba(102, 126, 234, 0.1)',
#                             showgrid=True,
#                             fixedrange=False
#                         ),
#                         yaxis=dict(
#                             title="",
#                             gridcolor='rgba(102, 126, 234, 0.1)',
#                             showgrid=False,
#                             fixedrange=False
#                         ),
#                         dragmode='pan',
#                         hovermode='closest'
#                     )
#                     st.plotly_chart(fig3, use_container_width=True, config=get_plot_config())
                    
#                     cola, colb = st.columns(2)
#                     with cola:
#                         if 'Male' in fraud_by_gender.index:
#                             if st.button(f"Male Details ({fraud_by_gender['Male']})", key='male_btn', on_click=toggle_male):
#                                 pass
#                     with colb:
#                         if 'Female' in fraud_by_gender.index:
#                             if st.button(f"Female Details ({fraud_by_gender['Female']})", key='female_btn', on_click=toggle_female):
#                                 pass
                    
#                     if st.session_state.show_male_details and 'Male' in fraud_by_gender.index:
#                         with st.expander("Top 5 Male Fraud Customers", expanded=True):
#                             male_df = fraud_df[fraud_df['Gender'] == 'Male']
#                             if not male_df.empty:
#                                 top5_male = male_df.groupby('CustomerID').agg({
#                                     'Amount': ['count', 'sum', 'mean'],
#                                     'TransactionLocationCity': 'nunique'
#                                 }).round(2)
#                                 top5_male.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Cities']
#                                 top5_male = top5_male.sort_values('Total_Amount', ascending=False).head(5)
#                                 st.dataframe(top5_male, use_container_width=True)
            
#                     if st.session_state.show_female_details and 'Female' in fraud_by_gender.index:
#                         with st.expander("Top 5 Female Fraud Customers", expanded=True):
#                             female_df = fraud_df[fraud_df['Gender'] == 'Female']
#                             if not female_df.empty:
#                                 top5_female = female_df.groupby('CustomerID').agg({
#                                     'Amount': ['count', 'sum', 'mean'],
#                                     'TransactionLocationCity': 'nunique'
#                                 }).round(2)
#                                 top5_female.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Cities']
#                                 top5_female = top5_female.sort_values('Total_Amount', ascending=False).head(5)
#                                 st.dataframe(top5_female, use_container_width=True)
#         with col2:

#             st.subheader("Fraud Transaction by Type")
#             if not fraud_df.empty:
#                 fraud_by_type = fraud_df['Type'].value_counts()
#                 if not fraud_by_type.empty:
#                     # Create horizontal bar chart
#                     total_type = fraud_by_type.sum()
#                     percentages = (fraud_by_type / total_type * 100).round(1)
                    
#                     # Define colors for each type
#                     color_mapping = {
#                         'Debit': '#0066cc',
#                         'Credit': '#4dabf7',
#                         'Transfer': '#e74c3c'
#                     }
#                     colors_list = [color_mapping.get(t, COLORS['primary']) for t in fraud_by_type.index]
                    
#                     fig4 = go.Figure()
#                     fig4.add_trace(go.Bar(
#                         y=fraud_by_type.index,
#                         x=fraud_by_type.values,
#                         orientation='h',
#                         marker=dict(
#                             color=colors_list,
#                             line=dict(color='white', width=2)
#                         ),
#                         text=[f"{count} ({percentages[t_type]}%)" for t_type, count in fraud_by_type.items()],
#                         textposition='inside',
#                         textfont=dict(color='white', size=13, family='Inter', weight='bold'),
#                         hovertemplate='<b>%{y}</b><br>Count: %{x}<br>Percentage: %{customdata}%<extra></extra>',
#                         customdata=percentages.values,
#                         showlegend=False
#                     ))
                    
#                     fig4.update_layout(
#                         height=280,
#                         margin=dict(t=20, b=30, l=80, r=20),
#                         paper_bgcolor='rgba(0,0,0,0)',
#                         plot_bgcolor='rgba(0,0,0,0)',
#                         xaxis=dict(
#                             title=dict(text="Number of Fraud Transactions", font=dict(size=11)),
#                             gridcolor='rgba(102, 126, 234, 0.1)',
#                             showgrid=True,
#                             fixedrange=False
#                         ),
#                         yaxis=dict(
#                             title="",
#                             gridcolor='rgba(102, 126, 234, 0.1)',
#                             showgrid=False,
#                             fixedrange=False,
#                             categoryorder='total ascending'
#                         ),
#                         dragmode='pan',
#                         hovermode='closest'
#                     )
#                     st.plotly_chart(fig4, use_container_width=True, config=get_plot_config())
                    
#                     col_c, col_d, col_e = st.columns(3)
#                     with col_c:
#                         if 'Debit' in fraud_by_type.index:
#                             if st.button(f"Debit ({fraud_by_type['Debit']})", key='debit_btn', on_click=toggle_debit):
#                                 pass
#                     with col_d:
#                         if 'Credit' in fraud_by_type.index:
#                             if st.button(f"Credit ({fraud_by_type['Credit']})", key='credit_btn', on_click=toggle_credit):
#                                 pass
#                     with col_e:
#                         if 'Transfer' in fraud_by_type.index:
#                             if st.button(f"Transfer ({fraud_by_type['Transfer']})", key='transfer_btn', on_click=toggle_transfer):
#                                 pass
                    
#                     # Type details sections
#                     for trans_type, state_key in [('Debit', 'show_debit_details'), ('Credit', 'show_credit_details'), ('Transfer', 'show_transfer_details')]:
#                         if st.session_state[state_key] and trans_type in fraud_by_type.index:
#                             with st.expander(f"Top 5 {trans_type} Fraud Customers", expanded=True):
#                                 type_df = fraud_df[fraud_df['Type'] == trans_type]
#                                 if not type_df.empty:
#                                     top5_type = type_df.groupby('CustomerID').agg({
#                                         'Amount': ['count', 'sum', 'mean'],
#                                         'TransactionLocationCity': 'nunique'
#                                     }).round(2)
#                                     top5_type.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Cities']
#                                     top5_type = top5_type.sort_values('Total_Amount', ascending=False).head(5)
#                                     st.dataframe(top5_type, use_container_width=True)

#         st.markdown("---")
#         col1, col2 = st.columns(2, gap="large")

#         with col1:
#             st.subheader("Fraud Transactions by Cities")
#             if not fraud_df.empty:
#                 usa_cities = load_usa_cities_coordinates()
#                 city_counts = fraud_df['TransactionLocationCity'].value_counts()
#                 map_data = []
#                 for city, count in city_counts.items():
#                     if city in usa_cities:
#                         lat, lon = usa_cities[city]
#                         map_data.append({'City': city, 'Count': count, 'lat': lat, 'lon': lon})
                
#                 if map_data:
#                     df_map = pd.DataFrame(map_data)
#                     fig5 = px.scatter_mapbox(
#                         df_map,
#                         lat='lat',
#                         lon='lon',
#                         size='Count',
#                         color='Count',
#                         hover_name='City',
#                         hover_data={'Count': True, 'lat': False, 'lon': False},
#                         color_continuous_scale=[[0, '#fee2e2'], [0.5, '#fca5a5'], [1, '#ef4444']],
#                         size_max=25,
#                         zoom=2.2,
#                         center={'lat': 39.5, 'lon': -98.35},
#                         mapbox_style='open-street-map'
#                     )
#                     fig5.update_layout(
#                         height=320,
#                         margin={"r":0,"t":0,"l":0,"b":0},
#                         coloraxis_colorbar=dict(
#                             title=dict(text="Fraud Count", font=dict(size=11)),
#                             thicknessmode="pixels",
#                             thickness=12,
#                             lenmode="pixels",
#                             len=150
#                         ),
#                         dragmode='zoom'
#                     )
#                     st.plotly_chart(fig5, use_container_width=True, config=get_plot_config())
#         with col2:        
#             top_5_cities = city_counts.head(5)
#             st.subheader("Top 5 Cities by Fraud Count:")
#             for i, (city, count) in enumerate(top_5_cities.items(), 1):
#                 st.write(f"{i}. {city}: {count:,}")
        
#         st.markdown("---")
#         st.subheader("Count by Fraud Reason")
#         if not fraud_df.empty:
#                 fraud_reasons = fraud_df['FraudReason'].value_counts().head(10)
#                 if not fraud_reasons.empty:
#                     fraud_df_plot = pd.DataFrame({
#                         'FraudReason': fraud_reasons.index,
#                         'Count': fraud_reasons.values
#                     })
#                     fraud_df_plot['ShortReason'] = fraud_df_plot['FraudReason'].apply(
#                         lambda x: x if len(x) <= 25 else x[:22] + '...'
#                     )
                    
#                     fig6 = go.Figure(data=[go.Bar(
#                         x=fraud_df_plot['Count'],
#                         y=fraud_df_plot['ShortReason'],
#                         orientation='h',
#                         marker=dict(
#                             color=fraud_df_plot['Count'],
#                             colorscale=[[0, COLORS['gradient_start']], [1, COLORS['gradient_end']]],
#                             line=dict(color='rgba(102, 126, 234, 0.8)', width=1.5)
#                         ),
#                         text=fraud_df_plot['Count'],
#                         textposition='auto',
#                         textfont=dict(color='white', size=11, family='Inter', weight='bold'),
#                         hovertext=fraud_df_plot['FraudReason'],
#                         hovertemplate='<b>%{hovertext}</b><br>Count: %{x}<extra></extra>'
#                     )])
                    
#                     fig6.update_layout(
#                         xaxis_title="Count (Log Scale)",
#                         yaxis_title="Fraud Reason",
#                         height=320,
#                         margin=dict(t=20, b=30, l=140, r=20),
#                         yaxis={'categoryorder': 'total ascending'},
#                         xaxis_type='log',
#                         paper_bgcolor='rgba(0,0,0,0)',
#                         plot_bgcolor='rgba(0,0,0,0)',
#                         xaxis=dict(
#                             title=dict(text="Count (Log Scale)", font=dict(size=11)),
#                             gridcolor='rgba(102, 126, 234, 0.1)',
#                             showgrid=True,
#                             type='log'
#                         ),
#                         yaxis_tickfont=dict(size=9, family='Inter'),
#                         dragmode='zoom'
#                     )
                    
#                     st.plotly_chart(fig6, use_container_width=True, config=get_plot_config())
               
#         if analysis_type != "Overview":
#             st.markdown("---")
            
#         if analysis_type == "Customer Deep Dive":
#             st.markdown("<h2 class='section-header'>Customer Deep Dive Analysis</h2>", unsafe_allow_html=True)
#             top_customers = filtered_df.groupby('CustomerID')['Amount'].sum().sort_values(ascending=False).head(50)
#             selected_customer = st.selectbox("Select Customer ID for Analysis:", [""] + list(top_customers.index))
            
#             if selected_customer:
#                 customer_data = filtered_df[filtered_df['CustomerID'] == selected_customer]
#                 col1, col2, col3, col4 = st.columns(4)
#                 with col1:
#                     st.metric("Total Transactions", len(customer_data))
#                 with col2:
#                     st.metric("Total Amount", f"${customer_data['Amount'].sum():.2f}")
#                 with col3:
#                     fraud_rate = (1 - customer_data['Legitimate'].mean()) * 100
#                     st.metric("Fraud Rate", f"{fraud_rate:.1f}%")
#                 with col4:
#                     st.metric("Unique Cities", customer_data['TransactionLocationCity'].nunique())
               
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     timeline = customer_data.set_index('DateTime').resample('D')['Amount'].sum()
#                     fig = go.Figure()
#                     fig.add_trace(go.Scatter(
#                         x=timeline.index,
#                         y=timeline.values,
#                         mode='lines+markers',
#                         line=dict(color=COLORS['primary'], width=2),
#                         fill='tozeroy',
#                         fillcolor='rgba(102, 126, 234, 0.2)'
#                     ))
#                     fig.update_layout(
#                         title="Transaction Timeline",
#                         height=250,
#                         paper_bgcolor='rgba(0,0,0,0)',
#                         plot_bgcolor='rgba(0,0,0,0)',
#                         dragmode='zoom',
#                         title_font=dict(size=13),
#                         margin=dict(t=30, b=20, l=40, r=20)
#                     )
#                     st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
                
#                 with col2:
#                     type_dist = customer_data['Type'].value_counts()
#                     fig = create_modern_pie(type_dist.values, type_dist.index, "Transaction Types")
#                     st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
                
#                 st.write("**All Transactions:**")
#                 display_data = customer_data[['DateTime', 'Type', 'Amount', 'TransactionLocationCity', 'Legitimate', 'FraudReason']].copy()
#                 display_data['Status'] = display_data['Legitimate'].map({1: 'Legitimate', 0: 'Fraud'})
#                 st.dataframe(display_data.drop('Legitimate', axis=1), use_container_width=True)
        
#         elif analysis_type == "Geographic Analysis":
#             st.markdown("<h2 class='section-header'>Geographic Analysis</h2>", unsafe_allow_html=True)
            
#             if 'State' in fraud_df.columns:
#                 state_analysis = fraud_df.groupby('State').agg({
#                     'Amount': ['count', 'sum', 'mean'],
#                     'CustomerID': 'nunique'
#                 }).round(2)
#                 state_analysis.columns = ['Fraud_Cases', 'Total_Amount', 'Avg_Amount', 'Customers']
#                 state_analysis = state_analysis.sort_values('Fraud_Cases', ascending=False)
                
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     st.write("**Fraud Cases by State:**")
#                     top_states = state_analysis['Fraud_Cases'].head(10)
#                     fig = go.Figure(data=[go.Bar(
#                         x=top_states.values,
#                         y=top_states.index,
#                         orientation='h',
#                         marker=dict(
#                             color=COLORS['primary'],
#                             line=dict(color='rgba(102, 126, 234, 0.8)', width=1.5)
#                         )
#                     )])
#                     fig.update_layout(
#                         height=320,
#                         paper_bgcolor='rgba(0,0,0,0)',
#                         plot_bgcolor='rgba(0,0,0,0)',
#                         dragmode='zoom',
#                         margin=dict(t=20, b=30, l=40, r=20)
#                     )
#                     st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
                
#                 with col2:
#                     st.write("**Average Fraud Amount by State:**")
#                     top_avg = state_analysis['Avg_Amount'].head(10)
#                     fig = go.Figure(data=[go.Bar(
#                         x=top_avg.values,
#                         y=top_avg.index,
#                         orientation='h',
#                         marker=dict(
#                             color=COLORS['danger'],
#                             line=dict(color='rgba(239, 68, 68, 0.8)', width=1.5)
#                         )
#                     )])
#                     fig.update_layout(
#                         height=320,
#                         paper_bgcolor='rgba(0,0,0,0)',
#                         plot_bgcolor='rgba(0,0,0,0)',
#                         dragmode='zoom',
#                         margin=dict(t=20, b=30, l=40, r=20)
#                     )
#                     st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
        
#         elif analysis_type == "Temporal Analysis":
#             st.markdown("<h2 class='section-header'>Temporal Analysis</h2>", unsafe_allow_html=True)
#             fraud_df['Hour'] = fraud_df['DateTime'].dt.hour
#             fraud_df['DayOfWeek'] = fraud_df['DateTime'].dt.day_name()
#             fraud_df['Month'] = fraud_df['DateTime'].dt.month_name()
            
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 hourly_fraud = fraud_df['Hour'].value_counts().sort_index()
#                 fig = go.Figure(data=[go.Bar(
#                     x=hourly_fraud.index,
#                     y=hourly_fraud.values,
#                     marker=dict(
#                         color=COLORS['primary'],
#                         line=dict(color='rgba(102, 126, 234, 0.8)', width=1.5)
#                     )
#                 )])
#                 fig.update_layout(
#                     title="Fraud by Hour of Day",
#                     height=250,
#                     paper_bgcolor='rgba(0,0,0,0)',
#                     plot_bgcolor='rgba(0,0,0,0)',
#                     dragmode='zoom',
#                     title_font=dict(size=13),
#                     margin=dict(t=30, b=30, l=40, r=20)
#                 )
#                 st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
            
#             with col2:
#                 daily_fraud = fraud_df['DayOfWeek'].value_counts()
#                 fig = go.Figure(data=[go.Bar(
#                     x=daily_fraud.index,
#                     y=daily_fraud.values,
#                     marker=dict(
#                         color=COLORS['secondary'],
#                         line=dict(color='rgba(118, 75, 162, 0.8)', width=1.5)
#                     )
#                 )])
#                 fig.update_layout(
#                     title="Fraud by Day of Week",
#                     height=250,
#                     paper_bgcolor='rgba(0,0,0,0)',
#                     plot_bgcolor='rgba(0,0,0,0)',
#                     dragmode='zoom',
#                     title_font=dict(size=13),
#                     margin=dict(t=30, b=30, l=40, r=20)
#                 )
#                 st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
            
#             with col3:
#                 monthly_fraud = fraud_df['Month'].value_counts()
#                 fig = go.Figure(data=[go.Bar(
#                     x=monthly_fraud.index,
#                     y=monthly_fraud.values,
#                     marker=dict(
#                         color=COLORS['accent'],
#                         line=dict(color='rgba(30, 60, 114, 0.8)', width=1.5)
#                     )
#                 )])
#                 fig.update_layout(
#                     title="Fraud by Month",
#                     height=250,
#                     paper_bgcolor='rgba(0,0,0,0)',
#                     plot_bgcolor='rgba(0,0,0,0)',
#                     dragmode='zoom',
#                     title_font=dict(size=13),
#                     margin=dict(t=30, b=30, l=40, r=20)
#                 )
#                 st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
        
#         elif analysis_type == "Fraud Pattern Analysis":
#             st.markdown("<h2 class='section-header'>Fraud Pattern Analysis</h2>", unsafe_allow_html=True)
            
#             fraud_df['Amount_Range'] = pd.cut(fraud_df['Amount'], 
#                                             bins=[0, 100, 500, 1000, 5000, float('inf')], 
#                                             labels=['$0-100', '$100-500', '$500-1K', '$1K-5K', '$5K+'])
            
#             col1, col2 = st.columns(2)
            
#             with col1:
#                 st.write("**Fraud by Amount Range:**")
#                 amount_dist = fraud_df['Amount_Range'].value_counts()
#                 fig = go.Figure(data=[go.Bar(
#                     x=amount_dist.index,
#                     y=amount_dist.values,
#                     marker=dict(
#                         color=COLORS['primary'],
#                         line=dict(color='rgba(102, 126, 234, 0.8)', width=1.5)
#                     )
#                 )])
#                 fig.update_layout(
#                     height=320,
#                     paper_bgcolor='rgba(0,0,0,0)',
#                     plot_bgcolor='rgba(0,0,0,0)',
#                     dragmode='zoom',
#                     margin=dict(t=20, b=30, l=40, r=20)
#                 )
#                 st.plotly_chart(fig, use_container_width=True, config=get_plot_config())
            
#             with col2:
#                 st.write("**Correlation Analysis:**")
#                 if len(fraud_df) > 1:
#                     corr_data = fraud_df[['Amount']].copy()
#                     corr_data['Hour'] = fraud_df['Hour']
#                     corr_data['Month_Num'] = fraud_df['DateTime'].dt.month
                    
#                     correlation_matrix = corr_data.corr()
#                     st.dataframe(correlation_matrix, use_container_width=True)
    
#     else:
#         st.info("Please select at least one month from the sidebar to view the analysis.")

# else:
#     st.warning("No data available. Please upload your CSV file.")
#     uploaded_file = st.file_uploader("Upload your fraud detection CSV file", type=['csv'])
#     if uploaded_file is not None:
#         with open(CSV_FILE, "wb") as f:
#             f.write(uploaded_file.getbuffer())
#         st.success("CSV file uploaded successfully!")
#         st.rerun()

# st.markdown("""
#     <div class='fixed-footer'>
#       <span>Where Innovation Meets Security</span>
#       <span class="sep">|</span>
#       <span>Zero Tolerance for Fraud</span>
#       <span class="sep">|</span>
#       <span>© Xforia DAD</span>
#     </div>
# """, unsafe_allow_html=True)






















import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os
import pathlib
from geopy.geocoders import Nominatim
from splash_screen import show_splash
from top_usa_cities_f import load_usa_cities_coordinates
import time
import base64

if "show_splash" not in st.session_state:
    st.session_state.show_splash = False


if st.session_state.show_splash:
    show_splash()  
    st.stop()     


st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
    /* Remove all top padding/margin */
    .main .block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }
    
    /* Extra safety for newer Streamlit versions */
    .css-18e3th9 {padding-top: 0rem !important;}
    .css-1outpf7 {margin-top: 0rem !important;}
    </style>
""", unsafe_allow_html=True)

def add_fixed_logo():
    cwd = pathlib.Path(os.getcwd())
    here = pathlib.Path(__file__).parent if "__file__" in globals() else cwd
    
    # Search for logo in multiple locations
    candidates = [
        cwd / "FDN.png", 
        here / "FDN.png", 
        here / "assets" / "FDN.png", 
        cwd / "assets" / "FDN.png",
        cwd / "FD.png",  # Also check for your original filename
        here / "FD.png"
    ]
    
    logo_path = next((p for p in candidates if p.exists()), None)
    
    if not logo_path:
        st.warning("Logo file 'FDN.png' or 'FD.png' not found.")
        return
    
    encoded = base64.b64encode(logo_path.read_bytes()).decode()
    
    st.markdown(f"""
        <style>
        .fixed-logo {{
            position: fixed;
            top: 12px;
            left: 60px;
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
            .fixed-logo {{
                left: 56px;
                top: 10px;
            }}
        }}
        </style>
        <div class="fixed-logo">
            <a href="/" target="_self">
                <img src="data:image/png;base64,{encoded}" alt="FDN Logo" />
            </a>
        </div>
    """, unsafe_allow_html=True)

# Call this function immediately after imports
add_fixed_logo()

st.set_page_config(
    page_title="AI Anomaly Insights ",
    page_icon="📈",
    layout="wide"
)

if st.session_state.show_splash:
    show_splash()
    st.stop()

st.markdown("""
    <style>
    .main-content {
        padding-bottom: 80px; /* Space for fixed footer */
    }
    .fixed-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #2d5282;
        color: white;
        text-align: center;
        padding: 20px;
        z-index: 1000;
        box-shadow: 0 -4px 20px rgba(45, 82, 130, 0.4);
        font-size: 0.95em;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    .info-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .detail-card {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

CSV_FILE = r"C:\Users\bhanukaranP\Desktop\DOC_AN_DET\Dataset_F_2.csv"

@st.cache_data
def get_city_coordinates(cities):
    """Get latitude and longitude for cities using GeoPy"""
    geolocator = Nominatim(user_agent="fraud_dashboard")
    coordinates = {}
    
    for city in cities:
        try:
            location = geolocator.geocode(f"{city}, USA")
            if location:
                coordinates[city] = {
                    'lat': location.latitude,
                    'lon': location.longitude
                }
            time.sleep(0.1)  
        except:
            continue
    
    return coordinates

def load_csv_data():
    """Load your CSV data"""
    try:
        if os.path.exists(CSV_FILE):
            df = pd.read_csv(CSV_FILE)
            df['DateTime'] = pd.to_datetime(df['DateTime'])
            # Create Month-Year column for filtering
            df['Month-Year'] = df['DateTime'].dt.to_period('M').astype(str)
            return df
        else:
            st.warning(f"CSV file '{CSV_FILE}' not found.")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Error loading CSV: {str(e)}")
        return pd.DataFrame()
    
# Initialize session state for interactivity
if 'selected_detail' not in st.session_state:
    st.session_state.selected_detail = None
if 'show_customer_details' not in st.session_state:
    st.session_state.show_customer_details = False
if 'show_transaction_details' not in st.session_state:
    st.session_state.show_transaction_details = False


# Dashboard Header
st.markdown('<h1 style="margin-bottom:20px;"><i class="fas fa-chart-line"></i> AI Anomaly Insights</h1>', unsafe_allow_html=True)

df = load_csv_data()
if not df.empty:
    st.sidebar.markdown('<h3><i class="fas fa-calendar-alt"></i> Filter</h3>', unsafe_allow_html=True)

    # Convert Month-Year to datetime for slider comparison
    df['Month-Year'] = pd.to_datetime(df['DateTime'].dt.to_period('M').dt.to_timestamp())
    available_months = sorted(df['Month-Year'].dt.to_pydatetime())

    # Slider for selecting range
    start_month, end_month = st.sidebar.slider(
        "Select Range",
        min_value=available_months[0],
        max_value=available_months[-1],
        value=(available_months[0], available_months[-1]),
        format="MMM-YYYY"
    )

    selected_months = [
        m.strftime("%Y-%m") for m in available_months
        if start_month <= m <= end_month
    ]

    if selected_months:
        filtered_df = df[df['Month-Year'].dt.strftime("%Y-%m").isin(selected_months)]
        fraud_df = filtered_df[filtered_df['Legitimate'] == 0]

        col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1.2])

        # ---------- Customers ----------
        with col1:
            total_users = filtered_df['CustomerID'].nunique()
            st.markdown(f"<div style='font-size:18px; font-weight:bold; margin:0'><i class='fas fa-users'></i> Customers</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:26px;  margin:0'>{total_users:,}</div>", unsafe_allow_html=True)

        # ---------- Transactions ----------
        with col2:
            total_transactions = len(filtered_df)
            st.markdown(f"<div style='font-size:18px; font-weight:bold; margin:0'><i class='fas fa-credit-card'></i> Transactions</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:26px;  margin:0'>{total_transactions:,}</div>", unsafe_allow_html=True)

        # ---------- Legit ----------
        with col3:
            legit_count = filtered_df['Legitimate'].sum()
            st.markdown(f"<div style='font-size:18px; font-weight:bold; margin-bottom:4px'><i class='fas fa-check-circle' style='color:#00CC96'></i> Legit</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:26px;  margin:0'>{legit_count}</div>", unsafe_allow_html=True)

        # ---------- Fraud ----------
        with col4:
            fraud_count = len(fraud_df)
            st.markdown(f"<div style='font-size:18px; font-weight:bold; margin-bottom:4px'><i class='fas fa-exclamation-triangle' style='color:#FF4C4C'></i> Fraud</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:26px;  margin:0'>{fraud_count}</div>", unsafe_allow_html=True)

        with col5:
            # Hidden Streamlit button
            if st.button("Customer Details", key="customers_btn"):
                st.session_state.show_customer_details = not st.session_state.show_customer_details

            # Style the button using CSS
            st.markdown("""
                <style>
                div.stButton > button:first-child {
                    font-weight:bold;
                    font-size:16px;
                    width:100%;
                    padding:8px;
                    border-radius:6px;
                    background-color:#667eea;
                    color:white;
                    border:none;
                }
                div.stButton > button:first-child:hover {
                    background-color:#5a67d8;
                }
                </style>
            """, unsafe_allow_html=True)

        # SHOW DETAILS BASED ON BUTTON CLICKS
        if st.session_state.show_customer_details:
            with st.expander("**Customer Analysis Details**", expanded=True):
                st.markdown('<h4><i class="fas fa-users"></i> Customer Analysis Details</h4>', unsafe_allow_html=True)
                customer_stats = filtered_df.groupby('CustomerID').agg({
                    'Amount': ['count', 'sum', 'mean'],
                    'Legitimate': lambda x: (x == 0).sum(),  
                    'TransactionLocationCity': 'nunique'
                }).round(2)
                customer_stats.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Fraud_Count', 'Cities']
                customer_stats['Fraud_Rate'] = (customer_stats['Fraud_Count'] / customer_stats['Transactions'] * 100).round(1)
                customer_stats = customer_stats.sort_values('Total_Amount', ascending=False).head(20)
                
                st.write("**Top 20 Customers by Transaction Volume:**")
                st.dataframe(customer_stats, use_container_width=True)
                
                # Quick stats
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Highest Spender", f"${customer_stats['Total_Amount'].max():,.2f}")
                with col2:
                    st.metric("Most Active", f"{customer_stats['Transactions'].max()} transactions")
                with col3:
                    avg_fraud_rate = customer_stats['Fraud_Rate'].mean()
                    st.metric("Avg Fraud Rate", f"{avg_fraud_rate:.1f}%")

        if st.session_state.show_transaction_details:
            with st.expander("**Transaction Timeline Analysis**", expanded=True):
                st.markdown('<h4><i class="fas fa-credit-card"></i> Transaction Timeline Analysis</h4>', unsafe_allow_html=True)
                # Daily transaction trends
                daily_stats = filtered_df.groupby(filtered_df['DateTime'].dt.date).agg({
                    'Amount': ['count', 'sum'],
                    'Legitimate': lambda x: (x == 0).sum()
                }).round(2)
                daily_stats.columns = ['Transaction_Count', 'Total_Amount', 'Fraud_Count']
                daily_stats['Fraud_Rate'] = (daily_stats['Fraud_Count'] / daily_stats['Transaction_Count'] * 100).round(1)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Daily Transaction Volume:**")
                    st.line_chart(daily_stats['Transaction_Count'])
                with col2:
                    st.write("**Daily Fraud Rate (%):**")
                    st.line_chart(daily_stats['Fraud_Rate'])

        if filtered_df['DateTime'].dtype != 'datetime64[ns]':
            filtered_df['DateTime'] = pd.to_datetime(filtered_df['DateTime'])
        if 'fraud_df' in globals():
            if fraud_df['DateTime'].dtype != 'datetime64[ns]':
                fraud_df['DateTime'] = pd.to_datetime(fraud_df['DateTime'])

        st.markdown("---")

        col1, col2, col3 = st.columns(3)

        with col1:
            status_counts = filtered_df['Legitimate'].value_counts()
            labels = ['Fraud', 'Legitimate']
            values = [status_counts.get(0, 0), status_counts.get(1, 0)]

            fig1 = px.pie(
                names=labels,
                values=values,
                color=labels, 
                hole=0.4,
                color_discrete_map={'Fraud': '#FF4C4C', 'Legitimate': '#00CC96'}
            )

            fig1.update_traces(
                textposition='inside',
                textinfo='percent+label',
                textfont_size=14
            )
            fig1.update_layout(height=400, title_font_size=16,title=dict(
                            text="Fraud vs Legitimate Transactions",          
                            font=dict(size=20, color='black', family='Arial Black'), 
                            x=0.5,                                 
                            xanchor='center'),)

            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            if not fraud_df.empty:
                line_df = fraud_df.copy()
                line_df['Month'] = line_df['DateTime'].dt.to_period('M').astype(str)
                monthly_trend = line_df.groupby('Month')['Amount'].sum().reset_index()
                fig2 = px.line(
                    monthly_trend,
                    x='Month',
                    y='Amount',
                    markers=True,
                    labels={'Amount':'Total Fraud Amount'},
                    color_discrete_sequence=['#FF5733']
                )
                fig2.update_layout(height=400, xaxis_tickangle=-45,title=dict(
                            text="Monthly Fraud Amount Trend",          
                            font=dict(size=20, color='black', family='Arial Black'), 
                            x=0.5,                                 
                            xanchor='center'),)
                st.plotly_chart(fig2, use_container_width=True)
            else:
                st.info("No fraud transactions for trend chart")

        with col3:
            numeric_cols = ['Amount','BalanceAfter','AvgDailyBalance','Legitimate']
            possible_cols = [col for col in filtered_df.columns if filtered_df[col].dtype in [np.int64,np.float64]]
            extra_cols = [c for c in possible_cols if c not in numeric_cols][:6]
            numeric_cols.extend(extra_cols)
            
            if len(numeric_cols) >= 2:
                corr_df = filtered_df[numeric_cols].corr()
                fig3 = px.imshow(
                    corr_df,
                    color_continuous_scale='RdBu',  
                    aspect='auto'
                )
                fig3.update_layout(height=400, title_font_size=16,title=dict(
                            text="Fraud Data Correlation Heatmap",          
                            font=dict(size=20, color='black', family='Arial Black'), 
                            x=0.5,                                 
                            xanchor='center'),)
                st.plotly_chart(fig3, use_container_width=True)
            else:
                st.info("Not enough numeric columns for heatmap")

        col4, col5, col6 = st.columns(3)

        with col4:
            if not fraud_df.empty:
                usa_cities = load_usa_cities_coordinates()
                city_counts = fraud_df['TransactionLocationCity'].value_counts()
                map_data = []
                for city, count in city_counts.items():
                    if city in usa_cities:
                        lat, lon = usa_cities[city]
                        map_data.append({'City':city,'Count':count,'lat':lat,'lon':lon})
                if map_data:
                    df_map = pd.DataFrame(map_data)
                    fig4 = px.scatter_mapbox(
                        df_map,
                        lat='lat',
                        lon='lon',
                        size='Count',
                        color='Count',
                        hover_name='City',
                        hover_data={'Count':True,'lat':False,'lon':False},
                        color_continuous_scale='Reds',
                        size_max=20,
                        zoom=2.2,
                        center={'lat':39.5,'lon':-98.35},
                        mapbox_style='open-street-map'
                    )
                    fig4.update_layout(height=400, margin={"r":0,"t":50,"l":0,"b":0},title=dict(
                            text="Fraud Transactions by Cities",          
                            font=dict(size=20, color='black', family='Arial Black'), 
                            x=0.5,                                 
                            xanchor='center'),)
                    st.plotly_chart(fig4, use_container_width=True)
                else:
                    st.info("No USA cities found in fraud data")
            else:
                st.info("No fraud transactions found for selected period")

        with col5:
            if not fraud_df.empty:
                fraud_reasons = fraud_df['FraudReason'].value_counts().head(10)
                if not fraud_reasons.empty:
                    fraud_df_plot = pd.DataFrame({'FraudReason':fraud_reasons.index,'Count':fraud_reasons.values})
                    fraud_df_plot['ShortReason'] = fraud_df_plot['FraudReason'].apply(lambda x: x if len(x)<=25 else x[:22]+'...')
                    fig5 = px.bar(
                        fraud_df_plot,
                        x='Count',
                        y='ShortReason',
                        orientation='h',
                        color_discrete_sequence=["#E05A5A"],
                        hover_name='FraudReason',
                        hover_data={'ShortReason':False,'Count':True}
                    )
                    fig5.update_layout(
                        yaxis_title="Fraud Reason",
                        height=400,
                        title=dict(
                            text="Top Fraud Reasons",          
                            font=dict(size=20, color='black', family='Arial Black'), 
                            x=0.5,                                 
                            xanchor='center'),
                        
                        yaxis={'categoryorder':'total ascending'},
                        xaxis_type='log'
                    )
                    st.plotly_chart(fig5, use_container_width=True)
                else:
                    st.info("No fraud reason data available")
            else:
                st.info("No fraud transactions found for selected period")

        with col6:
            if not fraud_df.empty:
                sankey_df = fraud_df.copy()
                sankey_df['LegitStr'] = sankey_df['Legitimate'].map({1:'Legitimate',0:'Fraud'})
                sankey_cols = ['Type','Merchant','LegitStr','Gender']
                labels = []
                for col in sankey_cols:
                    labels.extend(list(sankey_df[col].unique()))
                labels = list(dict.fromkeys(labels))  
                label_to_idx = {label:i for i,label in enumerate(labels)}

                source = []
                target = []
                value = []

                for i in range(len(sankey_cols)-1):
                    group = sankey_df.groupby([sankey_cols[i], sankey_cols[i+1]]).size().reset_index(name='count')
                    for _, row in group.iterrows():
                        source.append(label_to_idx[row[sankey_cols[i]]])
                        target.append(label_to_idx[row[sankey_cols[i+1]]])
                        value.append(row['count'])

                fig6 = go.Figure(data=[go.Sankey(
                    node=dict(label=labels, pad=15, thickness=10, color='skyblue',line=dict(color='black', width=0.5)),
                    link=dict(source=source, target=target, value=value)
                )])
                fig6.update_layout(
                        title=dict(
                            text="Fraud Flow Sankey Diagram",          
                            font=dict(size=20, color='black', family='Arial Black'), 
                            x=0.5,                                    
                            xanchor='center'
                        ),
                        height=400,
                        width=1000,
                        font=dict(size=14, color='black', family='Arial'),
                        template=None
                    )

                st.plotly_chart(fig6)
            else:
                st.info("No fraud transactions found for Sankey diagram")
    
    else:
        st.sidebar.markdown('<p style="color:#ff9800;"><i class="fas fa-exclamation-circle"></i> No months selected. Please select at least one month.</p>', unsafe_allow_html=True)
        st.info("Please select at least one month from the sidebar to view the analysis.")

else:
    st.warning("No data available. Please upload your CSV file in the main fraud detection app.")
    
    uploaded_file = st.file_uploader(
        "Upload your fraud detection CSV file",
        type=['csv']
    )
    
    if uploaded_file is not None:
        with open(CSV_FILE, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("CSV file uploaded successfully!")
        st.rerun()

# FOOTER
st.markdown("""
    <div class='fixed-footer'>
        Where Innovation Meets Security &nbsp; | &nbsp;  Zero Tolerance for Fraud &nbsp; | &nbsp; © 2025 Xforia DAD 
    </div>
""", unsafe_allow_html=True)