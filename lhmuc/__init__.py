"""LHμC-VirtualLab core package.

Phase 0 scope: provenance-aware parameter registry, schema validation, registry export and the
audit arithmetic used to cross-check reported LHμC values. Nothing here is a digital twin.
"""
from pathlib import Path

__version__ = "0.0.1"
REPO_ROOT = Path(__file__).resolve().parent.parent
