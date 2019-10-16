from collections import namedtuple

MinMax = namedtuple("MinMax", ["min", "max"])


class UserInputParser:
    """
    Helper class to interpret text input from user
    """
    def __init__(self, invalid_token):
        self.invalid_token = invalid_token

    def parse_number(self, submission):
        try:
            return float(submission)
        except ValueError:
            return self.invalid_token

    def parse_number_range(self, submission):
        if "-" in submission:
            min_max_entries = submission.split("-")
            min_max = MinMax(self.parse_number(min_max_entries[0]),
                             self.parse_number(min_max_entries[1]))
            if min_max.min == self.invalid_token or min_max.max == self.invalid_token:
                return self.invalid_token
            if min_max.min > min_max.max:
                return MinMax(min_max.max, min_max.min)
            return min_max
        return self.parse_number(submission)
