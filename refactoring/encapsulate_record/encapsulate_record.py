
# old_data
organization = {"name": "acme", "country": "GB"}

#new data
class Organization(object):
    def __init__(self):
        self._name = "acme"
        self._country = "GB"

    def get_name(self):
        return self._name

    def get_country(self):
        return self._country
