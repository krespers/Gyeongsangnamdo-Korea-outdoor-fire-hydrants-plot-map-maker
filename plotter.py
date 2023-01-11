import folium
import pandas as pd
from folium.plugins import MarkerCluster

m=folium.Map(location=[35.5446, 128.4922], zoom_start=10)

df=pd.read_csv('myfile (1).csv', encoding='cp949')
coords = df[['위도', '경도', '소재지도로명주소', '상세위치', '관할소방서명']]

marker_cluster=MarkerCluster().add_to(m)

for lat, long, address, place in zip(coords['위도'], coords['경도'], coords['소재지도로명주소'], coords['상세위치']):
    folium.Marker([lat, long], icon = folium.Icon(color="red"), tooltip=[address, place]).add_to(marker_cluster)

m.save('filename.html')