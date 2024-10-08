from product_fusion_backend.core.schema.common_response_schema import APIResponse, CommonResponseSchema
from product_fusion_backend.core.services.email_service import email_service
from product_fusion_backend.core.services.redis_service import redis_service
from product_fusion_backend.core.utils.constants import (
    DEFAULT_ROUTE_OPTIONS,
    INVITE_MEMBER_MAIL_TEMPLATE,
    LOGIN_ALERT_MAIL_TEMPLATE,
    PASSWORD_RESET_MAIL_TEMPLATE,
    PASSWORD_UPDATE_MAIL_TEMPLATE,
    SKIP_URLS,
    VERIFY_EMAIL_TEMPLATE,
    VERIFY_EMAIL_WITH_PASS_RESET_TEMPLATE,
)
from product_fusion_backend.core.utils.enums import StatusEnum
from product_fusion_backend.core.utils.hash_utils import HashManager
from product_fusion_backend.core.utils.logging import configure_logging, end_stage_logger, logger, stage_logger
from product_fusion_backend.core.utils.open_telemetry_config import OpenTelemetry

__all__ = [
    # Constants
    "StatusEnum",
    "DEFAULT_ROUTE_OPTIONS",
    "SKIP_URLS",
    # Common Schemas
    "CommonResponseSchema",
    "APIResponse",
    # Logging
    "logger",
    "stage_logger",
    "end_stage_logger",
    "configure_logging",
    # Tracing
    "OpenTelemetry",
    # Utils
    "HashManager",
    # Services
    "email_service",
    "redis_service",
    # Templates
    "PASSWORD_RESET_MAIL_TEMPLATE",
    "INVITE_MEMBER_MAIL_TEMPLATE",
    "VERIFY_EMAIL_TEMPLATE",
    "PASSWORD_UPDATE_MAIL_TEMPLATE",
    "LOGIN_ALERT_MAIL_TEMPLATE",
    "VERIFY_EMAIL_WITH_PASS_RESET_TEMPLATE",
]
