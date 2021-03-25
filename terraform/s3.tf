resource "aws_s3_bucket" "sample_s3_bucket" {
    bucket = "${var.app_prefix}-${var.stage_name}-${data.aws_caller_identity.current.account_id}"
    acl = "private"

    tags = {
        Name = "Sample S3 bucket"
        Environment = var.stage_name
    }
}

output "S3" {
    value = aws_s3_bucket.sample_s3_bucket
}