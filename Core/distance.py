from math import sin, cos, sqrt, atan2, radians

def get_direct_distance_between_two_points(self, pickup_geo, vehicle_geo, radius):
	# approximate radius of earth in km
	R = 6373.0
	pickup_latitude = radians(pickup_geo['latitude'])
	pickup_longitude = radians(pickup_geo['longitude'])

	vehicle_latitude = radians(vehicle_geo['latitude'])
	vehicle_longitude = radians(vehicle_geo['longitude']) 

	dlon = vehicle_longitude - pickup_longitude
	dlat = vehicle_latitude - pickup_latitude

	a = sin(dlat / 2)**2 + cos(pickup_latitude) * cos(vehicle_latitude) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance_km = R * c
	distance_mtr = distance_km*1000
	logging.info('Distance %s ==> %s : %s meters' %(pickup_geo, vehicle_geo, distance_mtr))

	vehicle_reached = False
	if distance_mtr <= radius :
	  reached = True
	return vehicle_reached, distance_mtr, distance_km  


pickup_geo = {}
vehicle_geo = {}

pickup_geo['latitude'] = 30.733315
pickup_geo['longitude'] = 76.779419

vehicle_geo['latitude'] = 30.755159
vehicle_geo['longitude'] = 76.798840
radius = 4000

# vehicle_reached, distance_mtr , distance_km = self.get_direct_distance_between_two_points(pickup_geo, vehicle_geo, radius)
vehicle_reached, distance_mtr , distance_km = get_direct_distance_between_two_points(pickup_geo, vehicle_geo, radius)

print(vehicle_reached, distance_mtr , distance_km)