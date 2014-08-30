SOURCES := $(wildcard *.vrt)

GMLS := $(patsubst %.vrt, %.gml, $(SOURCES))
OSMS := $(patsubst %.vrt, %.osm, $(SOURCES))
SHPS := $(patsubst %.vrt, %.shp, $(SOURCES))

%.gml: %.vrt
	ogr2ogr -a_srs EPSG:4326 -f gml $@ $<

%.osm: %.vrt
	ogr2osm -e 4326 -o $@ $<

%.shp: %.vrt
	ogr2ogr -a_srs EPSG:4326 -f 'ESRI Shapefile' $@ $<

all: osm

gml: $(GMLS)
osm: $(OSMS)
shp: $(SHPS)

clean:
	rm -rf $(GMLS) $(OSMS)
