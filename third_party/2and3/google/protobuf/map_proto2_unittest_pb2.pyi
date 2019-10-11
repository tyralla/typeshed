
from google.protobuf.message import (
    Message,
)
from google.protobuf.unittest_import_pb2 import (
    ImportEnumForMap,
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


class Proto2MapEnum(int):

    @classmethod
    def Name(cls, number: int) -> bytes: ...

    @classmethod
    def Value(cls, name: bytes) -> Proto2MapEnum: ...

    @classmethod
    def keys(cls) -> List[bytes]: ...

    @classmethod
    def values(cls) -> List[Proto2MapEnum]: ...

    @classmethod
    def items(cls) -> List[Tuple[bytes, Proto2MapEnum]]: ...
PROTO2_MAP_ENUM_FOO: Proto2MapEnum
PROTO2_MAP_ENUM_BAR: Proto2MapEnum
PROTO2_MAP_ENUM_BAZ: Proto2MapEnum


class Proto2MapEnumPlusExtra(int):

    @classmethod
    def Name(cls, number: int) -> bytes: ...

    @classmethod
    def Value(cls, name: bytes) -> Proto2MapEnumPlusExtra: ...

    @classmethod
    def keys(cls) -> List[bytes]: ...

    @classmethod
    def values(cls) -> List[Proto2MapEnumPlusExtra]: ...

    @classmethod
    def items(cls) -> List[Tuple[bytes, Proto2MapEnumPlusExtra]]: ...
E_PROTO2_MAP_ENUM_FOO: Proto2MapEnumPlusExtra
E_PROTO2_MAP_ENUM_BAR: Proto2MapEnumPlusExtra
E_PROTO2_MAP_ENUM_BAZ: Proto2MapEnumPlusExtra
E_PROTO2_MAP_ENUM_EXTRA: Proto2MapEnumPlusExtra


class TestEnumMap(Message):

    class KnownMapFieldEntry(Message):
        key: int
        value: Proto2MapEnum

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[Proto2MapEnum] = ...,
                     ) -> None: ...

    class UnknownMapFieldEntry(Message):
        key: int
        value: Proto2MapEnum

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[Proto2MapEnum] = ...,
                     ) -> None: ...

    @property
    def known_map_field(self) -> MutableMapping[int, Proto2MapEnum]: ...

    @property
    def unknown_map_field(self) -> MutableMapping[int, Proto2MapEnum]: ...

    def __init__(self,
                 known_map_field: Optional[Mapping[int, Proto2MapEnum]] = ...,
                 unknown_map_field: Optional[Mapping[int, Proto2MapEnum]] = ...,
                 ) -> None: ...


class TestEnumMapPlusExtra(Message):

    class KnownMapFieldEntry(Message):
        key: int
        value: Proto2MapEnumPlusExtra

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[Proto2MapEnumPlusExtra] = ...,
                     ) -> None: ...

    class UnknownMapFieldEntry(Message):
        key: int
        value: Proto2MapEnumPlusExtra

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[Proto2MapEnumPlusExtra] = ...,
                     ) -> None: ...

    @property
    def known_map_field(self) -> MutableMapping[int, Proto2MapEnumPlusExtra]: ...

    @property
    def unknown_map_field(self) -> MutableMapping[int, Proto2MapEnumPlusExtra]: ...

    def __init__(self,
                 known_map_field: Optional[Mapping[int, Proto2MapEnumPlusExtra]] = ...,
                 unknown_map_field: Optional[Mapping[int, Proto2MapEnumPlusExtra]] = ...,
                 ) -> None: ...


class TestImportEnumMap(Message):

    class ImportEnumAmpEntry(Message):
        key: int
        value: ImportEnumForMap

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[ImportEnumForMap] = ...,
                     ) -> None: ...

    @property
    def import_enum_amp(self) -> MutableMapping[int, ImportEnumForMap]: ...

    def __init__(self,
                 import_enum_amp: Optional[Mapping[int, ImportEnumForMap]] = ...,
                 ) -> None: ...


class TestIntIntMap(Message):

    class MEntry(Message):
        key: int
        value: int

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[int] = ...,
                     ) -> None: ...

    @property
    def m(self) -> MutableMapping[int, int]: ...

    def __init__(self,
                 m: Optional[Mapping[int, int]] = ...,
                 ) -> None: ...


