"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import shared.user_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class FeatureToggleHistory(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HISTORY_FIELD_NUMBER: builtins.int
    @property
    def history(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FeatureToggle]: ...
    def __init__(self,
        *,
        history: typing.Optional[typing.Iterable[global___FeatureToggle]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["history",b"history"]) -> None: ...
global___FeatureToggleHistory = FeatureToggleHistory

class Platform(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Platform._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        DEFAULT: Platform._Type.ValueType  # 0
        WEB: Platform._Type.ValueType  # 1
        IOS: Platform._Type.ValueType  # 2
        ANDROID: Platform._Type.ValueType  # 3
    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        pass

    DEFAULT: Platform.Type.ValueType  # 0
    WEB: Platform.Type.ValueType  # 1
    IOS: Platform.Type.ValueType  # 2
    ANDROID: Platform.Type.ValueType  # 3

    def __init__(self,
        ) -> None: ...
global___Platform = Platform

class FeatureToggle(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[FeatureToggle._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ON_OFF: FeatureToggle._Type.ValueType  # 0
        PERCENTAGE: FeatureToggle._Type.ValueType  # 1
        PERMISSION: FeatureToggle._Type.ValueType  # 2
        """Fail if can't confirm. Must be used by server-side code only."""

        EXPERIMENT: FeatureToggle._Type.ValueType  # 3
        """MultiVariant."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        pass

    ON_OFF: FeatureToggle.Type.ValueType  # 0
    PERCENTAGE: FeatureToggle.Type.ValueType  # 1
    PERMISSION: FeatureToggle.Type.ValueType  # 2
    """Fail if can't confirm. Must be used by server-side code only."""

    EXPERIMENT: FeatureToggle.Type.ValueType  # 3
    """MultiVariant."""


    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    TOGGLE_TYPE_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    PLATFORMS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    DELETED_AT_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    UPDATED_BY_FIELD_NUMBER: builtins.int
    ON_OFF_FIELD_NUMBER: builtins.int
    PERCENTAGE_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    EXPERIMENT_FIELD_NUMBER: builtins.int
    id: typing.Text
    """Read-only"""

    name: typing.Text
    toggle_type: global___FeatureToggle.Type.ValueType
    """Set once."""

    version: builtins.int
    """Read-only."""

    enabled: builtins.bool
    description: typing.Text
    @property
    def platforms(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___Platform.Type.ValueType]: ...
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def deleted_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    project_id: typing.Text
    @property
    def created_by(self) -> shared.user_pb2.User: ...
    @property
    def updated_by(self) -> shared.user_pb2.User: ...
    @property
    def on_off(self) -> global___OnOffFeature: ...
    @property
    def percentage(self) -> global___PercentageFeature: ...
    @property
    def permission(self) -> global___PermissionFeature: ...
    @property
    def experiment(self) -> global___ExperimentFeature: ...
    def __init__(self,
        *,
        id: typing.Text = ...,
        name: typing.Text = ...,
        toggle_type: global___FeatureToggle.Type.ValueType = ...,
        version: builtins.int = ...,
        enabled: builtins.bool = ...,
        description: typing.Text = ...,
        platforms: typing.Optional[typing.Iterable[global___Platform.Type.ValueType]] = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        updated_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        deleted_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        project_id: typing.Text = ...,
        created_by: typing.Optional[shared.user_pb2.User] = ...,
        updated_by: typing.Optional[shared.user_pb2.User] = ...,
        on_off: typing.Optional[global___OnOffFeature] = ...,
        percentage: typing.Optional[global___PercentageFeature] = ...,
        permission: typing.Optional[global___PermissionFeature] = ...,
        experiment: typing.Optional[global___ExperimentFeature] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["FeatureDefinition",b"FeatureDefinition","created_at",b"created_at","created_by",b"created_by","deleted_at",b"deleted_at","experiment",b"experiment","on_off",b"on_off","percentage",b"percentage","permission",b"permission","updated_at",b"updated_at","updated_by",b"updated_by"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["FeatureDefinition",b"FeatureDefinition","created_at",b"created_at","created_by",b"created_by","deleted_at",b"deleted_at","description",b"description","enabled",b"enabled","experiment",b"experiment","id",b"id","name",b"name","on_off",b"on_off","percentage",b"percentage","permission",b"permission","platforms",b"platforms","project_id",b"project_id","toggle_type",b"toggle_type","updated_at",b"updated_at","updated_by",b"updated_by","version",b"version"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["FeatureDefinition",b"FeatureDefinition"]) -> typing.Optional[typing_extensions.Literal["on_off","percentage","permission","experiment"]]: ...
global___FeatureToggle = FeatureToggle

class StringOp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Operator:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _OperatorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[StringOp._Operator.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        EQ: StringOp._Operator.ValueType  # 0
        CONTAINS: StringOp._Operator.ValueType  # 1
        IN: StringOp._Operator.ValueType  # 2
        """TODO: Regex"""

    class Operator(_Operator, metaclass=_OperatorEnumTypeWrapper):
        pass

    EQ: StringOp.Operator.ValueType  # 0
    CONTAINS: StringOp.Operator.ValueType  # 1
    IN: StringOp.Operator.ValueType  # 2
    """TODO: Regex"""


    OP_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    op: global___StringOp.Operator.ValueType
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        op: global___StringOp.Operator.ValueType = ...,
        values: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["op",b"op","values",b"values"]) -> None: ...
global___StringOp = StringOp

class BoolOp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.bool
    def __init__(self,
        *,
        value: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["value",b"value"]) -> None: ...
global___BoolOp = BoolOp

class FloatOp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Operator:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _OperatorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[FloatOp._Operator.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        EQ: FloatOp._Operator.ValueType  # 0
        GT: FloatOp._Operator.ValueType  # 1
        LT: FloatOp._Operator.ValueType  # 2
        GTE: FloatOp._Operator.ValueType  # 3
        LTE: FloatOp._Operator.ValueType  # 4
        NEQ: FloatOp._Operator.ValueType  # 5
        IN: FloatOp._Operator.ValueType  # 6
    class Operator(_Operator, metaclass=_OperatorEnumTypeWrapper):
        pass

    EQ: FloatOp.Operator.ValueType  # 0
    GT: FloatOp.Operator.ValueType  # 1
    LT: FloatOp.Operator.ValueType  # 2
    GTE: FloatOp.Operator.ValueType  # 3
    LTE: FloatOp.Operator.ValueType  # 4
    NEQ: FloatOp.Operator.ValueType  # 5
    IN: FloatOp.Operator.ValueType  # 6

    OP_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    op: global___FloatOp.Operator.ValueType
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(self,
        *,
        op: global___FloatOp.Operator.ValueType = ...,
        values: typing.Optional[typing.Iterable[builtins.float]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["op",b"op","values",b"values"]) -> None: ...
global___FloatOp = FloatOp

class IntOp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Operator:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _OperatorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[IntOp._Operator.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        EQ: IntOp._Operator.ValueType  # 0
        GT: IntOp._Operator.ValueType  # 1
        LT: IntOp._Operator.ValueType  # 2
        GTE: IntOp._Operator.ValueType  # 3
        LTE: IntOp._Operator.ValueType  # 4
        NEQ: IntOp._Operator.ValueType  # 5
        IN: IntOp._Operator.ValueType  # 6
    class Operator(_Operator, metaclass=_OperatorEnumTypeWrapper):
        pass

    EQ: IntOp.Operator.ValueType  # 0
    GT: IntOp.Operator.ValueType  # 1
    LT: IntOp.Operator.ValueType  # 2
    GTE: IntOp.Operator.ValueType  # 3
    LTE: IntOp.Operator.ValueType  # 4
    NEQ: IntOp.Operator.ValueType  # 5
    IN: IntOp.Operator.ValueType  # 6

    OP_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    op: global___IntOp.Operator.ValueType
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(self,
        *,
        op: global___IntOp.Operator.ValueType = ...,
        values: typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["op",b"op","values",b"values"]) -> None: ...
global___IntOp = IntOp

class DateTimeOp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Operator:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _OperatorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DateTimeOp._Operator.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        BEFORE: DateTimeOp._Operator.ValueType  # 0
        AFTER: DateTimeOp._Operator.ValueType  # 1
    class Operator(_Operator, metaclass=_OperatorEnumTypeWrapper):
        pass

    BEFORE: DateTimeOp.Operator.ValueType  # 0
    AFTER: DateTimeOp.Operator.ValueType  # 1

    OP_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    op: global___DateTimeOp.Operator.ValueType
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        op: global___DateTimeOp.Operator.ValueType = ...,
        timestamp: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp",b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["op",b"op","timestamp",b"timestamp"]) -> None: ...
global___DateTimeOp = DateTimeOp

class Key(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Key._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STRING: Key._Type.ValueType  # 0
        BOOLEAN: Key._Type.ValueType  # 1
        FLOAT: Key._Type.ValueType  # 2
        INT: Key._Type.ValueType  # 3
        DATE_TIME: Key._Type.ValueType  # 4
    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        pass

    STRING: Key.Type.ValueType  # 0
    BOOLEAN: Key.Type.ValueType  # 1
    FLOAT: Key.Type.ValueType  # 2
    INT: Key.Type.ValueType  # 3
    DATE_TIME: Key.Type.ValueType  # 4

    KEY_FIELD_NUMBER: builtins.int
    KEY_TYPE_FIELD_NUMBER: builtins.int
    key: typing.Text
    key_type: global___Key.Type.ValueType
    def __init__(self,
        *,
        key: typing.Text = ...,
        key_type: global___Key.Type.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key","key_type",b"key_type"]) -> None: ...
global___Key = Key

class Match(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    STRING_OP_FIELD_NUMBER: builtins.int
    BOOL_OP_FIELD_NUMBER: builtins.int
    FLOAT_OP_FIELD_NUMBER: builtins.int
    INT_OP_FIELD_NUMBER: builtins.int
    DATE_TIME_OP_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> global___Key: ...
    @property
    def string_op(self) -> global___StringOp: ...
    @property
    def bool_op(self) -> global___BoolOp: ...
    @property
    def float_op(self) -> global___FloatOp: ...
    @property
    def int_op(self) -> global___IntOp: ...
    @property
    def date_time_op(self) -> global___DateTimeOp: ...
    def __init__(self,
        *,
        key: typing.Optional[global___Key] = ...,
        string_op: typing.Optional[global___StringOp] = ...,
        bool_op: typing.Optional[global___BoolOp] = ...,
        float_op: typing.Optional[global___FloatOp] = ...,
        int_op: typing.Optional[global___IntOp] = ...,
        date_time_op: typing.Optional[global___DateTimeOp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["Operation",b"Operation","bool_op",b"bool_op","date_time_op",b"date_time_op","float_op",b"float_op","int_op",b"int_op","key",b"key","string_op",b"string_op"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["Operation",b"Operation","bool_op",b"bool_op","date_time_op",b"date_time_op","float_op",b"float_op","int_op",b"int_op","key",b"key","string_op",b"string_op"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["Operation",b"Operation"]) -> typing.Optional[typing_extensions.Literal["string_op","bool_op","float_op","int_op","date_time_op"]]: ...
global___Match = Match

class Variant(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MATCHES_FIELD_NUMBER: builtins.int
    WEIGHT_FIELD_NUMBER: builtins.int
    @property
    def matches(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Match]: ...
    weight: builtins.float
    def __init__(self,
        *,
        matches: typing.Optional[typing.Iterable[global___Match]] = ...,
        weight: builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["matches",b"matches","weight",b"weight"]) -> None: ...
global___Variant = Variant

class OnOffFeature(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ON_FIELD_NUMBER: builtins.int
    OFF_FIELD_NUMBER: builtins.int
    @property
    def on(self) -> global___Variant: ...
    @property
    def off(self) -> global___Variant: ...
    def __init__(self,
        *,
        on: typing.Optional[global___Variant] = ...,
        off: typing.Optional[global___Variant] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["off",b"off","on",b"on"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["off",b"off","on",b"on"]) -> None: ...
global___OnOffFeature = OnOffFeature

class Stickiness(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Stickiness._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        RANDOM: Stickiness._Type.ValueType  # 0
        KEYS: Stickiness._Type.ValueType  # 1
    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        pass

    RANDOM: Stickiness.Type.ValueType  # 0
    KEYS: Stickiness.Type.ValueType  # 1

    STICKINESS_TYPE_FIELD_NUMBER: builtins.int
    KEYS_FIELD_NUMBER: builtins.int
    stickiness_type: global___Stickiness.Type.ValueType
    @property
    def keys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Key]: ...
    def __init__(self,
        *,
        stickiness_type: global___Stickiness.Type.ValueType = ...,
        keys: typing.Optional[typing.Iterable[global___Key]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["keys",b"keys","stickiness_type",b"stickiness_type"]) -> None: ...
global___Stickiness = Stickiness

class PercentageFeature(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SALT_FIELD_NUMBER: builtins.int
    ON_FIELD_NUMBER: builtins.int
    OFF_FIELD_NUMBER: builtins.int
    STICKINESS_FIELD_NUMBER: builtins.int
    salt: typing.Text
    @property
    def on(self) -> global___Variant: ...
    @property
    def off(self) -> global___Variant: ...
    @property
    def stickiness(self) -> global___Stickiness: ...
    def __init__(self,
        *,
        salt: typing.Text = ...,
        on: typing.Optional[global___Variant] = ...,
        off: typing.Optional[global___Variant] = ...,
        stickiness: typing.Optional[global___Stickiness] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["off",b"off","on",b"on","stickiness",b"stickiness"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["off",b"off","on",b"on","salt",b"salt","stickiness",b"stickiness"]) -> None: ...
global___PercentageFeature = PercentageFeature

class PermissionFeature(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SALT_FIELD_NUMBER: builtins.int
    ON_FIELD_NUMBER: builtins.int
    OFF_FIELD_NUMBER: builtins.int
    salt: typing.Text
    @property
    def on(self) -> global___Variant: ...
    @property
    def off(self) -> global___Variant: ...
    def __init__(self,
        *,
        salt: typing.Text = ...,
        on: typing.Optional[global___Variant] = ...,
        off: typing.Optional[global___Variant] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["off",b"off","on",b"on"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["off",b"off","on",b"on","salt",b"salt"]) -> None: ...
global___PermissionFeature = PermissionFeature

class ExperimentFeature(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SALT_FIELD_NUMBER: builtins.int
    VARIANTS_FIELD_NUMBER: builtins.int
    salt: typing.Text
    @property
    def variants(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Variant]: ...
    def __init__(self,
        *,
        salt: typing.Text = ...,
        variants: typing.Optional[typing.Iterable[global___Variant]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["salt",b"salt","variants",b"variants"]) -> None: ...
global___ExperimentFeature = ExperimentFeature