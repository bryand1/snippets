provider "aws" {
    region = "${var.region}"
}

resource "aws_vpc" "mysql" {
  cidr_block = "${var.vpc_cidr}"
  instance_tenancy = "default"

  tags {
      Name = "main"
      Location = "California"
  }
}

resource "aws_subnet" "subnet1" {
    vpc_id = "${aws_vpc.mysql.id}"
    cidr_block = "${var.subnet_cidr}"

    tags {
        Name = "Subnet1"
    }
}
