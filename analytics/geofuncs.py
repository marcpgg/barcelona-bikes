import numpy as np



def geodesic_distance(lat1, lon1, lat2, lon2):
    R = 6372.795477598

    # lat1 = np.deg2rad(lat1)
    # lat2 = np.deg2rad(lat2)
    # lon1 = np.deg2rad(lon1)
    # lon2 = np.deg2rad(lon2)

    lat1,lat2,lon1,lon2 = map(np.radians, [ lat1, lat2, lon1, lon2,])

    dist = R*np.arccos(np.sin(lat1)*np.sin(lat2)+ np.cos(lat1)*np.cos(lat2)*np.cos(lon1-lon2))
    return dist



def distancefunc(group):
    #The indexing below can be adjusted as you see fit
    for i in range(len(group)):
        coord1 = [group['lat'].iloc[i], group['lon'].iloc[i]]
        coord2 = [group['lat'].iloc[i-1], group['lon'].iloc[i-1]]

        dist = geodesic_distance(*coord1, *coord2)

    group['geopydistance'] = dist

    return group