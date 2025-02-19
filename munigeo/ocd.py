"""
Open Civic Data helper functions
"""

import re


def make_id(parent=None, **kwargs):
    country = kwargs.pop("country", "us")
    if len(kwargs) > 1:
        raise ValueError("only one kwarg is allowed for make_id")
    type, type_id = list(kwargs.items())[0]
    if not re.match(r"^[\w_-]+$", type):
        raise ValueError(r"type must match [\w_]+ [%s]" % type)
    type_id = type_id.lower()
    type_id = re.sub(r"\.? ", "_", type_id)
    type_id = re.sub(r"[^\w0-9~_.-]", "~", type_id)
    if parent:
        return "{parent}/{type}:{type_id}".format(
            parent=parent, type=type, type_id=type_id
        )
    else:
        return "ocd-division/country:{country}/{type}:{type_id}".format(
            type=type, type_id=type_id, country=country
        )
