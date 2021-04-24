DROP TABLE destinations;
DROP TABLE cities;
DROP TABLE countries;
DROP TABLE users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    visited BOOLEAN
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255),
    country_id INT REFERENCES countries(id)
);

CREATE TABLE destinations (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    country_id INT REFERENCES countries(id),
    city_id INT REFERENCES cities(id),
    favorite_thing TEXT
);