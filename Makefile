.DEFAULT_GOAL := help
.PHONY : clean help ALL


help:
	@echo 'Run `make ALL` to see how things run from scratch'

ALL: clean



collect: fetch_zips unpack_zips split_csvs
	@echo 'this wont work'




split_csvs:
	./scripts/collect/split_csvs.py


unpack_zips:
	./scripts/collect/unpack_zips.py

fetch_zips:
	./scripts/collect/fetch_zips.py



clean:
	@echo --- Cleaning stubs
