import streamlit as st
import requests
import json


st.title("📏 Unit Converter")

# agar user dropdown menu ya kise button par click karry ga to app reload ho ta hai ye page app ko reload sy lokta hai
if "selected_mode" not in st.session_state:
    st.session_state.selected_mode = None



# is main user select karry ga ky wo manual convert karry ga ya AI sa kawaye ga
manage_unit = ["Ai Convert Unit", "Manual Convert Unit"]
selete_unit = st.selectbox("Choose Option", manage_unit) # jo user selete karry ga wo is main aye ga


# When user selects an option, store it in session state
if st.button("Select"):
    st.session_state.selected_mode = selete_unit # is ky anadr jo user uppar selete karry ga wo is main save hoye ga



# agar user manual selete karry ga to ye show ho ye ga
if st.session_state.selected_mode == "Manual Convert Unit":

    categories = ["Length", "Weight", "Temperature", "Volume", "Time", "Speed", "Pressure"] 
    selected_category = st.selectbox("Choose a Category", categories) # is user categories main selete karry ga wo is main save hogaye ga

    unit_con = {
        "Length": ["Meter", "Centimeter", "Kilometer", "Millimeter", "Inch", "Foot", "Yard", "Mile"],
        "Weight": ["Kilogram", "Gram", "Pound", "Ounce", "Ton"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
        "Volume": ["Liter", "Milliliter", "Cubic Meter", "Gallon"],
        "Time": ["Second", "Minute", "Hour", "Day"],
        "Speed": ["Meter/Second", "Kilometer/Hour", "Mile/Hour"],
        "Pressure": ["Pascal", "Bar", "Atmosphere"]
    }

    units = unit_con[selected_category] # selected_category ky andar jo user ny selete kia hoye ga wo unit_con ky andar pass kia hai

    col1, col2 = st.columns(2)

    with col1:
        form_unit = st.selectbox("From", units)

    with col2:
        to_unit = st.selectbox("To", units)

    input_value = st.number_input(f"Enter value in {form_unit}", value=1.0) # ye input field hai is main user number dy ga

    if st.button("Convert"):
        # is main sary formula h
        conversion = {
            "Length": {
                "Meter": {"Meter": 1, "Centimeter": 100, "Kilometer": 0.001, "Millimeter": 1000, "Inch": 39.37, "Foot": 3.28084, "Yard": 1.09361, "Mile": 0.000621371},
                "Centimeter": {"Meter": 0.01, "Centimeter": 1, "Kilometer": 0.00001, "Millimeter": 10, "Inch": 0.393701, "Foot": 0.0328084, "Yard": 0.0109361, "Mile": 0.00000621371},
                "Kilometer": {"Meter": 1000, "Centimeter": 100000, "Kilometer": 1, "Millimeter": 1000000, "Inch": 39370.1, "Foot": 3280.84, "Yard": 1093.61, "Mile": 0.621371},
                "Millimeter": {"Meter": 0.001, "Centimeter": 0.1, "Kilometer": 0.000001, "Millimeter": 1, "Inch": 0.0393701, "Foot": 0.00328084, "Yard": 0.00109361, "Mile": 0.000000621371},
                "Inch": {"Meter": 0.0254, "Centimeter": 2.54, "Kilometer": 0.0000254, "Millimeter": 25.4, "Inch": 1, "Foot": 0.0833333, "Yard": 0.0277778, "Mile": 0.0000157828},
                "Foot": {"Meter": 0.3048, "Centimeter": 30.48, "Kilometer": 0.0003048, "Millimeter": 304.8, "Inch": 12, "Foot": 1, "Yard": 0.333333, "Mile": 0.000189394},
                "Yard": {"Meter": 0.9144, "Centimeter": 91.44, "Kilometer": 0.0009144, "Millimeter": 914.4, "Inch": 36, "Foot": 3, "Yard": 1, "Mile": 0.000568182},
                "Mile": {"Meter": 1609.34, "Centimeter": 160934, "Kilometer": 1.60934, "Millimeter": 1609340, "Inch": 63360, "Foot": 5280, "Yard": 1760, "Mile": 1},
            },
            "Weight": {
                "Kilogram": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274, "Ton": 0.001},
                "Gram": {"Kilogram": 0.001, "Gram": 1, "Pound": 0.00220462, "Ounce": 0.035274, "Ton": 0.000001},
                "Pound": {"Kilogram": 0.453592, "Gram": 453.592, "Pound": 1, "Ounce": 16, "Ton": 0.0005},
                "Ounce": {"Kilogram": 0.0283495, "Gram": 28.3495, "Pound": 0.0625, "Ounce": 1, "Ton": 0.00003125},
                "Ton": {"Kilogram": 1000, "Gram": 1000000, "Pound": 2204.62, "Ounce": 35274, "Ton": 1},
            },
            "Temperature": {
                "Celsius": {"Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15},
                "Fahrenheit": {"Celsius": lambda x: (x - 32) * 5/9, "Fahrenheit": lambda x: x, "Kelvin": lambda x: (x - 32) * 5/9 + 273.15},
                "Kelvin": {"Celsius": lambda x: x - 273.15, "Fahrenheit": lambda x: (x - 273.15) * 9/5 + 32, "Kelvin": lambda x: x},
            },
            "Volume": {
                "Liter": {"Liter": 1, "Milliliter": 1000, "Cubic Meter": 0.001, "Gallon": 0.264172},
                "Milliliter": {"Liter": 0.001, "Milliliter": 1, "Cubic Meter": 0.000001, "Gallon": 0.000264172},
                "Cubic Meter": {"Liter": 1000, "Milliliter": 1000000, "Cubic Meter": 1, "Gallon": 264.172},
                "Gallon": {"Liter": 3.78541, "Milliliter": 3785.41, "Cubic Meter": 0.00378541, "Gallon": 1},
            },
            "Time": {
                "Second": {"Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400},
                "Minute": {"Second": 60, "Minute": 1, "Hour": 1/60, "Day": 1/1440},
                "Hour": {"Second": 3600, "Minute": 60, "Hour": 1, "Day": 1/24},
                "Day": {"Second": 86400, "Minute": 1440, "Hour": 24, "Day": 1},
            },
            "Speed": {
                "Meter/Second": {"Meter/Second": 1, "Kilometer/Hour": 3.6, "Mile/Hour": 2.23694},
                "Kilometer/Hour": {"Meter/Second": 0.277778, "Kilometer/Hour": 1, "Mile/Hour": 0.621371},
                "Mile/Hour": {"Meter/Second": 0.44704, "Kilometer/Hour": 1.60934, "Mile/Hour": 1},
            },
            "Pressure": {
                "Pascal": {"Pascal": 1, "Bar": 0.00001, "Atmosphere": 9.8692e-6},
                "Bar": {"Pascal": 100000, "Bar": 1, "Atmosphere": 0.986923},
                "Atmosphere": {"Pascal": 101325, "Bar": 1.01325, "Atmosphere": 1},
            },
        }
        
        try:
            if selected_category == "Temperature": # Temperature ka alak method sy ho ta hai is liye is ko alak dia hai
                convert_value = conversion[selected_category][form_unit][to_unit](input_value)
            else: 
                # is ky andar Temperature ky ye wala or sab aye gy
                convert_value = input_value * conversion[selected_category][form_unit][to_unit]

            st.success(f"## {input_value} {form_unit} = {convert_value:.5f} {to_unit}") # is ky andar answer aye ga

        except KeyError:
            st.error("Invalid conversion. Please check the units.")





#  agar user AI selete karry ga to ye show hoye ga
elif st.session_state.selected_mode == "Ai Convert Unit":



    DEEPSEEK_API_URL = "https://openrouter.ai/api/v1/chat/completions" # ye api ka endpoint hai
    API_KEY = "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" # is ky andar .streamlit\secrets.toml sy R1 ki key arahe hai

    st.title("Convert Unit With The Help Of Ai")

    user_input = st.text_input("Enter") # is ky andar user prompt dy ga

    if st.button("Process"):
        if user_input:
            with st.spinner("Processing ..."):  # jab tak R1 sy data nhi aye ga ye show hoye ag

                headers = {
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://yourwebsite.com",
                    "X-Title": "DeepSeek App"
                }

                payload = {
                    "model": "deepseek/deepseek-r1:free",
                    "messages": [{"role": "user", "content": user_input}],
                    "temperature": 0.6,
                    "top_p": 0.7,
                    "top_k": 40
                }

                try:
                    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload, timeout=10)  # Increased timeout
                    if response.status_code == 200:
                        data = response.json()
                        print("API Response:", data)  # Debugging: Print API response
                        if "choices" in data and data["choices"]:
                            message = data["choices"][0].get("message", {}).get("content", "No response.")
                            st.success("Data processed successfully!")
                            st.subheader("Assistant's Response:")
                            st.write(message)
                        else:
                            st.error("No valid response received. Check API response format.")
                    else:
                        st.error(f"Error {response.status_code}: {response.text}")
                except requests.exceptions.Timeout:
                    st.error("⏳ Request timed out in 10 seconds.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter value.")
