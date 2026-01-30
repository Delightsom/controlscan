resource "aws_s3_bucket" "logs_bucket" {
  bucket = "example-logs-bucket"
}

resource "aws_s3_bucket_logging" "logs" {
  bucket        = aws_s3_bucket.logs_bucket.id
  target_bucket = aws_s3_bucket.logs_bucket.id
  target_prefix = "access-logs/"
}
