import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature
import netCDF4 as nc

def ncplotter(mrc, file: str, dep_var: str, width = 6, height = 6, ax_title = "Colorbar", plt_title = "Plot Name", temp = False):

    netcdf = nc.Dataset(file, mode='r')
    dep = np.array(netcdf.variables[dep_var])
    longs = np.array(netcdf.variables['longitude'])
    lats = np.array(netcdf.variables['latitude'])
    netcdf.close()

    if temp == True:
        dep = (dep-273.15)*(9/5)+32

    xs = []
    ys = []
    zs = []

    for lat in range(len(lats)):
        for lon in range(len(longs)):
            total = list(filter(lambda x: x>=0, dep[::, lat, lon]))
            if len(total) > 0:
                average = sum(total)/len(total)
                xs.append(longs[lon])
                ys.append(lats[lat])
                zs.append(average)

    fig = plt.figure(figsize=(width, height), dpi = 100, facecolor="none")

    extents = np.array([min(longs), max(longs), min(lats), max(lats)])

    ax = fig.add_subplot(1,1,1, projection = mrc)
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cartopy.feature.STATES)
    ax.set_extent(extents, crs=mrc)

    plt.scatter(xs, ys, c=zs, cmap='rainbow', marker='s')
    cb = plt.colorbar()
    cb.ax.set_title(ax_title)
    plt.title(plt_title)

    gls = ax.gridlines(draw_labels=True, color='none')
    gls.top_labels = False
    gls.right_labels = False

    plt.show()

    return None

