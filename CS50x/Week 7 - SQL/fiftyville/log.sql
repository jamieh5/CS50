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

-- Looking for id for the fiftyville airport
SELECT id FROM airports WHERE city = "Fiftyville" -- ID = 8