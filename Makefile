.DEFAULT_GOAL := help
.PHONY : clean help ALL


help:
	@echo 'Run `make ALL` to see how things run from scratch'

ALL: clean



collect: fetch_zips unpack_zips stash_csvs




stash_csvs:
	./scripts/collect/stash_csvs.py


unpack_zips:
	./scripts/collect/unpack_zips.py

fetch_zips:
	./scripts/collect/fetch_zips.py



clean:
	@echo --- Cleaning stubs
