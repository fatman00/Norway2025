import json

# Input: path to your JSON file
INPUT_JSON_FILE = "all_eon.json"

# Output: path to GeoJSON file
OUTPUT_GEOJSON_FILE = "charging_stations.geojson"

def convert_to_geojson(input_file, output_file):
    # Load the JSON data (list of charging stations)
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Build the GeoJSON FeatureCollection
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for item in data:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [item["lng"], item["lat"]]
            },
            "properties": {
                key: value
                for key, value in item.items()
                if key not in ["lat", "lng"]  # Exclude coords from properties
            }
        }
        geojson["features"].append(feature)

    # Save to GeoJSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    print(f"GeoJSON saved to: {output_file}")

if __name__ == "__main__":
    convert_to_geojson(INPUT_JSON_FILE, OUTPUT_GEOJSON_FILE)
