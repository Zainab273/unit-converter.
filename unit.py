import streamlit as st

conversions = {
    "Length": {
        "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Micrometers": 1e6, "Nanometers": 1e9,
        "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701, "Nautical Miles": 0.000539957
    },
    "Weight": {
        "Kilograms": 1, "Grams": 1000, "Milligrams": 1e6, "Micrograms": 1e9, "Pounds": 2.20462, "Ounces": 35.274, 
        "Stones": 0.157473, "Tons (Metric)": 0.001, "Tons (US)": 0.00110231
    },
    "Temperature": None,
    "Volume": {
        "Liters": 1, "Milliliters": 1000, "Cubic Meters": 0.001, "Cubic Centimeters": 1000,
        "Cubic Inches": 61.0237, "Cubic Feet": 0.0353147, "Cubic Yards": 0.00130795, "Gallons (US)": 0.264172,
        "Gallons (UK)": 0.219969, "Pints (US)": 2.11338, "Pints (UK)": 1.75975
    },
    "Speed": {
        "Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694,
        "Knots": 1.94384, "Feet per second": 3.28084
    },
    "Time": {
        "Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400,
        "Weeks": 1/604800, "Months": 1/2.628e6, "Years": 1/3.154e7
    },
    "Energy": {
        "Joules": 1, "Kilojoules": 0.001, "Calories": 0.239006, "Kilocalories": 0.000239006,
        "Watt-hours": 0.000277778, "Kilowatt-hours": 2.77778e-7, "Electronvolts": 6.242e18, "BTU": 0.000947817
    },
    "Pressure": {
        "Pascals": 1, "Kilopascals": 0.001, "Bars": 1e-5, "Atmospheres": 9.86923e-6,
        "Millimeters of Mercury": 0.00750062, "Pounds per Square Inch": 0.000145038
    },
    "Power": {
        "Watts": 1, "Kilowatts": 0.001, "Megawatts": 1e-6, "Horsepower": 0.00134102,
        "BTU per hour": 3.41214
    },
    "Data Storage": {
        "Bits": 1, "Bytes": 0.125, "Kilobytes": 0.000125, "Megabytes": 1.25e-7,
        "Gigabytes": 1.25e-10, "Terabytes": 1.25e-13, "Petabytes": 1.25e-16
    }
}

def convert_units(category, unit_from, unit_to, value):
    if category == "Temperature":
        if unit_from == "Celsius" and unit_to == "Fahrenheit":
            return (value * 9/5) + 32
        elif unit_from == "Fahrenheit" and unit_to == "Celsius":
            return (value - 32) * 5/9
        elif unit_from == "Celsius" and unit_to == "Kelvin":
            return value + 273.15
        elif unit_from == "Kelvin" and unit_to == "Celsius":
            return value - 273.15
        elif unit_from == "Fahrenheit" and unit_to == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif unit_from == "Kelvin" and unit_to == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    
    factor_from = conversions[category][unit_from]
    factor_to = conversions[category][unit_to]
    return (value / factor_from) * factor_to

st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
st.title("🔄 Classic Unit Converter")
st.markdown("### Convert between different units easily")

category = st.selectbox("Select Category", list(conversions.keys()))

units = list(conversions[category].keys()) if category != "Temperature" else ["Celsius", "Fahrenheit", "Kelvin"]

unit_from = st.selectbox("From", units)
unit_to = st.selectbox("To", units)
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
if st.button("Convert"):
    result = convert_units(category, unit_from, unit_to, value)
    st.success(f"{value} {unit_from} is equal to {result:.2f} {unit_to}")
