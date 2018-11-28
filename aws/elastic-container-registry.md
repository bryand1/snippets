## Get started with Amazon ECR

1) Retrieve the login command to use to authenticate your docker registry.

For macOS or Linux systems, use the AWS CLI:

```bash
$(aws ecr get-login --no-include-email --region us-east-1)
```

2) Build your Docker image using the following command:

```bash
docker build -t [IMAGE_NAME] .
```

3) After the build completes, tag your image so you can push the image to this repository:

```bash
docker tag [IMAGE_NAME]:latest [REPOSITORY_NAME]/[IMAGE_NAME]:latest
```

4) Run the following command to push this image to your newly created AWS repository

```bash
docker push [REPOSITORY_NAME]/[IMAGE_NAME]:latest
```

