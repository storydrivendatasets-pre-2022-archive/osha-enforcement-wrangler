.DEFAULT_GOAL := help
.PHONY : clean_wrangled_db clean_compiled_db help ALL

clean:
	@echo --- Cleaning stubs


help:
	@echo 'Run `make ALL` to see how things run from scratch'

ALL: wrangle_db

WRANGLED_DB_PATH = 	data/wrangled/osha_wrangled.sqlite
COMPILED_DB_PATH = data/compiled/osha_compiled.sqlite

## wrangle phase
wrangle_db: clean_wrangled_db ${WRANGLED_DB_PATH} index_wrangled_db


${WRANGLED_DB_PATH}: ${COMPILED_DB_PATH}
	./scripts/wrangle/sqlize_wrangled.py

## compile phase

compile_db: clean_compiled_db ${COMPILED_DB_PATH} index_compiled_db

${COMPILED_DB_PATH}: data/compiled/osha/raw/
	./scripts/compile/sqlize_compiled.py



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


#### sql stuff
index_wrangled_db: $(WRANGLED_DB_PATH)
	# indexing wrangled db
	sqlite3 $< < scripts/wrangle/index_wrangled.sql


index_compiled_db: ${COMPILED_DB_PATH}
	# indexing compiled db
	sqlite3 $< < scripts/compile/index_compiled.sql




clean_wrangled_db:
	rm -f ${WRANGLED_DB_PATH}

clean_compiled_db:
	rm -f ${COMPILED_DB_PATH}
