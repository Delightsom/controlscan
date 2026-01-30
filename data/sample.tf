resource "aws_s3_bucket" "secure_bucket" {
  bucket = "example-secure-bucket"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}
