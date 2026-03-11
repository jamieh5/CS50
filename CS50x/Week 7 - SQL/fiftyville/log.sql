-- Problem set: https://cs50.harvard.edu/x/psets/7/fiftyville/
-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Getting the description from the crime reports when the crime was commited
SELECT * FROM crime_scene_reports WHERE day = 28 AND month = 7 AND street = "Humphrey Street"