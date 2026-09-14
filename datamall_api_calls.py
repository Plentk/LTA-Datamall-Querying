import requests

print('Thank you for importing LTA DataMall API Calls Python Package')

class LTA_DATAMALL_QUERY:
    '''
    A class representing a LTA DataMall User

    Attributes:
        api_key (str): User's own registered API key as received from LTA
    '''

    def __init__(self, api_key: str):
        '''Initialise an LTA_DATAMALL_QUERY object

        Parameters:
            api_key (str): User's own registered API key as received from LTA
        '''
        if not isinstance(api_key, str):
            raise TypeError('parameter api_key must be string')
        self.api_key = api_key

    def lta_datamall_query(self, subdirectory: str, query_dict: dict = {}) -> str:
        '''Queries LTA DataMall using provided url_suffix, parameters and initialised API key.
        Returns 


        Parameters:
            subdirectory (str): subdirectory of `https://datamall2.mytransport.sg/ltaodataservice`
            query_dict (dict): Dictionary of parameter key value pairs
        '''
        if not isinstance(subdirectory, str):
            raise TypeError('parameter subdirectory must be string')
        query = ''.join([f'{param[0]}={param[1]}' for param in query_dict])
        url = f'''https://datamall2.mytransport.sg/ltaodataservice/{subdirectory}?{query}'''
        print(url)

        payload = {}
        headers = {
            'AccountKey': self.api_key,
            'accept': 'application/json'
        }

        response = requests.request('GET', url, headers=headers, data=payload)

        return response.text

    def bus_arrival(self, BusStopCode: str, ServiceNo: str = None):
        '''Returns real-time Bus Arrival information of Bus Services at a queried Bus Stop, including Est. Arrival Time, Est. Current Location, Est. Current Load.

        Update Freq: 20 sec

        Parameters:
            BusStopCode (str): Bus stop reference code
            ServiceNo (int): Bus service number
        :return:
        '''
        subdirectory = 'v3/BusArrival'
        if ServiceNo is None:
            query_dict = {'BusStopCode': BusStopCode}
        else:
            query_dict = {'BusStopCode': BusStopCode, 'ServiceNo': ServiceNo}
        bus_arrival_data = self.lta_datamall_query(subdirectory=subdirectory, query_dict=query_dict)
        return bus_arrival_data

    def bus_services(self, ServiceNo: str = None):
        '''Returns detailed service information for all buses currently in operation, including: first stop, last stop, peak / offpeak frequency of dispatch.

        Update Freq: Ad hoc

        Parameters:
            ServiceNo (int): The bus service number
        :return:
        '''
        subdirectory = ''
        if ServiceNo is None:
            pass
        else:
            pass

    def bus_routes(self):
        '''Returns detailed route information for all services currently in operation, including: all bus stops along each route, first/last bus timings for each stop

        Update Freq: Ad hoc

        :return:
        '''
        pass

    def bus_stops(self, BusStopCode: str = None):
        '''Returns detailed information for all bus stops currently being serviced by buses, including: Bus Stop Code, location coordinates.

        Parameters:
            BusStopCode (str): The unique 5-digit identifier for this physical bus stop
        :return:
        '''
        if BusStopCode is None:
            pass
        else:
            pass

    def passenger_volume_by_bus_stops(self, date: str = None):
        '''Returns tap in and tap out passenger volume by weekdays and weekends for individual bus stop

        Update Freq: By 10th of every month, the passenger volume for previous month data will be generated

        Parameters:
            date (str): Input in YYYYMM format. Request for files up to last three months
        :return:
        '''
        pass

    def passenger_volume_by_origin_destination_bus_stops(self, date: str = None):
        '''Returns number of trips by weekdays and weekends from origin to destination bus stops

        Update Freq: By 10th of every month, the passenger volume for previous month data will be generated

        Parameters:
            date (str): Input in YYYYMM format. Request for files up to last three months
        :return:
        '''
        pass

    def passenger_volume_by_origin_destination_train_stations(self, date: str = None):
        '''Returns number of trips by weekdays and weekends from origin to destination train stations

        Update Freq: By 10th of every month, the passenger volume for previous month data will be generated

        Parameters:
            date (str): Input in YYYYMM format. Request for files up to last three months
        :return:
        '''
        pass

    def passenger_volume_by_train_stations(self, date: str = None):
        '''Returns tap in and tap out passenger volume by weekdays and weekends for individual train station

        Update Freq: By 10th of every month, the passenger volume for previous month data will be generated

        Parameters:
            date (str): in YYYYMM format. Request for files up to last three months
        :return:
        '''
        pass

    def taxi_availability(self):
        '''Returns location coordinates of all Taxis that are currently available for hire. Does not include "Hired" or "Busy" Taxis.

        Update Freq: 1 min

        :return:
        '''
        pass

    def taxi_stands(self):
        '''Returns detailed information of Taxi stands, such as location and whether is it barrier free.

        Update Freq: Monthly

        :return:
        '''
        pass

    def train_service_alerts():
        '''Returns detailed information on train service unavailability during scheduled operating hours, such as affected line and stations etc.

        Update Freq: Ad hoc

        :return:
        '''
        pass

    def facilities_maintenance(self):
        '''Returns adhoc lift maintenance in MRT stations

        Update Freq: Ad hoc

        :return:
        '''
        pass

    def station_crowd_density_realtime(self, TrainLine: str):
        '''Returns real-time MRT/LRT station crowdedness level of a particular train network line

        Update Freq: 10 min

        Parameters:
            TrainLine (str): Code of train network line.
        :return:
        '''
        pass

    def station_crowd_density_forecast(self, TrainLine: str):
        '''Returns forecasted MRT/LRT station crowdedness level of a particular train network line at 30 minutes interval

        Update Freq: 24 hrs

        Parameters:
            TrainLine (str): Code of train network line.
        :return:
        '''
        pass

    def planned_bus_routes(self):
        '''Returns planned new/updated bus routes information.

        Important Note: Data to be released only ON/AFTER the Effective Date.

        :return:
        '''
        pass

    def gtfs_schedule_train(self):
        '''GTFS Schedule (Train) is a feed specification that defines a common format for static public transportation information. It is composed of a collection of simple files, mostly text files (.txt) that are contained in a single ZIP file.

        Each file describes a particular aspect of transit information such as stops, routes, trips, etc. At its most basic form, a GTFS Schedule dataset is composed of files: agency.txt, routes.txt, trips.txt, stops.txt, stop_times.txt, calendar.txt and calendar_dates.txt.

        Please refer to General Transit Feed Specification documentation for more details.

        Update Freq: Ad hoc

        :return:
        '''
        pass

    def gtfs_realtime_train_service_alerts(self):
        '''GTFS Realtime (Train Service Alerts) is a feed specification that allows public transportation agencies to provide up-to-date information about service alerts allowing users to smoothly plan their trips

        Examples of information provided: Service alerts - unforseen events affecting a station, route or the entire network

        Please refer to General Transit Feed Specification documentation for more details.

        Update Freq: Ad hoc

        :return:
        '''
        pass

    def gtfs_realtime_train_trip_updates_disruption(self):
        '''GTFS Realtime (Train Trip Updates - Disruption) is a feed specification that provides real-time arrival/departure predictions, delays, cancellations for scheduled trips during train service disruptions.

        Examples of information provided: Trip updates - delays, cancellations

        Please refer to General Transit Feed Specification documentation for more details.

        Update Freq: Ad hoc

        :return:
        '''
        pass

    def carpark_availability(self):
        '''Returns no. of available lots for HDB, LTA and URA carpark data.

        The LTA carpark data consist of major shopping malls and developments within Orchard, Marina, HarbourFront, Jurong Lake District.

        (Note: list of LTA carpark data available on this API is subset of those listed on One.Motoring and MyTransport Portals)

        Update Freq: 1 min

        :return:
        '''
        subdirectory = "CarParkAvailabilityv2"
        carpark_availability_data = self.lta_datamall_query(subdirectory=subdirectory)
        return carpark_availability_data

    def estimated_travel_times(self):
        '''Returns estimated travel times of expressways (in segments)

        Update Freq: 5 min

        :return:
        '''
        subdirectory = 'EstTravelTimes'
        estimated_travel_times_data = self.lta_datamall_query(subdirectory=subdirectory)
        return estimated_travel_times_data

    def faulty_traffic_lights(self):
        '''Returns alerts of traffic lights that are currently faulty, or currently undergoing scheduled maintenance.

        Update Freq: 2 min - whenever there are updates

        :return:
        '''
        subdirectory = 'FaultyTrafficLights'
        faulty_traffic_lights_data = self.lta_datamall_query(subdirectory=subdirectory)
        return faulty_traffic_lights_data

    def planned_road_openings(self):
        '''Information on planned road openings.

        Update Freq: 24 hrs - whenever there are updates

        :return:
        '''
        subdirectory = 'RoadOpenings'
        planned_road_openings_data = self.lta_datamall_query(subdirectory=subdirectory)
        return planned_road_openings_data

    def approved_road_works(self):
        '''Information on approved road works to be carried out/being carried out.

        Update Freq: 24 hrs - whenever there are updates

        :return:
        '''
        subdirectory = 'RoadWorks'
        approved_road_works_data = self.lta_datamall_query(subdirectory=subdirectory)
        return approved_road_works_data

    def traffic_images(self):
        '''Returns links to images of live traffic conditions along expressways and Woodlands & Tuas Checkpoints.

        Update Freq: 1 - 5 min

        :return:
        '''
        subdirectory = 'Traffic-Imagesv2'
        traffic_images_data = self.lta_datamall_query(subdirectory=subdirectory)
        return traffic_images_data

    def traffic_incidents(self):
        '''Returns incidents currently happening on the roads, such as Accidents, Vehicle Breakdowns, Road Blocks, Traffic Diversions etc.

        Update Freq: 2 min - whenever there are updates

        :return:
        '''
        subdirectory = 'TrafficIncidents'
        traffic_incidents_data = self.lta_datamall_query(subdirectory=subdirectory)
        return traffic_incidents_data

    def traffic_speed_bands(self):
        '''Returns current traffic speeds on expressways and arterial roads, expressed in speed bands.

        Update Freq: 5 min

        :return:
        '''
        subdirectory = 'v4/TrafficSpeedBands'
        traffic_speed_bands_data = self.lta_datamall_query(subdirectory=subdirectory)
        return traffic_speed_bands_data

    def vms_emas(self):
        '''Returns traffic advisories (via variable message services) concerning current traffic conditions that are displayed on EMAS signboards along expressways and arterial roads.

        Update Freq: 2 min

        :return:
        '''
        subdirectory = 'VMS'
        vms_emas_data = self.lta_datamall_query(subdirectory=subdirectory)
        return vms_emas_data

    def traffic_flow(self):
        '''Returns hourly average traffic flow, taken from a representative month of every quarter during 0700-0900 hours.

        Update Freq: Quarterly

        :return: Link for downloading file that will expire after 15 minutes.
        '''
        subdirectory = 'TrafficFlow'
        traffic_flow_data = self.lta_datamall_query(subdirectory=subdirectory)
        return traffic_flow_data

    def flood_alerts(self):
        '''Returns flood alert information across Singapore, provided by PUB.

        Update Freq: 3 min

        :return:
        '''
        subdirectory = 'PubFloodAlerts'
        flood_alerts_data = self.lta_datamall_query(subdirectory=subdirectory)
        return flood_alerts_data

    def bicycle_parking(self, Lat: float, Long: float, Dist: float = 0.5):
        '''Returns bicycle parking locations within a radius. The default radius is set as 0.5km

        Update Freq: Monthly

        Parameters:
            Lat (float): Latitude map coordinates of location
            Long (float): Longitude map coordinates of location
            Dist (float): Radius in kilometre
        :return:
        '''
        pass

    def geospatial_whole_island(self, ID: str):
        '''Returns the SHP files of the requested geospatial layer

        Update Freq: Ad hoc

        Parameters:
            ID: str Name of Geospatial Layer
        :return:
        '''
        pass

    def ev_charging_points(self):
        '''Returns all electric vehicle charging points in Singapore and their availabilities by Postal Code.

        Update Freq: 5 min

        :return:
        '''
        pass

    def ev_charging_points_batch(self):
        '''Returns all electric vehicle charging points in Singapore and their availabilities in a single file.

        Update Freq: 5 min

        :return:
        '''
        pass
