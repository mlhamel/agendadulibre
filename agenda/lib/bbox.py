# -*- coding: utf-8 -*-

"""
Utilities to calculate the bounding box on a map using a LAT and LONG

Thanks to Federico A. Ramponi from:

http://stackoverflow.com/questions/238260/how-to-calculate-the-bounding-box-for-a-given-lat-lng-location
"""


import math

# Semi-axes of WGS-84 geoidal reference
WGS84_a = 6378137.0  # Major semiaxis [m]
WGS84_b = 6356752.3  # Minor semiaxis [m]


def deg2rad(degrees):
    """ degrees to radians """
    return math.pi*degrees/180.0


def rad2deg(radians):
    """ radians to degrees """
    return 180.0*radians/math.pi


def WGS84EarthRadius(lat):
    """
    Earth radius at a given latitude, according to the WGS-84 ellipsoid
    [m] http://en.wikipedia.org/wiki/Earth_radius
    """
    An = WGS84_a*WGS84_a * math.cos(lat)
    Bn = WGS84_b*WGS84_b * math.sin(lat)
    Ad = WGS84_a * math.cos(lat)
    Bd = WGS84_b * math.sin(lat)
    return math.sqrt( (An*An + Bn*Bn)/(Ad*Ad + Bd*Bd) )


def boundingBox(latitudeInDegrees, longitudeInDegrees, halfSideInKm):
    """
    Bounding box surrounding the point at given coordinates,
    assuming local approximation of Earth surface as a sphere
    of radius given by WGS84
    """
    lat = deg2rad(latitudeInDegrees)
    lon = deg2rad(longitudeInDegrees)
    halfSide = 1000*halfSideInKm

    # Radius of Earth at given latitude
    radius = WGS84EarthRadius(lat)
    # Radius of the parallel at given latitude
    pradius = radius*math.cos(lat)

    latMin = lat - halfSide/radius
    latMax = lat + halfSide/radius
    lonMin = lon - halfSide/pradius
    lonMax = lon + halfSide/pradius

    return (rad2deg(lonMin), rad2deg(latMin), rad2deg(lonMax), rad2deg(latMax))
