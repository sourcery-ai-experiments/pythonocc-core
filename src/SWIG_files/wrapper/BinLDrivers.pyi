from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Message import *
from OCC.Core.BinMDF import *
from OCC.Core.TDocStd import *
from OCC.Core.PCDM import *
from OCC.Core.TCollection import *
from OCC.Core.CDM import *
from OCC.Core.Storage import *

# the following typedef cannot be wrapped as is
BinLDrivers_VectorOfDocumentSection = NewType("BinLDrivers_VectorOfDocumentSection", Any)

class BinLDrivers_Marker(IntEnum):
    BinLDrivers_ENDATTRLIST: int = ...
    BinLDrivers_ENDLABEL: int = ...

BinLDrivers_ENDATTRLIST = BinLDrivers_Marker.BinLDrivers_ENDATTRLIST
BinLDrivers_ENDLABEL = BinLDrivers_Marker.BinLDrivers_ENDLABEL

class binldrivers:
    @staticmethod
    def AttributeDrivers(MsgDrv: Message_Messenger) -> BinMDF_ADriverTable: ...
    @staticmethod
    def DefineFormat(theApp: TDocStd_Application) -> None: ...
    @staticmethod
    def Factory(theGUID: Standard_GUID) -> Standard_Transient: ...

class BinLDrivers_DocumentRetrievalDriver(PCDM_RetrievalDriver):
    def __init__(self) -> None: ...
    def AttributeDrivers(self, theMsgDriver: Message_Messenger) -> BinMDF_ADriverTable: ...
    @overload
    def Read(self, theFileName: str, theNewDocument: CDM_Document, theApplication: CDM_Application, theFilter: Optional[PCDM_ReaderFilter] = PCDM_ReaderFilter(), theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def Read(self, theIStream: str, theStorageData: Storage_Data, theDoc: CDM_Document, theApplication: CDM_Application, theFilter: Optional[PCDM_ReaderFilter] = PCDM_ReaderFilter(), theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...

class BinLDrivers_DocumentSection:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theName: str, isPostRead: bool) -> None: ...
    def IsPostRead(self) -> bool: ...
    def Length(self) -> False: ...
    def Name(self) -> str: ...
    def Offset(self) -> False: ...
    @staticmethod
    def ReadTOC(theSection: BinLDrivers_DocumentSection, theIS: str, theDocFormatVersion: TDocStd_FormatVersion) -> bool: ...
    def WriteTOC(self, theDocFormatVersion: TDocStd_FormatVersion) -> str: ...

class BinLDrivers_DocumentStorageDriver(PCDM_StorageDriver):
    def __init__(self) -> None: ...
    def AddSection(self, theName: str, isPostRead: Optional[bool] = True) -> None: ...
    def AttributeDrivers(self, theMsgDriver: Message_Messenger) -> BinMDF_ADriverTable: ...
    def IsQuickPart(self, theVersion: int) -> bool: ...
    @overload
    def Write(self, theDocument: CDM_Document, theFileName: str, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def Write(self, theDocument: CDM_Document, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> str: ...

# harray1 classes
# harray2 classes
# hsequence classes

