from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.TopLoc import *
from OCC.Core.Message import *
from OCC.Core.TopAbs import *
from OCC.Core.TCollection import *

# the following typedef cannot be wrapped as is
TopTools_Array2OfShape = NewType("TopTools_Array2OfShape", Any)
# the following typedef cannot be wrapped as is
TopTools_DataMapIteratorOfDataMapOfShapeBox = NewType("TopTools_DataMapIteratorOfDataMapOfShapeBox", Any)
# the following typedef cannot be wrapped as is
TopTools_IndexedDataMapOfShapeAddress = NewType("TopTools_IndexedDataMapOfShapeAddress", Any)
# the following typedef cannot be wrapped as is
TopTools_IndexedDataMapOfShapeListOfShape = NewType("TopTools_IndexedDataMapOfShapeListOfShape", Any)
# the following typedef cannot be wrapped as is
TopTools_IndexedDataMapOfShapeReal = NewType("TopTools_IndexedDataMapOfShapeReal", Any)
# the following typedef cannot be wrapped as is
TopTools_IndexedDataMapOfShapeShape = NewType("TopTools_IndexedDataMapOfShapeShape", Any)
# the following typedef cannot be wrapped as is
TopTools_IndexedMapOfOrientedShape = NewType("TopTools_IndexedMapOfOrientedShape", Any)
# the following typedef cannot be wrapped as is
TopTools_IndexedMapOfShape = NewType("TopTools_IndexedMapOfShape", Any)
# the following typedef cannot be wrapped as is
TopTools_ListIteratorOfListOfListOfShape = NewType("TopTools_ListIteratorOfListOfListOfShape", Any)
TopTools_LocationSetPtr = NewType("TopTools_LocationSetPtr", TopTools_LocationSet)
# the following typedef cannot be wrapped as is
TopTools_MapIteratorOfMapOfOrientedShape = NewType("TopTools_MapIteratorOfMapOfOrientedShape", Any)
# the following typedef cannot be wrapped as is
TopTools_MapIteratorOfMapOfShape = NewType("TopTools_MapIteratorOfMapOfShape", Any)
# the following typedef cannot be wrapped as is
TopTools_MapOfOrientedShape = NewType("TopTools_MapOfOrientedShape", Any)
# the following typedef cannot be wrapped as is
TopTools_MapOfShape = NewType("TopTools_MapOfShape", Any)

class TopTools_Array1OfListOfShape:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> TopTools_ListOfShape: ...
    def __setitem__(self, index: int, value: TopTools_ListOfShape) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[TopTools_ListOfShape]: ...
    def next(self) -> TopTools_ListOfShape: ...
    __next__ = next
    def Init(self, theValue: TopTools_ListOfShape) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> TopTools_ListOfShape: ...
    def Last(self) -> TopTools_ListOfShape: ...
    def Value(self, theIndex: int) -> TopTools_ListOfShape: ...
    def SetValue(self, theIndex: int, theValue: TopTools_ListOfShape) -> None: ...

class TopTools_Array1OfShape:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> TopoDS_Shape: ...
    def __setitem__(self, index: int, value: TopoDS_Shape) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[TopoDS_Shape]: ...
    def next(self) -> TopoDS_Shape: ...
    __next__ = next
    def Init(self, theValue: TopoDS_Shape) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> TopoDS_Shape: ...
    def Last(self) -> TopoDS_Shape: ...
    def Value(self, theIndex: int) -> TopoDS_Shape: ...
    def SetValue(self, theIndex: int, theValue: TopoDS_Shape) -> None: ...

class TopTools_ListOfListOfShape:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> TopTools_ListOfShape: ...
    def Last(self) -> TopTools_ListOfShape: ...
    def Append(self, theItem: TopTools_ListOfShape) -> TopTools_ListOfShape: ...
    def Prepend(self, theItem: TopTools_ListOfShape) -> TopTools_ListOfShape: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> TopTools_ListOfShape: ...
    def SetValue(self, theIndex: int, theValue: TopTools_ListOfShape) -> None: ...

class TopTools_ListOfShape:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> TopoDS_Shape: ...
    def Last(self) -> TopoDS_Shape: ...
    def Append(self, theItem: TopoDS_Shape) -> TopoDS_Shape: ...
    def Prepend(self, theItem: TopoDS_Shape) -> TopoDS_Shape: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> TopoDS_Shape: ...
    def SetValue(self, theIndex: int, theValue: TopoDS_Shape) -> None: ...

class TopTools_SequenceOfShape:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> TopoDS_Shape: ...
    def Last(self) -> TopoDS_Shape: ...
    def Length(self) -> int: ...
    def Append(self, theItem: TopoDS_Shape) -> TopoDS_Shape: ...
    def Prepend(self, theItem: TopoDS_Shape) -> TopoDS_Shape: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> TopoDS_Shape: ...
    def SetValue(self, theIndex: int, theValue: TopoDS_Shape) -> None: ...


