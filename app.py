import streamlit as st


st.title("📏  Unit Converter")

categories = ["Length", "Weight", "Temperature", "Volume", "Time", "Speed", "Pressure"]
selected_category = st.selectbox("Choose a Category", categories)

unit_con = {
     "Length": ["Meter", "Centimeter", "Kilometer", "Millimeter", "Inch", "Foot", "Yard", "Mile"],
    "Weight": ["Kilogram", "Gram", "Pound", "Ounce", "Ton"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Volume": ["Liter", "Milliliter", "Cubic Meter", "Gallon"],
    "Time": ["Second", "Minute", "Hour", "Day"],
    "Speed": ["Meter/Second", "Kilometer/Hour", "Mile/Hour"],
    "Pressure": ["Pascal", "Bar", "Atmosphere"]
}

units = unit_con[selected_category]

col1,col2 = st.columns(2)

with col1:
    form_unit = st.selectbox("From", units)


with col2:
    to_unit = st.selectbox("To", units)


input_value = st.number_input(f"Enter value in {form_unit}", value=1)

if st.button("convert"):

    conversion = {
         "Length": {
            "Meter": {"Meter": 1, "Centimeter": 100, "Kilometer": 0.001, "Millimeter": 1000, "Inch": 39.37, "Foot": 3.28084, "Yard": 1.09361, "Mile": 0.000621371},
            "Centimeter": {"Meter": 0.01, "Centimeter": 1, "Kilometer": 0.00001, "Millimeter": 10, "Inch": 0.393701, "Foot": 0.0328084, "Yard": 0.0109361, "Mile": 0.00000621371},
        },
        "Weight": {
            "Kilogram": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274, "Ton": 0.001},
            "Gram": {"Kilogram": 0.001, "Gram": 1, "Pound": 0.00220462, "Ounce": 0.035274, "Ton": 0.000001},
        },
        "Temperature": {
            "Celsius": {"Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15},
            "Fahrenheit": {"Celsius": lambda x: (x - 32) * 5/9, "Fahrenheit": lambda x: x, "Kelvin": lambda x: (x - 32) * 5/9 + 273.15},
        },
        "Volume": {
            "Liter": {"Liter": 1, "Milliliter": 1000, "Cubic Meter": 0.001, "Gallon": 0.264172},
            "Milliliter": {"Liter": 0.001, "Milliliter": 1, "Cubic Meter": 0.000001, "Gallon": 0.000264172},
        },
        "Time": {
            "Second": {"Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400},
            "Minute": {"Second": 60, "Minute": 1, "Hour": 1/60, "Day": 1/1440},
        },
        "Speed": {
            "Meter/Second": {"Meter/Second": 1, "Kilometer/Hour": 3.6, "Mile/Hour": 2.23694},
            "Kilometer/Hour": {"Meter/Second": 0.277778, "Kilometer/Hour": 1, "Mile/Hour": 0.621371},
        },
        "Pressure": {
            "Pascal": {"Pascal": 1, "Bar": 0.00001, "Atmosphere": 9.8692e-6},
            "Bar": {"Pascal": 100000, "Bar": 1, "Atmosphere": 0.986923},
        }
    }
    
    if selected_category == "Temperature":
        convert_value = conversion[selected_category][form_unit][to_unit](input_value)
    else:
        convert_value = input_value * conversion[selected_category][form_unit][to_unit]

    st.markdown(f"## {input_value} {form_unit} = {convert_value:.5f} {to_unit}")