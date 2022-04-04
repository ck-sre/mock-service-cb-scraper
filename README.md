# Coinbase scraper project

Source code is in ./src

Metrics are on /metrics

    ➜ curl 127.0.0.1:5001/metrics/
    # HELP python_gc_objects_collected_total Objects collected during gc
    # TYPE python_gc_objects_collected_total counter
    python_gc_objects_collected_total{generation="0"} 402.0
    python_gc_objects_collected_total{generation="1"} 0.0
    python_gc_objects_collected_total{generation="2"} 0.0
    # HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
    # TYPE python_gc_objects_uncollectable_total counter
    python_gc_objects_uncollectable_total{generation="0"} 0.0
    python_gc_objects_uncollectable_total{generation="1"} 0.0
    python_gc_objects_uncollectable_total{generation="2"} 0.0
    # HELP python_gc_collections_total Number of times this generation was collected
    # TYPE python_gc_collections_total counter
    python_gc_collections_total{generation="0"} 88.0
    python_gc_collections_total{generation="1"} 7.0
    python_gc_collections_total{generation="2"} 0.0
    # HELP python_info Python platform information
    # TYPE python_info gauge
    python_info{implementation="CPython",major="3",minor="9",patchlevel="10",version="3.9.10"} 1.0
    # HELP flask_exporter_info Information about the Prometheus Flask exporter
    # TYPE flask_exporter_info gauge
    flask_exporter_info{version="0.19.0"} 1.0
    # HELP flask_http_request_duration_seconds Flask HTTP request duration in seconds
    # TYPE flask_http_request_duration_seconds histogram
    flask_http_request_duration_seconds_bucket{le="0.005",method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.01",method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.025",method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.05",method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.075",method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.1",method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.25",method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.5",method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.75",method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_bucket{le="1.0",method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_bucket{le="2.5",method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_bucket{le="5.0",method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_bucket{le="7.5",method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_bucket{le="10.0",method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_bucket{le="+Inf",method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_count{method="GET",path="/health/",status="404"} 1.0
    flask_http_request_duration_seconds_sum{method="GET",path="/health/",status="404"} 0.00029430099999672166
    flask_http_request_duration_seconds_bucket{le="0.005",method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.01",method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.025",method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.05",method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.075",method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.1",method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.25",method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.5",method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.75",method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_bucket{le="1.0",method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_bucket{le="2.5",method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_bucket{le="5.0",method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_bucket{le="7.5",method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_bucket{le="10.0",method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_bucket{le="+Inf",method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_count{method="GET",path="/health",status="200"} 1.0
    flask_http_request_duration_seconds_sum{method="GET",path="/health",status="200"} 0.0001483759999985068
    flask_http_request_duration_seconds_bucket{le="0.005",method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.01",method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.025",method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.05",method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.075",method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.1",method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.25",method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.5",method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_bucket{le="0.75",method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_bucket{le="1.0",method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_bucket{le="2.5",method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_bucket{le="5.0",method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_bucket{le="7.5",method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_bucket{le="10.0",method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_bucket{le="+Inf",method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_count{method="GET",path="/metrics",status="308"} 1.0
    flask_http_request_duration_seconds_sum{method="GET",path="/metrics",status="308"} 0.00018226200000981407
    # HELP flask_http_request_duration_seconds_created Flask HTTP request duration in seconds
    # TYPE flask_http_request_duration_seconds_created gauge
    flask_http_request_duration_seconds_created{method="GET",path="/health/",status="404"} 1.649082248855795e+09
    flask_http_request_duration_seconds_created{method="GET",path="/health",status="200"} 1.649082276716737e+09
    flask_http_request_duration_seconds_created{method="GET",path="/metrics",status="308"} 1.6490823167148092e+09
    # HELP flask_http_request_total Total number of HTTP requests
    # TYPE flask_http_request_total counter
    flask_http_request_total{method="GET",status="404"} 1.0
    flask_http_request_total{method="GET",status="200"} 1.0
    flask_http_request_total{method="GET",status="308"} 1.0
    # HELP flask_http_request_created Total number of HTTP requests
    # TYPE flask_http_request_created gauge
    flask_http_request_created{method="GET",status="404"} 1.649082248856246e+09
    flask_http_request_created{method="GET",status="200"} 1.649082276716809e+09
    flask_http_request_created{method="GET",status="308"} 1.649082316714883e+09
    # HELP flask_http_request_exceptions_total Total number of HTTP requests which resulted in an exception
    # TYPE flask_http_request_exceptions_total counter
    # HELP app_info Coinbase scraper info
    # TYPE app_info gauge
    app_info{version="1.0.0"} 1.0
    # HELP in_progress Long running requests in progress
    # TYPE in_progress gauge
    in_progress 0.0
    # HELP requests_by_status Request latencies by status
    # TYPE requests_by_status summary





Healthcheck is on /health

    curl 127.0.0.1:5001/health
    {"hostname": "Cyrils-MBP", "status": "success", "timestamp": 1649082276.7165859, "results": []}%

To run the dockerfile:

    docker build ./src -t  cyrilkurian/coinbase_scraper:2.0.0
    docker run -p 0.0.0.0:5001:5001/tcp cyrilkurian/coinbase_scraper:0.0.1

The above steps are github action steps as well

## Github Actions
Github actions are defined in .github/workflows

## Helm
Helm deployment and slack messaging are also defined in workflows.
Helm charts are defined in ./helm


## Terraform deployments

Commands:

    terraform init
    terraform plan

Terraform sample plan:

    Terraform will perform the following actions:

    # aws_iam_policy.iam_policy_for_lambda will be created
    + resource "aws_iam_policy" "iam_policy_for_lambda" {
        + arn         = (known after apply)
        + description = "AWS IAM Policy for managing aws lambda role"
        + id          = (known after apply)
        + name        = "aws_iam_policy_for_terraform_aws_lambda_role"
        + path        = "/"
        + policy      = jsonencode(
                {
                + Statement = [
                    + {
                        + Action   = [
                            + "logs:CreateLogGroup",
                            + "logs:CreateLogStream",
                            + "logs:PutLogEvents",
                            ]
                        + Effect   = "Allow"
                        + Resource = "arn:aws:logs:*:*:*"
                        },
                    ]
                + Version   = "2012-10-17"
                }
            )
        + policy_id   = (known after apply)
        + tags_all    = (known after apply)
        }

    # aws_iam_role.lambda_role will be created
    + resource "aws_iam_role" "lambda_role" {
        + arn                   = (known after apply)
        + assume_role_policy    = jsonencode(
                {
                + Statement = [
                    + {
                        + Action    = "sts:AssumeRole"
                        + Effect    = "Allow"
                        + Principal = {
                            + Service = "lambda.amazonaws.com"
                            }
                        + Sid       = ""
                        },
                    ]
                + Version   = "2012-10-17"
                }
            )
        + create_date           = (known after apply)
        + force_detach_policies = false
        + id                    = (known after apply)
        + managed_policy_arns   = (known after apply)
        + max_session_duration  = 3600
        + name                  = "scraper_lambda_role"
        + name_prefix           = (known after apply)
        + path                  = "/"
        + tags_all              = (known after apply)
        + unique_id             = (known after apply)

        + inline_policy {
            + name   = (known after apply)
            + policy = (known after apply)
            }
        }

    # aws_iam_role_policy_attachment.attach_iam_policy_to_iam_role will be created
    + resource "aws_iam_role_policy_attachment" "attach_iam_policy_to_iam_role" {
        + id         = (known after apply)
        + policy_arn = (known after apply)
        + role       = "scraper_lambda_role"
        }

    # aws_lambda_function.coinbase_lambda will be created
    + resource "aws_lambda_function" "coinbase_lambda" {
        + architectures                  = (known after apply)
        + arn                            = (known after apply)
        + filename                       = "lambda_function_payload.zip"
        + function_name                  = "lambda_function_name"
        + handler                        = "index.lambda_handler"
        + id                             = (known after apply)
        + invoke_arn                     = (known after apply)
        + last_modified                  = (known after apply)
        + memory_size                    = 128
        + package_type                   = "Zip"
        + publish                        = false
        + qualified_arn                  = (known after apply)
        + reserved_concurrent_executions = -1
        + role                           = (known after apply)
        + runtime                        = "python3.8"
        + signing_job_arn                = (known after apply)
        + signing_profile_version_arn    = (known after apply)
        + source_code_hash               = "./lambda-container/coinbase-scraper.zip"
        + source_code_size               = (known after apply)
        + tags_all                       = (known after apply)
        + timeout                        = 3
        + version                        = (known after apply)

        + environment {
            + variables = {
                + "APP_PORT" = "5001"
                }
            }

        + ephemeral_storage {
            + size = (known after apply)
            }

        + tracing_config {
            + mode = (known after apply)
            }
        }

    Plan: 4 to add, 0 to change, 0 to destroy.
