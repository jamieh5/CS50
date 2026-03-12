-- Problem set: https://cs50.harvard.edu/x/psets/7/fiftyville/
-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Getting the description from the crime reports when the crime was commited
SELECT * FROM crime_scene_reports WHERE day = 28 AND month = 7 AND street = "Humphrey Street"
    -- Clues found:
        -- Theft was at 10:15am at the Humphrey Street Bakery. Three witnesses were present
        -- Littering took place at 16:36. No witnesses

-- Looking at the witness statements
SELECT name, transcript FROM interviews WHERE day = 28 AND month = 7 AND transcript LIKE "%bakery%"
    -- Clues found:
        -- Witness Raymond: The thief left the bakery and called someone for less than a minute. The thief is leaving fiftyville with the earliest flight and asked the other person to purchase the flight ticket
        -- Witness Ruth: Within 10mins of the theft the thief got into a car and left
        -- Witness Eugene: Didnt know the thiefs name, but recognized him. The thief was withdrawing money from an ATM on Leggett Street

-- Intersection and joining the queries to find out the name of the thief
SELECT people.name FROM people JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate WHERE day = 28 AND month = 7
INTERSECT
SELECT people.name FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number WHERE day = 28 AND month = 7 AND atm_location = "Leggett Street" AND transaction_type = "withdraw"
INTERSECT
SELECT people.name FROM people JOIN phone_calls ON people.phone_number = phone_calls.caller WHERE day = 28 AND month = 7 AND duration < 60
INTERSECT
SELECT people.name FROM people JOIN passengers ON people.passport_number = passengers.passport_number WHERE passengers.flight_id IS (
    SELECT id FROM flights WHERE day = 29 AND month = 7
)
-- The name of the thief is Diana

-- Getting destination airport_id for Diana´s flight
SELECT destination_airport_id FROM flights JOIN passengers ON passengers.flight_id = flights.id WHERE day = 29 AND month = 7 AND passengers.passport_number IS (
    SELECT passport_number FROM people WHERE name = "Diana"
)

-- Getting Airport name for the airport with ID 6
SELECT city FROM airports WHERE id = 6
-- Diana fled to Boston
