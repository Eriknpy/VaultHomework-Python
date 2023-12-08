<!-- Top of your README.md -->
<a name="top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a><img src="https://i.imgur.com/dZVNWFP.png" alt="Logo" width="80" height="80"></a>

 ######  <h3 align="center">Vault Homework in Python</h3>

  <p align="center">
    Well-documented FP console app to solve an algorithm
    <br />
    <a href="https://i.imgur.com/4UYAoUO.png"><strong>Codecoverage </strong></a>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-solution">About The Solution</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#python-unittest-test">Python unittest Test</a></li>
    <li><a href="#code-coverage">Code coverage</a></li>
  </ol>
</details>

<!--About The Solution -->
## About The Solution

I used Functional Programming this time. There are two different approaches to coding:
* General: The least language-specific approach
* Python specific: Comprehensions

Each approach solves the algorithmical part in 3 steps. For better understanding I created a diagram.
<div align="center">
  <a><img src="https://i.imgur.com/LwSPDSU.png" alt="Logo" ></a>
</div>
<p align="center">
    <strong>Flow diagram</strong><br>
    (click to zoom)</a>

<!-- GETTING STARTED -->
## Getting Started

There are two recommended ways to run this project.
* Run the project from your IDE
* You can also add your input.txt:
        1. Go to the VaultHomework folder where main.py is located and add your file.
    2. Specify the file location with CLI:
     ```sh
     dotnet run yourfilename.txt
     ```
* Docker container: Navigate to the root folder of the repo where Dockerfile is located.
1. Build the docker image: 
    ```sh
    docker build -t vaulthomework .
    ```
2. Run the docker container:
    ```sh
    docker run --rm vaulthomework
    ```

<!-- Code coverage -->
### Code coverage 
* Manually opening from your local env. <a href="https://i.imgur.com/4UYAoUO.png">» VaultHomework/htmlcov/index.html</a>
* How to generate a new report?
1. Generate coverage data:
    ```sh
    python -m coverage run -m unittest
    ```
2. Coverage data into report:

    ```sh
    python -m coverage report
    ```
3. Generate Code coverage as html:
    ```sh
    python -m coverage html 
    ```

<!-- Python unittest Test -->
### Python unittest Test

In total, there are 11 unit tests.
<p align="right">(<a href="#vault-homework-in-python">back to top</a>)</p>