class TestMaps(Message):

    class MInt32Entry(Message):
        key: int

        @property
        def value(self) -> TestIntIntMap: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[TestIntIntMap] = ...,
                     ) -> None: ...

    class MInt64Entry(Message):
        key: int

        @property
        def value(self) -> TestIntIntMap: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[TestIntIntMap] = ...,
                     ) -> None: ...

    class MUint32Entry(Message):
        key: int

        @property
        def value(self) -> TestIntIntMap: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[TestIntIntMap] = ...,
                     ) -> None: ...

    class MUint64Entry(Message):
        key: int

        @property
        def value(self) -> TestIntIntMap: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[TestIntIntMap] = ...,
                     ) -> None: ...

    class MSint32Entry(Message):
        key: int

        @property
        def value(self) -> TestIntIntMap: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[TestIntIntMap] = ...,
                     ) -> None: ...

    class MSint64Entry(Message):
        key: int

        @property
        def value(self) -> TestIntIntMap: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[TestIntIntMap] = ...,
                     ) -> None: ...

    class MFixed32Entry(Message):
        key: int

        @property
        def value(self) -> TestIntIntMap: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[TestIntIntMap] = ...,
                     ) -> None: ...

    class MFixed64Entry(Message):
        key: int

        @property
        def value(self) -> TestIntIntMap: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[TestIntIntMap] = ...,
                     ) -> None: ...

    class MSfixed32Entry(Message):
        key: int

        @property
        def value(self) -> TestIntIntMap: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[TestIntIntMap] = ...,
                     ) -> None: ...

    class MSfixed64Entry(Message):
        key: int

        @property
        def value(self) -> TestIntIntMap: ...

        def __init__(self,
                     key: Optional[int] = ...,
                     value: Optional[TestIntIntMap] = ...,
                     ) -> None: ...

    class MBoolEntry(Message):
        key: bool

        @property
        def value(self) -> TestIntIntMap: ...

        def __init__(self,
                     key: Optional[bool] = ...,
                     value: Optional[TestIntIntMap] = ...,
                     ) -> None: ...

    class MStringEntry(Message):
        key: Text

        @property
        def value(self) -> TestIntIntMap: ...

        def __init__(self,
                     key: Optional[Text] = ...,
                     value: Optional[TestIntIntMap] = ...,
                     ) -> None: ...

    @property
    def m_int32(self) -> MutableMapping[int, TestIntIntMap]: ...

    @property
    def m_int64(self) -> MutableMapping[int, TestIntIntMap]: ...

    @property
    def m_uint32(self) -> MutableMapping[int, TestIntIntMap]: ...

    @property
    def m_uint64(self) -> MutableMapping[int, TestIntIntMap]: ...

    @property
    def m_sint32(self) -> MutableMapping[int, TestIntIntMap]: ...

    @property
    def m_sint64(self) -> MutableMapping[int, TestIntIntMap]: ...

    @property
    def m_fixed32(self) -> MutableMapping[int, TestIntIntMap]: ...

    @property
    def m_fixed64(self) -> MutableMapping[int, TestIntIntMap]: ...

    @property
    def m_sfixed32(self) -> MutableMapping[int, TestIntIntMap]: ...

    @property
    def m_sfixed64(self) -> MutableMapping[int, TestIntIntMap]: ...

    @property
    def m_bool(self) -> MutableMapping[bool, TestIntIntMap]: ...

    @property
    def m_string(self) -> MutableMapping[Text, TestIntIntMap]: ...

    def __init__(self,
                 m_int32: Optional[Mapping[int, TestIntIntMap]] = ...,
                 m_int64: Optional[Mapping[int, TestIntIntMap]] = ...,
                 m_uint32: Optional[Mapping[int, TestIntIntMap]] = ...,
                 m_uint64: Optional[Mapping[int, TestIntIntMap]] = ...,
                 m_sint32: Optional[Mapping[int, TestIntIntMap]] = ...,
                 m_sint64: Optional[Mapping[int, TestIntIntMap]] = ...,
                 m_fixed32: Optional[Mapping[int, TestIntIntMap]] = ...,
                 m_fixed64: Optional[Mapping[int, TestIntIntMap]] = ...,
                 m_sfixed32: Optional[Mapping[int, TestIntIntMap]] = ...,
                 m_sfixed64: Optional[Mapping[int, TestIntIntMap]] = ...,
                 m_bool: Optional[Mapping[bool, TestIntIntMap]] = ...,
                 m_string: Optional[Mapping[Text, TestIntIntMap]] = ...,
                 ) -> None: ...


class TestSubmessageMaps(Message):

    @property
    def m(self) -> TestMaps: ...

    def __init__(self,
                 m: Optional[TestMaps] = ...,
                 ) -> None: ...
