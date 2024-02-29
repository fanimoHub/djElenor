import json

from .encoder import SafeJSONEncoder
from .sanitizer import DraftJSSanitizer

__all__ = ["DraftJSSanitizer", "SafeJSONEncoder", "clean_draft_js", "to_string"]


def clean_draft_js(definitions: dict):
    """Sanitize a given DraftJS JSON definitions for saving or exporting."""
    cls = DraftJSSanitizer()
    return cls.sanitize(definitions)


def to_string(definitions: dict, full_clean=False, **kwargs) -> str:
    """Sanitize risky characters from the definitions to allow putting the JSON safely
    into HTML code.

    :param definitions: The DraftJS dictionary to make safe for HTML.

    :param kwargs: Additional parameters for ``json.dumps(...)``.

    :param full_clean: Whether all the checks should be ran instead of only checking for
        dangerous characters. Basically runs ``clean_draft_js`` before dumping.
    """
    kwargs.setdefault("cls", SafeJSONEncoder)

    if full_clean:
        definitions = definitions.copy()
        clean_draft_js(definitions)

    return json.dumps(definitions, **kwargs)
