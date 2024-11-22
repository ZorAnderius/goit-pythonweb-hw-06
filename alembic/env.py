import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from dotenv import load_dotenv  # Завантаження dotenv

# Завантажуємо змінні середовища з файлу .env
load_dotenv('.env')

# Конфігурація Alembic
config = context.config

# Встановлюємо URL бази даних з використанням змінних середовища
config.set_main_option(
    'sqlalchemy.url',
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@postgres:5432/{os.getenv('POSTGRES_DB')}"
)

# Налаштування логування
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Імпортуйте Base з вашого проекту для відстеження моделей
from models import Base  # Замість models використайте ваш шлях до модулю
target_metadata = Base.metadata

def run_migrations_offline():
    """Запуск міграцій в офлайн режимі."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Запуск міграцій в онлайн режимі."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
