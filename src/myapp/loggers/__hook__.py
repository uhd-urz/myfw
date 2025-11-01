# ┌────────────────────────── Note ──────────────────────────┐
# │                                                          │
# │ The __hook__ module is imported by the top-most          │
# │ level__init__.py module, which will trigger/run all      │
# │ imports in __init__.py. If you wish to avoid that, you   │
# │ can remove this file before making sure that you import  │
# │ get_logger outside the box found in the top-most level   │
# │ __init__.py. Calling get_logger early makes sure the     │
# │ logger named '<your app>' is registered to Python's      │
# │ logging so you can do `logging.getLogger("<your app>")`. │
# │                                                          │
# └──────────────────────────────────────────────────────────┘
