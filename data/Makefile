SOURCES := $(wildcard *.vrt)

GMLS := $(patsubst %.vrt, %.gml, $(SOURCES))
OSMS := $(patsubst %.vrt, %.osm, $(SOURCES))

%.gml: %.vrt
	ogr2ogr -a_srs EPSG:4326 -f gml $@ $<

%.osm: %.vrt
	ogr2osm -e 4326 -o $@ $<

all: osm

gml: $(GMLS)
osm: $(OSMS)

clean:
	rm -rf $(GMLS) $(OSMS)
