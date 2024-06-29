-- create_tables.sql
CREATE SCHEMA IF NOT EXISTS stocks;

CREATE TABLE IF NOT EXISTS stocks."AI.PA" (
    Date TIMESTAMP,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Volume INTEGER,
    Dividends FLOAT,
    Stock_Splits FLOAT,
    date_modification TIMESTAMP
);

-- Répétez pour chaque ticker
CREATE TABLE IF NOT EXISTS stocks."AIR.PA" (
    Date TIMESTAMP,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Volume INTEGER,
    Dividends FLOAT,
    Stock_Splits FLOAT,
    date_modification TIMESTAMP
);


