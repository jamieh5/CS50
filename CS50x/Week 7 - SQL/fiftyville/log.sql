-- Problem set: https://cs50.harvard.edu/x/psets/7/fiftyville/
-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Getting the description from the crime reports when the crime was commited
SELECT * FROM crime_scene_reports WHERE day = 28 AND month = 7 AND street = "Humphrey Street"
    -- Clues found:
        -- Theft was at 10:15am at the Humphrey Street Bakery. Three witnesses were present
        -- Littering took place at 16:36. No witnesses

-- Looking at the witness statements
SELECT name, transcript FROM interviews WHERE day = 28 AND month = 7
    -- Clues found:
        -- Witness Raymond: The thief left the bakery and called someone for less than a minute. The thief is leaving fiftyville with the earliest flight and asked the other person to purchase the flight ticket

-- Looking for id for the fiftyville airport
SELECT id FROM airports WHERE city = "Fiftyville" -- ID = 8

-- Looking for earliest flight from fiftyville airport
SELECT * FROM flights WHERE day = 28 AND month = 7 AND origin_airport_id = 8
    -- Earliest flight: at 13:49, id = 6 destination_airport_id = 5
    -- Getting name for the destination airport
    SELECT * FROM airports WHERE id = 5 -- Destination Airport: DFS, Dallas