import requests
from account_keys import LTA_DATAMALL_API_KEY

api_list = ['LTA Datamall Keys', 'v3/BusArrival']

def lta_datamall_query(url_suffix:str, parameters:dict, api_key:str=LTA_DATAMALL_API_KEY)->str:
  '''
  lta_datamall_query(url_suffix:str, parameters:dict, api_key:str)->str
  '''
  url = f'''https://datamall2.mytransport.sg/ltaodataservice/{url_suffix}?{''.join([f'{param[0]}={param[1]}' for param in parameters])}'''
  print(url)

  payload = {}
  headers = {
    'AccountKey': api_key,
    'accept': 'application/json'
  }

  response = requests.request('GET', url, headers=headers, data=payload)

  return response.text

def bus_arrival():
  pass

def bus_services():
  pass

def bus_routes():
  pass

def bus_stops():
  pass

def passenger_volume_by_bus_stops():
  pass

def passenger_volume_by_origin_destination_bus_stops():
  pass

def passenger_volume_by_origin_destination_train_stations():
  pass

def passenger_volume_by_train_stations():
  pass

def taxi_availability():
  pass

def taxi_stands():
  pass

def train_service_alerts():
  pass

def facilities_maintenance():
  pass

def station_crowd_density_realtime():
  pass

def station_crowd_density_forecast():
  pass

def planned_bus_routes():
  pass

def gtfs_schedule_train():
  pass

def gtfs_realtime_train_service_alerts():
  pass

def gtfs_realtime_train_trip_updates_disruption():
  pass

def carpark_availability():
  pass

def estimated_travel_times():
  pass

def faulty_traffic_lights():
  pass

def planned_road_openings():
  pass

def approved_road_works():
  pass

def traffic_images():
  pass

def traffic_incidents():
  pass

def traffic_speed_bands():
  pass

def vms_emas():
  pass

def traffic_flow():
  pass

def flood_alerts():
  pass

def bicycle_parking():
  pass

def geospatial_whole_island():
  pass

def ev_charging_points():
  pass

def ev_charging_points_batch():
  pass

lta_datamall_query(1)
