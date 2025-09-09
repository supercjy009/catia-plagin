from collections.abc import Generator
import json
import re
import time
from typing import Any
import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
# 导入 logging 和自定义处理器
import logging
from dify_plugin.config.logger_format import plugin_logger_handler

from tools.api_request import ApiRequest
# 使用自定义处理器设置日志
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(plugin_logger_handler)

class CatiaModelTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        api_url = self.runtime.credentials.get("api_url")
        if not api_url:
            yield self.create_text_message("Error: Catia Server Host IP 未配置.")
        if not api_url.startswith(("http://", "https://")):
            api_url = "http://" + api_url
        ### 测试http://192.168.31.114:5000/test这个地址是否能联通
        # url = "http://192.168.31.114:5000/test"

        # try:
        #     response = requests.get(url, timeout=5)  # 设置超时时间为5秒
        #     print(f"✅ 连接成功！状态码：{response.status_code}")
        #     print(f"响应内容（前200字符）：{response.text[:200]}")
        # except requests.exceptions.RequestException as e:
        #     print(f"❌ 连接失败！错误信息：{e}")

        parameter = tool_parameters.get("Parameter", "No Parameter provided")
        # logger.info(f"get param.{parameter}")
        json_objects = re.findall(r'\{.*?\}', parameter)
        # 用于存放解析后的字典
        parsed_data = []
        for obj_str in json_objects:
            try:
                # 解析每个 JSON 字符串对象
                parsed = json.loads(obj_str)
                parsed_data.append(parsed)
            except json.JSONDecodeError as e:
                yield self.create_text_message(f"Error parsing JSON object: {e}")
        template = tool_parameters.get("Template", "No Template provided")
        output_location = tool_parameters.get("OutputLocation", "No OutputLocation provided")
        api = ApiRequest(api_url)
        print(f"✅ parsed_data：{parsed_data}")
        # 模拟耗时1秒
        time.sleep(1)
        # 根据template进行不同的处理
        if template == "创建基本结构" or template == "BasicShape":
            api.callModelingTemplate("BasicShape", output_location, parsed_data)
            yield self.create_text_message(f"\n调用[创建基本结构]模板完成.\n")
        elif template == "创建加强筋结构" or template == "Reinforcement":
            api.callModelingTemplate("Reinforcement", output_location, parsed_data)
            yield self.create_text_message(f"\n调用[创建加强筋结构]完成.\n")
        elif template == "裁切边界" or template == "TrimBoundary":
            api.callModelingTemplate("TrimBoundary", output_location, parsed_data)
            yield self.create_text_message(f"\n调用[裁切边界]完成.\n")
        else: yield self.create_text_message(f"ERROR未找到调用模板.")
