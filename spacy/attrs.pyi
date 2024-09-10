from spacy.strings import StringStore

DEP: int
ENT_ID: int
ENT_IOB: int
ENT_KB_ID: int
ENT_TYPE: int

FLAG19: int
FLAG20: int
FLAG21: int
FLAG22: int
FLAG23: int
FLAG24: int
FLAG25: int
FLAG26: int
FLAG27: int
FLAG28: int
FLAG29: int
FLAG30: int
FLAG31: int
FLAG32: int
FLAG33: int
FLAG34: int
FLAG35: int
FLAG36: int
FLAG37: int
FLAG38: int
FLAG39: int
FLAG40: int
FLAG41: int
FLAG42: int
FLAG43: int
FLAG44: int
FLAG45: int
FLAG46: int
FLAG47: int
FLAG48: int
FLAG49: int
FLAG50: int
FLAG51: int
FLAG52: int
FLAG53: int
FLAG54: int
FLAG55: int
FLAG56: int
FLAG57: int
FLAG58: int
FLAG59: int
FLAG60: int
FLAG61: int
FLAG62: int
FLAG63: int
HEAD: int
ID: int
IDS: int
IDX: int

IOB_STRINGS: tuple[str]

IS_ALPHA: int
IS_ASCII: int
IS_BRACKET: int
IS_CURRENCY: int
IS_DIGIT: int
IS_LEFT_PUNCT: int
IS_LOWER: int
IS_OOV_DEPRECATED: int
IS_PUNCT: int
IS_QUOTE: int
IS_RIGHT_PUNCT: int
IS_SPACE: int
IS_STOP: int
IS_TITLE: int
IS_UPPER: int
LANG: int
LEMMA: int
LENGTH: int
LIKE_EMAIL: int
LIKE_NUM: int
LIKE_URL: int
LOWER: int
MORPH: int

NAMES: list[str]

NORM: int
ORTH: int
POS: int
PREFIX: int
SENT_START: int
SHAPE: int
SPACY: int
SUFFIX: int
TAG: int

def intify_attrs(
    stringy_attr: dict[str, str | int], strings_map: StringStore | None = None, _do_deprecated: bool = False
) -> dict[str, int]: ...

def intify_attr(stringy_attr: str) -> int: ...
