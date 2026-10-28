"""Unit handling. SI internally; explicit conversions at tool boundaries.

Uses pint. Extra units needed in collider physics are registered here once so that every YAML
`unit` string is parseable with :func:`parse_unit`.
"""
from __future__ import annotations

from functools import lru_cache

import pint

_EXTRA_DEFINITIONS = [
    "barn = 1e-28 m**2 = b",
    "femtobarn = 1e-15 * barn = fb",
    "picobarn = 1e-12 * barn = pb",
    "attobarn = 1e-18 * barn = ab",
    "inverse_femtobarn = 1 / femtobarn = fb^-1 = ifb",
    "inverse_picobarn = 1 / picobarn = pb^-1 = ipb",
    "inverse_attobarn = 1 / attobarn = ab^-1 = iab",
    "tesla_metre = tesla * meter = T_m",
    "teslametre = tesla * meter",
    "pi_mm_mrad = 1e-6 * meter = pimmmrad",
    "mm_mrad = 1e-6 * meter = mmmrad",
    "GeV_per_c = gigaelectron_volt / speed_of_light",
    "MeV_per_c = megaelectron_volt / speed_of_light",
    "eVc = electron_volt / speed_of_light",
    "micrometre = micrometer = um",
    "percent_ = 0.01 * dimensionless",
]


@lru_cache(maxsize=1)
def ureg() -> pint.UnitRegistry:
    reg = pint.UnitRegistry()
    for d in _EXTRA_DEFINITIONS:
        try:
            reg.define(d)
        except (pint.errors.DefinitionSyntaxError, pint.errors.RedefinitionError):
            pass
    return reg


# Canonical unit strings accepted in parameter records that pint cannot parse literally.
UNIT_ALIASES = {
    "dimensionless": "dimensionless",
    "1": "dimensionless",
    "cm^-2 s^-1": "1/(centimeter**2 * second)",
    "cm**-2 s**-1": "1/(centimeter**2 * second)",
    "1/(cm^2 s)": "1/(centimeter**2 * second)",
    "fb^-1": "1/femtobarn",
    "pb^-1": "1/picobarn",
    "ab^-1": "1/attobarn",
    "fb^-1/year": "1/(femtobarn*year)",
    "T/m": "tesla/meter",
    "T*m": "tesla*meter",
    "T m": "tesla*meter",
    "mm mrad": "mm_mrad",
    "pi mm mrad": "pi_mm_mrad",
    "um": "micrometer",
    "µm": "micrometer",
    "μm": "micrometer",
    "GeV/c": "GeV_per_c",
    "MeV/c": "MeV_per_c",
    "percent": "percent_",
    "%": "percent_",
    "turns": "dimensionless",
    "bunches": "dimensionless",
    "particles": "dimensionless",
    "events": "dimensionless",
    "events/year": "1/year",
    "degree": "degree",
    "deg": "degree",
    "mrad": "milliradian",
    "mA": "milliampere",
    "MW": "megawatt",
    "kW": "kilowatt",
    "GV": "gigavolt",
    "MHz": "megahertz",
    "kHz": "kilohertz",
    "Hz": "hertz",
    "ms": "millisecond",
    "us": "microsecond",
    "µs": "microsecond",
    "ns": "nanosecond",
    "km": "kilometer",
    "m": "meter",
    "cm": "centimeter",
    "mm": "millimeter",
    "GeV": "gigaelectron_volt",
    "TeV": "teraelectron_volt",
    "MeV": "megaelectron_volt",
    "keV": "kiloelectron_volt",
    "eV": "electron_volt",
    "meV": "millielectron_volt",
    "nC": "nanocoulomb",
    "T": "tesla",
    "s": "second",
    "year": "year",
    "g/cm^3": "gram/centimeter**3",
    "string": "dimensionless",
}


def parse_unit(unit: str):
    """Return a pint Unit for a registry unit string, or raise ValueError."""
    reg = ureg()
    text = UNIT_ALIASES.get(unit.strip(), unit)
    try:
        return reg.parse_units(text)
    except Exception as exc:  # pint raises several error types
        raise ValueError(f"unparseable unit {unit!r}: {exc}") from exc


def quantity(value: float, unit: str):
    return value * parse_unit(unit)


def to_si(value: float, unit: str) -> float:
    """Convert a value in `unit` to SI base units (magnitude only)."""
    return float(quantity(value, unit).to_base_units().magnitude)
