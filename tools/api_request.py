import json
from typing import Any, Optional, cast

import httpx

class ApiRequest:
    def __init__(self,  host: str):
        self.host = host
    def _send_request(
        self,
        url: str,
        method: str = "post",
        payload: Optional[dict] = None,
        params: Optional[dict] = None,
    ):
        headers = {
            "Content-Type": "application/json",
            "user-agent": "Dify",
        }
        res = httpx.request(method=method, url=url, headers=headers, json=payload, params=params, timeout=30).json()
        if res.get("code") != 0:
            raise Exception(res)
        return res

    def callModelingTemplate(
        self,
        template: str,
        paramList:list,
    ) -> dict:
        # 调用建模接口
        url = f"{self.host}/api/post"
        params = {
            "template": template,
        }
        # if not fields:
        #     fields_list = []
        # else:
        #     try:
        #         fields_list = json.loads(fields)
        #     except json.JSONDecodeError:
        #         raise ValueError("The input string is not valid JSON")
        payload = {
            "template": template,
            "paramList": paramList,
        }
        res: dict = self._send_request(url, params=params, payload=payload)
        if "data" in res:
            data: dict = res.get("data", {})
            return data
        return res