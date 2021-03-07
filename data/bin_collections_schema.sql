CREATE TABLE IF NOT EXISTS person (
    first_name varchar(32),
    last_name varchar(32),
    phone_number varchar(16),
    PRIMARY KEY (phone_number)
);

CREATE TABLE IF NOT EXISTS property (
    uprn varchar(12),
    postcode varchar(8),
    house_number varchar(4),
    street_name varchar(32),
    PRIMARY KEY (uprn)
);

CREATE table IF NOT EXISTS residency (
    phone_number varchar(16),
    uprn varchar(12),
    PRIMARY KEY (uprn, phone_number),
    FOREIGN KEY (phone_number) REFERENCES person(phone_number),
    FOREIGN KEY (uprn) REFERENCES property(uprn)
);

CREATE TABLE IF NOT EXISTS council (
    url varchar(64),
    name varchar(64),
    PRIMARY KEY (url)
);

CREATE TABLE IF NOT EXISTS council_by_postcode (
    postcode varchar(8),
    url varchar(64),
    PRIMARY KEY (postcode, url),
    FOREIGN KEY (postcode) references property(postcode),
    FOREIGN KEY (url) references council(url)
);
