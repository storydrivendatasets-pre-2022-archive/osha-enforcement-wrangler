.DEFAULT_GOAL := help
.PHONY : clean help ALL


help:
	@echo 'Run `make ALL` to see how things run from scratch'

ALL: clean



## compile phase

collate_stash:
	./scripts/compile/collate_stashes.py



## collect phase
collect: fetch unpack_zips stash


stash:
	./scripts/collect/stash_csvs.py


unpack_zips:
	./scripts/collect/unpack_zips.py

fetch:
	./scripts/collect/fetch_zips.py



clean:
	@echo --- Cleaning stubs
