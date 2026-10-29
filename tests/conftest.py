import functools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import lhmuc.registry as _registry  # noqa: E402

# One registry load per test session: test modules import load_all after this conftest runs, so they share
# the cached Evidence. No test mutates it; tools that rewrite files run in subprocesses and load fresh.
_load_all_uncached = _registry.load_all


@functools.lru_cache(maxsize=None)
def _load_all_cached(root: Path = _registry.REPO_ROOT):
    return _load_all_uncached(root)


_registry.load_all = _load_all_cached
