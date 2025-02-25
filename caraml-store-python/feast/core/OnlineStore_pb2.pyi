"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _StoreType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _StoreTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_StoreType.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNSET: _StoreType.ValueType  # 0
    """Unset"""
    BIGTABLE: _StoreType.ValueType  # 1
    """google cloud NOSQL database service"""
    REDIS: _StoreType.ValueType  # 2
    """redis in-memory database"""

class StoreType(_StoreType, metaclass=_StoreTypeEnumTypeWrapper): ...

UNSET: StoreType.ValueType  # 0
"""Unset"""
BIGTABLE: StoreType.ValueType  # 1
"""google cloud NOSQL database service"""
REDIS: StoreType.ValueType  # 2
"""redis in-memory database"""
global___StoreType = StoreType

class OnlineStore(google.protobuf.message.Message):
    """OnlineStore provides a location where Feast reads and writes feature values.
    Feature values will be written to the Store in the form of FeatureRow elements.
    The way FeatureRow is encoded and decoded when it is written to and read from
    the Store depends on the type of the Store.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the store."""
    type: global___StoreType.ValueType
    """Type of store."""
    description: builtins.str
    """Description."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        type: global___StoreType.ValueType = ...,
        description: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "name", b"name", "type", b"type"]) -> None: ...

global___OnlineStore = OnlineStore
