from urban_journey.ujml.element_types.data_base import DataBaseElement
from urban_journey.ujml.attribute_types import string_t
from urban_journey.ujml.exceptions import DataLoadError

import sys
import pickle


class PickleLoaderClass(DataBaseElement):
    """This element is used to load in python pickle files.

        **UJML attributes**

        .. attribute:: file

           **type:** string

        **Members**

    """

    # Attributes
    file = string_t()

    def _init(self):
        try:
            self.__data = pickle.load(open(self.file, "rb"))
        except Exception as e:
            raise DataLoadError(self.dtsml.filename, self.sourceline, "pickle").with_traceback(sys.exc_info()[2])

    @property
    def data(self):
        return self.__data
