import pandas as pd
import pytest
from chapter9_core import Chapter9Core

# Load book numbers for verification
BOOK_NUMBERS = pd.read_csv("data/book_numbers.csv").set_index("metric")

def test_energy_poverty_threshold():
    """Verify the Energy Poverty Threshold from the book."""
    expected_value = 10.0 # From prompt
    assert BOOK_NUMBERS.loc["Energy Poverty Threshold", "value"] == expected_value

def test_energy_burden_low_income():
    """Verify the Energy Burden for Low Income from the book."""
    expected_value = 15.0 # From prompt
    assert BOOK_NUMBERS.loc["Energy Burden - Low Income", "value"] == expected_value

def test_energy_burden_medium_income():
    """Verify the Energy Burden for Medium Income from the book."""
    expected_value = 8.0 # From prompt
    assert BOOK_NUMBERS.loc["Energy Burden - Medium Income", "value"] == expected_value

def test_energy_burden_high_income():
    """Verify the Energy Burden for High Income from the book."""
    expected_value = 3.0 # From prompt
    assert BOOK_NUMBERS.loc["Energy Burden - High Income", "value"] == expected_value

def test_protocol_offset():
    """Verify the Protocol Offset from the book."""
    expected_value = 60.0 # From prompt
    assert BOOK_NUMBERS.loc["Protocol Offset", "value"] == expected_value

def test_demographic_drain_rate():
    """Verify the Demographic Drain Rate from the book."""
    expected_value = 5.0 # From prompt
    assert BOOK_NUMBERS.loc["Demographic Drain Rate", "value"] == expected_value

def test_aep_node_efficiency():
    """Verify the AEP Node Efficiency from the book."""
    expected_value = 85.0 # From prompt
    assert BOOK_NUMBERS.loc["AEP Node Efficiency", "value"] == expected_value

def test_unrest_factor():
    """Verify the Unrest Factor from the book."""
    expected_value = 0.5 # From prompt
    assert BOOK_NUMBERS.loc["Unrest Factor", "value"] == expected_value

def test_sovereign_citizen_metric_2025():
    """Verify the 2025 Sovereign Citizen Metric from the book."""
    expected_value = 0.2 # From prompt
    assert BOOK_NUMBERS.loc["Sovereign Citizen Metric - 2025", "value"] == expected_value

def test_sovereign_citizen_metric_2030():
    """Verify the 2030 Sovereign Citizen Metric from the book."""
    expected_value = 0.8 # From prompt
    assert BOOK_NUMBERS.loc["Sovereign Citizen Metric - 2030", "value"] == expected_value


# Test for core calculations (simplified, as exact equations are placeholders)
def test_calculate_energy_burden():
    core = Chapter9Core()
    # Test with known inputs and expected outputs based on the simplified model
    # Assuming base_energy_burden = 0.20 as in chapter9_core.py
    # adjusted_burden = base_energy_burden * (1 - protocol_offset_rate * self.protocol_offset_max)
    # 0.20 * (1 - 0.3 * 0.6) = 0.20 * (1 - 0.18) = 0.20 * 0.82 = 0.164
    assert core.calculate_energy_burden(0.05, 0.3) == pytest.approx(0.164)

def test_protocol_enabled_utility_equation():
    core = Chapter9Core()
    # utility_gain = aep_node_efficiency * (1 - demographic_drain_rate)
    # 0.85 * (1 - 0.05) = 0.85 * 0.95 = 0.8075
    assert core.protocol_enabled_utility_equation(0.05, 0.85) == pytest.approx(0.8075)

def test_polynomial_of_social_unrest():
    core = Chapter9Core()
    # social_unrest = self.unrest_factor * (energy_burden**3)
    # Using energy_burden from previous test: 0.164
    # 0.5 * (0.164**3) = 0.5 * 0.004410944 = 0.002205472
    energy_burden_for_unrest = core.calculate_energy_burden(0.05, 0.3)
    assert core.polynomial_of_social_unrest(0.05, energy_burden_for_unrest) == pytest.approx(0.002205472)
