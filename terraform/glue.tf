resource "aws_glue_catalog_database" "db" {
  name        = "${var.app_prefix}-database"
  description = "Sample Glue database"
}

resource "aws_glue_crawler" "crawler" {
  database_name = aws_glue_catalog_database.db.name
  name          = "crawler"
  role          = data.aws_iam_role.glue.arn

  depends_on = [
    aws_s3_bucket.sample_s3_bucket
  ]

  s3_target {
    path = "s3://${aws_s3_bucket.sample_s3_bucket.bucket}/read"
  }
}

resource "aws_glue_job" "job" {
  name     = "movie_stats"
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

resource "aws_glue_connection" "snowflake-glue-jdbc-connection" {
  name = "snowflake-glue-jdbc-connection"
  connection_properties = {
    CONNECTOR_CLASS_NAME = "net.snowflake.client.jdbc.SnowflakeDriver"
    CONNECTOR_TYPE       = "Jdbc"
    CONNECTOR_URL        = "s3://app-dev-797814256012/jars/snowflake-jdbc-3.9.2.jar"
    JDBC_CONNECTION_URL  = "jdbc:snowflake://vc70612.east-us-2.azure.snowflakecomputing.com?user=$${Username}&password=$${Password}&warehouse=compute_wh"
    PASSWORD             = "_kYRV@ck2Y"
    USERNAME             = "codeninja"
  }

  connection_type = "CUSTOM"
  match_criteria  = ["Connection", "snowflake-jdbc-connector"]
}