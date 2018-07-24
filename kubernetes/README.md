# Kubernetes

## Launching Pod from Docker image

#### 1. Create secret docker-registry key

```bash
DOCKER_REGISTRY_SERVER=docker.io
DOCKER_USER=Type your dockerhub username, same as when you `docker login`
DOCKER_EMAIL=Type your dockerhub email, same as when you `docker login`
DOCKER_PASSWORD=Type your dockerhub pw, same as when you `docker login`

kubectl create secret docker-registry myregistrykey \
  --docker-server=$DOCKER_REGISTRY_SERVER \
  --docker-username=$DOCKER_USER \
  --docker-password=$DOCKER_PASSWORD \
  --docker-email=$DOCKER_EMAIL
```

#### 2. Create yaml file

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: POD_NAME
spec:
  containers:
    - name: CONTAINER_NAME
      image: DOCKER_USER/PRIVATE_REPO_NAME
      imagePullPolicy: Always
      command: ["python"]
      args: ["-c", "import time; time.sleep(5); print('Hello, world!')"]
  imagePullSecrets:
    - name: myregistrykey
```

#### 3. Create pod using kubectl and yaml file

```bash
kubectl create -f example.yaml
```

#### References

  [How to access private Docker registry from Kubernetes](https://stackoverflow.com/questions/36232906/how-to-access-private-docker-hub-repository-from-kubernetes-on-vagrant)
  [Creating a secret with a Docker config](https://kubernetes.io/docs/concepts/containers/images/#using-a-private-registry)
  [How to change Docker registry to private registry](https://stackoverflow.com/questions/33054369/how-to-change-the-default-docker-registry-from-docker-io-to-my-private-registry)
