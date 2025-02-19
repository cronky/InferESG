# InferESG: AI-Augmented ESG Analysis

InferESG is an open-source solution that transforms how analysts interact with ESG (Environmental, Social, and Governance) data. Built upon the InferLLM framework, it helps combat greenwashing and validates ESG claims through AI-augmented analysis.

## 🎯 Mission

InferESG's mission is to augment ESG analysts' capabilities through intelligent automation while maintaining human expertise and judgment in the loop. Rather than attempting to automate the entire analysis process, InferESG serves as an intelligent assistant that augments human expertise through three key capabilities:

### 🔍 Comprehensive Report Analysis
- Thorough analysis of sustainability reports
- Step-by-step materiality assessment
- Examination of environmental targets, social initiatives, and governance structures
- Identification of both strong performance areas and potential concerns

### 💬 Interactive Investigation
- Natural language query interface for ESG data exploration
- Evidence-based responses through multi-agent framework
- Deep dive capabilities into areas of interest or concern
- Cross-referencing claims against external sources

### 📊 Evidence-Based Analysis
- Clear evidence trails for all conclusions
- Transparent verification paths
- Effective challenge processes
- Support for manual verification

## 🏗️ Technical Architecture

InferESG employs a sophisticated multi-agent architecture:

- Materiality Agent: Evaluates companies against established frameworks
- Report Agent: Coordinates comprehensive document analysis
- Web Agent: Validates claims against external sources
- Intent Agent: Processes and routes natural language queries
- Validator Agent: Improves response accuracy and completeness

## 🚀 Key Features

- Integration with key frameworks (TNFD, GRI)
- Materiality assessment capabilities
- Greenwashing detection
- Interactive query system
- Evidence trail generation
- Multi-source validation

## 📈 Validation & Testing

The system has been validated through rigorous testing:
- Testing across multiple industry sectors
- F1 score metrics for accuracy measurement
- Real-world validation with research industry sponsor
- Cross-validation using multiple AI systems and manual exploratory testing

## InferESG Roadmap & Docs
InferESG is based on InferGPT/LLM - more details below:

Want more context about how it works, our roadmap and documentation? Check out the [wiki](https://github.com/WaitThatShouldntWork/InferGPT/wiki)

For further reading on LLMs's components, see any of the following

- [Full system testing](test/README.md)
- [Data persistence](data/README.md)
- [Backend](backend/README.md)
- [Frontend](frontend/README.md)
- [Assets](assets/README.md)
- [Testing](test/README.md)
- [Financial Bot](financialhealthcheckScottLogic/README.md)

## Contribute
We welcome contributions from the community! Whether you're interested in:
- Enhancing the analysis capabilities
- Adding new materiality frameworks
- Improving the agent architecture
- Expanding validation capabilities
See [the contribution guide](CONTRIBUTING.md) for further guidance. Note this guide is in progress!

## Getting Started

In the top-right corner of the page, click Fork.

On the next page, select your GitHub account to create the fork under.
Wait for the forking process to complete. You now have a copy of the repository in your GitHub account.

### Clone the Repository

To clone the repository, you need to have Git installed on your system. Use the [official Git installer](https://git-scm.com/download/win) or [follow the terminal commands guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Once you have Git installed, follow these steps:

- Open your preferred terminal.
- Navigate to the directory where you want to clone the repository.
- Run the git clone command for the fork you just created.

### Initial configuration

There is a example property file `.env.example` at the root of this project.

Configuration steps:

- Copy the `.env.example` file at the root of this project.
- Rename the copied file as `.env`.
- Update the `.env` file with your wanted configuration following the guidance in the file.

### Running the application

There are a few ways to run the application:

1. **Docker Compose** - run the entire application within Docker containers configured by Docker Compose.
2. **Locally** - run local instances of the front-end, back-end and a neo4j database.
3. **Individual Docker Containers** - you may choose to run individual components within a Docker container.

For ease of use, we would recommended that you run the application using **Docker Compose**.

For instructions on how to run indivdual components locally or within Docker containers, refer to appropriate READMEs:

- [frontend README](frontend/README.md)
- [backend README](backend/README.md)
- [data README](data/README.md)

### Running with Docker Compose

- **Ensure Docker is installed and running**. The easiest way to do this is by using the Docker Desktop app (install it from [docker.com](docker.com) if you don't have it).
- In the root directory of the project run `docker compose up`
  > [!WARNING]  
  > the first time you do this it may take longer as the compose file builds the images.

> To re-build the docker images following any changes, run `docker compose build` first or use `docker compose up --build`.

For ease of development, after running `docker compose build` you can run `docker compose up --watch`. Watch mode allows for the docker container to rebuild when you save a file. This means that it is not required to take down the service after every change to see these implemented. This option is recommended.

- View the frontend at [localhost:8650](http://localhost:8650)
- View the Neo4j Browser at [localhost:7474](http://localhost:7474)
- Type the phrase "healthcheck" into the frontend UI to test if everything is connected successfully

### Usage

Coming

### LICENCE

See [LICENCE.md](LICENCE.md)
