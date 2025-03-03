import streamlit as st
from pint import UnitRegistry
ureg = UnitRegistry()
st.set_page_config(page_title="Unit Converter", layout="centered")
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f4f4f4;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            max-width: 500px;
            margin: auto;
            text-align: center;
        }
        .stButton button {
            color: black;
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
            width: 100%;
        }
        .stButton button:hover {
            background-color: green
        }
        .result-box {
            background-color: white;
            padding: 15px;
            border-radius: 8px;
            font-size:20px;
            font-weight: bold;
            color: #333;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)

##name 
st.markdown("<h1> Unit Converter </h1>", unsafe_allow_html=True)

##categories
categories = {
    "Length": ["meter", "kilometer", "mile", "yard", "foot", "inch"],
    "Weight": ["gram", "kilogram", "pound", "ounce", "ton"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Speed": ["meter per second", "kilometer per hour", "mile per hour", "knot"],
    "Volume": ["liter", "milliliter", "cubic meter", "gallon"],
    "Time": ["second", "minute", "hour", "day"]
}

category = st.selectbox("Select Category", list(categories.keys()))
value = st.number_input("Enter Value", min_value=0.0, format="%.f")
from_unit = st.selectbox("From", categories[category])
to_unit = st.selectbox("To", categories[category])

def convert(value, from_unit, to_unit):
    try:
        return (value * ureg(from_unit)).to(to_unit).magnitude
    except:
        return None
if st.button("Convert"):
    result = convert(value, from_unit, to_unit)
    if result is not None:
        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
    else:
        st.error("Invalid conversion!")

