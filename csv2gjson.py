import csv
import json

# Replace this with the path to your CSV file
input_csv = "fall2024.csv"
output_geojson = "fall2024.geojson"

features = []

with open(input_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lat = float(row["GPSLatitude"])
        lon = float(row["GPSLongitude"])
        feature = {
            "type": "Feature",
            "properties": {
                "SourceFile": row["SourceFile"]
            },
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat]
            }
        }
        features.append(feature)

geojson = {
    "type": "FeatureCollection",
    "features": features
}

with open(output_geojson, "w", encoding="utf-8") as f:
    json.dump(geojson, f, indent=2)

print(f"GeoJSON saved to {output_geojson}")
