from dataclasses import dataclass

from properpath import P

from .names import app_dirs


@dataclass
class InternalPluginLoaderDefinitions:
    root_installation_dir: P = P(__file__).parent.parent
    directory_name: str = "plugins"
    typer_app_file_name_prefix: str = "cli"
    typer_app_file_name: str = f"{typer_app_file_name_prefix}.py"
    typer_app_var_name: str = "app"


@dataclass
class ExternalPluginLoaderDefinitions:
    directory_name: str = InternalPluginLoaderDefinitions.directory_name
    dir: P = app_dirs.user_data_dir / directory_name
    typer_app_file_name_prefix: str = (
        InternalPluginLoaderDefinitions.typer_app_file_name_prefix
    )
    typer_app_file_name: str = InternalPluginLoaderDefinitions.typer_app_file_name
    typer_app_var_name: str = InternalPluginLoaderDefinitions.typer_app_var_name
    file_name_prefix: str = "plugin_metadata"
    file_ext: str = "yml"
    file_name: str = f"{file_name_prefix}.{file_ext}"


@dataclass
class ExternalPluginMetadataDefinitions:
    file_exists: str = f"{ExternalPluginLoaderDefinitions.file_name_prefix}_exists"
    plugin_name: str = "plugin_name"
    cli_script_path: str = "cli_script"
    venv_path: str = "venv_dir"
    project_path: str = "project_dir"
    plugin_root_dir: str = "plugin_root_dir"
