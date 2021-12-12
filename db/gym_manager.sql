DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS activities;
DROP TABLE IF EXISTS workouts;


CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    age INT,
    memb_status BOOLEAN,
    memb_type VARCHAR(255)
);

CREATE TABLE workouts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    capacity INT,
    prem_only BOOLEAN
);


CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    workout_id SERIAL REFERENCES workouts(id) ON DELETE CASCADE,
    member_id SERIAL REFERENCES members(id) ON DELETE CASCADE
);
