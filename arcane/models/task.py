# coding: utf-8

"""
    Arcane Engine API

    API for creating Arcane Engine tasks

    The version of the OpenAPI document: 1.12.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Task(BaseModel):
    """
    Task
    """ # noqa: E501
    id: StrictStr
    title: Annotated[str, Field(strict=True, max_length=200)]
    user_request: Optional[StrictStr] = None
    github_project: Annotated[str, Field(strict=True, max_length=200)]
    github_user: Annotated[str, Field(strict=True, max_length=200)]
    status: Annotated[str, Field(strict=True, max_length=200)]
    created: datetime
    result: Optional[StrictStr] = None
    issue_number: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    pr_number: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    gpt_model: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    branch: Annotated[str, Field(strict=True, max_length=200)]
    __properties: ClassVar[List[str]] = ["id", "title", "user_request", "github_project", "github_user", "status", "created", "result", "issue_number", "pr_number", "gpt_model", "branch"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Task from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "created",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if issue_number (nullable) is None
        # and model_fields_set contains the field
        if self.issue_number is None and "issue_number" in self.model_fields_set:
            _dict['issue_number'] = None

        # set to None if pr_number (nullable) is None
        # and model_fields_set contains the field
        if self.pr_number is None and "pr_number" in self.model_fields_set:
            _dict['pr_number'] = None

        # set to None if gpt_model (nullable) is None
        # and model_fields_set contains the field
        if self.gpt_model is None and "gpt_model" in self.model_fields_set:
            _dict['gpt_model'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Task from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "user_request": obj.get("user_request"),
            "github_project": obj.get("github_project"),
            "github_user": obj.get("github_user"),
            "status": obj.get("status"),
            "created": obj.get("created"),
            "result": obj.get("result"),
            "issue_number": obj.get("issue_number"),
            "pr_number": obj.get("pr_number"),
            "gpt_model": obj.get("gpt_model"),
            "branch": obj.get("branch")
        })
        return _obj


