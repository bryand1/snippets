variable "region" {
  default = "us-west-1"
}

variable "vpc_cidr" {
  default = "190.160.0.0/16"
}

variable "subnet_cidr" {
  type = "list"
  default = ["190.160.1.0/24", "190.160.2.0/24", "190.160.3.0/24"]
}

# variable "azs" {
#     type = "list"
#     default = ["us-west-1a", "us-west-1b", "us-west-1c"]
# }

data "aws_availability_zones" "azs" {}
