from ._api import Yuuz12Api


class Invitation(Yuuz12Api):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["invitation"],
            key_name="invitation",
            version=1,
            **kwargs
        )
        self._base_url = f"{self.BASE_URL_FST}/{'/'.join(self._nodes)}"

    def __getattr__(self, api_name: str):
        return self.call_api(f"{api_name}.php")