class TopTools_FormatVersion(IntEnum):
    TopTools_FormatVersion_VERSION_1: int = ...
    TopTools_FormatVersion_VERSION_2: int = ...
    TopTools_FormatVersion_VERSION_3: int = ...
    TopTools_FormatVersion_CURRENT: int = ...

TopTools_FormatVersion_VERSION_1 = TopTools_FormatVersion.TopTools_FormatVersion_VERSION_1
TopTools_FormatVersion_VERSION_2 = TopTools_FormatVersion.TopTools_FormatVersion_VERSION_2
TopTools_FormatVersion_VERSION_3 = TopTools_FormatVersion.TopTools_FormatVersion_VERSION_3
TopTools_FormatVersion_CURRENT = TopTools_FormatVersion.TopTools_FormatVersion_CURRENT

class toptools:
    @staticmethod
    def Dummy(I: int) -> None: ...
    @staticmethod
    def Dump(Sh: TopoDS_Shape) -> str: ...

class TopTools_LocationSet:
    def __init__(self) -> None: ...
    def Add(self, L: TopLoc_Location) -> int: ...
    def Clear(self) -> None: ...
    def Dump(self) -> str: ...
    def Index(self, L: TopLoc_Location) -> int: ...
    def Location(self, I: int) -> TopLoc_Location: ...
    def Read(self, IS: str, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def Write(self, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> str: ...

class TopTools_MutexForShapeProvider:
    def __init__(self) -> None: ...
    def CreateMutexForShape(self, theShape: TopoDS_Shape) -> None: ...
    def CreateMutexesForSubShapes(self, theShape: TopoDS_Shape, theType: TopAbs_ShapeEnum) -> None: ...
    def GetMutex(self, theShape: TopoDS_Shape) -> Standard_Mutex: ...
    def RemoveAllMutexes(self) -> None: ...

class TopTools_OrientedShapeMapHasher:
    @staticmethod
    def HashCode(theShape: TopoDS_Shape, theUpperBound: int) -> int: ...
    @staticmethod
    def IsEqual(S1: TopoDS_Shape, S2: TopoDS_Shape) -> bool: ...

class TopTools_ShapeMapHasher:
    @staticmethod
    def HashCode(theShape: TopoDS_Shape, theUpperBound: int) -> int: ...
    @staticmethod
    def IsEqual(S1: TopoDS_Shape, S2: TopoDS_Shape) -> bool: ...

class TopTools_ShapeSet:
    def __init__(self) -> None: ...
    def Add(self, S: TopoDS_Shape) -> int: ...
    def AddGeometry(self, S: TopoDS_Shape) -> None: ...
    def AddShapes(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> None: ...
    def ChangeLocations(self) -> TopTools_LocationSet: ...
    def Check(self, T: TopAbs_ShapeEnum, S: TopoDS_Shape) -> None: ...
    def Clear(self) -> None: ...
    @overload
    def Dump(self) -> str: ...
    @overload
    def Dump(self, S: TopoDS_Shape) -> str: ...
    @overload
    def DumpExtent(self) -> Tuple[Standard_OStream, str]: ...
    @overload
    def DumpExtent(self, S: str) -> None: ...
    @overload
    def DumpGeometry(self) -> str: ...
    @overload
    def DumpGeometry(self, S: TopoDS_Shape) -> str: ...
    def FormatNb(self) -> int: ...
    def Index(self, S: TopoDS_Shape) -> int: ...
    def Locations(self) -> TopTools_LocationSet: ...
    def NbShapes(self) -> int: ...
    @overload
    def Read(self, IS: str, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def Read(self, S: TopoDS_Shape, IS: str) -> None: ...
    @overload
    def ReadGeometry(self, IS: str, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def ReadGeometry(self, T: TopAbs_ShapeEnum, IS: str, S: TopoDS_Shape) -> None: ...
    def SetFormatNb(self, theFormatNb: int) -> None: ...
    def Shape(self, I: int) -> TopoDS_Shape: ...
    @overload
    def Write(self, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> str: ...
    @overload
    def Write(self, S: TopoDS_Shape) -> str: ...
    @overload
    def WriteGeometry(self, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> str: ...
    @overload
    def WriteGeometry(self, S: TopoDS_Shape) -> str: ...

# harray1 classes

class TopTools_HArray1OfShape(TopTools_Array1OfShape, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> TopTools_Array1OfShape: ...


class TopTools_HArray1OfListOfShape(TopTools_Array1OfListOfShape, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> TopTools_Array1OfListOfShape: ...

# harray2 classes

class TopTools_HArray2OfShape(TopTools_Array2OfShape, Standard_Transient):
    @overload
    def __init__(self, theRowLow: int, theRowUpp: int, theColLow: int, theColUpp: int) -> None: ...
    @overload
    def __init__(self, theOther: TopTools_Array2OfShape) -> None: ...
    def Array2(self) -> TopTools_Array2OfShape: ...

# hsequence classes

class TopTools_HSequenceOfShape(TopTools_SequenceOfShape, Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: TopTools_SequenceOfShape) -> None: ...
    def Sequence(self) -> TopTools_SequenceOfShape: ...
    def Append(self, theSequence: TopTools_SequenceOfShape) -> None: ...


