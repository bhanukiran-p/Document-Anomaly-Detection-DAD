# DASHBOARD.py

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
from pandas.api.types import is_datetime64_any_dtype as is_datetime

# ---------- SPLASH FLAG ----------
if "show_splash" not in st.session_state:
    st.session_state.show_splash = False
if st.session_state.show_splash:
    show_splash()
    st.stop()

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="AI Anomaly Insights", layout="wide")

# ---------- SESSION STATE INITIALIZATION ----------
if 'selected_detail' not in st.session_state:
    st.session_state.selected_detail = None
if 'show_customer_details' not in st.session_state:
    st.session_state.show_customer_details = False
if 'show_transaction_details' not in st.session_state:
    st.session_state.show_transaction_details = False
if 'date_reset_counter' not in st.session_state:
    st.session_state.date_reset_counter = 0
if 'uploaded_data' not in st.session_state:
    st.session_state.uploaded_data = None
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'upload'
if 'show_preview' not in st.session_state:
    st.session_state.show_preview = False

# ---------- GLOBAL CSS ----------
st.markdown("""
    <style>
    /* Hide sidebar */
    [data-testid="stSidebar"], button[title*="sidebar"],
    section[data-testid="stSidebar"], [data-testid="stSidebarNav"],
    [data-testid="stSidebarCollapseButton"] { display: none !important; }

    /* Make app full-height for fixed footer */
    html, body, [data-testid="stApp"] { height: 100%; }
    [data-testid="stAppViewContainer"] { display:flex; flex-direction:column; min-height:100vh; }

    /* Reduce the top gap */
    header[data-testid="stHeader"] { height: 36px; background: transparent; }
    [data-testid="stAppViewContainer"] > .main { padding-top: 0 !important; }
    .main .block-container { padding-top: .25rem !important; margin-top: -.75rem !important; }

    /* FIXED footer */
    .fixed-footer {
        position: fixed; left: 0; right: 0; bottom: 0; height: 64px; z-index: 9999;
        background: #1e3c72; color: #fff; display: flex; justify-content: center; align-items: center; gap: 18px;
        font-weight: 700;
    }
    .with-footer { padding-bottom: 72px; }

    /* Fixed Logo */
    .fixed-logo {
        position: fixed;
        top: 6px;
        left: 60px;
        z-index: 2147482000;
        background: rgba(255,255,255,0.95);
        border-radius: 6px;
        padding: 4px 6px;
    }
    .fixed-logo img {
        width: 150px;
        height: 50px;
        display: block;
        cursor: pointer;
    }
    @media (max-width: 768px) {
        .fixed-logo {
            left: 56px;
            top: 6px;
        }
    }

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
        padding: 0 32px 0 220px;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.08);
    }

    .header-left {
        display: flex;
        align-items: center;
        gap: 20px;
    }

    .header-title {
        color: #1e3c72;
        font-size: 1.5rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        margin: 0;
    }

    /* Upload Box Styling */
    .upload-box {
        background: #1e3c72;
        color: #fff;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.12);
    }
    .upload-box h2 {
        font-size: 1.3rem;
        margin: 0 0 8px 0;
    }
    .upload-box p {
        font-size: 0.9rem;
        margin: 0;
        opacity: 0.95;
    }

    /* Preview Box */
    .preview-box {
        background: #f8f9fa;
        border: 2px solid #e2e8f0;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }
    .preview-header {
        color: #1e3c72;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .preview-stats {
        display: flex;
        gap: 20px;
        margin-bottom: 15px;
        flex-wrap: wrap;
    }
    .stat-item {
        background: white;
        padding: 10px 15px;
        border-radius: 6px;
        border: 1px solid #dee2e6;
    }
    .stat-label {
        font-size: 0.85rem;
        color: #6c757d;
        margin-bottom: 3px;
    }
    .stat-value {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1e3c72;
    }

    /* Compact headings + icons */
    .fa, .fas, .far, .fal, .fab { font-size: .9em; }
    h1, h2, h3, h4 { line-height: 1.15; }
    .kpi-title { font-size:16px; font-weight:700; margin:0 0 4px 0; }
    .kpi-value { font-size:22px; font-weight:600; margin:0; }

    /* Buttons */
    div.stButton > button:first-child { font-weight:700; font-size:14px; width:100%; padding:8px;
        border-radius:6px; background-color:#d0113a; color:#fff; border:none; }
    div.stButton > button:first-child:hover { background-color:#a00d2e; }

    /* Cards */
    .info-box { background: linear-gradient(135deg,#667eea 0%,#764ba2 100%); color:#fff; padding: 12px;
                border-radius:10px; margin:10px 0; box-shadow:0 4px 6px rgba(0,0,0,.08); }
    .detail-card { background:#f8f9fa; border:1px solid #dee2e6; border-radius:8px; padding:12px;
                   margin:10px 0; box-shadow:0 2px 4px rgba(0,0,0,.06); }
    
    /* Navigation Buttons */
    .nav-button {
        background: #d0113a;
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        border: none;
        font-weight: 700;
        font-size: 16px;
        cursor: pointer;
        transition: all 0.3s;
        display: inline-flex;
        align-items: center;
        gap: 8px;
    }
    .nav-button:hover {
        background: #a00d2e;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
""", unsafe_allow_html=True)

