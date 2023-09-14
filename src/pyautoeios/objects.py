from pyautoeios._internal.rs_tile import RSTile
from src.pyautoeios._internal.rs_client import RSClient
from src.pyautoeios._internal.rs_object_definition import RSObjectDefinition, RSObjectType
from src.pyautoeios._internal.rs_object import RSObject

from typing import List, Optional

def R_FindObject(ObjectType: RSObjectType, X: int, Y: int) -> RSObject:
    Obj = RSObject.get(ObjectType, X, Y)
    if Obj.ref is not None:
        Definition = Obj.definition()
        result = RSObject(Obj.oid(), Obj.tile(), ObjectType)
        if Definition.ref is not None:
            result.Name = Definition.name()
        return result
    return None

def R_FindObjects(ID: int, ObjectType: RSObjectType) -> List[RSObject]:
    Objects = RSObject.get(ObjectType)
    results = []
    for obj in Objects:
        if obj.oid() == ID:
            Definition = obj.definition()
            result = RSObject(ID, obj.tile(), ObjectType)
            if Definition.ref is not None:
                result.Name = Definition.name()
            results.append(result)
    return results

def R_FindObjects(ObjectType: RSObjectType) -> List[RSObject]:
    Objects = RSObject.get(ObjectType)
    results = []
    for obj in Objects:
        Definition = obj.definition()
        result = RSObject(obj.oid(), obj.tile(), ObjectType)
        if Definition.ref is not None:
            result.Name = Definition.name()
        results.append(result)
    return results
