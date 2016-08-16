'''There can only exist one RequiredType and EmptyType objects at a time, Required and Empty. These objects can be used
in the same manner as the python build in constant None. Create a new instance of either RequiredType or EmptyType will
return the already existing objects.'''


class RequiredType:
    val = None

    def __new__(cls, *args, **kwargs):
        if cls.val is None:
            cls.val = super().__new__(cls)
        return cls.val

    def __repr__(self):
        return "Required"

    def __str__(self):
        return "Required"


class EmptyType:
    val = None

    def __new__(cls, *args, **kwargs):
        if cls.val is None:
            cls.val = super().__new__(cls)
        return cls.val

    def __repr__(self):
        return "Empty"

    def __str__(self):
        return "Empty"

Required = RequiredType()
Empty = EmptyType()


if __name__ == "__main__":
    r2 = RequiredType()
    print(id(r2))
    print(id(Required))
