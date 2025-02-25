import streamlit as st


st.title("📏 Length Converter")

units = ["Meter", "Centimeter", "Kilometer", "Millimeter", "Inch", "Foot", "Yard", "Mile"]

col1,col2 = st.columns(2)

with col1:
    form_unit = st.selectbox("From", units)


with col2:
    to_unit = st.selectbox("To", units)


input_value = st.number_input(f"Enter value in {form_unit}", value=1)

if st.button("convert"):

    conversion = {
    "Meter": {"Meter": 1, "Centimeter": 100, "Kilometer": 0.001, "Millimeter": 1000, "Inch": 39.3701, "Foot": 3.28084, "Yard": 1.09361, "Mile": 0.000621371},
    "Centimeter": {"Meter": 0.01, "Centimeter": 1, "Kilometer": 0.00001, "Millimeter": 10, "Inch": 0.393701, "Foot": 0.0328084, "Yard": 0.0109361, "Mile": 0.00000621371},
    "Kilometer": {"Meter": 1000, "Centimeter": 100000, "Kilometer": 1, "Millimeter": 1e6, "Inch": 39370.1, "Foot": 3280.84, "Yard": 1093.61, "Mile": 0.621371},
    "Millimeter": {"Meter": 0.001, "Centimeter": 0.1, "Kilometer": 1e-6, "Millimeter": 1, "Inch": 0.0393701, "Foot": 0.00328084, "Yard": 0.00109361, "Mile": 6.2137e-7},
    "Inch": {"Meter": 0.0254, "Centimeter": 2.54, "Kilometer": 0.0000254, "Millimeter": 25.4, "Inch": 1, "Foot": 0.0833333, "Yard": 0.0277778, "Mile": 0.0000157828},
    "Foot": {"Meter": 0.3048, "Centimeter": 30.48, "Kilometer": 0.0003048, "Millimeter": 304.8, "Inch": 12, "Foot": 1, "Yard": 0.333333, "Mile": 0.000189394},
    "Yard": {"Meter": 0.9144, "Centimeter": 91.44, "Kilometer": 0.0009144, "Millimeter": 914.4, "Inch": 36, "Foot": 3, "Yard": 1, "Mile": 0.000568182},
    "Mile": {"Meter": 1609.34, "Centimeter": 160934, "Kilometer": 1.60934, "Millimeter": 1.609e6, "Inch": 63360, "Foot": 5280, "Yard": 1760, "Mile": 1},
}
    
    convert_value = input_value * conversion[form_unit][to_unit]

    st.markdown(f"## {input_value} {form_unit} = {convert_value:.5f} {to_unit}")
