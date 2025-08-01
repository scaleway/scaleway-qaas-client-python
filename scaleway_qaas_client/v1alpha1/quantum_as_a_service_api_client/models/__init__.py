"""Contains all the data models used in inputs/outputs"""

from .cancel_job_body import CancelJobBody
from .cancel_process_body import CancelProcessBody
from .create_job_body import CreateJobBody
from .create_job_body_circuit import CreateJobBodyCircuit
from .create_process_body import CreateProcessBody
from .create_session_body import CreateSessionBody
from .create_session_body_booking_demand import CreateSessionBodyBookingDemand
from .list_applications_application_type import ListApplicationsApplicationType
from .list_applications_order_by import ListApplicationsOrderBy
from .list_bookings_order_by import ListBookingsOrderBy
from .list_job_results_order_by import ListJobResultsOrderBy
from .list_jobs_order_by import ListJobsOrderBy
from .list_platforms_order_by import ListPlatformsOrderBy
from .list_platforms_platform_technology import ListPlatformsPlatformTechnology
from .list_platforms_platform_type import ListPlatformsPlatformType
from .list_process_results_order_by import ListProcessResultsOrderBy
from .list_processes_order_by import ListProcessesOrderBy
from .list_sessions_order_by import ListSessionsOrderBy
from .scaleway_qaas_v1_alpha_1_application import ScalewayQaasV1Alpha1Application
from .scaleway_qaas_v1_alpha_1_application_type import (
    ScalewayQaasV1Alpha1ApplicationType,
)
from .scaleway_qaas_v1_alpha_1_booking import ScalewayQaasV1Alpha1Booking
from .scaleway_qaas_v1_alpha_1_booking_status import ScalewayQaasV1Alpha1BookingStatus
from .scaleway_qaas_v1_alpha_1_job import ScalewayQaasV1Alpha1Job
from .scaleway_qaas_v1_alpha_1_job_circuit import ScalewayQaasV1Alpha1JobCircuit
from .scaleway_qaas_v1_alpha_1_job_result import ScalewayQaasV1Alpha1JobResult
from .scaleway_qaas_v1_alpha_1_job_status import ScalewayQaasV1Alpha1JobStatus
from .scaleway_qaas_v1_alpha_1_list_applications_response import (
    ScalewayQaasV1Alpha1ListApplicationsResponse,
)
from .scaleway_qaas_v1_alpha_1_list_bookings_response import (
    ScalewayQaasV1Alpha1ListBookingsResponse,
)
from .scaleway_qaas_v1_alpha_1_list_job_results_response import (
    ScalewayQaasV1Alpha1ListJobResultsResponse,
)
from .scaleway_qaas_v1_alpha_1_list_jobs_response import (
    ScalewayQaasV1Alpha1ListJobsResponse,
)
from .scaleway_qaas_v1_alpha_1_list_platforms_response import (
    ScalewayQaasV1Alpha1ListPlatformsResponse,
)
from .scaleway_qaas_v1_alpha_1_list_process_results_response import (
    ScalewayQaasV1Alpha1ListProcessResultsResponse,
)
from .scaleway_qaas_v1_alpha_1_list_processes_response import (
    ScalewayQaasV1Alpha1ListProcessesResponse,
)
from .scaleway_qaas_v1_alpha_1_list_session_ac_ls_request_order_by import (
    ScalewayQaasV1Alpha1ListSessionACLsRequestOrderBy,
)
from .scaleway_qaas_v1_alpha_1_list_session_ac_ls_response import (
    ScalewayQaasV1Alpha1ListSessionACLsResponse,
)
from .scaleway_qaas_v1_alpha_1_list_sessions_response import (
    ScalewayQaasV1Alpha1ListSessionsResponse,
)
from .scaleway_qaas_v1_alpha_1_platform import ScalewayQaasV1Alpha1Platform
from .scaleway_qaas_v1_alpha_1_platform_availability import (
    ScalewayQaasV1Alpha1PlatformAvailability,
)
from .scaleway_qaas_v1_alpha_1_platform_booking_requirement import (
    ScalewayQaasV1Alpha1PlatformBookingRequirement,
)
from .scaleway_qaas_v1_alpha_1_platform_hardware import (
    ScalewayQaasV1Alpha1PlatformHardware,
)
from .scaleway_qaas_v1_alpha_1_platform_price_per_circuit import (
    ScalewayQaasV1Alpha1PlatformPricePerCircuit,
)
from .scaleway_qaas_v1_alpha_1_platform_price_per_hour import (
    ScalewayQaasV1Alpha1PlatformPricePerHour,
)
from .scaleway_qaas_v1_alpha_1_platform_price_per_shot import (
    ScalewayQaasV1Alpha1PlatformPricePerShot,
)
from .scaleway_qaas_v1_alpha_1_platform_technology import (
    ScalewayQaasV1Alpha1PlatformTechnology,
)
from .scaleway_qaas_v1_alpha_1_platform_type import ScalewayQaasV1Alpha1PlatformType
from .scaleway_qaas_v1_alpha_1_process import ScalewayQaasV1Alpha1Process
from .scaleway_qaas_v1_alpha_1_process_result import ScalewayQaasV1Alpha1ProcessResult
from .scaleway_qaas_v1_alpha_1_process_status import ScalewayQaasV1Alpha1ProcessStatus
from .scaleway_qaas_v1_alpha_1_session import ScalewayQaasV1Alpha1Session
from .scaleway_qaas_v1_alpha_1_session_access import ScalewayQaasV1Alpha1SessionAccess
from .scaleway_qaas_v1_alpha_1_session_origin_type import (
    ScalewayQaasV1Alpha1SessionOriginType,
)
from .scaleway_qaas_v1_alpha_1_session_status import ScalewayQaasV1Alpha1SessionStatus
from .terminate_session_body import TerminateSessionBody
from .update_booking_body import UpdateBookingBody
from .update_job_body import UpdateJobBody
from .update_process_body import UpdateProcessBody
from .update_session_body import UpdateSessionBody

