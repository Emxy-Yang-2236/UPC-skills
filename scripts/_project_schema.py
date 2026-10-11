"""Small shared schema for research artifacts, not activity logging."""

TABLES = {
    "requirements": ("id", "question", "status"),
    "sources": ("id", "kind", "locator", "status"),
    "parameters": ("symbol", "value", "unit", "role", "source_ids"),
    "claims": ("id", "requirement_ids", "statement", "source_ids", "artifact_paths", "status"),
    "validation": ("id", "claim_ids", "method", "criterion", "result", "artifact_paths", "status"),
    "runs": ("id", "kind", "command", "input_paths", "output_paths", "status"),
}


def split_items(value):
    return [part.strip() for part in value.split(";") if part.strip()]
