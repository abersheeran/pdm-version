import argparse

from pdm.cli.commands.base import BaseCommand, Project


class VersionCommand(BaseCommand):
    """Set project.version to the given version"""

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        """Manipulate the argument parser to add more arguments"""
        parser.add_argument("version")

    def handle(self, project: Project, options: argparse.Namespace) -> None:
        """The command handler function.

        :param project: the pdm project instance
        :param options: the parsed Namespace object
        """
        project.pyproject["project"]["version"] = options.version
        project.write_pyproject(True)


def version(core):
    core.register_command(VersionCommand, "version")
