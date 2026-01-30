from pathlib import Path

def scan_terraform(path: str) -> dict:
    results = {
        "encryption_at_rest": False,
        "logging_enabled": False,
    }

    for tf_file in Path(path).glob("*.tf"):
        content = tf_file.read_text(encoding="utf-8", errors="ignore")

        if "server_side_encryption_configuration" in content:
            results["encryption_at_rest"] = True

        if "aws_s3_bucket_logging" in content:
            results["logging_enabled"] = True

    return results


