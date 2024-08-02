import streamlit as st

st.title("Battery Charge calculator for SOE")
st.write(
    """Calculate how fast your battery will fill up depending on the amount of 
    EV vehicles you want to charge and your daily average energy generation! """
)

# Slider for daily average energy generation
energy_generation = st.slider("Daily Average Energy Generation (kWh)", 0, 1000, 210)
panel_multiplier = energy_generation / 210
st.write(f"This is ~{panel_multiplier:.2f}x the amount of panels you have now.")

# Input box for battery capacity
battery_capacity = st.number_input("Total Battery Capacity (kWh)", min_value=0, max_value=5000, value=300)

# Plus/Minus buttons for EV vehicles
num_vehicles = st.number_input("Number of EV Vehicles to Charge per day", min_value=0, max_value=20, value=1, step=1)

vehicle_charge_total = num_vehicles*80

daily_battery_input = energy_generation - vehicle_charge_total

days_to_full = battery_capacity / daily_battery_input
if days_to_full < 0:
    days_to_full = 0
else:
    days_to_full = days_to_full

# Display the values
st.write(f"Battery will fill up in approximately {days_to_full:.1f} days")