def add_fixed_logo():
    """Add fixed logo with back to home functionality"""
    import pathlib
    cwd = pathlib.Path(os.getcwd())
    here = pathlib.Path(__file__).parent if "__file__" in globals() else cwd
    candidates = [cwd / "FDN.png", here / "FDN.png", here / "assets" / "FDN.png", cwd / "assets" / "FDN.png"]
    logo_path = next((p for p in candidates if p.exists()), None)
    
    if logo_path:
        encoded = base64.b64encode(logo_path.read_bytes()).decode()
        st.markdown(f"""
            <div class="fixed-logo">
                <a href="/" target="_self">
                    <img src="data:image/png;base64,{encoded}" alt="FDN Logo" />
                </a>
            </div>
        """, unsafe_allow_html=True)

def add_header():
    """Add header section"""
    st.markdown("""
    <div class="app-header">
      <div class="header-left">
        <!-- Logo is now in fixed position via add_fixed_logo() -->
      </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- HELPERS ----------
def apply_title(fig, text):
    """Center title and add top margin so titles never clip."""
    fig.update_layout(
        title=dict(text=text, x=0.5, xanchor="center", y=0.96, yanchor="top", font=dict(size=15)),
        margin=dict(t=70, r=10, l=10, b=10)
    )
    return fig

@st.cache_data
def get_city_coordinates(cities):
    geolocator = Nominatim(user_agent="fraud_dashboard")
    coordinates = {}
    for city in cities:
        try:
            location = geolocator.geocode(f"{city}, USA")
            if location:
                coordinates[city] = {'lat': location.latitude, 'lon': location.longitude}
            time.sleep(0.1)
        except Exception:
            continue
    return coordinates

@st.cache_data
def load_excel_data(uploaded_file):
    """Load data from uploaded Excel file"""
    try:
        df = pd.read_excel(uploaded_file)
        
        if 'DateTime' in df.columns:
            df['DateTime'] = pd.to_datetime(df['DateTime'], errors='coerce')
            df['Month-Year'] = df['DateTime'].dt.to_period('M').astype(str)
        
        return df
    except Exception as e:
        st.error(f"Error loading Excel file: {str(e)}")
        return pd.DataFrame()

def show_data_preview(df):
    """Display preview of uploaded data"""
    st.markdown("""
        <div class='preview-box'>
            <div class='preview-header'>
                <i class='fas fa-table'></i> Data Preview
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Statistics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
            <div class='stat-item'>
                <div class='stat-label'>Total Rows</div>
                <div class='stat-value'>{:,}</div>
            </div>
        """.format(len(df)), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='stat-item'>
                <div class='stat-label'>Total Columns</div>
                <div class='stat-value'>{}</div>
            </div>
        """.format(len(df.columns)), unsafe_allow_html=True)
    
    with col3:
        fraud_count = len(df[df['Legitimate'] == 0]) if 'Legitimate' in df.columns else 0
        st.markdown("""
            <div class='stat-item'>
                <div class='stat-label'>Fraud Transactions</div>
                <div class='stat-value'>{:,}</div>
            </div>
        """.format(fraud_count), unsafe_allow_html=True)
    
    with col4:
        date_range = ""
        if 'DateTime' in df.columns:
            min_date = df['DateTime'].min().strftime('%Y-%m-%d')
            max_date = df['DateTime'].max().strftime('%Y-%m-%d')
            date_range = f"{min_date} to {max_date}"
        st.markdown("""
            <div class='stat-item'>
                <div class='stat-label'>Date Range</div>
                <div class='stat-value' style='font-size:0.85rem;'>{}</div>
            </div>
        """.format(date_range if date_range else "N/A"), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Column information
    st.markdown("** Column Information:**")
    col_info = pd.DataFrame({
        'Column Name': df.columns,
        'Data Type': df.dtypes.astype(str),
        'Non-Null Count': df.count(),
        'Null Count': df.isnull().sum()
    })
    st.dataframe(col_info, use_container_width=True, height=200)
    
    # Sample data
    st.markdown("** First 10 Rows:**")
    st.dataframe(df.head(10), use_container_width=True, height=300)
    
    # Action buttons
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        if st.button("Proceed to Insights", key="proceed_to_insights", use_container_width=True):
            st.session_state.current_page = 'insights'
            st.session_state.uploaded_data = df
            st.rerun()
    
    with col2:
        if st.button("Upload Different File", key="upload_different", use_container_width=True):
            st.session_state.uploaded_data = None
            st.session_state.current_page = 'upload'
            st.rerun()

# Add both logo and header
add_fixed_logo()
add_header()

# ---------- CONTENT WRAPPER ----------
st.markdown("<div class='with-footer'>", unsafe_allow_html=True)

# ---------- PAGE ROUTING ----------
if st.session_state.current_page == 'upload':
    # ---------- UPLOAD PAGE ----------
    st.markdown('<h1 style="margin:2px 0 10px 0; font-size:28px;"><i class="fas fa-upload"></i> Data Upload</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='upload-box'>
        <h2><i class='fas fa-file-upload'></i> Upload Your Data File</h2>
        <p>Upload an Excel file (.xlsx, .xls) or CSV file containing your transaction data</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Choose a file", type=['xlsx', 'xls', 'csv'], label_visibility="collapsed")
    
    if uploaded_file is not None:
        with st.spinner('Loading and processing your data...'):
            # Load the data based on file type
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
                if 'DateTime' in df.columns:
                    df['DateTime'] = pd.to_datetime(df['DateTime'], errors='coerce')
                    df['Month-Year'] = df['DateTime'].dt.to_period('M').astype(str)
            else:
                df = load_excel_data(uploaded_file)
            
            if not df.empty:
                st.success(f"Successfully loaded {len(df):,} rows and {len(df.columns)} columns!")
                show_data_preview(df)
            else:
                st.error("Failed to load data. Please check your file format.")

elif st.session_state.current_page == 'insights':
    # ---------- INSIGHTS PAGE ----------
    st.markdown('<h1 style="margin:2px 0 10px 0; font-size:28px;"><i class="fas fa-chart-line"></i> AI Anomaly Insights</h1>', unsafe_allow_html=True)
    
    # Back button
    if st.button("Back to Upload", key="back_to_upload"):
        st.session_state.current_page = 'upload'
        st.rerun()
    
    df = st.session_state.uploaded_data
    
    if df is not None and not df.empty:
        min_date = df['DateTime'].min().date()
        max_date = df['DateTime'].max().date()

        # Filters + KPIs
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1,1,1,1,1,1.2,1])

        with col5:
            st.markdown("<div class='kpi-title'><i class='fas fa-calendar-alt'></i> Start Date</div>", unsafe_allow_html=True)
            start_date = st.date_input(
                "Start",
                min_date,
                min_value=min_date,
                max_value=max_date,
                key=f"start_date_{st.session_state.date_reset_counter}",
                label_visibility="collapsed"
            )

        with col6:
            col6a, col6b = st.columns([3,1])
            with col6a:
                st.markdown("<div class='kpi-title'><i class='fas fa-calendar-alt'></i> End Date</div>", unsafe_allow_html=True)
                end_date = st.date_input(
                    "End",
                    max_date,
                    min_value=min_date,
                    max_value=max_date,
                    key=f"end_date_{st.session_state.date_reset_counter}",
                    label_visibility="collapsed"
                )
            with col6b:
                st.markdown("<div class='kpi-title' style='visibility:hidden;'>.</div>", unsafe_allow_html=True)
                if st.button("🔄", key="reset_dates", help="Reset to default date range", use_container_width=True):
                    st.session_state.date_reset_counter += 1
                    st.rerun()

        filtered_df = df[(df['DateTime'].dt.date >= start_date) & (df['DateTime'].dt.date <= end_date)]
        fraud_df = filtered_df[filtered_df['Legitimate'] == 0]

        with col1:
            total_users = filtered_df['CustomerID'].nunique()
            st.markdown("<div class='kpi-title'><i class='fas fa-users'></i> Customers</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='kpi-value'>{total_users:,}</div>", unsafe_allow_html=True)

        with col2:
            total_transactions = len(filtered_df)
            st.markdown("<div class='kpi-title'><i class='fas fa-credit-card'></i> Transactions</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='kpi-value'>{total_transactions:,}</div>", unsafe_allow_html=True)

        with col3:
            legit_count = filtered_df['Legitimate'].sum()
            st.markdown("<div class='kpi-title'><i class='fas fa-check-circle' style='color:#00CC96'></i> Legit</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='kpi-value'>{legit_count}</div>", unsafe_allow_html=True)

        with col4:
            fraud_count = len(fraud_df)
            st.markdown("<div class='kpi-title'><i class='fas fa-exclamation-triangle' style='color:#FF4C4C'></i> Fraud</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='kpi-value'>{fraud_count}</div>", unsafe_allow_html=True)

        with col7:
            st.markdown("<div class='kpi-title' style='visibility:hidden;'>.</div>", unsafe_allow_html=True)
            if st.button("Customer Details", key="customers_btn"):
                st.session_state.show_customer_details = not st.session_state.show_customer_details

        # Customer details expander
        if st.session_state.show_customer_details:
            with st.expander("Customer Analysis Details", expanded=True):
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
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.metric("Highest Spender", f"${customer_stats['Total_Amount'].max():,.2f}")
                with c2:
                    st.metric("Most Active", f"{customer_stats['Transactions'].max()} transactions")
                with c3:
                    avg_fraud_rate = customer_stats['Fraud_Rate'].mean()
                    st.metric("Avg Fraud Rate", f"{avg_fraud_rate:.1f}%")

        # Transaction timeline
        if st.session_state.show_transaction_details:
            with st.expander("Transaction Timeline Analysis", expanded=True):
                daily_stats = filtered_df.groupby(filtered_df['DateTime'].dt.date).agg({
                    'Amount': ['count', 'sum'],
                    'Legitimate': lambda x: (x == 0).sum()
                }).round(2)
                daily_stats.columns = ['Transaction_Count', 'Total_Amount', 'Fraud_Count']
                daily_stats['Fraud_Rate'] = (daily_stats['Fraud_Count'] / daily_stats['Transaction_Count'] * 100).round(1)
                c1, c2 = st.columns(2)
                with c1:
                    st.write("**Daily Transaction Volume:**")
                    st.line_chart(daily_stats['Transaction_Count'])
                with c2:
                    st.write("**Daily Fraud Rate (%):**")
                    st.line_chart(daily_stats['Fraud_Rate'])

        # Ensure datetime types
        if 'DateTime' in filtered_df.columns and not is_datetime(filtered_df['DateTime']):
            filtered_df['DateTime'] = pd.to_datetime(filtered_df['DateTime'], errors='coerce')
        if (not fraud_df.empty) and ('DateTime' in fraud_df.columns) and not is_datetime(fraud_df['DateTime']):
            fraud_df['DateTime'] = pd.to_datetime(fraud_df['DateTime'], errors='coerce')

        st.markdown("---")

        # ---------- ROW 1 CHARTS ----------
        col1c, col2c, col3c = st.columns(3)

        with col1c:
            status_counts = filtered_df['Legitimate'].value_counts()
            labels = ['Fraud', 'Legitimate']
            values = [status_counts.get(0, 0), status_counts.get(1, 0)]
            fig1 = px.pie(
                names=labels, values=values, color=labels, hole=0.4,
                color_discrete_map={'Fraud': '#FF4C4C', 'Legitimate': '#00CC96'}
            )
            fig1.update_traces(textposition='inside', textinfo='percent+label', textfont_size=12)
            fig1.update_layout(height=360)
            apply_title(fig1, "Fraud vs Legitimate")
            st.plotly_chart(fig1, use_container_width=True)

        with col2c:
            if not fraud_df.empty:
                line_df = fraud_df.copy()
                line_df['Month'] = line_df['DateTime'].dt.to_period('M').astype(str)
                monthly_trend = line_df.groupby('Month')['Amount'].sum().reset_index()
                fig2 = px.line(
                    monthly_trend, x='Month', y='Amount', markers=True,
                    labels={'Amount': 'Total Fraud Amount'},
                    color_discrete_sequence=['#FF5733']
                )
                fig2.update_layout(height=360, xaxis_tickangle=-45)
                apply_title(fig2, "Monthly Fraud Amount")
                st.plotly_chart(fig2, use_container_width=True)
            else:
                st.info("No fraud transactions for trend chart")

        with col3c:
            numeric_cols = ['Amount','BalanceAfter','AvgDailyBalance','Legitimate']
            possible_cols = [c for c in filtered_df.columns if filtered_df[c].dtype in [np.int64, np.float64]]
            extra_cols = [c for c in possible_cols if c not in numeric_cols][:6]
            numeric_cols.extend(extra_cols)
            if len(numeric_cols) >= 2:
                corr_df = filtered_df[numeric_cols].corr()
                fig3 = px.imshow(corr_df, color_continuous_scale='RdBu', aspect='auto')
                fig3.update_layout(height=360)
                apply_title(fig3, "Correlation Heatmap")
                st.plotly_chart(fig3, use_container_width=True)
            else:
                st.info("Not enough numeric columns for heatmap")

        # ---------- ROW 2 CHARTS ----------
        col4c, col5c, col6c = st.columns(3)

        with col4c:
            if not fraud_df.empty:
                usa_cities = load_usa_cities_coordinates()
                city_counts = fraud_df['TransactionLocationCity'].value_counts()
                map_data = []
                for city, count in city_counts.items():
                    if city in usa_cities:
                        lat, lon = usa_cities[city]
                        map_data.append({'City': city, 'Count': count, 'lat': lat, 'lon': lon})
                if map_data:
                    df_map = pd.DataFrame(map_data)
                    fig4 = px.scatter_mapbox(
                        df_map, lat='lat', lon='lon', size='Count', color='Count',
                        hover_name='City', hover_data={'Count': True, 'lat': False, 'lon': False},
                        color_continuous_scale='Reds', size_max=18, zoom=2.2,
                        center={'lat': 39.5, 'lon': -98.35}, mapbox_style='open-street-map'
                    )
                    fig4.update_layout(height=360, margin={"r":0,"t":40,"l":0,"b":0})
                    apply_title(fig4, "Fraud by City")
                    st.plotly_chart(fig4, use_container_width=True)
                else:
                    st.info("No USA cities found in fraud data")
            else:
                st.info("No fraud transactions found for selected period")

        with col5c:
            if not fraud_df.empty:
                fraud_reasons = fraud_df['FraudReason'].value_counts().head(10)
                if not fraud_reasons.empty:
                    fraud_df_plot = pd.DataFrame({'FraudReason': fraud_reasons.index, 'Count': fraud_reasons.values})
                    fraud_df_plot['ShortReason'] = fraud_df_plot['FraudReason'].apply(lambda x: x if len(x) <= 25 else x[:22] + '...')
                    fig5 = px.bar(
                        fraud_df_plot, x='Count', y='ShortReason', orientation='h',
                        color_discrete_sequence=["#E05A5A"], hover_name='FraudReason',
                        hover_data={'ShortReason': False, 'Count': True}
                    )
                    fig5.update_layout(
                        yaxis_title="Fraud Reason", height=360,
                        yaxis={'categoryorder': 'total ascending'}, xaxis_type='log'
                    )
                    apply_title(fig5, "Top Fraud Reasons")
                    st.plotly_chart(fig5, use_container_width=True)
                else:
                    st.info("No fraud reason data available")
            else:
                st.info("No fraud transactions found for selected period")

        with col6c:
            if not fraud_df.empty:
                sankey_df = fraud_df.copy()
                sankey_df['LegitStr'] = sankey_df['Legitimate'].map({1: 'Legitimate', 0: 'Fraud'})
                sankey_cols = ['Type', 'Merchant', 'LegitStr', 'Gender']
                labels = []
                for col in sankey_cols:
                    labels.extend(list(sankey_df[col].unique()))
                labels = list(dict.fromkeys(labels))
                label_to_idx = {label: i for i, label in enumerate(labels)}
                source, target, value = [], [], []
                for i in range(len(sankey_cols) - 1):
                    group = sankey_df.groupby([sankey_cols[i], sankey_cols[i + 1]]).size().reset_index(name='count')
                    for _, row in group.iterrows():
                        source.append(label_to_idx[row[sankey_cols[i]]])
                        target.append(label_to_idx[row[sankey_cols[i + 1]]])
                        value.append(row['count'])

                fig6 = go.Figure(data=[go.Sankey(
                    arrangement='snap',
                    node=dict(
                        label=labels,
                        pad=12,
                        thickness=14,
                        color='rgba(135,206,235,0.65)',
                        line=dict(color='rgba(0,0,0,0.6)', width=0.5)
                    ),
                    link=dict(source=source, target=target, value=value),
                    textfont=dict(color='black', size=12)
                )])
                fig6.update_layout(
                    height=360,
                    font=dict(color='black', size=12),
                    paper_bgcolor='white',
                    plot_bgcolor='white'
                )
                apply_title(fig6, "Fraud Flow (Type → Merchant → Status → Gender)")
                st.plotly_chart(fig6, use_container_width=True)
            else:
                st.info("No fraud transactions found for Sankey diagram")
    else:
        st.warning("No data available. Please go back and upload a file.")
        if st.button("Go to Upload Page"):
            st.session_state.current_page = 'upload'
            st.rerun()

# ---------- FIXED FOOTER ----------
st.markdown("""
    </div>  <!-- close .with-footer -->
    <div style="padding:10px 16px; color:#fff; background:#1e3c72; display:flex; align-items:center; justify-content:center; gap:10px; box-shadow:0 -2px 10px rgba(0,0,0,.22); font-weight:600; position:fixed; left:0; right:0; bottom:0; height:64px; z-index:9999; font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,'Noto Sans';">
      <span>Where Innovation Meets Security</span>
      <span style="opacity:.6; padding:0 8px;">|</span>
      <span>Zero Tolerance for Fraud</span>
      <span style="opacity:.6; padding:0 8px;">|</span>
      <span>© Xforia DAD</span>
    </div>
""", unsafe_allow_html=True)