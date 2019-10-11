
from google.protobuf.message import (
    Message,
)
from google.protobuf.unittest_no_arena_pb2 import (
    ForeignMessage,
)
from google.protobuf.unittest_pb2 import (
    ForeignMessage as ForeignMessage1,
    TestAllTypes,
    TestRequired,
)
from typing import (
    List,
    Mapping,
    MutableMapping,
    Optional,
    Text,
    Tuple,
    cast,
)


class MapEnum(int):

    @classmethod
    def Name(cls, number: int) -> bytes: ...

    @classmethod
    def Value(cls, name: bytes) -> MapEnum: ...

    @classmethod
    def keys(cls) -> List[bytes]: ...

    @classmethod
    def values(cls) -> List[MapEnum]: ...

    @classmethod
    def items(cls) -> List[Tuple[bytes, MapEnum]]: ...


MAP_ENUM_FOO: MapEnum
MAP_ENUM_BAR: MapEnum
MAP_ENUM_BAZ: MapEnum


class TestMap(Message):

    class MapInt32Int32Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapInt64Int64Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapUint32Uint32Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapUint64Uint64Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapSint32Sint32Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapSint64Sint64Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapFixed32Fixed32Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapFixed64Fixed64Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapSfixed32Sfixed32Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapSfixed64Sfixed64Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapInt32FloatEntry(Message):
        key: int
        value: float

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[float] = ...,
                     ) -> None: ...

    class MapInt32DoubleEntry(Message):
        key: int
        value: float

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[float] = ...,
                     ) -> None: ...

    class MapBoolBoolEntry(Message):
        key: bool
        value: bool

        def __init__(self,
                     key: Optional[bool] = ...,
                     value: Optional[bool] = ...,
                     ) -> None: ...

    class MapStringStringEntry(Message):
        key: Text
        value: Text

        def __init__(self,
                     key: Optional[Text] = ...,
                     value: Optional[Text] = ...,
                     ) -> None: ...

    class MapInt32BytesEntry(Message):
        key: int
        value: bytes

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[bytes] = ...,
                     ) -> None: ...

    class MapInt32EnumEntry(Message):
        key: int
        value: MapEnum

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[MapEnum] = ...,
                     ) -> None: ...

    class MapInt32ForeignMessageEntry(Message):
        key: int

        @property
        def value(self) -> ForeignMessage1: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[ForeignMessage1] = ...,
                     ) -> None: ...

    class MapStringForeignMessageEntry(Message):
        key: Text

        @property
        def value(self) -> ForeignMessage1: ...

        def __init__(self,
                     key: Optional[Text] = ...,
                     value: Optional[ForeignMessage1] = ...,
                     ) -> None: ...

    class MapInt32AllTypesEntry(Message):
        key: int

        @property
        def value(self) -> TestAllTypes: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[TestAllTypes] = ...,
                     ) -> None: ...

    @property
    def map_int32_int32(self) -> MutableMapping[int, int]: ...

    @property
    def map_int64_int64(self) -> MutableMapping[int, int]: ...

    @property
    def map_uint32_uint32(self) -> MutableMapping[int, int]: ...

    @property
    def map_uint64_uint64(self) -> MutableMapping[int, int]: ...

    @property
    def map_sint32_sint32(self) -> MutableMapping[int, int]: ...

    @property
    def map_sint64_sint64(self) -> MutableMapping[int, int]: ...

    @property
    def map_fixed32_fixed32(self) -> MutableMapping[int, int]: ...

    @property
    def map_fixed64_fixed64(self) -> MutableMapping[int, int]: ...

    @property
    def map_sfixed32_sfixed32(self) -> MutableMapping[int, int]: ...

    @property
    def map_sfixed64_sfixed64(self) -> MutableMapping[int, int]: ...

    @property
    def map_int32_float(self) -> MutableMapping[int, float]: ...

    @property
    def map_int32_double(self) -> MutableMapping[int, float]: ...

    @property
    def map_bool_bool(self) -> MutableMapping[bool, bool]: ...

    @property
    def map_string_string(self) -> MutableMapping[Text, Text]: ...

    @property
    def map_int32_bytes(self) -> MutableMapping[int, bytes]: ...

    @property
    def map_int32_enum(self) -> MutableMapping[int, MapEnum]: ...

    @property
    def map_int32_foreign_message(
        self) -> MutableMapping[int, ForeignMessage1]: ...

    @property
    def map_string_foreign_message(
        self) -> MutableMapping[Text, ForeignMessage1]: ...

    @property
    def map_int32_all_types(self) -> MutableMapping[int, TestAllTypes]: ...

    def __init__(self,
                 map_int32_int32: Optional[Mapping[int, int]] = ...,
                 map_int64_int64: Optional[Mapping[int, int]] = ...,
                 map_uint32_uint32: Optional[Mapping[int, int]] = ...,
                 map_uint64_uint64: Optional[Mapping[int, int]] = ...,
                 map_sint32_sint32: Optional[Mapping[int, int]] = ...,
                 map_sint64_sint64: Optional[Mapping[int, int]] = ...,
                 map_fixed32_fixed32: Optional[Mapping[int, int]] = ...,
                 map_fixed64_fixed64: Optional[Mapping[int, int]] = ...,
                 map_sfixed32_sfixed32: Optional[Mapping[int, int]] = ...,
                 map_sfixed64_sfixed64: Optional[Mapping[int, int]] = ...,
                 map_int32_float: Optional[Mapping[int, float]] = ...,
                 map_int32_double: Optional[Mapping[int, float]] = ...,
                 map_bool_bool: Optional[Mapping[bool, bool]] = ...,
                 map_string_string: Optional[Mapping[Text, Text]] = ...,
                 map_int32_bytes: Optional[Mapping[int, bytes]] = ...,
                 map_int32_enum: Optional[Mapping[int, MapEnum]] = ...,
                 map_int32_foreign_message: Optional[Mapping[int, ForeignMessage1]] = ...,
                 map_string_foreign_message: Optional[Mapping[Text, ForeignMessage1]] = ...,
                 map_int32_all_types: Optional[Mapping[int, TestAllTypes]] = ...,
                 ) -> None: ...


