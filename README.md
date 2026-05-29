# AI Assignment 5
This repository contains four Artificial Intelligence assignments covering search algorithms, knowledge-based systems, knowledge graphs, and probabilistic reasoning.

Each assignment includes source code, documentation, demonstrations, and reports explaining the implementation and underlying concepts.

---

## Projects

### 1. Game Search Algorithms

Implementation and comparison of classical game-tree search techniques using Tic-Tac-Toe.

Algorithms implemented:

* Minimax Search
* Alpha-Beta Pruning
* Heuristic Alpha-Beta Search
* Monte-Carlo Tree Search (MCTS)

Features:

* Common game framework
* Tic-Tac-Toe environment
* Algorithm comparison
* Demonstration of optimal move selection
* Test cases

Project Folder:

```text
AI_Search_Algorithms/
```

---

### 2. AI Travel Planner

A knowledge-based travel recommendation system that generates personalized itineraries using predefined travel knowledge bases.

Features:

* Tourist place recommendations
* Food recommendations
* Personalized tour planning
* Budget estimation
* Day-wise itinerary generation

Project Folder:

```text
AI_Travel_Planner/
```

---

### 3. Knowledge Graphs

Exploration of Knowledge Graph concepts, RDF triples, ontologies, and tools used for constructing Knowledge Graphs.

Includes:

* Knowledge Graph demonstration
* Triple-based knowledge representation
* Querying relationships between entities
* Study of popular Knowledge Graph tools

Tools discussed:

* Neo4j
* Protégé
* Apache Jena
* GraphDB
* RDF4J

Project Folder:

```text
Knowledge_Graphs/
```

---

### 4. Bayesian Networks

Implementation of a simple Bayesian Network demonstrating probabilistic modelling and inference.

Example Network:

```text
Rain ------\
             ---> Wet Grass
Sprinkler --/
```

Features:

* Probabilistic modelling
* Conditional Probability Tables (CPTs)
* Bayesian inference
* Posterior probability computation

Project Folder:

```text
Bayesian_Networks/
```

---

## Repository Structure

```text
AI_Assignment5/
│
├── AI_Search_Algorithms/
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── minimax.py
│   │   ├── alpha_beta.py
│   │   ├── heuristic_alpha_beta.py
│   │   └── mcts.py
│   │
│   ├── games/
│   │   ├── __init__.py
│   │   ├── game.py
│   │   ├── tic_tac_toe.py
│   │   └── display.py
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_minimax.py
│   │   ├── test_alpha_beta.py
│   │   ├── test_heuristic_alpha_beta.py
│   │   └── test_mcts.py
│   │
│   ├── docs/
│   │   └── report1.pdf
│   │
│   └── main.py
│
├── AI_Travel_Planner/
│   │
│   ├── knowledge_base/
│   │   ├── __init__.py
│   │   ├── places.py
│   │   ├── food.py
│   │   └── budgets.py
│   │
│   ├── planner/
│   │   ├── __init__.py
│   │   ├── recommender.py
│   │   └── itinerary.py
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_planner.py
│   │
│   ├── docs/
│   │   └── report2.pdf
│   │
│   └── main.py
│
├── Knowledge_Graphs/
│   │
│   ├── kg/
│   │   ├── __init__.py
│   │   ├── graph.py
│   │   └── sample_data.py
│   │
│   ├── docs/
│   │   └── report3.pdf
│   │
│   └── main.py
│
├── Bayesian_Networks/
│   │
│   ├── bayes/
│   │   ├── __init__.py
│   │   ├── network.py
│   │   └── inference.py
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_inference.py
│   │
│   ├── docs/
│   │   └── report4.pdf
│   │
│   └── main.py
│
├── README.md
└── requirements.txt
```

---

## Technologies Used

* Python 3
* Object-Oriented Programming
* Knowledge-Based Systems
* Knowledge Graphs
* Bayesian Networks
* Search Algorithms

---

## Running the Projects

Navigate to the desired project directory and execute:

```bash
py main.py
```

Most projects use only Python's standard library and do not require additional dependencies.

---

## Documentation

Each project contains its own report under the corresponding `docs/` directory.

For implementation details, methodology, results, and discussion, refer to the project-specific reports.

---

