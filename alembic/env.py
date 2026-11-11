
"""
SRE Agent - Alembic Environment

Configures database migrations using SQLAlchemy's asynchronous
engine and the application's database configuration.
"""

from __future__ import annotations

import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config

from sre_agent.core.config import settings
from sre_agent.persistence.database import Base

# --------------------------------------------------
# Alembic configuration
# --------------------------------------------------

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --------------------------------------------------
# SQLAlchemy metadata
# --------------------------------------------------

target_metadata = Base.metadata

# Import models here as they are implemented.
# This ensures Alembic discovers their table definitions.
#
# Example:
# from sre_agent.persistence.models import organization
# from sre_agent.persistence.models import investigation


# --------------------------------------------------
# Database URL
# --------------------------------------------------

def get_database_url() -> str:
    """Return the configured asynchronous database URL."""

    return str(settings.DATABASE_URL)


# --------------------------------------------------
# Offline migrations
# --------------------------------------------------

def run_migrations_offline() -> None:
    """Run migrations without creating a database connection."""

    context.configure(
        url=get_database_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
        compare_server_default=True,
        render_as_batch=False,
    )

    with context.begin_transaction():
        context.run_migrations()


# --------------------------------------------------
# Online migrations
# --------------------------------------------------

def do_run_migrations(connection) -> None:
    """Configure and execute migrations using a database connection."""

    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
        compare_server_default=True,
        render_as_batch=False,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """Create an asynchronous engine and execute migrations."""

    configuration = config.get_section(
        config.config_ini_section,
        {},
    )

    configuration["sqlalchemy.url"] = get_database_url()

    connectable = async_engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    try:
        async with connectable.connect() as connection:
            await connection.run_sync(do_run_migrations)
    finally:
        await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations using an asynchronous database connection."""

    asyncio.run(run_async_migrations())


# --------------------------------------------------
# Migration entry point
# --------------------------------------------------

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
