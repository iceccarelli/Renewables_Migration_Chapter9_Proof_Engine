import streamlit as st
import pandas as pd
import numpy as np
from chapter9_core import Chapter9Core
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("Chapter 9: The Human Receipt - Proof Engine")

# Initialize core logic
core = Chapter9Core()

# Load book numbers for display
BOOK_NUMBERS = pd.read_csv("data/book_numbers.csv").set_index("metric")

# --- Spy Mode Button ---
if st.sidebar.button("Activate Spy Mode"):
    st.sidebar.subheader("Spy Mode Activated: Exact Book Claims")
    claims = core.spy_mode_claims()
    for claim_title, claim_text in claims.items():
        st.sidebar.write(f"**{claim_title}:** {claim_text}")

# --- Streamlit Tabs ---
tabs = [
    "Energy Burden vs Protocol-Offset Simulator",
    "Utility Equation Calculator",
    "AEP Intelligent Grid Nodes",
    "Sovereign Citizen Explorer",
    "Prove Every Equation",
    "Download Book Data",
]
selected_tab = st.sidebar.radio("Navigation", tabs)

if selected_tab == "Energy Burden vs Protocol-Offset Simulator":
    st.header("Energy Burden vs Protocol-Offset Simulator")
    st.write("Explore how Protocol-Offset impacts Energy Burden, matching Figure 9.2.")

    # Sliders
    protocol_offset_rate = st.slider(
        "Protocol Offset Rate (0-60%)", 0, 60, 30, format="%d%%"
    ) / 100
    # Assuming a representative income level for the curve
    income_level_mwh_per_euro = st.slider(
        "Representative Energy Intensity (MWh/€)", 0.01, 0.10, 0.05, format="%.2f"
    )

    # Calculate data for the curve
    protocol_offsets = np.linspace(0, core.protocol_offset_max, 100)
    energy_burdens = [
        core.calculate_energy_burden(income_level_mwh_per_euro, po)
        for po in protocol_offsets
    ]

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(protocol_offsets * 100, np.array(energy_burdens) * 100, label="Energy Burden")
    ax.set_xlabel("Protocol Offset (%)")
    ax.set_ylabel("Energy Burden (%)")
    ax.set_title("Energy Burden vs Protocol-Offset (Figure 9.2)")
    ax.grid(True)
    st.pyplot(fig)

    st.subheader("Current Simulation Results:")
    current_energy_burden = core.calculate_energy_burden(
        income_level_mwh_per_euro, protocol_offset_rate
    )
    st.write(
        f"With {protocol_offset_rate*100:.0f}% Protocol Offset, Energy Burden is: {current_energy_burden*100:.2f}%"
    )

elif selected_tab == "Utility Equation Calculator":
    st.header("Utility Equation Calculator")
    st.write("Calculate the Protocol-Enabled Utility and its impact on Demographic Drain.")

    # Sliders
    demographic_drain_rate = st.slider(
        "Demographic Drain Rate (0-10%)", 0, 10, 5, format="%d%%"
    ) / 100
    aep_node_efficiency = st.slider(
        "AEP Node Efficiency (0-100%)", 0, 100, 85, format="%d%%"
    ) / 100

    # Calculation
    utility_gain = core.protocol_enabled_utility_equation(
        demographic_drain_rate, aep_node_efficiency
    )

    st.subheader("Calculation Results:")
    st.write(
        f"Protocol-Enabled Utility Gain: {utility_gain:.2f} (higher is better)"
    )
    st.info(
        "This metric quantifies how effectively the protocol mitigates demographic drain."
    )

elif selected_tab == "AEP Intelligent Grid Nodes":
    st.header("AEP Intelligent Grid Nodes")
    st.write("Understanding the AEP Framework and its role in social migration.")
    st.write(core.aep_framework_description())
    st.subheader("Key Metrics:")
    st.write(f"AEP Node Efficiency: {core.aep_node_efficiency*100:.0f}%")
    st.info(
        "The AEP Framework empowers citizens and reduces energy burden through intelligent grid participation."
    )

elif selected_tab == "Sovereign Citizen Explorer":
    st.header("Sovereign Citizen Explorer")
    st.write("Track the evolution of the Sovereign Citizen Metric.")

    metrics = core.get_sovereign_citizen_metrics()
    st.subheader("Sovereign Citizen Metric:")
    st.write(f"2025: {metrics["2025 Sovereign Citizen Metric"]:.2f}")
    st.write(f"2030 (Projected): {metrics["2030 Sovereign Citizen Metric"]:.2f}")

    st.info(
        "This metric reflects the level of citizen empowerment and resilience within the energy system."
    )

elif selected_tab == "Prove Every Equation":
    st.header("Prove Every Equation")
    st.write("Here you can interact with the core equations from Chapter 9.")

    st.subheader("1. Energy Burden Calculation")
    eb_income = st.slider(
        "Income Level (MWh/€)", 0.01, 0.10, 0.05, key="eb_income_slider", format="%.2f"
    )
    eb_protocol_offset = st.slider(
        "Protocol Offset Rate", 0.0, core.protocol_offset_max, 0.3, key="eb_po_slider"
    )
    calculated_eb = core.calculate_energy_burden(eb_income, eb_protocol_offset)
    st.write(f"Calculated Energy Burden: {calculated_eb*100:.2f}%")
    st.code(
        """
        # Simplified representation of the book's logic:
        # adjusted_burden = base_energy_burden * (1 - protocol_offset_rate * protocol_offset_max)
        """
    )

    st.subheader("2. Protocol-Enabled Utility Equation")
    ue_drain_rate = st.slider(
        "Demographic Drain Rate", 0.0, 0.1, 0.05, key="ue_drain_slider"
    )
    ue_aep_efficiency = st.slider(
        "AEP Node Efficiency", 0.0, 1.0, 0.85, key="ue_aep_slider"
    )
    calculated_utility = core.protocol_enabled_utility_equation(
        ue_drain_rate, ue_aep_efficiency
    )
    st.write(f"Calculated Protocol-Enabled Utility: {calculated_utility:.2f}")
    st.code(
        """
        # Simplified representation of the book's logic:
        # utility_gain = aep_node_efficiency * (1 - demographic_drain_rate)
        """
    )

    st.subheader("3. Polynomial of Social Unrest")
    psu_unrest_factor = st.slider(
        "Unrest Factor", 0.1, 1.0, core.unrest_factor, key="psu_unrest_slider"
    )
    psu_energy_burden = st.slider(
        "Energy Burden (for Unrest)", 0.0, 0.5, calculated_eb, key="psu_eb_slider"
    )
    calculated_unrest = core.polynomial_of_social_unrest(
        psu_unrest_factor, psu_energy_burden
    )
    st.write(f"Calculated Social Unrest: {calculated_unrest:.4f}")
    st.code(
        """
        # Simplified representation of the book's logic (example cubic):
        # social_unrest = unrest_factor * (energy_burden**3)
        """
    )

elif selected_tab == "Download Book Data":
    st.header("Download Book Data")
    st.write("Download the raw data used to verify Chapter 9 claims.")

    csv_data = BOOK_NUMBERS.to_csv().encode("utf-8")
    st.download_button(
        label="Download book_numbers.csv",
        data=csv_data,
        file_name="book_numbers.csv",
        mime="text/csv",
    )

    st.info(
        "This CSV contains all hardcoded numbers from Chapter 9, verified by pytest."
    )
