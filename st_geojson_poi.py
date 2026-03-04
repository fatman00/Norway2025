## Run this core with streamlit run st_geojson_poi.py
# and past in the coordinate directly from google maps

import streamlit as st
import json

st.title("GPS → GeoJSON Point Converter")

st.write("Enter coordinates and attributes to generate a GeoJSON Point.")

# Inputs
latlon = st.text_input("Google lat Long") # 56.090430039231826, 9.220140823757152
(lat, lon) = latlon.split(',')
text = st.text_input("Text / name")
desc = st.text_input("Text / description")

# Generate button
if st.button("Generate GeoJSON"):

    geojson = {
        "type": "Feature",
        "properties": {
            "name": text,
            "description": desc 
        },
        "geometry": {
            "type": "Point",
            "coordinates": [float(lon.strip()), float(lat.strip())]  # GeoJSON uses lon, lat
        }
    }
    geojson_str = ","
    geojson_str += json.dumps(geojson, indent=2)

    st.subheader("GeoJSON Output")
    st.code(geojson_str, language="json")

    st.download_button(
        label="Download GeoJSON",
        data=geojson_str,
        file_name="point.geojson",
        mime="application/json"
    )