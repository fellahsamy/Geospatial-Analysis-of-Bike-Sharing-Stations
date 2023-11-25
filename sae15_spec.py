
import pandas as pd             # pour la mise en forme, l'analyse et la publication
import datetime as dt           # pour la détermination de la date
import geopandas as gpd         # pour la spatialisation des données
import matplotlib.pyplot as plt # pour les graphes
import contextily as ctx        # pour l'utilisation de cartes géographiques

#------------------------------------------------------------------------------------------------
# fonction qui retourne le taux de disponibilité des stands (en %)
def availableDocksRate(stations_df):
    rate = (stations_df['numDocksAvailable'].sum() / 
            (stations_df['numDocksAvailable'].sum() + stations_df['numBikesAvailable'].sum())) * 100
    return rate

#------------------------------------------------------------------------------------------------
# fonction qui retourne le taux de disponibilité des vélos (en %)
def availableBikesRate(stations_df):
    rate = (stations_df['numBikesAvailable'].sum() / 
            (stations_df['numDocksAvailable'].sum() + stations_df['numBikesAvailable'].sum())) * 100
    return rate

#------------------------------------------------------------------------------------------------
# fonction qui retourne la date la plus récente de la mise à jour des données dynamiques
def getLatestDate(stations_df):
    latest_date = pd.to_datetime(stations_df['last_reported'], unit='s').max()
    return latest_date

#------------------------------------------------------------------------------------------------
# fonction qui retourne les mesures statistiques  d'une clé du DataFrame de stations
def stationStatistics(stations_df, key):
    stats = stations_df[key].describe()
    stats_df = pd.DataFrame(stats)
    stats_df.columns = [key]
    return stats_df

#------------------------------------------------------------------------------------------------
# fonction qui exporte au format HTML le DataFrame des mesures statistiques
def exportStatistics(stats_df, filename):
    stats_df.to_html(filename)
#------------------------------------------------------------------------------------------------
# fonction qui affiche et exporte la carte des stations Vélibs géolocalisées
def exportCityMap(geo_stations, marker_size, marker_color, title, date=None, filename=None) :
  def exportCityMap(geo_stations, marker_size, marker_color, title, date=None, filename=None):
    fig, ax = plt.subplots(figsize=(10, 10))
    geo_stations.plot(ax=ax, color=marker_color, markersize=marker_size)
    ctx.add_basemap(ax, crs=geo_stations.crs.to_string())
    ax.set_axis_off()
    if date:
        title += f" - {date.strftime('%Y-%m-%d')}"
    plt.title(title)
    if filename:
        plt.savefig(filename)
    plt.show()

  return 

