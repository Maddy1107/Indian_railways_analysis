import os
from pathlib import Path

import geopandas as gpd
import pandas as pd
from shapely import wkt

shp_file_path = "data\shp"
csv_file_path = "data\csv"
current_dir = Path(__file__).resolve().parent.parent.parent


def read_shp(filename, data_path=shp_file_path):
    file_path = os.path.join(current_dir, "..", data_path, filename)

    file_path = os.path.normpath(file_path)

    print(file_path)

    if os.path.isfile(path=file_path):
        gdf = gpd.read_file(filename=file_path)
    else:
        print("Invalid path specified.")
        gdf = [None]

    return gdf


def read_csv(filename, data_path=csv_file_path):
    file_path = os.path.join(current_dir, data_path, filename)

    print(f"@@@@@@@@@{current_dir}")

    print(f"##################{file_path}")

    if os.path.isfile(path=file_path):
        df = pd.read_csv(filepath_or_buffer=file_path)
    else:
        print("Invalid path specified.")
        df = {}

    return df


def convert_to_gpd(filename):
    df = read_csv(filename)
    if df['geometry'] == df['geometry'].astype(str):
        df["geometry"] = df["geometry"].apply(wkt.loads)
        gdf = gpd.GeoDataFrame(df, geometry="geometry")
        gdf.set_crs(epsg=4326, inplace=True)
    return df


trains = convert_to_gpd("trains.csv")
stations = convert_to_gpd("stations.csv")
schedules = read_csv("schedules.csv")
states = read_shp("Admin2.shp")
