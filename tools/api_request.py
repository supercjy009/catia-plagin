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
            "Tecwin3DEUnitId": "CreateUdf"
        }
        response = httpx.request(method=method, url=url, headers=headers, json=payload, params=params, timeout=30)
        print(f"✅ response status>>>>>>>>{response.status_code}")

        # 检查响应内容类型是否为JSON
        content_type = response.headers.get('content-type', '')
        if response.status_code != 200:
            raise Exception(response.text)
        if 'application/json' in content_type:
            res = response.json()
            print(f"✅ res>>>>>>>>{res}")
            return res
        else:
            # 如果不是JSON，则返回文本内容
            res = response.text
            print(f"✅ res>>>>>>>>{res}")
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
        res = self._send_request(api_url, params={}, payload=payload)
        return res