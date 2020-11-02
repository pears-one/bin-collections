rm data/bin_collections.db
cat data/bin_collections_schema.sql | sqlite3 -echo data/bin_collections.db
cat data/bin_collections_data.sql | sqlite3 -echo data/bin_collections.db
