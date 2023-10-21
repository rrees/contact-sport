-- migrate:up

CREATE TABLE contact (
	id serial,
	external_id uuid UNIQUE,
	name text,
	tags text[],
	created timestamp default current_timestamp,
	updated timestamp default current_timestamp
);

CREATE OR REPLACE FUNCTION update_modified_column() 
	RETURNS TRIGGER AS $$
	BEGIN
	    NEW.modified = now();
	    RETURN NEW; 
	END;
	$$ language 'plpgsql';

CREATE TRIGGER update_contact_modtime
BEFORE UPDATE ON contact
FOR EACH ROW EXECUTE PROCEDURE update_modified_column();


-- migrate:down

DROP TABLE table contact;

DROP FUNCTION update_modified_column;