---

title: Practical L5 - Solutions

site:
    outline_maxdepth: 1

---

<div class="page-subtitle">
Connecting Python to the real world
</div>

---

## Learning objectives

After completing this practical, you will be able to:

* geocode real world addresses into coordinate pairs using `geopy`
* establish a geodesic distance baseline for spatial comparisons
* fetch live routing data from the OpenRouteService API using `requests`
* parse JSON responses to extract driving distances and travel times
* automate API queries safely using loops, `tqdm`, and `time.sleep()`

---

## Practical storyline

In previous practicals, you built tools to calculate the distance between cities. However, calculating the mathematical distance across a sphere assumes you can fly like a bird. In reality, mountains, lakes, oceans, and road networks force us to take longer paths.

Imagine you are building a logistics tool for a long haul European delivery company. Your task is to geocode customer locations, establish the absolute shortest path (the geodesic distance), and then use a Web API to query the actual driving distance. Finally, you will automate this process for a list of international deliveries, ensuring you respect the server's rate limits.

---

## 1. Geocoding the locations

Before we can calculate distances or query APIs, we need exact coordinates. Your delivery truck starts at a warehouse in Bern, Switzerland, and the first delivery is to a science museum in Trento, Italy.

### Code

```{code-cell} python
from geopy.geocoders import Nominatim

# Initialize the geocoder with a unique app name
geolocator = Nominatim(user_agent="sds_euro_logistics_YOUR_ID")

origin_address = "Spitalgasse 47-51, 3001 Bern, Switzerland"
dest_address = "Corso del Lavoro e della Scienza, 3, 38122 Trento TN, Italy"

origin_loc = geolocator.geocode(origin_address)
dest_loc = geolocator.geocode(dest_address)

# Extract coordinates as (latitude, longitude) tuples
origin_coords = (origin_loc.latitude, origin_loc.longitude)
dest_coords = (dest_loc.latitude, dest_loc.longitude)

print(f"Origin: {origin_coords}")
print(f"Destination: {dest_coords}")


```

### Tasks

1. Run the code above to verify the geocoder is working.
2. Change the destination address to a real street address of your choice anywhere in the world.
3. Print the full official address returned by Nominatim for your new destination to ensure it found the correct place.

```{admonition} Sample solution
:class: dropdown

```{code-cell} python
# 2. Change the destination address
dest_address = "Buckingham Palace, London, UK"
dest_loc = geolocator.geocode(dest_address)

dest_coords = (dest_loc.latitude, dest_loc.longitude)
print(f"New Destination Coordinates: {dest_coords}")

# 3. Print the full official address
print(f"Official Address: {dest_loc.address}")
```

**Key idea:**
Nominatim standardizes the output, often returning a highly detailed, hierarchical address that includes the postal code, city, and country, even if your input was just a landmark name.

```

---

## 2. The geodesic baseline

To understand how much the road network bends and curves around the Alps, we first need to know the absolute shortest possible path between our two points.

### Code

```{code-cell} python
from geopy import distance

geodesic_dist = distance.geodesic(origin_coords, dest_coords).km

print(f"The bird flies: {geodesic_dist:.1f} km")


```

### Tasks

1. Calculate the geodesic distance between your origin and your newly chosen destination.
2. Store the result in a variable called `baseline_km` so we can compare it later.

```{admonition} Sample solution
:class: dropdown

```{code-cell} python
# 1 & 2. Calculate and store the geodesic baseline
baseline_km = distance.geodesic(origin_coords, dest_coords).km

print(f"The geodesic baseline is {baseline_km:.1f} km")
```

**Key idea:**
Storing the result in a well named variable like `baseline_km` allows you to easily reuse this metric in later calculations without repeating the math.

```

---

## 3. Setting up OpenRouteService

Now we want the real world driving distance. For this, we will use the **OpenRouteService (ORS)** API. Because calculating road routes across entire countries is computationally heavy, ORS requires a personal API key to track usage.

