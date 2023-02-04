# nurl - Run curl commands through a webpage

## What it does

You input your commands into a text box and command is executed with output of the command sent back

## Why would I use this

- If you dont have direct access to your pods in a cluster and can't exec into them
- You want to quickly check the behaviour of another deployment in your cluster. (Checking that your service is correctly connect to a pod for example)
- Perform a quick sanity check that your cluster is set up correctly
- You are new to kubenetes 
## Commands avaliable 

`curl & jq` are currently avaliable

Raise an issue if you want another tool added, or clone the repo and build it yourself. Commands are installed via the `Dockerfile`

## Roadmap 

- Kubectl support
- Basic authentication support
- Configuration options 

## Run with docker 

#### Build the image

`docker build -t nurl .`

#### Run the imaqe

`docker run -p 5000:5000 nurl`

## Deploy to a cluster

[deployment.yaml](./deployment.yaml) is a sample manifest that deploys nurl to a cluster & attaches a service to it.

```
# Deploy to the cluster
kubectl apply -f ./deployment.yaml

# Port forward the pod to access directly 
kubectl port-forward <pod-name> 5000:5000

# You can also access through the service if you cant port-forward
```

