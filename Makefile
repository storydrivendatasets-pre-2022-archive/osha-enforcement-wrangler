.DEFAULT_GOAL := help
.PHONY : clean help ALL


help:
	@echo 'Run `make ALL` to see how things run from scratch'

ALL: clean



## compile phase

compile_db: data/compiled/osha/raw/
	rm -f data/compiled/osha/raw.sqlite
	./scripts/compile/sqlize_raw.py

data/compiled/osha/raw.sqlite: data/compiled/osha/raw/ compile_db



data/compiled/osha/raw/: data/collected/osha/stash/
	# compile_stash
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

