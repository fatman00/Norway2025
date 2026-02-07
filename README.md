# Norway2025
Find the Map [HERE](map.html)
## Resources for trip planning
This is a list of some of the planning, mapping converting tools I have used for the trip:
* [Super charger information](https://supercharge.info/map)
* [Sun up and down times](https://www.timeanddate.no/astronomi/sol/norge/bergen)
* [Fjord Guide](https://www.visitnorway.dk/aktiviteter/naturattraktioner/fjorde/fjordguide/)
* [Norwegian Scenic Routes](https://www.nasjonaleturistveger.no/en/)
* Google Maps to [GPX converter](https://mapstogpx.com/)
* Converter for GPS to [GeoJSON converter](https://geojsonconverter.vercel.app/)
* [Visualize](https://www.gpsvisualizer.com/map?output_home) the GPX track to make sure it is correct
* Find GPS coordinates from a [Search](https://www.gps-coordinates.net/)
* Generate a [Route](https://maps.openrouteservice.org/) and export as GeoJSON

## Extract OSM data
Use [Overpass Turbo](https://overpass-turbo.eu/) To extract data from OSM dataset.

    [out:json];
    node
    [amenity=charging_station]
    [brand = "Tesla"]
    (\{\{bbox\}\});
    out;

Get it using a regex

    [out:json];
    node
    [amenity=charging_station]
    [operator ~ "Tesla.*"]
    (\{\{bbox\}\});
    out;

## Convert images from trip to thumpnails
Remember to brew install imagemagic exiftool

    for img in *.jpg; do
      convert "$img" -resize 250x250\> "resized_$img"
    done

Use exiftool to extract GPS coords:

    exiftool -gpslatitude -gpslongitude -n -csv -r . > ../spring2025.csv