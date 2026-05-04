from math import radians, sin, cos, atan2, sqrt, degrees, asin


def haversine_distance(lat1, lon1, lat2, lon2, *, miles=False):
    R_km = 6371.0088  # mean Earth radius in kilometers
    φ1, φ2 = radians(lat1), radians(lat2)
    Δφ = radians(lat2 - lat1)
    Δλ = radians(lon2 - lon1)

    a = sin(Δφ/2)**2 + cos(φ1) * cos(φ2) * sin(Δλ/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    dist_km = R_km * c
    return dist_km if not miles else dist_km * 0.621371192237334

def destination_point(lat, lon, distance_km, bearing_deg, *, radius_km=6371.0088):
    """
    Return (lat2, lon2) reached from (lat, lon) after moving distance_km along bearing_deg.
    Uses a spherical Earth model (good for typical distances).
    """
    φ1 = radians(lat)
    λ1 = radians(lon)
    θ = radians(bearing_deg)
    δ = distance_km / radius_km  # angular distance

    φ2 = asin(sin(φ1) * cos(δ) + cos(φ1) * sin(δ) * cos(θ))
    λ2 = λ1 + atan2(sin(θ) * sin(δ) * cos(φ1),
                   cos(δ) - sin(φ1) * sin(φ2))

    return (degrees(φ2), (degrees(λ2) + 540) % 360 - 180)  # normalize lon to [-180,180]