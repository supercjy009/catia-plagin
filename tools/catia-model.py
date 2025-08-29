from collections.abc import Generator
import json
import re
import time
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
# 导入 logging 和自定义处理器
import logging
from dify_plugin.config.logger_format import plugin_logger_handler
# 使用自定义处理器设置日志
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(plugin_logger_handler)

class CatiaModelTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
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
        # 模拟耗时两秒
        time.sleep(2)
        # 根据template进行不同的处理
        if template == "创建基本结构" or template == "CreateBasicStructure":
            # 这里可以添加对CreateBasicStructure模板的具体处理逻辑
            yield self.create_text_message(f"参数解析完成\n开始调用[创建基本结构]模板...\n")
        elif template == "创建加强筋结构" or template == "CreateRibStructure":
            # 这里可以添加对CreateRibStructure模板的具体处理逻辑
            yield self.create_text_message(f"参数解析完成\n开始调用[创建加强筋结构]模板...\n")
        elif template == "裁切边界" or template == "CuttingBoundary":
            yield self.create_text_message(f"参数解析完成\n开始调用[裁切边界]模板...\n")
        else: yield self.create_text_message(f"ERROR未找到调用模板.")
