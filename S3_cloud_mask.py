import os
import xarray as xr
import numpy
from shapely import geometry, vectorized
import eumartools
import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib.cm import get_cmap
from matplotlib import animation
from matplotlib.axes import Axes
from shapely import geometry, vectorized
import eumartools
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature
from cartopy.mpl.geoaxes import GeoAxes
GeoAxes._pcolormesh_patched = Axes.pcolormesh


# Location
roi =  [[-30.0, 30.0], [-30.0, 60.0], [30.0, 60.0], [30.0, 30.0], [-30.0, 30.0]]

# Read in the coordinate data and build a spatial mask
geo_fid = xr.open_dataset('data/S3/S3B_20220412/geo_coordinates.nc')
lat = geo_fid.get('latitude').data
lon = geo_fid.get('longitude').data
geo_fid.close()

# Now check the flag content for our polygon
flag_file = os.path.join('data/S3/S3B_20220412/lqsf.nc')
flag_variable = 'LQSF'
flags_to_use = ['CLOUD']
flag_mask = eumartools.flag_mask(flag_file, flag_variable, flags_to_use)

point_mask = vectorized.contains(geometry.Polygon(roi), lon,lat)

def geoviz_s3(array, latitude, longitude, title):
    """
    Visualizes a numpy array (Sentinel-3 cloud mask) with matplotlib's 'pcolormesh' function.

    Parameters:
        color_array (numpy MaskedArray): any numpy MaskedArray, e.g. loaded with the NetCDF library and the Dataset function
        longitude (numpy Array): array with longitude values
        latitude (numpy Array) : array with latitude values
        title (str): title of the resulting plot
    """
    fig=plt.figure(figsize=(20, 12))

    ax=plt.axes(projection=ccrs.Mercator())
    ax.add_feature(cfeature.BORDERS, edgecolor='black', linewidth=1)
    ax.add_feature(cfeature.COASTLINE, edgecolor='black', linewidth=1)
    #ax.add_feature(cfeature.LAND, color='black')

    gl = ax.gridlines(draw_labels=True, linestyle='--')
    #gl.xlabels_top=False
    gl.top_labels=False
    #gl.ylabels_right=False
    gl.right_labels=False
    gl.xformatter=LONGITUDE_FORMATTER
    gl.yformatter=LATITUDE_FORMATTER
    gl.xlabel_style={'size':14}
    gl.ylabel_style={'size':14}

    img1 = plt.pcolormesh(longitude, latitude, array,
                          clip_on = True,
                          edgecolors=None,
                          cmap=plt.cm.Blues_r,
                          #cmap='gray',
                          zorder=0,
                          transform=ccrs.PlateCarree())
    ax.set_title(title, fontsize=20, pad=20.0)
    plt.show()


date = geo_fid.attrs['product_name'][16:24]
time = geo_fid.attrs['product_name'][25:29];

geoviz_s3(flag_mask, lat, lon, 'Clouds on: ' + date + ' ' + time)
