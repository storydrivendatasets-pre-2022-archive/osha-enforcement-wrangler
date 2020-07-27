.DEFAULT_GOAL := help
.PHONY : clean help ALL


help:
	@echo 'Run `make ALL` to see how things run from scratch'

ALL: clean



split_csvs:
	@echo 'hey'


unpack_zips:
	./scripts/collect/unpack_zips.py

fetch_zips:
	./scripts/collect/collect_catalog_zips.py



clean:
	@echo --- Cleaning stubs
