# private-blockchain
Blockchain Implementation in python using Flask for setting up the node. I am using Proof of Work as the consensus protocol. There's a blockchain API which works as the interface to interact with the blockchain. You can make GET and POST requests to the node. 

# Inspiration
I have been actively involved in the blockchain community for quite some time. To look at blockchain from a technical perspective and learn how it works ground up, I worked on this project. I would like to thank Daniel for this article here:https://hackernoon.com/learn-blockchains-by-building-one-117428612f46 which helped me throughout the process. 

# How to run it?
You can run the flask app by simply running ``` python node.py```. This basically runs a flask server as a node on the blockchain, and there's blockchain interface with the API. 

# Blockchain API
Once the Flask node is running, we can start making requests. Here's a list of interfaces available:
- /mine (GET) : This is uses to mine the block with current transactions
- /transactions/new (POST): This is used to post a new transaction to the block. 
- /nodes/register (POST): This is used to register new nodes/ nodes which are part of the network
- /nodes/resolve (GET): This looks at the nodes in the network and resolves itself. 
- /chain (GET): This is used to get the entire blockchain info

# DEMO
So, for a demo, these are the steps that could be followed. You can clone the repo first and then cd into the directory

## First Setting up the Environment - (Using conda here) <br>
```conda env create --name private-blockchain --file environment.yml```<br>
## Activating Environment <br>
``` source activate private-blockchain``` <br>
## Running the blockchain node <br>
``` python node.py``` <br>
## Adding transaction to the node - ( I am using curl for this) <br>
``` curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5000/transactions/new" 
``` 
### We can run the step above multiple times <br>
### Now we mine the block <br>
```curl http://localhost:5000/mine``` <br>
### Now we can look at the blockchain
``` curl "http://localhost:5000/chain ```


