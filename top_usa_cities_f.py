import streamlit as st
@st.cache_data
def load_usa_cities_coordinates():
    """Load coordinates for real USA cities found in your dataset"""
    return {
        'Austin': (30.2672, -97.7431),
        'Los Angeles': (34.0522, -118.2437), 
        'New York': (40.7128, -74.0060),
        'Phoenix': (33.4484, -112.0740),
        'Houston': (29.7604, -95.3698),
        'Columbus': (39.9612, -82.9988),
        'San Diego': (32.7157, -117.1611),
        'Chicago': (41.8781, -87.6298),
        'San Francisco': (37.7749, -122.4194),
        'Indianapolis': (39.7684, -86.1581),
        'San Antonio': (29.4241, -98.4936),
        'Dallas': (32.7767, -96.7970),
        'Miami': (25.7617, -80.1918),
        'Philadelphia': (39.9526, -75.1652),
        'Jacksonville': (30.3322, -81.6557),
        'Fort Worth': (32.7555, -97.3308),
        'Charlotte': (35.2271, -80.8431),
        'Seattle': (47.6062, -122.3321),
        'Denver': (39.7392, -104.9903),
        'Boston': (42.3601, -71.0589)
    }
