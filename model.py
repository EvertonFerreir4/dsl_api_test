class ApiSpec:
    def __init__(self, base_url=None, scenarios=None):
        self.base_url = base_url
        self.scenarios = scenarios or []

class Scenario:
    def __init__(self, name, cases=None):
        self.name = name
        self.cases = cases or []

class Case:
    def __init__(self, name, request=None, expect=None):
        self.name = name
        self.request = request or {}
        self.expect = expect or {}
