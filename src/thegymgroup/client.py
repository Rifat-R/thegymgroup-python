import requests

BASE_URL = "https://thegymgroup.netpulse.com"

BASE_HEADERS = {
    "accept": "application/json",
    "accept-encoding": "gzip",
    "connection": "Keep-Alive",
    "host": "thegymgroup.netpulse.com",
    "user-agent": "okhttp/3.12.3",
    "x-np-api-version": "1.5",
    "x-np-app-version": "9999",
}

USER_AGENT_TEMPLATE = (
    "clientType=MOBILE_DEVICE; devicePlatform=ANDROID; deviceUid={device_uid}; "
    "applicationName=The Gym Group; applicationVersion={app_version}; "
    "applicationVersionCode={app_version_code}"
)


class Client:
    def __init__(self, session: requests.Session, exerciser_uuid: str):
        self.session = session
        self.exerciser_uuid = exerciser_uuid

    def _get(self, path: str, params: dict | None = None):
        response = self.session.get(f"{BASE_URL}{path}", params=params)
        response.raise_for_status()
        return response.json()

    def _post(self, path: str, data: dict | None = None):
        response = self.session.post(f"{BASE_URL}{path}", data=data)
        response.raise_for_status()
        if response.content:
            return response.json()
        return None

    @staticmethod
    def _build_user_agent(
        device_uid: str,
        app_version: str,
        app_version_code: str,
    ) -> str:
        return USER_AGENT_TEMPLATE.format(
            device_uid=device_uid,
            app_version=app_version,
            app_version_code=app_version_code,
        )

    @classmethod
    def login(
        cls,
        email: str,
        pin: str,
        *,
        device_uid: str = "",
        app_version: str = "6.5.1",
        app_version_code: str = "38",
        app_version_header: str = "9999",
    ):
        session = requests.Session()
        headers = BASE_HEADERS.copy()
        headers["x-np-app-version"] = app_version_header
        headers["x-np-user-agent"] = cls._build_user_agent(
            device_uid=device_uid,
            app_version=app_version,
            app_version_code=app_version_code,
        )
        headers["content-type"] = "application/x-www-form-urlencoded"
        session.headers.update(headers)

        creds = {"username": email, "password": pin}
        response = session.post(f"{BASE_URL}/np/exerciser/login", data=creds)
        response.raise_for_status()
        user_id = response.json()["uuid"]
        return cls(session, user_id)

    def logout(self):
        return self._post("/np/logout")

    def get_schedule(
        self,
        *,
        start_datetime: int | None = None,
        end_datetime: int | None = None,
        club_uuid: str | None = None,
    ):
        params = {}
        if start_datetime is not None:
            params["startDateTime"] = start_datetime
        if end_datetime is not None:
            params["endDateTime"] = end_datetime
        if club_uuid is not None:
            params["clubUuid"] = club_uuid
        return self._get(f"/np/exerciser/{self.exerciser_uuid}/schedule", params=params)

    def get_class(self, company_uuid: str, class_uuid: str):
        return self._get(f"/np/company/{company_uuid}/class/{class_uuid}")

    def get_classes(
        self,
        company_uuid: str,
        *,
        start_datetime: int,
        end_datetime: int,
        exerciser_uuid: str | None = None,
        class_type: str | None = None,
    ):
        params = {
            "startDateTime": start_datetime,
            "endDateTime": end_datetime,
            "exerciserUuid": exerciser_uuid or self.exerciser_uuid,
        }
        if class_type is not None:
            params["type"] = class_type
        return self._get(f"/np/company/{company_uuid}/classes", params=params)

    def get_gym_busyness(self, gym_location_id: str):
        params = {"gymLocationId": gym_location_id}
        return self._get(
            f"/np/thegymgroup/v1.0/exerciser/{self.exerciser_uuid}/gym-busyness",
            params=params,
        )

    def get_check_ins_history(self, start_date: str, end_date: str):
        params = {"startDate": start_date, "endDate": end_date}
        return self._get(
            f"/np/exercisers/{self.exerciser_uuid}/check-ins/history",
            params=params,
        )

    def get_latest_check_in(self):
        return self._get(f"/np/exercisers/{self.exerciser_uuid}/latest-check-in")

    def get_exerciser(self):
        return self._get(f"/np/exerciser/{self.exerciser_uuid}")

    def get_membership(self):
        return self._get(f"/np/exerciser/{self.exerciser_uuid}/membership")

    def get_hours_in_gym(self, start_date: str, end_date: str) -> int:
        mins = 0
        visits = self.get_check_ins_history(start_date=start_date, end_date=end_date)

        for i in visits.get("checkIns", []):
            mins += i.get("duration", 0) / 60000

        return round(mins / 60)
