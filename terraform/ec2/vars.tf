variable "region" {
    default = "us-west-1"
}

variable "ec2_ami" {
	type = "map"

	default = {
		ap-south-1 = "ami-76d6f519"
		us-west-1 = "ami-e251209a"
	}
}
