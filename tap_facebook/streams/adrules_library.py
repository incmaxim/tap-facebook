"""Stream class for AdRules Library."""

from __future__ import annotations

import typing as t

from singer_sdk.streams.core import REPLICATION_INCREMENTAL
from singer_sdk.typing import (
    ArrayType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

from tap_facebook.client import IncrementalFacebookStream

if t.TYPE_CHECKING:
    from singer_sdk.helpers.types import Context, Record


class AdRulesLibraryStream(IncrementalFacebookStream):
    """https://developers.facebook.com/docs/marketing-api/reference/ad-account/adrules_library/."""

    """
    columns: columns which will be added to fields parameter in api
    name: stream name
    account_id: facebook account
    path: path which will be added to api url in client.py
    schema: instream schema
    tap_stream_id = stream id
    """

    columns = [  # noqa: RUF012
        "id",
        "name",
        "account_id",
        "created_by",
        "evaluation_spec",
        "execution_spec",
        "schedule_spec",
        "updated_time",
    ]

    name = "adrules_library"
    filter_entity = "adrules_library"

    path = f"/adrules_library?fields={columns}"
    primary_keys = ["id", "updated_time"]  # noqa: RUF012
    tap_stream_id = "adrules_library"
    replication_method = REPLICATION_INCREMENTAL
    replication_key = "updated_time"

    PropertiesList = PropertiesList
    Property = Property
    ObjectType = ObjectType
    StringType = StringType
    ArrayType = ArrayType(StringType)

    schema = PropertiesList(
        Property("id", StringType),
        Property("name", StringType),
        Property("account_id", StringType),
        Property(
            "created_by",
            ObjectType(
                Property("id", StringType),
                Property("name", StringType),
            ),
        ),
        Property(
            "evaluation_spec",
            ObjectType(
                Property("evaluation_type", StringType),
                Property(
                    "filters",
                    ArrayType(
                        ObjectType(
                            Property("field", StringType),
                            Property("value", StringType),
                            Property("operator", StringType),
                        )
                    ),
                ),
            ),
        ),
        Property(
            "execution_spec",
            ObjectType(
                Property("execution_type", StringType),
                Property(
                    "execution_options",
                    ArrayType(
                        ObjectType(
                            Property("field", StringType),
                            Property("value", StringType),
                            Property("operator", StringType),
                        )
                    ),
                ),
            ),
        ),
        Property(
            "schedule_spec",
            ObjectType(
                Property("schedule_type", StringType),
            ),
        ),
        Property("updated_time", StringType),
    ).to_dict()