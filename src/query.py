get_people_statement = """
    SELECT 
    person.first_name as name, 
    person.phone_number as number, 
    property.uprn as uprn
    FROM person
    JOIN residency ON (person.phone_number = residency.phone_number)
    JOIN property ON (residency.uprn = property.uprn)
    """

get_property_statement = """
    SELECT 
    property.uprn, 
    property.postcode, 
    property.house_number,
    property.street_name,
    cbp.url
    FROM property
    JOIN council_by_postcode cbp on property.postcode = cbp.postcode
    """

get_residents_statement = """
    SELECT 
    person.first_name as name, 
    person.phone_number as number, 
    r.uprn
    FROM person
    JOIN residency r on person.phone_number = r.phone_number
    WHERE r.uprn = '{uprn}'
    """


