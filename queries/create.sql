PRAGMA foreign_keys=on;
CREATE TABLE IF NOT EXISTS bus
                  (id integer PRIMARY KEY, 
                  bus_id text, long real,
                  lat real, 
                  latest_bus_stop_id integer,
                  iteration integer, 
                  time_at text);

CREATE TABLE IF NOT EXISTS bus_stop 
                   (id integer PRIMARY KEY,
                   long real,
                   lat real, 
                   last_bus_stop_time_visit text,
                   delay_history integer not null)

CREATE TABLE IF NOT EXISTS bus_stop_delay_history 
                    (id integer PRIMARY KEY,
                    time text,
                    delay text,
                    foreign key (bus_stop_id) REFERENCES bus_stop(id)
