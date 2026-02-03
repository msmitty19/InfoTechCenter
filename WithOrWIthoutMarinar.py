#Gasoline Branch
import random

# -------------------------------
# CAR & DRIVER SETTINGS (RANDOMIZED)
# -------------------------------

TANK_CAPACITY = 14.0
MPG = random.randint(22, 35)
CURRENT_GAS = round(random.uniform(0.5, TANK_CAPACITY), 2)

BASE_ALARM_TIME = 7 * 60          # 7:00 AM in minutes
LOW_GAS_THRESHOLD = 0.25
GAS_STOP_DELAY = random.randint(8, 15)


# -------------------------------
# RANDOM GAS STATION GENERATOR
# -------------------------------

station_names = [
    "QuickFuel", "MegaMart Gas", "RoadKing",
    "Budget Pump", "FuelUp", "Speedway Plus"
]

gas_stations = [
    {
        "name": name,
        "distance": round(random.uniform(1.0, 10.0), 1),
        "price": round(random.uniform(3.10, 3.80), 2),
        "snack_score": random.randint(1, 10)
    }
    for name in station_names
]


# -------------------------------
# GAS CALCULATIONS
# -------------------------------

remaining_range = CURRENT_GAS * MPG
tank_percentage = CURRENT_GAS / TANK_CAPACITY
needs_gas = tank_percentage <= LOW_GAS_THRESHOLD


# -------------------------------
# FILTER REACHABLE STATIONS
# -------------------------------

reachable_stations = [
    station for station in gas_stations
    if station["distance"] <= remaining_range
]


# -------------------------------
# RANK GAS STATIONS
# -------------------------------

ranked_stations = sorted(
    reachable_stations,
    key=lambda s: (
        s["price"],
        -s["snack_score"],
        s["distance"]
    )
)


# -------------------------------
# ALARM & LEAVE TIME LOGIC
# -------------------------------

leave_earlier_minutes = 0
alarm_time = BASE_ALARM_TIME

if needs_gas and ranked_stations:
    leave_earlier_minutes = GAS_STOP_DELAY
    alarm_time -= leave_earlier_minutes


# -------------------------------
# OUTPUT
# -------------------------------

print("🚗 Smart Commute Assistant")
print("-------------------------")

print(f"MPG: {MPG}")
print(f"Gas in tank: {CURRENT_GAS} gallons ({tank_percentage:.0%})")
print(f"Estimated range: {remaining_range:.1f} miles")

if needs_gas:
    print("⚠️ Gas level is LOW — refueling recommended.")
else:
    print("✅ Gas level is sufficient.")

print("\n⛽ Reachable Gas Stations (Ranked):")

if not ranked_stations:
    print("❌ No reachable gas stations with current fuel!")
else:
    for i, station in enumerate(ranked_stations, start=1):
        print(
            f"{i}. {station['name']} | "
            f"${station['price']}/gal | "
            f"{station['distance']} mi | "
            f"Snacks: {station['snack_score']}/10"
        )

# Convert alarm time to HH:MM
alarm_hour = alarm_time // 60
alarm_minute = alarm_time % 60

print(f"\n⏰ Alarm set for {alarm_hour:02d}:{alarm_minute:02d}")

# Human-friendly leave message
if leave_earlier_minutes > 0:
    print(f"🕒 Leave {leave_earlier_minutes} minutes earlier.")
else:
    print("🕒 No need to leave earlier today.")
