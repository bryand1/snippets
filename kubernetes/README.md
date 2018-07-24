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


## Use ConfigMap to load Container environment

#### 1. Create environment file

```bash
MYSQL_HOST=55.100.100.100
MYSQL_USER=mysql
MYSQL_PASSWORD=password
```

#### 2. Create ConfigMap using the environment file

```bash
kubectl create configmap example-configmap --from-env-file=/path/to/environment-file 
```

#### 3. Check ConfigMap was created properly 

```bash
kubectl get configmap example-configmap -o yaml
```

```yaml
apiVersion: v1
data:
  MYSQL_HOST: 55.100.100.100
  MYSQL_PASSWORD: password
  MYSQL_USER: mysql
kind: ConfigMap
metadata:
  creationTimestamp: 2018-07-01T00:00:00Z
  name: example-configmap
  namespace: default
  resourceVersion: "544516"
  selfLink: /api/v1/namespaces/default/configmaps/example-configmap
  uid: 5649117d-8f9b-11e8-b77e-0a6bb0c2c302
```

#### 4. Create pod.yaml file

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
      args: ["-c", "iimport os; print(os.environ)"]
      envFrom:
        - configMapRef:
            name: example-configmap
  imagePullSecrets:
    - name: myregistrykey
  restartPolicy: Never
```
