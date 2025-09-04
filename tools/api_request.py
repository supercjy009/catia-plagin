import json
from typing import Any, Optional, cast

import httpx

class ApiRequest:
    def __init__(self,  api_url: str):
        self.api_url = api_url
    def _send_request(
        self,
        url: str,
        method: str = "post",
        payload: Optional[dict] = None,
        params: Optional[dict] = None,
    ):
        headers = {
            "Content-Type": "application/json",
        }
        res = httpx.request(method=method, url=url, headers=headers, json=payload, params=params, timeout=30).json()
        if res.get("code") != 200:
            raise Exception(res)
        return res

    def callModelingTemplate(
        self,
        template: str,
        output_location: str,
        paramList:list,
    ) -> dict:
        # 调用建模接口
        api_url = f"{self.api_url}"
        input_parameters = {}
        input_features = {}
        
        for item in paramList:
            if "paramName" in item and "paramValue" in item:
                input_parameters[item["paramName"]] = item["paramValue"]
            elif "featureName" in item and "featureValue" in item:
                input_features[item["featureName"]] = item["featureValue"]
        template_to_id = {
            "BasicShape": "1",
            "Reinforcement": "2",
            "TrimBoundary": "3"
        }
        payload = {
            "Id": template_to_id.get(template, ""),
            "Description": template,
            "input_features": input_features,
            "input_parameters": input_parameters,
            "module": "",
            "template": "PC/" + template,
            "output_location": output_location,
            "output_name": template,
        }
        # if not fields:
        #     fields_list = []
        # else:
        #     try:
        #         fields_list = json.loads(fields)
        #     except json.JSONDecodeError:
        #         raise ValueError("The input string is not valid JSON")
        res: dict = self._send_request(api_url, params={}, payload=payload)
        if "data" in res:
            data: dict = res.get("data", {})
            return data
        return res