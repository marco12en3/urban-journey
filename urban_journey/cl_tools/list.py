from os.path import isdir, join

from .cl_base import ClBase
from urban_journey import UjProject
from urban_journey.uj_project import InvalidUjProjectError


class list(ClBase):
    @staticmethod
    def description():
        return "Prints the list of dependencies and extensions in this project."

    @staticmethod
    def usage():
        return "usage: uj list"

    @staticmethod
    def main(args):
        try:
            uj_project = UjProject()
        except InvalidUjProjectError:
            print("error: Not a uj project (or any of the parent directories)")
            return

        print("dependencies:")
        for name in uj_project.dependencies:
            try:
                UjProject(join(uj_project.path, "dependencies", name))
                source = uj_project.get_metadata()[name]
                present = "present"
            except InvalidUjProjectError:
                present = "missing"
                source = ""

            print(" ", name, present, source)

