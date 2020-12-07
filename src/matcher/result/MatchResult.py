from typing import Any


class MatchResult:
    sentence: str
    matches: list
    match_groups = None
    processed = []
    expression = False

    def __init__(self, sentence: str = '', matches=None, match_groups=None) -> None:
        if matches is None:
            self.matches = self.processed = []

        self.sentence = sentence
        self.matches = matches
        self.match_groups = match_groups

    def __getattribute__(self, name: str) -> Any:
        value = super(MatchResult, self).__getattribute__(name)

        if name == 'processed' and len(value) == 0:
            return self.matches

        if value is None:
            return ''

        return super(MatchResult, self).__getattribute__(name)

    def get_matches(self, key):
        if len(self.matches) > key:
            return self.matches[key]

        return None

    def is_matched(self) -> bool:
        return self.matches != '' and (isinstance(self.matches, str) or len(self.matches) > 0)
