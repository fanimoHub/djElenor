from json import JSONEncoder
from json.encoder import ESCAPE_DCT, INFINITY, _make_iterencode, c_make_encoder

from .definitions import ESCAPE_CHARS

__all__ = ["SafeJSONEncoder"]


class SafeJSONEncoder(JSONEncoder):
    @property
    def escape_chars_pattern(self):
        return ESCAPE_CHARS

    def make_safe_string(self, s: str):
        def replace(match):
            c = match.group(0)
            if c not in ESCAPE_DCT:
                return r"\u{:04x}".format(ord(c))
            return ESCAPE_DCT[c]

        return '"{}"'.format(self.escape_chars_pattern.sub(replace, s))

    def encode(self, o):
        if isinstance(o, str):
            return self.make_safe_string(o)
        return super().encode(o)

    def iterencode(self, o, _one_shot=False):
        """Encode the given object and yield each string
        representation as available.

        For example::

            for chunk in JSONEncoder().iterencode(bigobject):
                mysocket.write(chunk)

        """
        if self.check_circular:
            markers = {}
        else:
            markers = None

        _encoder = self.make_safe_string

        def floatstr(
            o,
            allow_nan=self.allow_nan,
            _repr=float.__repr__,
            _inf=INFINITY,
            _neginf=-INFINITY,
        ):
            # Check for specials.  Note that this type of test is processor
            # and/or platform-specific, so do tests which don't depend on the
            # internals.

            if o != o:
                text = "NaN"
            elif o == _inf:
                text = "Infinity"
            elif o == _neginf:
                text = "-Infinity"
            else:
                return _repr(o)

            if not allow_nan:
                raise ValueError(
                    "Out of range float values are not JSON compliant: " + repr(o)
                )

            return text

        if _one_shot and c_make_encoder is not None and self.indent is None:
            _iterencode = c_make_encoder(
                markers,
                self.default,
                _encoder,
                self.indent,
                self.key_separator,
                self.item_separator,
                self.sort_keys,
                self.skipkeys,
                self.allow_nan,
            )
        else:
            _iterencode = _make_iterencode(
                markers,
                self.default,
                _encoder,
                self.indent,
                floatstr,
                self.key_separator,
                self.item_separator,
                self.sort_keys,
                self.skipkeys,
                _one_shot,
            )
        return _iterencode(o, 0)
