
#Возвращает все автобусы которые вошли/коснулись  буферной зоны остановки 
#param: iteration number

getBusesLiedOnBusStopBuffer = """
select bus.*,bus_stop.*  from bus, bus_stop where ST_contains(ST_Buffer(bus_stop.pt,0.0008,'quad_segs=8'),bus.pt) and 
(bus.iteration = %s) and (bus.latest_bus_stop_id is null or bus.latest_bus_stop_id != bus_stop.id);
 """
#на истинные значения записать bus.latest_bus_stop_id  = bus_stop.id

updateLatestBusStopId = """
        update bus set latest_bus_stop_id = %s where id = %s;
        """

setDelayHistoryForBus = """
insert into bus_stop_delay_history (time,bus_id,bus_stop_id) values (%s,%s,%s) 
            """