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

resource "aws_subnet" "subnets" {
  count = "${length(data.aws_availability_zones.azs.names)}"
  availability_zone = "${element(data.aws_availability_zones.azs.names, count.index)}"
  vpc_id = "${aws_vpc.mysql.id}"
  cidr_block = "${element(var.subnet_cidr, count.index)}"

  tags {
    Name = "Subnet-${count.index+1}"
  }
}
