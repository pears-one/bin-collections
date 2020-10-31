get_people_statement = """
    SELECT 
    person.first_name as name, 
    person.phone_number as number, 
    property.uprn as uprn
    FROM person
    JOIN residency ON (person.phone_number = residency.phone_number)
    JOIN property ON (residency.uprn = property.uprn)
        """

get_council_by_uprn = """
    SELECT 
    council.url as url,
    council.headers as headers,
    council.body as body,
    council.container_selector as container_selector,
    council.bin_type_selector as bin_type_selector,
    council.bin_type_regex as bin_type_regex,
    council.date_selector as date_selector,
    council.date_regex as date_regex,
    council.date_format as date_format
    FROM council 
    JOIN council_by_postcode cbp on council.url = cbp.url
    JOIN property p on cbp.postcode = p.postcode
    WHERE p.uprn = ?
"""

