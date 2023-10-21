-- migrate:up

CREATE TABLE address (
	id INT GENERATED ALWAYS AS IDENTITY,
	external_id uuid UNIQUE NOT NULL,
	contact_id integer NOT NULL,
	label text NOT NULL,
	address text NOT NULL,
	created timestamp default current_timestamp,
	updated timestamp default current_timestamp,
	PRIMARY KEY(id),
	CONSTRAINT fk_contact
		FOREIGN KEY(contact_id)
		REFERENCES contact(id)
);

CREATE TRIGGER update_address_modtime
BEFORE UPDATE ON address
FOR EACH ROW EXECUTE PROCEDURE update_modified_column();

-- migrate:down

DROP TABLE address;
DROP TRIGGER
IF EXISTS update_address_modtime
ON address;