import ctypes
from pyautoeios.eios import EIOS

RI_CHAR = 0
RI_BYTE = 1
RI_BOOLEAN = 2
RI_SHORT = 3
RI_INT = 4
RI_LONG = 5
RI_FLOAT = 6
RI_DOUBLE = 7
RI_STRING = 8
RI_OBJECT = 9


from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


class RSType:
    def __init__(self, eios: EIOS = None, ref=None):
        self.eios = eios
        self.ref = ref
        if self.ref:
            eios._objects[eios._pid][ref] = eios._objects[eios._pid].get(ref, 0) + 1
            # print(f"refcount of {self.__class__.__name__}({ref}) = {eios._objects[eios._pid][ref]}")

    def __str__(self):
        return (
            f"{self.__class__.__name__}({self.ref}) paired with EIOS({self.eios._pid})"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.ref}) paired with EIOS({self.eios._pid})"
        )

    def __del__(self):
        if self.ref:
            ref_count = self.eios._objects[self.eios._pid][self.ref]
            if ref_count == 1:
                self.eios._objects[self.eios._pid].pop(self.ref)
                self.eios._Reflect_Release_Object(self.ref)
                # print(f"refcount of {self.__class__.__name__}({self.ref}) = {ref_count-1}")
            else:
                self.eios._objects[self.eios._pid][self.ref] -= 1
                # print(f"refcount of {self.__class__.__name__}({self.ref}) = {ref_count-1}")


class RSArray(RSType):
    def __init__(self, eios: EIOS = None, ref=None, size=None, ra_type: int = None, ctype=None):
        self.elements = None
        self.size = size
        self.ra_type = ra_type
        self.ctype = ctype
        super().__init__(eios, ref)

    def __getitem__(self, key: int = None):
        if not self.elements:
            element = self.eios._Reflect_Array_Index(self.ref, self.ra_type, key, 1)
            pi = ctypes.cast(element, ctypes.POINTER(self.ctype))
            # print(f"{element = } , {pi = }, {pi.contents.value = }")
            return pi.contents.value
        else:
            return self.elements[key]

    def all(self, refresh: bool = False):
        if refresh or not self.elements:
            if not self.size:
                self.size = self.eios._Reflect_Array_Size(self.ref)
            self.elements = []
            for i in range(0,self.size):
                self.elements.append(self[i])
        return self.elements


class RSIntArray(RSArray):
    def __init__(self, eios: EIOS = None, ref=None, size=None):
        super().__init__(eios=eios, ref=ref, size=size, ra_type=RI_INT, ctype=ctypes.c_int)


class RSLongArray(RSArray):
    def __init__(self, eios: EIOS = None, ref=None, size=None):
        super().__init__(eios=eios, ref=ref, size=size, ra_type=RI_LONG, ctype=ctypes.c_long)


class RSStringArray(RSArray):
    def __init__(self, eios: EIOS = None, ref=None, size=None, max_size=2000):
        self.max_size = max_size
        super().__init__(eios=eios, ref=ref, size=size, ra_type=RI_STRING, ctype=ctypes.c_char_p)

    def __getitem__(self, key: int = None):
        element = self.eios._Reflect_Array_Index(self.ref, self.ra_type, key, 1)
        length = ctypes.cast(element, ctypes.POINTER(ctypes.c_int32)).contents.value
        return strip_tags(ctypes.string_at(element,length+4)[4:].replace(b"\xc2\xa0", b" ").decode("utf8"))
