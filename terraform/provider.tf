provider "aws" {
    region = "us-west-1"
}

resource "aws_vpc" "mysql" {
  cidr_block = "190.160.0.0/16"
  instance_tenancy = "default"

  tags {
      Name = "main"
      Location = "California"
  }
}

resource "aws_subnet" "subnet1" {
    vpc_id = "${aws_vpc.mysql.id}"
    cidr_block = "190.160.1.0/24"

    tags {
        Name = "Subnet1"
    }
}
