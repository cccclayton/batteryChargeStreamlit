import streamlit as st
import time

st.title("Battery Charge Calculator for SOE")
st.write(
    """Calculate how fast your battery will fill up depending on the amount of 
    EV vehicles you want to charge and your daily average energy generation!"""
)

# Slider for daily average energy generation
energy_generation = st.slider("Daily Average Energy Generation (kWh)", 0, 1000, 210)

# Calculate how many more solar panels are needed to hit this amount of energy generation as compared to now
panel_multiplier = energy_generation / 210
st.write(f"This is ~{panel_multiplier:.2f}x the amount of panels you have now.")

# Input box for battery capacity
battery_capacity = st.number_input("Total Battery Capacity (kWh)", min_value=0, max_value=5000, value=300)

# Plus/Minus buttons for EV vehicles
num_vehicles = st.number_input("Number of EV Vehicles to Charge per day", min_value=0, max_value=20, value=1, step=1)

# Button for calculation
if st.button("Calculate"):
    with st.spinner('Calculating...'):
        time.sleep(1)  # Simulate a delay for calculation

        # Total battery output per day from charging EV vehicles
        vehicle_charge_total = num_vehicles * 80

        # Net sum of daily energy generation
        daily_battery_input = energy_generation - vehicle_charge_total

        # Calculate days to full or empty
        if daily_battery_input > 0:
            days_to_full = battery_capacity / daily_battery_input
            st.subheader(f"Battery will fill up in approximately {days_to_full:.1f} days")
        elif daily_battery_input < 0:
            days_to_empty = battery_capacity / abs(daily_battery_input)
            st.subheader(f"Battery will EMPTY in approximately {days_to_empty:.1f} days")
        else:
            st.subheader("Battery charge remains constant with the current configuration.")

# Expandable notes section
with st.expander("To the markers"):
    st.write("""
            You may have realised that this Streamlit was not present in the main Ecolume website, despite it being mentioned in my report
             that it would be. This is because we ran into deployment issues on Vercel side that could not be fixed before submission, 
             so the Streamlit was not able to be integrated into the website by then.

             As a result, I had to add the Streamlit to the dashboard website as it was not affected by the aforementioned issues.

             I hope you understand and can excuse this 🙏. Thank you.

             -Ecosystem
            """)
