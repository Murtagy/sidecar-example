This repo serves like as an example of two http services written in Python served together as a single pod.

Note: this is a simplistic example. 
On production you might want to:
- define probes;
- assure sidecar fully starts before main app (e.g. move sidecar into `initContainers` section) ;
- think through what should happen if any of the apps is not healthy;
- etc...


How to follow the example:

0) Install docker (follow the official guide)
1) Install minikube (follow official guide)
    If you run into any issues I recommend installing minikube' dashboard for ease of debugging and overview.
2) Make sure you are not targetting production with kubectl (e.g. run kubectx)
3) Run local image registry 
 - https://minikube.sigs.k8s.io/docs/handbook/registry/#docker-on-macos
 - run `minikube addons enable registry`
 - run `minikube ip`
 - run `export MINIKUBE_IP=<>` and put ip from previous step there. I do this explicitly because output of my command had a section about running on M1 and thus spoiling the official guide.
 - run `docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:${MINIKUBE_IP}:5000"`
4) Build image
- run `docker build -t sidedemo .`
- run `docker tag sidedemo localhost:5000/sidedemo`
- run `docker push docker tag sidedemo localhost:5000/sidedemo`
5) Start the service
- run `kubectl apply -f my_demo.yaml`
- run `kubectl port-forward sidecar-python-demo 8080:80`

Now you should be able to open localhost:80. 
Good luck, sailor!

