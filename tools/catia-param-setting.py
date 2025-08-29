from collections.abc import Generator
import json
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class CatiaParamSettingTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        paramName = tool_parameters["ParameterName"]
        paramValue = tool_parameters["ParameterValue"]
        data = {
            "paramName": paramName,
            "paramValue": paramValue,
        }
        message = json.dumps(data, ensure_ascii=False) 
        yield self.create_text_message(message)
