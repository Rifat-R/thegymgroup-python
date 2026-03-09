import requests

BASE_HEADERS = {
    "accept": "application/json",
    "accept-encoding": "gzip",
    "connection": "Keep-Alive",
    "host": "thegymgroup.netpulse.com",
    "user-agent": "okhttp/3.12.3",
    "x-np-user-agent": "clientType=MOBILE_DEVICE; devicePlatform=ANDROID; deviceUid=; applicationName=The Gym Group; applicationVersion=5.0; applicationVersionCode=38",
}


class Client:
    def __init__(self, profile_headers, uuid):
        self.profile_headers = profile_headers
        self.uuid = uuid

    def _get_url(self, url):
        profile = requests.get(url, headers=self.profile_headers)
        return profile.json()

    @classmethod
    def login(cls, email: str, pin: str):
        creds = {"username": email, "password": pin}
        base_headers = BASE_HEADERS.copy()

        response = requests.post(
            "https://thegymgroup.netpulse.com/np/exerciser/login",
            data=creds,
            headers=base_headers,
        )
        profile_headers = base_headers.copy()
        cookie = response.headers["Set-Cookie"]
        profile_headers["cookie"] = cookie
        user_id = response.json()["uuid"]
        return cls(profile_headers, user_id)

    def get_hours_in_gym(self) -> int:
        mins = 0
        visits = self._get_url(
            "https://thegymgroup.netpulse.com/np/exercisers/"
            + self.uuid
            + "/check-ins/history?endDate=2026-10-09T15%3A02%3A56",
        )

        for i in visits["checkIns"]:
            mins += i["duration"] / 60000

        return round(mins / 60)
