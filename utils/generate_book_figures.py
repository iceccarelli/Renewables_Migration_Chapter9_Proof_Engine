import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os
import sys

# Add the parent directory to the system path to import chapter9_core
sys.path.insert(0, os.path.abspath("."))
from chapter9_core import Chapter9Core

# Initialize core logic
core = Chapter9Core()

def plot_energy_burden_vs_protocol_offset():
    """
    Reproduces Figure 9.2: Energy Burden vs Protocol-Offset.
    """
    protocol_offsets = np.linspace(0, core.protocol_offset_max, 100)
    # Assuming a representative income level for the curve, as in Streamlit
    income_level_mwh_per_euro = 0.05
    energy_burdens = [
        core.calculate_energy_burden(income_level_mwh_per_euro, po)
        for po in protocol_offsets
    ]

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=protocol_offsets * 100, y=np.array(energy_burdens) * 100)
    plt.xlabel("Protocol Offset (%)")
    plt.ylabel("Energy Burden (%)")
    plt.title("Figure 9.2: Energy Burden vs Protocol-Offset")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.ylim(0, 25)  # Consistent with Streamlit for visualization
    plt.xlim(0, core.protocol_offset_max * 100)
    plt.savefig("../plots/energy_burden_vs_protocol_offset.png")
    plt.close()
    print("Generated energy_burden_vs_protocol_offset.png")

def plot_demographic_drain_recovery():
    """
    Generates a placeholder plot for Demographic Drain Recovery.
    This would be based on the Protocol-Enabled Utility Equation.
    """
    demographic_drain_rates = np.linspace(0, 0.1, 100) # 0-10%
    aep_efficiency = core.aep_node_efficiency # Fixed for this plot
    utility_gains = [
        core.protocol_enabled_utility_equation(dr, aep_efficiency)
        for dr in demographic_drain_rates
    ]

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=demographic_drain_rates * 100, y=utility_gains)
    plt.xlabel("Demographic Drain Rate (%)")
    plt.ylabel("Protocol-Enabled Utility Gain")
    plt.title("Demographic Drain Recovery (Conceptual)")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.savefig("../plots/demographic_drain_recovery.png")
    plt.close()
    print("Generated demographic_drain_recovery.png")

def plot_social_migration_projection():
    """
    Generates a placeholder plot for Social Migration Projection.
    This would be based on the Polynomial of Social Unrest.
    """
    energy_burdens = np.linspace(0, 0.3, 100) # 0-30% energy burden
    unrest_factor = core.unrest_factor # Fixed for this plot
    social_unrest_values = [
        core.polynomial_of_social_unrest(unrest_factor, eb)
        for eb in energy_burdens
    ]

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=energy_burdens * 100, y=social_unrest_values)
    plt.xlabel("Energy Burden (%)")
    plt.ylabel("Social Unrest Index")
    plt.title("Social Migration Projection (Conceptual)")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.savefig("../plots/social_migration_projection.png")
    plt.close()
    print("Generated social_migration_projection.png")

if __name__ == "__main__":
    # Ensure the plots directory exists
    os.makedirs("../plots", exist_ok=True)

    plot_energy_burden_vs_protocol_offset()
    plot_demographic_drain_recovery()
    plot_social_migration_projection()
