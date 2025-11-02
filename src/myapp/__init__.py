# ╭─────────────────────── Important ────────────────────────╮
# │                                                          │
# │ Don't modify code within the border down below, unless   │
# │ you know what you are doing. The "import" sequences      │
# │ below controls the trigger points for overloading rya.   │
# │ You can import your own modules as you wish outside the  │
# │ border.                                                  │
# │                                                          │
# ╰──────────────────────────────────────────────────────────╯

from properpath import P

# Only modules from rya.pre_utils should be imported.
from rya.pre_utils import (
    LayerLoader,
    get_logger,
    load_basic_debug_mode,
)

# Only main app layers that don't rely on rya (except
# rya.pre_utils)layer should be imported. The following
# triggers sys.modules registration of the
# .names. __init__
from .names import AppIdentity

LayerLoader.logger = P.default_err_logger = get_logger()
load_basic_debug_mode(AppIdentity.app_name, reload=True)
LayerLoader.enable_bootstrap_mode(
    root_installation_dir=P(__file__).parent,
    app_name=AppIdentity.app_name,
)
# The following triggers .config.__hook__ where the Pydantic
# configuration model can be defined. You can also import your
# model directly here (and remove this line).
from .config import __hook__  # noqa: E402, F401

# The border
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# The following import calls get_logger. This makes sure when
# the app is imported as a package "import <myapp>", it
# automatically registers the main "myapp" logger to
# Python's built-in logging.
from .loggers import __hook__  # noqa: E402, F401

__all__ = []
