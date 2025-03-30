import streamlit as st

# Conversion functions
def convert_length(value, from_unit, to_unit):
    conversions = {
        'meter': 1,
        'kilometer': 1000,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254,
    }
    value_in_meters = value * conversions[from_unit]
    return value_in_meters / conversions[to_unit]

def convert_mass(value, from_unit, to_unit):
    conversions = {
        'kilogram': 1,
        'gram': 1000,
        'milligram': 1000000,
        'pound': 2.20462,
        'ounce': 35.274,
    }
    value_in_kg = value * conversions[from_unit]
    return value_in_kg / conversions[to_unit]

def convert_time(value, from_unit, to_unit):
    conversions = {
        'second': 1,
        'minute': 60,
        'hour': 3600,
        'day': 86400,
    }
    value_in_seconds = value * conversions[from_unit]
    return value_in_seconds / conversions[to_unit]

# Streamlit UI
st.title("Basic Unit Converter")

st.markdown("""
    This is a simple unit converter built with Python and Streamlit.
    Select the units you want to convert.
""")

# Dropdowns for selecting unit categories
unit_type = st.selectbox("Select Unit Type:", ['Length', 'Mass', 'Time'])

# Based on unit type, show corresponding units
if unit_type == 'Length':
    units = ['meter', 'kilometer', 'mile', 'yard', 'foot', 'inch']
    convert_function = convert_length
elif unit_type == 'Mass':
    units = ['kilogram', 'gram', 'milligram', 'pound', 'ounce']
    convert_function = convert_mass
elif unit_type == 'Time':
    units = ['second', 'minute', 'hour', 'day']
    convert_function = convert_time

# Input value to convert
value = st.number_input(f"Enter value in {units[0]}:", min_value=0.0)

# Dropdowns for selecting units
from_unit = st.selectbox(f"Convert from {unit_type}:", units)
to_unit = st.selectbox(f"Convert to {unit_type}:", units)

# Perform conversion
if st.button("Convert"):
    result = convert_function(value, from_unit, to_unit)
    st.write(f"Converted Value: {result} {to_unit}")


