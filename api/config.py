from pathlib import Path

from dynaconf import Dynaconf, Validator

ROOT_FOLDER = Path(__file__).parent.parent

settings = Dynaconf(
    envvar_prefix='vm_exchange',
    settings_files=[
        ROOT_FOLDER / 'settings.toml',
        ROOT_FOLDER / '.secrets.toml'
    ],
    default_env='default',
    environments=['development', 'testing', 'production'],
    env_switcher='vm_exchange_env',
    merge_enabled=True,
    load_dotenv=False
)

# Ensures API_KEY exists in .secrets.toml or as an environment variable
settings.validators.register(Validator("security.API_KEY", must_exist=True, is_type_of=str))
settings.validators.validate()
