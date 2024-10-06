-- migrate:up


CREATE TABLE email (
	id INT GENERATED ALWAYS AS IDENTITY,
	external_id uuid UNIQUE NOT NULL DEFAULT gen_random_uuid(),
	contact_id integer NOT NULL,
	label text NOT NULL,
	email text NOT NULL,
	created timestamp default current_timestamp,
	updated timestamp default current_timestamp,
	PRIMARY KEY(id),
	CONSTRAINT email_contact_fk
		FOREIGN KEY(contact_id)
		REFERENCES contact(id)
);

CREATE TRIGGER update_email_modtime
BEFORE UPDATE ON email
FOR EACH ROW EXECUTE PROCEDURE update_modified_column();

-- migrate:down

DROP TABLE IF EXISTS email;
DROP TRIGGER
IF EXISTS update_email_modtime
ON email;