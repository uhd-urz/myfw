from dataclasses import dataclass
from typing import ClassVar

from properpath import P
from rya.pre_utils import PublicLayerNames

from .names import app_dirs


@dataclass
class PluginDefinitions:
    dir: P
    typer_app_file_name_prefix: str = "cli"
    typer_app_file_name: str = f"{typer_app_file_name_prefix}.py"
    typer_app_var_name: str = "app"
    config_section_name: ClassVar[str] = PublicLayerNames.plugins


@dataclass
class InternalPluginLoaderDefinitions(PluginDefinitions):
    directory_name: str = PublicLayerNames.plugins
    dir: P = P(__file__).parent.parent / directory_name


@dataclass
class ExternalPluginLoaderDefinitions(PluginDefinitions):
    directory_name: str = PublicLayerNames.plugins
    dir: P = app_dirs.user_data_dir / directory_name
    file_name_prefix: str = "plugin_metadata"
    file_ext: str = "toml"
    file_name: str = f"{file_name_prefix}.{file_ext}"


@dataclass
class ExternalPluginMetadataDefinitions:
    file_exists: str = f"{ExternalPluginLoaderDefinitions.file_name_prefix}_exists"
    plugin_name: str = "plugin_name"
    cli_script_path: str = "cli_script"
    venv_path: str = "venv_dir"
    project_path: str = "project_dir"
    plugin_root_dir: str = "plugin_root_dir"
