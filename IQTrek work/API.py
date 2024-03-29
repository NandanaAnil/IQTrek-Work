import requests

def get_restaurants(city, has_table_booking=False, has_online_delivery=False, cuisines=None):
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    api_key = "YOUR_API_KEY"
    
    params = {
        "query": f"restaurants in {city}",
        "key": api_key
    }

    if has_table_booking:
        params["query"] += " table booking"
    if has_online_delivery:
        params["query"] += " online delivery"
    if cuisines:
        params["query"] += f" {cuisines} cuisine"
    
    response = requests.get(base_url, params=params)
    data = response.json()

    if data["status"] == "OK":
        restaurants = data["results"]
        restaurants.sort(key=lambda x: x.get("rating", 0), reverse=True)
        return restaurants
    else:
        print("Error:", data["status"])
        return []

def display_restaurants(restaurants):
    for idx, restaurant in enumerate(restaurants, start=1):
        name = restaurant["name"]
        rating = restaurant.get("rating", "N/A")
        address = restaurant["formatted_address"]
        print(f"{idx}. {name} (Rating: {rating}) - {address}")

def main():
    city = input("Enter your city: ").strip()
    has_table_booking = input("Do you need table booking? (yes/no): ").strip().lower() == "yes"
    has_online_delivery = input("Do you need online delivery? (yes/no): ").strip().lower() == "yes"
    cuisines = input("Enter preferred cuisine(s) (optional): ").strip()

    restaurants = get_restaurants(city, has_table_booking, has_online_delivery, cuisines)
    if restaurants:
        print("\nRestaurants in", city, "sorted by rating:")
        display_restaurants(restaurants)
    else:
        print("No restaurants found.")

if __name__ == "__main__":
    main()