__all__ = (
    "CancelJobBody",
    "CancelProcessBody",
    "CreateJobBody",
    "CreateJobBodyCircuit",
    "CreateProcessBody",
    "CreateSessionBody",
    "CreateSessionBodyBookingDemand",
    "ListApplicationsApplicationType",
    "ListApplicationsOrderBy",
    "ListBookingsOrderBy",
    "ListJobResultsOrderBy",
    "ListJobsOrderBy",
    "ListPlatformsOrderBy",
    "ListPlatformsPlatformTechnology",
    "ListPlatformsPlatformType",
    "ListProcessesOrderBy",
    "ListProcessResultsOrderBy",
    "ListSessionsOrderBy",
    "ScalewayQaasV1Alpha1Application",
    "ScalewayQaasV1Alpha1ApplicationType",
    "ScalewayQaasV1Alpha1Booking",
    "ScalewayQaasV1Alpha1BookingStatus",
    "ScalewayQaasV1Alpha1Job",
    "ScalewayQaasV1Alpha1JobCircuit",
    "ScalewayQaasV1Alpha1JobResult",
    "ScalewayQaasV1Alpha1JobStatus",
    "ScalewayQaasV1Alpha1ListApplicationsResponse",
    "ScalewayQaasV1Alpha1ListBookingsResponse",
    "ScalewayQaasV1Alpha1ListJobResultsResponse",
    "ScalewayQaasV1Alpha1ListJobsResponse",
    "ScalewayQaasV1Alpha1ListPlatformsResponse",
    "ScalewayQaasV1Alpha1ListProcessesResponse",
    "ScalewayQaasV1Alpha1ListProcessResultsResponse",
    "ScalewayQaasV1Alpha1ListSessionACLsRequestOrderBy",
    "ScalewayQaasV1Alpha1ListSessionACLsResponse",
    "ScalewayQaasV1Alpha1ListSessionsResponse",
    "ScalewayQaasV1Alpha1Platform",
    "ScalewayQaasV1Alpha1PlatformAvailability",
    "ScalewayQaasV1Alpha1PlatformBookingRequirement",
    "ScalewayQaasV1Alpha1PlatformHardware",
    "ScalewayQaasV1Alpha1PlatformPricePerCircuit",
    "ScalewayQaasV1Alpha1PlatformPricePerHour",
    "ScalewayQaasV1Alpha1PlatformPricePerShot",
    "ScalewayQaasV1Alpha1PlatformTechnology",
    "ScalewayQaasV1Alpha1PlatformType",
    "ScalewayQaasV1Alpha1Process",
    "ScalewayQaasV1Alpha1ProcessResult",
    "ScalewayQaasV1Alpha1ProcessStatus",
    "ScalewayQaasV1Alpha1Session",
    "ScalewayQaasV1Alpha1SessionAccess",
    "ScalewayQaasV1Alpha1SessionOriginType",
    "ScalewayQaasV1Alpha1SessionStatus",
    "TerminateSessionBody",
    "UpdateBookingBody",
    "UpdateJobBody",
    "UpdateProcessBody",
    "UpdateSessionBody",
)
