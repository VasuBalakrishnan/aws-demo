resource "aws_glue_catalog_database" "db" {
    name = "${var.app_prefix}-database"
    description = "Sample Glue database"
}

resource "aws_glue_crawler" "crawler" {
  database_name = aws_glue_catalog_database.db.name
  name = "crawler"
  role = data.aws_iam_role.glue.arn

  depends_on = [
    aws_s3_bucket.sample_s3_bucket
  ]

  s3_target {
    path = "s3://${aws_s3_bucket.sample_s3_bucket.bucket}/read"
  }
}

resource "aws_glue_job" "job" {
  name = "movie_stats"
  role_arn = data.aws_iam_role.glue.arn

  command {
      script_location = "s3://${aws_s3_bucket.sample_s3_bucket.bucket}/jobs/movies.py"
  }
}

resource "aws_glue_trigger" "trigger" {
  name = "trigger"
  type = "ON_DEMAND"

  actions {
    job_name = aws_glue_job.job.name
  }
}