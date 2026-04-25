import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUTS_DIR = BASE_DIR / "outputs"
DEFAULT_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://stratega-five.vercel.app",
]


def _normalize_origin(origin: str):
    return origin.strip().rstrip("/")


def get_allowed_origins():
    raw_origins = os.getenv("ALLOWED_ORIGINS", "")
    configured_origins = [
        _normalize_origin(origin)
        for origin in raw_origins.split(",")
        if origin.strip()
    ]

    merged_origins = []
    for origin in [*DEFAULT_ALLOWED_ORIGINS, *configured_origins]:
        normalized = _normalize_origin(origin)
        if normalized and normalized not in merged_origins:
            merged_origins.append(normalized)

    return merged_origins


def get_allowed_origin_regex():
    return os.getenv(
        "ALLOWED_ORIGIN_REGEX",
        r"^https:\/\/stratega(?:-[a-z0-9-]+)?\.vercel\.app$",
    ).strip() or None
