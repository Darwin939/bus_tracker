CREATE TABLE IF NOT EXISTS bus
                  (id serial PRIMARY KEY, 
                  bus_id varchar,
                  route_number varchar, 
                  latest_bus_stop_id integer,
                  iteration integer, 
                  time_at timestamp,
                  pt geometry);

CREATE TABLE IF NOT EXISTS bus_stop 
                   (id serial PRIMARY KEY,
                   last_bus_stop_time_visit varchar,
                   pt geometry);

CREATE TABLE IF NOT EXISTS bus_stop_delay_history 
                    (id serial PRIMARY KEY,
                    time timestamp,
                    delay varchar,
                    CONSTRAINT fk_bus foreign key (id) REFERENCES bus(id),
                    CONSTRAINT fk_bus_stop foreign key (id) REFERENCES bus_stop(id));
