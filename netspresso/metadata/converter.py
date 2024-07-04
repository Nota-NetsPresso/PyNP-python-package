from dataclasses import dataclass, field
from typing import List

from netspresso.enums import (
    DataType,
    DeviceName,
    Framework,
    SoftwareVersion,
    Status,
    TaskType,
)
from netspresso.metadata.common import AvailableOption, ExceptionDetail, ModelInfo


@dataclass
class ConvertInfo:
    convert_task_uuid: str = ""
    framework: Framework = ""
    display_framework: str = ""
    device_name: DeviceName = ""
    display_device_name: str = ""
    display_brand_name: str = ""
    data_type: DataType = ""
    software_version: SoftwareVersion = ""
    display_software_version: str = ""
    model_file_name: str = ""
    input_model_uuid: str = ""
    output_model_uuid: str = ""


@dataclass
class ConverterMetadata:
    status: Status = Status.IN_PROGRESS
    message: str = ""
    task_type: TaskType = TaskType.CONVERT
    input_model_path: str = ""
    converted_model_path: str = ""
    model_info: ModelInfo = field(default_factory=ModelInfo)
    convert_task_info: ConvertInfo = field(default_factory=ConvertInfo)
    available_options: List[AvailableOption] = field(default_factory=list)

    def update_message(self, exception_detail):
        if isinstance(exception_detail, str):
            self.message.message = exception_detail
        else:
            self.message = ExceptionDetail(**exception_detail)