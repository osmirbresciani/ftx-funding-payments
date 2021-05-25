import time
import urllib.parse
from typing import Optional, Dict, Any, List
import csv
from requests import Request, Session, Response
import hmac
from utils.csv_lib import *
from .api_keys import *


class FtxClient:
    _ENDPOINT = "https://ftx.com/api/"

    def __init__(self, api_key=API_KEY, api_secret=API_SECRET, subaccount_name=None) -> None:
        self._session = Session()
        self._api_key = api_key
        self._api_secret = api_secret
        self._subaccount_name = subaccount_name

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("GET", path, params=params)

    def _post(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("POST", path, json=params)

    def _delete(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("DELETE", path, json=params)

    def _request(self, method: str, path: str, **kwargs) -> Any:
        request = Request(method, self._ENDPOINT + path, **kwargs)
        self._sign_request(request)
        response = self._session.send(request.prepare())
        return self._process_response(response)

    def _sign_request(self, request: Request) -> None:
        ts = int(time.time() * 1000)
        prepared = request.prepare()
        signature_payload = f"{ts}{prepared.method}{prepared.path_url}".encode()
        if prepared.body:
            signature_payload += prepared.body
        signature = hmac.new(self._api_secret.encode(), signature_payload, "sha256").hexdigest()
        request.headers["FTX-KEY"] = self._api_key
        request.headers["FTX-SIGN"] = signature
        request.headers["FTX-TS"] = str(ts)
        if self._subaccount_name:
            request.headers["FTX-SUBACCOUNT"] = urllib.parse.quote(self._subaccount_name)

    def _process_response(self, response: Response) -> Any:
        try:
            data = response.json()
        except ValueError:
            response.raise_for_status()
            raise
        else:
            if not data["success"]:
                raise Exception(data["error"])
            return data["result"]

    def get_funding_payment_history(
        self,
        market: str = None,
        side: str = None,
        order_type: str = None,
        start_time: float = None,
        end_time: float = None,
    ) -> List[dict]:
        return self._get(
            f"funding_payments",
            {"market": market, "side": side, "orderType": order_type, "start_time": start_time, "end_time": end_time},
        )
