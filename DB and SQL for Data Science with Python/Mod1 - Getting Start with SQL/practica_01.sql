-- Active: 1769991717238@@127.0.0.1@3306@mysql

# First a create a new table 
CREATE TABLE Toys (
    ID INTEGER NOT NULL,
    VARIETY VARCHAR(20),
    QUANTITY INTEGER
    );

SELECT * FROM Toys;

# Now insert some values
INSERT INTO Toys VALUES
    (1,'Chew toy',20),
    (2,'Balls',50),
    (3,'Bowls',30),
    (4,'Foldable bed', 40);

SELECT * FROM Toys;

# Now i will alter the length of the VARIETY column
ALTER TABLE Toys
MODIFY VARIETY VARCHAR(30);

SELECT * FROM Toys;

# Truncate the table
TRUNCATE TABLE Toys;

SELECT * FROM Toys;

# Drop the table
DROP TABLE Toys;