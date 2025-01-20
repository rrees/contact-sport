-- migrate:up


CREATE TABLE IF NOT EXISTS directories (
	id INT GENERATED ALWAYS AS IDENTITY,
	external_id uuid UNIQUE NOT NULL,
	name text NOT NULL,
	created timestamp default current_timestamp,
	updated timestamp default current_timestamp,
	PRIMARY KEY(id)
);


CREATE TRIGGER update_directory_modtime
BEFORE UPDATE ON directories
FOR EACH ROW EXECUTE PROCEDURE update_modified_column();

CREATE TABLE IF NOT EXISTS directory_entries (
	contact_id INT NOT NULL
		REFERENCES contact (id),
	directory_id INT NOT NULL
		REFERENCES directories (id),
	UNIQUE (
		contact_id,
		directory_id
		)
);

-- migrate:down


DROP TABLE IF EXISTS directory_entries;


DROP TRIGGER IF EXISTS update_directory_modtime ON directories;

DROP TABLE IF EXISTS directories;
