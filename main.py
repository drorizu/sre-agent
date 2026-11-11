
"""
SRE Agent - Application Entry Point

Initializes the FastAPI application, configures middleware,
registers API routes, and manages application lifecycle.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sre_agent.api.middleware import RequestContextMiddleware
from sre_agent.api.routes import health
from sre_agent.core.config import settings
from sre_agent.core.lifecycle import (
    startup_application,
    shutdown_application,
)
from sre_agent.core.logging import configure_logging


# --------------------------------------------------
# Logging Configuration
# --------------------------------------------------

configure_logging()


# --------------------------------------------------
# Application Lifecycle
# --------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """
    Manage application startup and shutdown.

    Startup:
        Initialize shared infrastructure and services.

    Shutdown:
        Close database connections and external resources.
    """

    await startup_application(app)

    yield

    await shutdown_application(app)


# --------------------------------------------------
# FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title=settings.APP_NAME,
    description=(
        "AI-powered Site Reliability Engineering platform "
        "for infrastructure investigations and incident analysis."
    ),
    version="0.1.0",
    openapi_url=(
        f"{settings.API_V1_PREFIX}/openapi.json"
        if settings.APP_ENV != "production"
        else None
    ),
    docs_url=(
        f"{settings.API_V1_PREFIX}/docs"
        if settings.APP_ENV != "production"
        else None
    ),
    redoc_url=(
        f"{settings.API_V1_PREFIX}/redoc"
        if settings.APP_ENV != "production"
        else None
    ),
    lifespan=lifespan,
)


# --------------------------------------------------
# Middleware Configuration
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=[
        "Authorization",
        "Content-Type",
        "X-Request-ID",
    ],
)

app.add_middleware(RequestContextMiddleware)


# --------------------------------------------------
# API Route Registration
# --------------------------------------------------

app.include_router(
    health.router,
    tags=["Health"],
)


# Additional routers will be registered here as
# their implementations become available.
#
# Example:
# app.include_router(investigations.router, prefix=settings.API_V1_PREFIX)
# app.include_router(organizations.router, prefix=settings.API_V1_PREFIX)


# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------

@app.get(
    "/",
    tags=["General"],
    summary="Application information",
)
async def root() -> dict[str, str]:
    """Return basic application information."""

    return {
        "application": settings.APP_NAME,
        "version": "0.1.0",
        "status": "running",
        "environment": settings.APP_ENV,
    }
