import streamlit as st
import pickle
import pandas as pd
import numpy as np

model = pickle.load(open("./model/model.pkl","rb"))

def convert_currency_simple(eur_amount, target_currency):
    # Approximate exchange rates as of mid-2025
    rates = {
        'EUR': 1.0,
        'INR': 90.0,
        'USD': 1.07,
        'GBP': 0.85,
        'JPY': 165.0
    }
    symbols = {
        'EUR': '€',
        'INR': '₹',
        'USD': '$',
        'GBP': '£',
        'JPY': '¥'
    }
    rate = rates.get(target_currency, 1.0)
    symbol = symbols.get(target_currency, '')

    return eur_amount * rate, rate, symbol
st.header("Know Your Laptop's Worth")
st.markdown("Enter laptop specs below to predict the **price**.")
with st.form("laptop_form"):
    col1, col2 = st.columns(2)

    with col1:
        company = st.selectbox("Brand", ['Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo', 'Chuwi', 'MSI', 'Microsoft', 'Toshiba', 'Huawei', 'Xiaomi', 'Vero', 'Razer', 'Mediacom', 'Samsung', 'Google', 'Fujitsu', 'LG'])
        typename = st.selectbox("Laptop Type", ['Ultrabook', 'Notebook', 'Gaming', '2 in 1 Convertible', 'Netbook', 'Workstation'])
        ram = st.slider("RAM (GB)", 2, 64, step=2)
        weight = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0, step=0.1)
        touchscreen = st.radio("Touchscreen", ['No', 'Yes'])
        ips = st.radio("IPS Display", ['No', 'Yes'])

    with col2:
        screen_size = st.number_input("Screen Size (inches)", min_value=10.0, max_value=18.0, step=0.1)
        resolution = st.selectbox("Screen Resolution", ['1920x1080', '1366x768', '1600x900', '2560x1440', '3840x2160'])
        cpu_brand = st.selectbox("CPU", ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'AMD Processor', 'Other Intel Processor'])
        gpu = st.selectbox("GPU", ['Intel', 'Nvidia', 'AMD', 'Other'])
        os = st.selectbox("Operating System", ['Windows', 'MacOS', 'Linux', 'Other OS', 'No OS'])

    hdd = st.slider("HDD (GB)", 0, 2000, step=256)
    ssd = st.slider("SSD (GB)", 0, 2000, step=256)
    flash_storage = st.slider("Flash Storage (GB)", 0, 512, step=64)
    clock_speed = st.slider("CPU Clock Speed (GHz)", 0.5, 5.0, step=0.1)
    
    currency = st.selectbox("Select currency", ['EUR', 'INR', 'USD', 'GBP', 'JPY'])
    submitted = st.form_submit_button("Predict Price 💸")

# --- On submit ---
if submitted:
    # Convert to numerical
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    # Calculate PPI (pixels per inch)
    X_res, Y_res = map(int, resolution.split('x'))
    ppi = ((X_res ** 2 + Y_res ** 2) ** 0.5) / screen_size

    # Prepare input as DataFrame
    input_data = pd.DataFrame({
        'Company': [company],
        'TypeName': [typename],
        'Ram': [ram],
        'Weight': [weight],
        'TouchScreen': [touchscreen],
        'IPS': [ips],
        'PPI': [ppi],
        'CPU clock speed': [clock_speed],
        'CPU brand': [cpu_brand],
        'Gpu': [gpu],
        'Operating_System': [os],
        'HDD': [hdd],
        'SSD': [ssd],
        'Flash_Storage': [flash_storage]
    })

    # Predict
    predicted_eur = model.predict(input_data)[0]
    converted_price, rate, symbol = convert_currency_simple(predicted_eur, currency)
    st.success(f"Estimated Price: {symbol} {np.round(converted_price, 2):,} ({currency})")
    
    # Optionally show input summary
    with st.expander("🔍 View Input Summary"):
        st.dataframe(input_data.astype(str).T.rename(columns={0: "Value"}))