### Task: Get your API Key

1. Visit the [OpenRouteService Sign Up page](https://www.google.com/search?q=https://openrouteservice.org/dev/%23/signup) and create a free account.
2. Once logged in, navigate to your Dashboard.
3. Generate a new token (you can select "Free" and name it "sds_course").
4. Copy the long string of characters and paste it into the variable below.

```{code-cell} python
# Paste your personal API key inside the quotes
ORS_API_KEY = "replace_this_with_your_actual_key"


```

---

## 4. Querying the driving route

With our key ready, we can construct a request to the ORS directions endpoint. The API requires the coordinates to be formatted in `longitude, latitude` order, which is the reverse of what `geopy` gives us!

### Code

```{code-cell} python
import requests

# Build the parameters dictionary
# Note: ORS requires coords as "longitude,latitude"
parameters = {
    'api_key': ORS_API_KEY,
    'start': f"{origin_coords[1]},{origin_coords[0]}",
    'end': f"{dest_coords[1]},{dest_coords[0]}"
}

# Define the API endpoint for car driving directions
api_url = 'https://api.openrouteservice.org/v2/directions/driving-car'

# Send the request
response = requests.get(api_url, params=parameters)

# Check if successful
if response.status_code == 200:
    data = response.json()
    
    # Extract the summary dictionary
    summary = data['features'][0]['properties']['summary']
    
    driving_km = summary['distance'] / 1000
    duration_mins = summary['duration'] / 60
    
    print(f"Driving distance: {driving_km:.1f} km")
    print(f"Estimated time: {duration_mins:.1f} minutes")
    
else:
    print("Request failed.")
    print("Reason:", response.text)


```

### Tasks

1. Run the code above to get the driving distance for your route across the Alps.
2. Calculate and print the **detour factor**: the driving distance divided by the geodesic baseline distance from Part 2. A detour factor of 1.0 means a perfectly straight road; 1.5 means you have to drive 50% further than the straight line distance.

```{admonition} Sample solution
:class: dropdown

```{code-cell} python
# 2. Calculate the detour factor
detour_factor = driving_km / baseline_km

print(f"Detour factor: {detour_factor:.2f}")
```

**Key idea:**
A high detour factor in mountainous regions like the Alps indicates a very complex road network full of switchbacks and detours around impassable terrain.

```

---

## 5. Fetching live weather for the driver

Before dispatching the driver across international borders, it is good practice to check the current weather at the destination. We can do this using the Open-Meteo API, which does not require a key.

### Tasks

1. Write a `requests.get()` call to the Open-Meteo API (`https://api.open-meteo.com/v1/forecast`).
2. Pass the `latitude` and `longitude` of your **destination** in the parameters, along with `"current_weather": "true"`.
3. Parse the JSON response to extract and print the current temperature.

```{admonition} Sample solution
:class: dropdown

```{code-cell} python
import requests

meteo_url = "https://api.open-meteo.com/v1/forecast"

# 2. Build parameters using the destination coordinates
weather_params = {
    "latitude": dest_coords[0],
    "longitude": dest_coords[1],
    "current_weather": "true"
}

# 1. Make the request
weather_response = requests.get(meteo_url, params=weather_params)

if weather_response.status_code == 200:
    weather_data = weather_response.json()
    
    # 3. Extract the temperature
    temp = weather_data["current_weather"]["temperature"]
    print(f"Current temperature at destination: {temp}°C")
else:
    print("Failed to fetch weather data.")
```

**Key idea:**
By reusing the exact same variables (`dest_coords`) across different APIs, you can build a seamless automated workflow that fetches multiple distinct types of data for a single location.

```

---

## 6. Automating the logistics pipeline

Now it is time to put everything together. The delivery company has given you a list of coordinates for long haul deliveries starting from Bern and heading to various corners of Europe.

You need to query the ORS API for the driving distance to each location. Because you are querying an external API inside a loop, you **must** use rate limiting to avoid getting your account temporarily blocked.

### Code

```{code-cell} python
# A list of international delivery destination coordinates (lat, lon)
deliveries = {
    "Prague": (50.0755, 14.4378),
    "Ljubljana": (46.0569, 14.5058),
    "Girona": (41.9794, 2.8214),
    "Plymouth": (50.3755, -4.1427),
    "Quimper": (47.9975, -4.0979),
    "Odense": (55.4038, 10.4024)
}

# The origin is always Bern
origin_lon = 7.4474
origin_lat = 46.9480
start_string = f"{origin_lon},{origin_lat}"


```

### Tasks

1. Import `time` and `tqdm`.
2. Write a `for` loop that iterates over the `deliveries` dictionary (using `.items()`). Wrap the dictionary items in `tqdm()` to show a progress bar.
3. Inside the loop, format the destination latitude and longitude into an `end_string` (`longitude,latitude`).
4. Build the `parameters` dictionary and make the `requests.get()` call to the ORS API.
5. Extract the driving distance in kilometers and print it alongside the city name.
6. **Crucial step**: Add `time.sleep(2)` at the end of the loop to ensure you stay well within the ORS limit of 40 requests per minute.

```{admonition} Sample solution
:class: dropdown

```{code-cell} python
import time
from tqdm import tqdm
import requests

# Re-define the ORS API endpoint
ors_url = 'https://api.openrouteservice.org/v2/directions/driving-car'

# 2. Iterate over the dictionary using tqdm
for city, coords in tqdm(deliveries.items()):
    
    # 3. Format the end string (longitude, latitude)
    end_string = f"{coords[1]},{coords[0]}"
    
    # 4. Build parameters and make the request
    route_params = {
        'api_key': ORS_API_KEY,
        'start': start_string,
        'end': end_string
    }
    
    route_response = requests.get(ors_url, params=route_params)
    
    if route_response.status_code == 200:
        route_data = route_response.json()
        
        # 5. Extract and print driving distance
        distance_km = route_data['features'][0]['properties']['summary']['distance'] / 1000
        print(f"Distance to {city}: {distance_km:.1f} km")
    else:
        print(f"Failed to calculate route for {city}.")
        
    # 6. Rate limit the loop
    time.sleep(2)
```

**Key idea:**
This is the core of spatial automation. A well constructed loop with robust error handling and rate limiting allows you to query thousands of routing calculations while you step away from the computer.

```

---

## Reflection

Take a moment to review what you have built. Answer briefly in comments or markdown:

1. Look at your detour factor from Part 4 (Bern to Trento). Why is the driving distance across the Alps so much longer than the geodesic distance?
2. Consider the route to Plymouth (UK) or Odense (Denmark). How do you think a driving routing API handles crossing large bodies of water?
3. What would happen if you ran your loop in Part 6 on a list of 500 deliveries without including `time.sleep(2)`?

```{admonition} Sample solution
:class: dropdown

1. **The Alps:** Mountainous terrain requires roads to follow valleys, weave through switchbacks, and detour toward major tunnels, drastically increasing the actual travel distance compared to a straight line.
2. **Bodies of water:** Routing engines like ORS utilize ferry network data mapped in OpenStreetMap, or major infrastructure like the Eurotunnel (trains that carry cars), treating them as connected parts of the road network.
3. **Missing `time.sleep(2)`:** Your code would fire dozens of requests per second. The ORS server would immediately block your IP address and return an HTTP 429 "Too Many Requests" error, crashing your script before it finished computing the routes.


```

---

## What comes next

You have successfully connected Python to the global ecosystem of Web APIs! You can now translate human addresses into coordinates, calculate precise international routing networks, and fetch live weather data.

However, printing numbers to a console is only the beginning. In the upcoming chapters, we will introduce **Pandas** and **GeoPandas**, which will allow you to store, analyze, and map thousands of API results simultaneously in powerful, structured tables.