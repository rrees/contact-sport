-- migrate:up

ALTER TABLE contact
ALTER external_id
SET DEFAULT gen_random_uuid ();

ALTER TABLE address
ALTER external_id
SET DEFAULT gen_random_uuid ();

-- migrate:down

