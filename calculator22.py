import streamlit as st
from forex_python.converter import CurrencyRates
import math
import pandas as pd

# Function to convert length units
def length_converter(value, from_unit, to_unit):
    conversions = {
        ('meters', 'kilometers'): lambda x: x / 1000,
        ('meters', 'miles'): lambda x: x / 1609.34,
        ('kilometers', 'meters'): lambda x: x * 1000,
        ('kilometers', 'miles'): lambda x: x / 1.60934,
        ('miles', 'meters'): lambda x: x * 1609.34,
        ('miles', 'kilometers'): lambda x: x * 1.60934,
        ('feet', 'meters'): lambda x: x * 0.3048,
    }
    return conversions.get((from_unit, to_unit), lambda x: x)(value)

# Function to convert weight units
def weight_converter(value, from_unit, to_unit):
    conversions = {
        ('kilograms', 'grams'): lambda x: x * 1000,
        ('kilograms', 'pounds'): lambda x: x * 2.20462,
        ('grams', 'kilograms'): lambda x: x / 1000,
        ('grams', 'pounds'): lambda x: x * 0.00220462,
        ('pounds', 'kilograms'): lambda x: x / 2.20462,
        ('pounds', 'grams'): lambda x: x / 0.00220462,
    }
    return conversions.get((from_unit, to_unit), lambda x: x)(value)

# Function to convert currency
def currency_converter(value, from_currency, to_currency):
    c = CurrencyRates()
    return c.convert(from_currency, to_currency, value)

# Function to calculate BMI
def bmi_calculator(weight, height):
    return weight / (height ** 2)

# Function to convert degrees to radians
def degrees_to_radians(degrees):
    return degrees * math.pi / 180

def main():
    st.title("Utility Converter")
    if st.button('About'):
        st.write('this is built for utility funct')

    chart_data

    st.sidebar.title("Select Conversion")
    choice = st.sidebar.radio("Choose conversion type:", ['Length', 'Weight', 'Currency', 'BMI', 'Degrees to Radians'])

    if choice == 'Length':
        st.subheader("Length Converter")
        value = st.number_input("Enter value to convert:")
        from_unit = st.selectbox("From unit:", ('meters', 'kilometers', 'miles', 'feet'))
        to_unit = st.selectbox("To unit:", ('meters', 'kilometers', 'miles', 'feet'))
        result = length_converter(value, from_unit, to_unit)
    elif choice == 'Weight':
        st.subheader("Weight Converter")
        value = st.number_input("Enter value to convert:")
        from_unit = st.selectbox("From unit:", ('kilograms', 'grams', 'pounds'))
        to_unit = st.selectbox("To unit:", ('kilograms', 'grams', 'pounds'))
        result = weight_converter(value, from_unit, to_unit)
    elif choice == 'Currency':
        st.subheader("Currency Converter")
        value = st.number_input("Enter value to convert:")
        from_currency = st.text_input("From currency (3-letter code, e.g., USD):").upper()
        to_currency = st.text_input("To currency (3-letter code, e.g., EUR):").upper()
        result = currency_converter(value, from_currency, to_currency)
    elif choice == 'BMI':
        st.subheader("BMI Calculator")
        weight = st.number_input("Enter weight (in kg):")
        height_meters = st.number_input("Enter height (in meters):")
        result = bmi_calculator(weight, height_meters)
    elif choice == 'Degrees to Radians':
        st.subheader("Degrees to Radians Converter")
        degrees = st.number_input("Enter value in degrees:")
        result = degrees_to_radians(degrees)

    if st.button("Convert"):
        st.success(f"Result: {result:.2f}")

if __name__ == "__main__":
    main()