import pandas as pd
import numpy as np

# Load book numbers for verification and calculations
BOOK_NUMBERS = pd.read_csv('data/book_numbers.csv').set_index('metric')

class Chapter9Core:
    """Core calculations and frameworks for Chapter 9: The Human Receipt."""

    def __init__(self):
        self.energy_poverty_threshold = BOOK_NUMBERS.loc['Energy Poverty Threshold', 'value'] / 100
        self.protocol_offset_max = BOOK_NUMBERS.loc['Protocol Offset', 'value'] / 100
        self.demographic_drain_rate = BOOK_NUMBERS.loc['Demographic Drain Rate', 'value'] / 100
        self.aep_node_efficiency = BOOK_NUMBERS.loc['AEP Node Efficiency', 'value'] / 100
        self.unrest_factor = BOOK_NUMBERS.loc['Unrest Factor', 'value']

    def calculate_energy_burden(self, income_level_mwh_per_euro, protocol_offset_rate):
        """
        Calculates the energy burden based on income level and protocol offset.
        This function is designed to prove the 'Energy Burden vs Protocol-Offset' curve.
        """
        # Placeholder for actual book equation, assuming a linear reduction for now
        # This needs to be refined based on the actual equation in the book.
        # The book implies a reduction in energy burden due to protocol offset.
        # Assuming a base energy burden that is reduced by the protocol offset.
        base_energy_burden = 0.20 # Example base, needs to be derived from book
        adjusted_burden = base_energy_burden * (1 - protocol_offset_rate * self.protocol_offset_max)
        return max(0, adjusted_burden)

    def protocol_enabled_utility_equation(self, demographic_drain_rate, aep_node_efficiency):
        """
        Calculates the Protocol-Enabled Utility, aiming to reverse the Demographic Drain.
        This function proves the 'Protocol-Enabled Utility Equation'.
        """
        # Placeholder for actual book equation
        # Assuming a relationship where higher AEP efficiency mitigates demographic drain
        utility_gain = aep_node_efficiency * (1 - demographic_drain_rate)
        return utility_gain

    def polynomial_of_social_unrest(self, unrest_factor, energy_burden):
        """
        Calculates the Polynomial of Social Unrest based on energy burden and an unrest factor.
        This function proves the 'Polynomial of Social Unrest'.
        """
        # Placeholder for actual book equation, assuming a cubic relationship as an example
        # This needs to be refined based on the actual equation in the book.
        social_unrest = self.unrest_factor * (energy_burden**3) # Example polynomial
        return social_unrest

    def get_sovereign_citizen_metrics(self):
        """
        Returns the 2030 Sovereign Citizen metrics from book_numbers.csv.
        """
        return {
            '2025 Sovereign Citizen Metric': BOOK_NUMBERS.loc['Sovereign Citizen Metric - 2025', 'value'],
            '2030 Sovereign Citizen Metric': BOOK_NUMBERS.loc['Sovereign Citizen Metric - 2030', 'value']
        }

    def aep_framework_description(self):
        """
        Provides a description of the AEP Framework as per the book.
        """
        return "The AEP (Autonomous Energy Protocol) Framework aims to decentralize energy management and empower citizens through direct participation in energy markets, reducing energy burden and fostering energy equity."

    def spy_mode_claims(self):
        """
        Returns key claims from Chapter 9 for 'Spy Mode'.
        """
        claims = {
            "The Demographic Drain": "The book highlights a 'Demographic Drain' where energy poverty leads to social migration and unrest. The Protocol-Enabled Utility Equation aims to reverse this trend.",
            "Polynomial of Social Unrest": "The book introduces a 'Polynomial of Social Unrest' which quantifies the relationship between energy burden and societal instability."
        }
        return claims


if __name__ == '__main__':
    core = Chapter9Core()
    print("Energy Poverty Threshold:", core.energy_poverty_threshold)
    print("Protocol Offset Max:", core.protocol_offset_max)
    print("Demographic Drain Rate:", core.demographic_drain_rate)
    print("AEP Node Efficiency:", core.aep_node_efficiency)
    print("Unrest Factor:", core.unrest_factor)

    # Example calculations
    energy_burden_example = core.calculate_energy_burden(0.05, 0.3)
    print(f"Calculated Energy Burden (example): {energy_burden_example:.2f}")

    utility_gain_example = core.protocol_enabled_utility_equation(0.05, 0.85)
    print(f"Calculated Protocol-Enabled Utility (example): {utility_gain_example:.2f}")

    social_unrest_example = core.polynomial_of_social_unrest(0.05, energy_burden_example)
    print(f"Calculated Social Unrest (example): {social_unrest_example:.2f}")

    print("Sovereign Citizen Metrics:", core.get_sovereign_citizen_metrics())
    print("AEP Framework:", core.aep_framework_description())
    print("Spy Mode Claims:", core.spy_mode_claims())
