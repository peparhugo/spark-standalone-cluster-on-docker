# Take Home Assignment

This repo is a clone of this [repo](https://github.com/cluster-apps-on-docker/spark-standalone-cluster-on-docker) and 
was selected because it runs a Spark Standalone cluster on Docker.


## Assignment Directory Structure
    .
    ├── ...
    ├── take-home-assigment  # assignment directory
    │   ├── bin          # shell scripts to run jobs
    │   ├── data         # storage for data files
    │   ├── scripts      # source script files
    |   |   ├── helpers     # helper functions (there may be no helper functions depending on the assignment)
    |   |   ├── notebooks   # development notebooks
    │   └── tests        # tests (there may be no tests depending on length of the assignment)
    └── ...

## Deploying and Un-deploying

To deploy the docker containers, run from the project root directory:
```
sh take-home-assignment/bin/deploy.sh
```
This deployment script will launch a spark cluster with 2 worker nodes. Ideally, the deployment script would take
a scale argument and would be able to deploy more than one configuration but I felt this was outside the scope of the 
assigment.

To un-deploy the docker containers, run from the project root directory:
```
sh take-home-assignment/bin/undeploy.sh
```

## Development

Once the docker containers are deployed, you can go to [JupyterLab](http://0.0.0.0:8888/lab?) to develop in Python, 
Scala or R. I used jupyter notebooks to iteratively develop the scripts for the assigment.

See take-home-assignment/scripts/notebooks/de-weather-challenge-20200903.ipynb

## Pipeline Scripts

These files are saved in the `take-home-assignment/scripts` directory.

## Running Pipeline Scripts

Pipeline scripts are run by sending docker exec commands to the `jupyterlab` container. This is fine for a local 
development but in a production environment the scripts should be run using `./bin/spark-submit`. For ease of not over 
building the solution of the assigment, I left it to run the spark job via the `jupyterlab` container.


To launch pipeline scripts, run from the project root directory:
```
sh take-home-assignment/bin/<run script name>.sh
```

Example:

To run the example pipeline provided, run the following from the project root directory:
```
sh take-home-assignment/bin/run-example.sh
```


### End of assignment
#
# Original Read Me
# Apache Spark Standalone Cluster on Docker

> The project just got its [own article](https://towardsdatascience.com/apache-spark-cluster-on-docker-ft-a-juyterlab-interface-418383c95445) at Towards Data Science Medium blog! :sparkles:

This project gives you an **Apache Spark** cluster in standalone mode with a **JupyterLab** interface built on top of **Docker**.
Learn Apache Spark through its **Scala**, **Python** (PySpark) and **R** (SparkR) API by running the Jupyter [notebooks](build/workspace/) with examples on how to read, process and write data.

<p align="center"><img src="docs/image/cluster-architecture.png"></p>

![build](https://github.com/andre-marcos-perez/spark-standalone-cluster-on-docker/workflows/build/badge.svg?branch=master)
![jupyterlab-latest-version](https://img.shields.io/docker/v/andreper/jupyterlab/2.1.4-spark-3.0.0?color=yellow&label=jupyterlab-latest)
![spark-latest-version](https://img.shields.io/docker/v/andreper/spark-master/3.0.0-hadoop-2.7?color=yellow&label=spark-latest)
![docker-version](https://img.shields.io/badge/docker-v1.13.0%2B-blue)
![docker-compose-file-version](https://img.shields.io/badge/docker--compose-v1.10.0%2B-blue)
![spark-scala-api](https://img.shields.io/badge/spark%20api-scala-red)
![spark-pyspark-api](https://img.shields.io/badge/spark%20api-pyspark-red)
![spark-sparkr-api](https://img.shields.io/badge/spark%20api-sparkr-red)

## TL;DR

```bash
curl -LO https://raw.githubusercontent.com/andre-marcos-perez/spark-standalone-cluster-on-docker/master/docker-compose.yml
docker-compose up
```

## Contents

- [Quick Start](#quick-start)
- [Tech Stack](#tech-stack)
- [Docker Hub Metrics](#docker-hub-metrics)
- [Contributing](#contributing)
- [Contributors](#contributors)

## <a name="quick-start"></a>Quick Start

### Cluster overview

| Application            | URL                                      | Description                                                |
| ---------------------- | ---------------------------------------- | ---------------------------------------------------------- |
| JupyterLab             | [localhost:8888](http://localhost:8888/) | Cluster interface with built-in Jupyter notebooks          |
| Apache Spark Master    | [localhost:8080](http://localhost:8080/) | Spark Master node                                          |
| Apache Spark Worker I  | [localhost:8081](http://localhost:8081/) | Spark Worker node with 1 core and 512m of memory (default) |
| Apache Spark Worker II | [localhost:8082](http://localhost:8082/) | Spark Worker node with 1 core and 512m of memory (default) |

### Prerequisites

 - Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/), check **infra** [supported versions](#tech-stack)

### Build from Docker Hub

1. Download the source code or clone the repository;
2. Edit the [docker compose](docker-compose.yml) file with your favorite tech stack version, check **apps** [supported versions](#tech-stack);
3. Build the cluster;

```bash
docker-compose up
```

4. Run Apache Spark code using the provided Jupyter [notebooks](build/workspace/) with Scala, PySpark and SparkR examples;
5. Stop the cluster by typing `ctrl+c`.

### Build from your local machine

> **Note**: Local build is currently only supported on Linux OS distributions.

1. Download the source code or clone the repository;
2. Move to the build directory;

```bash
cd build
```

3. Edit the [build.yml](build/build.yml) file with your favorite tech stack version;
4. Match those version on the [docker compose](build/docker-compose.yml) file;
5. Build the images;

```bash
chmod +x build.sh ; ./build.sh
```

6. Build the cluster;

```bash
docker-compose up
```

7. Run Apache Spark code using the provided Jupyter [notebooks](build/workspace/) with Scala, PySpark and SparkR examples;
8. Stop the cluster by typing `ctrl+c`.

## <a name="tech-stack"></a>Tech Stack

- Infrastructure

| Component      | Version |
| -------------- | ------- |
| Docker Engine  | 1.13.0+ |
| Docker Compose | 1.10.0+ |
| Python         | 3.7.3   |
| Scala          | 2.12.11 |
| R              | 3.5.2   |

- Jupyter Kernels

| Component      | Version | Provider                                |
| -------------- | ------- | --------------------------------------- |
| Python         | 2.1.4   | [Jupyter](https://jupyter.org/)         |
| Scala          | 0.10.0  | [Almond](https://almond.sh/)            |
| R              | 1.1.1   | [IRkernel](https://irkernel.github.io/) |

- Applications

| Component      | Version                 | Docker Tag                                           |
| -------------- | ----------------------  | ---------------------------------------------------- |
| Apache Spark   | 2.4.0 \| 2.4.4 \| 3.0.0 | **\<spark-version>**-hadoop-2.7                      |
| JupyterLab     | 2.1.4                   | **\<jupyterlab-version>**-spark-**\<spark-version>** |

> Apache Spark R API (SparkR) is only supported on version **2.4.4**. Full list can be found [here](https://cran.r-project.org/src/contrib/Archive/SparkR/).

## <a name="docker-hub-metrics"></a>Docker Hub Metrics

| Image                                                          | Size                                                                                           | Downloads                                                                 |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [JupyterLab](https://hub.docker.com/r/andreper/jupyterlab)     | ![docker-size-jupyterlab](https://img.shields.io/docker/image-size/andreper/jupyterlab/latest) | ![docker-pull](https://img.shields.io/docker/pulls/andreper/jupyterlab)   |
| [Spark Master](https://hub.docker.com/r/andreper/spark-master) | ![docker-size-master](https://img.shields.io/docker/image-size/andreper/spark-master/latest)   | ![docker-pull](https://img.shields.io/docker/pulls/andreper/spark-master) |
| [Spark Worker](https://hub.docker.com/r/andreper/spark-worker) | ![docker-size-worker](https://img.shields.io/docker/image-size/andreper/spark-worker/latest)   | ![docker-pull](https://img.shields.io/docker/pulls/andreper/spark-worker) |

## <a name="contributing"></a>Contributing

We'd love some help. To contribute, please read [this file](CONTRIBUTING.md).

> Staring us on GitHub is also an awesome way to show your support :star:

## <a name="contributors"></a>Contributors

 - **André Perez** - [dekoperez](https://twitter.com/dekoperez) - andre.marcos.perez@gmail.com
