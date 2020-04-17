## Overview

Allows you to search on Twitter. The search returns 100 "last" tweets max.
You can easily search tweets, including the text you are looking for.

## Benefits 

* Make it easier to something on Twitter.

* Provide an interface.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

- Rename the config-template.py file to config.py
- Put the right parameters in the config.py file

### Prerequisites

* Windows 7+ or Linux kernel version 3.10 or higher
* 2.00 GB of RAM
* 3.00 GB of available disk space

Use with Docker http://www.docker.io

### Installation

To build an image with docker is pretty simple:
```
docker build -t search-tweets .
```

## Running the tests

Then to run that image and attach to it at the same time:
```
docker run -p 5000:5000 search-tweets
```

Go to your web browser: http://localhost:5000/
