SOURCES := $(wildcard *.csv)

OBJS := $(patsubst %.csv, %.gml, $(SOURCES))

%.gml: %.csv
	ogr2ogr -a_srs EPSG:4326 -f gml $@ $<

all: gml

gml: $(OBJS)

clean:
	rm -rf $(OBJS)
