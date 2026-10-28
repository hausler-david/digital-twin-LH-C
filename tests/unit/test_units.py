import math

import pytest

from lhmuc.units import parse_unit, to_si


@pytest.mark.parametrize("u", ["GeV", "TeV", "cm^-2 s^-1", "fb^-1", "um", "T/m", "mm mrad", "MHz", "Hz",
                               "dimensionless", "degree", "mrad", "ms", "km", "percent", "nC", "T m", "g/cm^3",
                               "ab^-1", "events/year"])
def test_units_parse(u):
    parse_unit(u)


def test_bad_unit():
    with pytest.raises(ValueError):
        parse_unit("furlongs per fortnight squared nonsense")


def test_si_conversions():
    assert math.isclose(to_si(1.0, "TeV"), 1.602176634e-7, rel_tol=1e-9)   # joules
    assert math.isclose(to_si(4.8, "um"), 4.8e-6)
    assert math.isclose(to_si(2.1, "cm^-2 s^-1"), 2.1e4)                     # m^-2 s^-1
    assert math.isclose(to_si(1.0, "fb^-1"), 1e43)                           # m^-2
