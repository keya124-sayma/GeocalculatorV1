import streamlit as st
import numpy as np

st.set_page_config(page_title="Geotechnical Calculator", layout="centered")

st.title("🧱 Geotechnical Engineering Calculator")
st.sidebar.header("Input Parameters")

# Input fields
H = st.sidebar.number_input("Clay layer thickness H (m)", value=5.0)
Cv = st.sidebar.number_input("Cv (m²/day)", value=1e-7, format="%.1e")
t = st.sidebar.number_input("Time t (days)", value=180.0)
p = st.sidebar.number_input("Δσ (Applied pressure) in kPa", value=100.0)
e0 = st.sidebar.number_input("Initial void ratio e₀", value=0.8)
Cc = st.sidebar.number_input("Compression index Cc", value=0.25)
σ0 = st.sidebar.number_input("Initial stress σ₀ (kPa)", value=150.0)

# Bearing capacity inputs
B = st.sidebar.number_input("Width B (m)", value=2.0)
Df = st.sidebar.number_input("Foundation depth Df (m)", value=1.0)
γ = st.sidebar.number_input("Unit weight γ (kN/m³)", value=18.0)
c = st.sidebar.number_input("Cohesion c (kPa)", value=25.0)
φ = st.sidebar.slider("Friction angle φ (°)", 0.0, 45.0, 30.0)

# Calculations
# Calculations (Cv in m²/day)
Tv = (Cv * t) / (H / 2) ** 2

U = np.sqrt(Tv / np.pi) * 100
sc = (Cc / (1 + e0)) * H * np.log10((σ0 + p) / σ0)

Nc = 5.14 if φ == 0 else 37.16
Nq = np.exp(np.pi * np.tan(np.radians(φ))) * np.tan(np.radians(45 + φ / 2)) ** 2
Ngamma = 2 * (Nq + 1) * np.tan(np.radians(φ))
qult = c * Nc + γ * Df * Nq + 0.5 * γ * B * Ngamma

# Display results
st.markdown("## 📊 Results")
st.write(f"**Time Factor (Tv)**: `{Tv:.4f}`")
st.write(f"**Degree of Consolidation (U)**: `{U:.2f}%`")
st.write(f"**Consolidation Settlement (Sc)**: `{sc:.3f} m`")
st.write(f"**Ultimate Bearing Capacity (qult)**: `{qult:.2f} kPa`")
