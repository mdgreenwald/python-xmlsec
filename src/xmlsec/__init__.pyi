import sys
from typing import AnyStr, IO, Iterable, Optional, Type, TypeVar, Union

from lxml.etree import _Element

from xmlsec import constants, template, tree
from xmlsec.constants import __KeyData as KeyData, __Transform as Transform

if sys.version_info >= (3, 6):
    from os import PathLike
    from pathlib import PurePath

    _Path = Union[str, bytes, PurePath, PathLike[str], PathLike[bytes]]
elif sys.version_info >= (3, 4):
    from pathlib import PurePath

    _Path = Union[str, bytes, PurePath]
else:
    _Path = Union[str, bytes]

_E = TypeVar('_E', bound=_Element)
_K = TypeVar('_K', bound=Key)

def enable_debug_trace(enabled: bool = ...) -> None: ...
def init() -> None: ...
def shutdown() -> None: ...

class EncryptionContext:
    key: Key
    def __init__(self, manager: Optional[KeysManager] = None) -> None: ...
    def decrypt(self, node: _Element = ...) -> _Element: ...
    def encrypt_binary(self, template: _E = ..., data: bytes = ...) -> _E: ...
    def encrypt_uri(self, template: _E = ..., uri: str = ...) -> _E: ...
    def encrypt_xml(self, template: _E = ..., node: _Element = ...) -> _E: ...
    def reset(self) -> None: ...

class Error(Exception): ...
class InternalError(Error): ...

class Key:
    name: str
    @classmethod
    def from_binary_data(cls: Type[_K], klass: KeyData = ..., data: AnyStr = ...) -> _K: ...
    @classmethod
    def from_binary_file(cls: Type[_K], klass: KeyData = ..., filename: _Path = ...) -> _K: ...
    @classmethod
    def from_file(
        cls: Type[_K], file: Union[_Path, IO[AnyStr]] = ..., format: int = ..., password: Optional[str] = ...
    ) -> _K: ...
    @classmethod
    def from_memory(cls: Type[_K], data: AnyStr = ..., format: int = ..., password: Optional[str] = ...) -> _K: ...
    @classmethod
    def generate(cls: Type[_K], klass: KeyData = ..., size: int = ..., type: int = ...) -> _K: ...
    def load_cert_from_file(self, file: Union[_Path, IO[AnyStr]] = ..., format: int = ...) -> None: ...
    def load_cert_from_memory(self, data: AnyStr, format: int = ...) -> None: ...
    def __copy__(self: _K) -> _K: ...
    def __deepcopy__(self: _K) -> _K: ...

class KeysManager:
    def add_key(self, key: Key = ...) -> None: ...
    def load_cert(self, filename: _Path = ..., format: int = ..., type: int = ...) -> None: ...
    def load_cert_from_memory(self, data: AnyStr = ..., format: int = ..., type: int = ...) -> None: ...

class SignatureContext:
    key: Key
    def enable_reference_transform(self, transform: Transform = ...) -> None: ...
    def enable_signature_transform(self, transform: Transform = ...) -> None: ...
    def register_id(self, node: _Element = ..., id_attr: str = "ID", id_ns: Optional[str] = None) -> None: ...
    def set_enabled_key_data(self, keydata_list: Iterable[KeyData] = ...) -> None: ...
    def sign(self, node: _Element = ...) -> None: ...
    def sign_binary(self, bytes: bytes = ..., transform: Transform = ...) -> bytes: ...
    def verify(self, node: _Element = ...) -> None: ...
    def verify_binary(self, bytes: bytes = ..., transform: Transform = ..., signature: bytes = ...) -> None: ...

class VerificationError(Error): ...