class TestMapSubmessage(Message):

    @property
    def test_map(self) -> TestMap: ...

    def __init__(self,
                 test_map: Optional[TestMap] = ...,
                 ) -> None: ...


class TestMessageMap(Message):

    class MapInt32MessageEntry(Message):
        key: int

        @property
        def value(self) -> TestAllTypes: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[TestAllTypes] = ...,
                     ) -> None: ...

    @property
    def map_int32_message(self) -> MutableMapping[int, TestAllTypes]: ...

    def __init__(self,
                 map_int32_message: Optional[Mapping[int, TestAllTypes]] = ...,
                 ) -> None: ...


class TestSameTypeMap(Message):

    class Map1Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class Map2Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    @property
    def map1(self) -> MutableMapping[int, int]: ...

    @property
    def map2(self) -> MutableMapping[int, int]: ...

    def __init__(self,
                 map1: Optional[Mapping[int, int]] = ...,
                 map2: Optional[Mapping[int, int]] = ...,
                 ) -> None: ...


class TestRequiredMessageMap(Message):

    class MapFieldEntry(Message):
        key: int

        @property
        def value(self) -> TestRequired: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[TestRequired] = ...,
                     ) -> None: ...

    @property
    def map_field(self) -> MutableMapping[int, TestRequired]: ...

    def __init__(self,
                 map_field: Optional[Mapping[int, TestRequired]] = ...,
                 ) -> None: ...


