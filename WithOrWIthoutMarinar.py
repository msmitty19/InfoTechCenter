
#BetaTestDev Branch

# ============================
# Welcome Branch
# Simulated OS Boot Screen
# ============================

# Libraries imported for system output control and timing delays
import sys
import time

# ----------------------------
# ANSI color codes for terminal text coloring
# ----------------------------
CYAN = "\033[96m"    # Cyan text (used for titles)
YELLOW = "\033[93m"  # Yellow text (used for boot animation)
GREEN = "\033[92m"   # Green text (used for success message)
RESET = "\033[0m"    # Resets text color back to default

# Display program title and version information
print(f"{CYAN}Welcome Branch - Developer: Matthew Smith{RESET}")
print(f"\n{CYAN}Welcome to InfoTechCenter V.1.0{RESET}")

# ----------------------------
# Boot animation variables
# ----------------------------
x = 0          # Counter to control how long the boot process runs
ellipsis = 0   # Controls the number of dots shown in the loading message

# ----------------------------
# Simulated OS boot loop
# ----------------------------
while x != 20:
    x += 1  # Increment loop counter each cycle

    # Create the boot message with animated dots
    ellipsisMessage = (
        f"{YELLOW}InfoTechCenter OS is Booting Up{'.' * ellipsis}{RESET}"
    )

    ellipsis += 1  # Increase dot count for animation effect

    # Overwrite the current terminal line with the updated message
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()  # Forces the output to appear immediately

    time.sleep(0.5)  # Pause to simulate boot delay

    # Reset dot animation after 3 dots
    if ellipsis == 4:
        ellipsis = 0

    # Final message once boot process is complete
    if x == 20:
        print(f"\n{GREEN}Operating System Booted Up - Access Granted{RESET}")


#Weather Branch
import random

import random  # Used to generate random numbers and make random selections

# Dictionary that stores all possible weather conditions and their effects
weather_data = {

    # ☀️ SUNNY WEATHER
    "☀️ Sunny": {
        # Probability weight (out of 100) for this weather type
        "chance": 25,

        # Messages the assistant may say when this weather is selected
        "messages": [
            "Roads are clear. Enjoy your drive!",
            "Perfect driving conditions today.",
            "Visibility is excellent."
        ],

        # Recommended driving speed ranges for sunny conditions
        "speed": ["55–65 mph", "60–70 mph", "50–60 mph"],

        # Alarm advice — no change needed because conditions are ideal
        "alarm": "No alarm change needed."
    },

    # ☁️ CLOUDY WEATHER
    "☁️ Cloudy": {
        "chance": 20,
        "messages": [
            "Cloudy skies. Stay focused.",
            "Low sunlight detected.",
            "Mild conditions ahead."
        ],
        "speed": ["50–60 mph", "45–55 mph", "55–60 mph"],

        # Alarm stays the same because conditions are still manageable
        "alarm": "Alarm time can stay the same."
    },

    # 🌧️ RAINY WEATHER
    "🌧️ Rain": {
        "chance": 20,
        "messages": [
            "Wet roads detected.",
            "Reduced tire traction.",
            "Rainfall increasing."
        ],
        "speed": ["40–50 mph", "35–45 mph", "45–50 mph"],

        # Alarm is set earlier to allow extra commute time due to wet roads
        "alarm": "Set your alarm 15 minutes earlier."
    },

    # ⛈️ THUNDERSTORM
    "⛈️ Thunderstorm": {
        "chance": 10,
        "messages": [
            "Severe storm warning.",
            "Heavy rain and lightning.",
            "Road visibility is low."
        ],
        "speed": ["25–35 mph", "30–40 mph", "20–30 mph"],

        # Earlier alarm needed because storms greatly slow travel
        "alarm": "Set your alarm 30 minutes earlier."
    },

    # ❄️ SNOW CONDITIONS
    "❄️ Snow": {
        "chance": 10,
        "messages": [
            "Snow buildup detected.",
            "Icy conditions possible.",
            "Slippery roads ahead."
        ],
        "speed": ["20–30 mph", "15–25 mph", "25–35 mph"],

        # Longest alarm adjustment due to very dangerous road conditions
        "alarm": "Set your alarm 45 minutes earlier."
    },

    # 💨 WINDY WEATHER
    "💨 Windy": {
        "chance": 10,
        "messages": [
            "Strong crosswinds detected.",
            "Vehicle stability reduced.",
            "Wind gusts incoming."
        ],
        "speed": ["45–55 mph", "40–50 mph", "50–55 mph"],

        # Slight alarm adjustment to account for slower, cautious driving
        "alarm": "Consider waking up 10 minutes earlier."
    },

    # 🌫️ FOGGY CONDITIONS
    "🌫️ Fog": {
        "chance": 5,
        "messages": [
            "Low visibility ahead.",
            "Fog density increasing.",
            "Use fog lights."
        ],
        "speed": ["25–35 mph", "30–40 mph", "20–30 mph"],

        # Alarm set earlier to compensate for reduced visibility
        "alarm": "Set your alarm 20 minutes earlier."
    }
}

# Generate a random number between 1 and 100
# This simulates rolling for the day's weather
roll = random.randint(1, 100)

# Keeps track of cumulative probability while looping
current = 0

print("🚗 Smart Car Assistant")
print("----------------------")

# Loop through each weather condition
for weather, data in weather_data.items():

    # Add this weather's chance to the cumulative total
    current += data["chance"]

    # If the random roll falls within this weather's range,
    # this weather is selected
    if roll <= current:

        # Randomly choose a message and speed for realism
        message = random.choice(data["messages"])
        speed = random.choice(data["speed"])

        # Retrieve the alarm advice associated with this weather
        alarm = data["alarm"]

        # Display results to the user
        print(f"Weather: {weather}")
        print(f"Assistant: {message}")
        print(f"Recommended Speed: {speed}")

        # This line shows how the system adjusts alarms based on weather
        print(f"Alarm Advice: {alarm}")

        # Shows the random roll for transparency/debugging
        print(f"System Roll: {roll}%")

        # Exit loop once a weather condition is selected
        break



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

