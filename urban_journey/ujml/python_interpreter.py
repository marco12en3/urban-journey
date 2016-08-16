import sys


class DTSMLPythonSourceClass(object):
    def __init__(self, source, filename, mode, lineno=0):
        self.__code = compile('\n'*(lineno-1)+source, filename, mode)
        self.__mode = mode
        self.__filename = filename
        self.__lineno = lineno

    @property
    def code(self):
        return self.__code

    @property
    def filename(self):
        return self.__filename

    @property
    def lineno(self):
        return self.__lineno


class DTSMLPythonInterpreterClass(object):
    def __init__(self):
        self.__dtsml_locals = {}

    def __getitem__(self, key):
        return self.__dtsml_locals[key]

    def __setitem__(self, key, value):
        self.__dtsml_locals[key] = value

    def exec(self, source, filename, lineno):
        exec(compile('\n'*(lineno-1)+source, filename, 'exec'), self.__dtsml_locals)

    def run_src_object(self, src_obj):
        if isinstance(src_obj, DTSMLPythonSourceClass):
            return eval(src_obj.code, self.__dtsml_locals)
        else:
            raise TypeError("Parameter should be of type 'DTSMLPythonSourceClass'")

    def eval(self, source, filename, lineno):
        lines = source.strip().splitlines()
        if len(lines) > 1:
            exec(compile('\n'*(lineno-1)+'\n'.join(lines[:-1]), filename, 'exec'), self.__dtsml_locals)
        return eval(compile('\n'*(lineno-1+len(lines)-1)+lines[-1], filename, 'eval'), self.__dtsml_locals)