class TestArenaMap(Message):

    class MapInt32Int32Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapInt64Int64Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapUint32Uint32Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapUint64Uint64Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapSint32Sint32Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapSint64Sint64Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapFixed32Fixed32Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapFixed64Fixed64Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapSfixed32Sfixed32Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapSfixed64Sfixed64Entry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    class MapInt32FloatEntry(Message):
        key: int
        value: float

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[float] = ...,
                     ) -> None: ...

    class MapInt32DoubleEntry(Message):
        key: int
        value: float

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[float] = ...,
                     ) -> None: ...

    class MapBoolBoolEntry(Message):
        key: bool
        value: bool

        def __init__(self,
                     key: Optional[bool] = ...,
                     value: Optional[bool] = ...,
                     ) -> None: ...

    class MapStringStringEntry(Message):
        key: Text
        value: Text

        def __init__(self,
                     key: Optional[Text] = ...,
                     value: Optional[Text] = ...,
                     ) -> None: ...

    class MapInt32BytesEntry(Message):
        key: int
        value: bytes

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[bytes] = ...,
                     ) -> None: ...

    class MapInt32EnumEntry(Message):
        key: int
        value: MapEnum

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[MapEnum] = ...,
                     ) -> None: ...

    class MapInt32ForeignMessageEntry(Message):
        key: int

        @property
        def value(self) -> ForeignMessage1: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[ForeignMessage1] = ...,
                     ) -> None: ...

    class MapInt32ForeignMessageNoArenaEntry(Message):
        key: int

        @property
        def value(self) -> ForeignMessage: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[ForeignMessage] = ...,
                     ) -> None: ...

    @property
    def map_int32_int32(self) -> MutableMapping[int, int]: ...

    @property
    def map_int64_int64(self) -> MutableMapping[int, int]: ...

    @property
    def map_uint32_uint32(self) -> MutableMapping[int, int]: ...

    @property
    def map_uint64_uint64(self) -> MutableMapping[int, int]: ...

    @property
    def map_sint32_sint32(self) -> MutableMapping[int, int]: ...

    @property
    def map_sint64_sint64(self) -> MutableMapping[int, int]: ...

    @property
    def map_fixed32_fixed32(self) -> MutableMapping[int, int]: ...

    @property
    def map_fixed64_fixed64(self) -> MutableMapping[int, int]: ...

    @property
    def map_sfixed32_sfixed32(self) -> MutableMapping[int, int]: ...

    @property
    def map_sfixed64_sfixed64(self) -> MutableMapping[int, int]: ...

    @property
    def map_int32_float(self) -> MutableMapping[int, float]: ...

    @property
    def map_int32_double(self) -> MutableMapping[int, float]: ...

    @property
    def map_bool_bool(self) -> MutableMapping[bool, bool]: ...

    @property
    def map_string_string(self) -> MutableMapping[Text, Text]: ...

    @property
    def map_int32_bytes(self) -> MutableMapping[int, bytes]: ...

    @property
    def map_int32_enum(self) -> MutableMapping[int, MapEnum]: ...

    @property
    def map_int32_foreign_message(
        self) -> MutableMapping[int, ForeignMessage1]: ...

    @property
    def map_int32_foreign_message_no_arena(
        self) -> MutableMapping[int, ForeignMessage]: ...

    def __init__(self,
                 map_int32_int32: Optional[Mapping[int, int]] = ...,
                 map_int64_int64: Optional[Mapping[int, int]] = ...,
                 map_uint32_uint32: Optional[Mapping[int, int]] = ...,
                 map_uint64_uint64: Optional[Mapping[int, int]] = ...,
                 map_sint32_sint32: Optional[Mapping[int, int]] = ...,
                 map_sint64_sint64: Optional[Mapping[int, int]] = ...,
                 map_fixed32_fixed32: Optional[Mapping[int, int]] = ...,
                 map_fixed64_fixed64: Optional[Mapping[int, int]] = ...,
                 map_sfixed32_sfixed32: Optional[Mapping[int, int]] = ...,
                 map_sfixed64_sfixed64: Optional[Mapping[int, int]] = ...,
                 map_int32_float: Optional[Mapping[int, float]] = ...,
                 map_int32_double: Optional[Mapping[int, float]] = ...,
                 map_bool_bool: Optional[Mapping[bool, bool]] = ...,
                 map_string_string: Optional[Mapping[Text, Text]] = ...,
                 map_int32_bytes: Optional[Mapping[int, bytes]] = ...,
                 map_int32_enum: Optional[Mapping[int, MapEnum]] = ...,
                 map_int32_foreign_message: Optional[Mapping[int, ForeignMessage1]] = ...,
                 map_int32_foreign_message_no_arena: Optional[Mapping[int, ForeignMessage]] = ...,
                 ) -> None: ...


class MessageContainingEnumCalledType(Message):

    class Type(int):

        @classmethod
        def Name(cls, number: int) -> bytes: ...

        @classmethod
        def Value(cls, name: bytes) -> MessageContainingEnumCalledType.Type: ...

        @classmethod
        def keys(cls) -> List[bytes]: ...

        @classmethod
        def values(cls) -> List[MessageContainingEnumCalledType.Type]: ...

        @classmethod
        def items(cls) -> List[Tuple[bytes,
                                     MessageContainingEnumCalledType.Type]]: ...
    TYPE_FOO: MessageContainingEnumCalledType.Type

    class TypeEntry(Message):
        key: Text

        @property
        def value(self) -> MessageContainingEnumCalledType: ...

        def __init__(self,
                     key: Optional[Text] = ...,
                     value: Optional[MessageContainingEnumCalledType] = ...,
                     ) -> None: ...

    @property
    def type(self) -> MutableMapping[Text,
                                     MessageContainingEnumCalledType]: ...

    def __init__(self,
                 type: Optional[Mapping[Text, MessageContainingEnumCalledType]] = ...,
                 ) -> None: ...


class MessageContainingMapCalledEntry(Message):

    class EntryEntry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    @property
    def entry(self) -> MutableMapping[int, int]: ...

    def __init__(self,
                 entry: Optional[Mapping[int, int]] = ...,
                 ) -> None: ...


class TestRecursiveMapMessage(Message):

    class AEntry(Message):
        key: Text

        @property
        def value(self) -> TestRecursiveMapMessage: ...

        def __init__(self,
                     key: Optional[Text] = ...,
                     value: Optional[TestRecursiveMapMessage] = ...,
                     ) -> None: ...

    @property
    def a(self) -> MutableMapping[Text, TestRecursiveMapMessage]: ...

    def __init__(self,
                 a: Optional[Mapping[Text, TestRecursiveMapMessage]] = ...,
                 ) -> None: ...
