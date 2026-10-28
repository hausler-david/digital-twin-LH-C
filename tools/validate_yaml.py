#!/usr/bin/env python3
"""Validate one YAML document against one schema: python tools/validate_yaml.py <schema-name> <file.yaml>
Schema names: provenance (parameter files), machine, assumption, material, source, conflict, proposal,
experiment, simulation_run, optimization, component."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lhmuc.registry import load_yaml, validator  # noqa: E402

name, path = sys.argv[1], Path(sys.argv[2])
doc = load_yaml(path)
errs = sorted(validator(name).iter_errors(doc), key=lambda e: list(e.path))
for e in errs:
    print("/".join(str(p) for p in e.path), ":", e.message[:400])
print(f"{len(errs)} schema errors in {path}")
sys.exit(1 if errs else 0)
