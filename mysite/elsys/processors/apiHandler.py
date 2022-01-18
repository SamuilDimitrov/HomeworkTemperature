import requests

class ApiHandler:
    def __init__(self):
        data = requests.get("https://tues2022.proxy.beeceptor.com/my/api/test").json()
        self.temps = []

        for i in data['data']:
            self.temps.append(i['temperature'])

    def minimum_temp(self):
        return min(self.temps)

    def maximum_temp(self):
        return max(self.temps)

    def avg_temp(self):
        return sum(self.temps) / len(self.temps)