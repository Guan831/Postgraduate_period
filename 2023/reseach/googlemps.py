import googlemaps

api_key = 'your_api_key_here'
gmaps = googlemaps.Client(key=api_key)

location = '40.748817,-73.985428'  # 纬度、经度
radius = 1000  # 搜索半径，以米为单位
types = ['restaurant']  # 商店类型，例如餐厅、咖啡店等

places_result = gmaps.places_nearby(
    location=location,
    radius=radius,
    type=types
)
place_id = places_result['results'][0]['place_id']  # 获取第一个商店的 Place ID

place_details = gmaps.place(
    place_id=place_id,
    fields=['name', 'rating', 'review']
)
print(place_details)
