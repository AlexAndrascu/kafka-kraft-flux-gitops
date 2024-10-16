# Kafka-Enabled HealthCheckService Deployment on Kubernetes with GitOps

This project is a microservices architecture with Kafka as the messaging backbone. It includes the deployment and management of services on a Kubernetes cluster using GitOps principles.


## Getting Started

To start the cluster and deploy the services, follow these steps:

1. Make sure Helm and kubectl are installed on your local machine
2. We'll be using Kind to setup a Kubernetes cluster with 1 control plane and 3 worker nodes
```
kind create cluster --name kafka-cluster --config .\kind-config.yaml
```
Output:
```
Creating cluster "kafka-cluster" ...
 ✓ Ensuring node image (kindest/node:v1.31.0) 🖼
 ✓ Preparing nodes 📦 📦 📦 📦
 ✓ Writing configuration 📜
 ✓ Starting control-plane 🕹️
 ✓ Installing CNI 🔌
 ✓ Installing StorageClass 💾
 ✓ Joining worker nodes 🚜
Set kubectl context to "kind-kafka-cluster"
You can now use your cluster with:

kubectl cluster-info --context kind-kafka-cluster
```
3. Optionally install kubernetes dashboard:

```
helm install dashboard kubernetes-dashboard/kubernetes-dashboard -n kubernetes-dashboard --create-namespace
```
4. Deploy Kafka 
```
helm -n kafka-healthcheck install kafka-h oci://registry-1.docker.io/bitnamicharts/kafka -f .\helm\kafka\values.yaml --create-namespace
```
5. Deploy the monitoring tools
```
cd helm/grafana
helm -n kafka-healthcheck install grafana .
cd helm/prometheus
helm install prometheus prometheus-community/prometheus -f values.yaml -n kafka-healthcheck
```

9. Configure logging for the services to log health check results.
10. Set up Flux to automatically deploy the services when changes are pushed to the GitOps repository.
11. Kubernetes Dashboard Service Account:
```
cd dashboard
kubectl apply -n kubernetes-dashboard -f .\dashboard-adminuser.yaml -f .\dashboard-clusterrole.yaml -f .\dash-secret.yaml
```
For detailed instructions on each step, refer to the documentation in the individual files and directories.

```
