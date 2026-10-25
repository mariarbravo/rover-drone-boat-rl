## Project Template: AI Algorithm Comparison

This repository serves as the template for your course project. Below is an explanation of the structure of the project and the purpose of each file. Your project must retain this basic structure. As you progress, you should add details about your specific project to this readme (e.g., Replace "This file will contain the implementations of the AI algorithms/agents used in your project" with "This file contains the implementations of the X, Y, and Z algorithms..."). 

---

## Repository Structure
The repository includes the following files:

### 1. `algorithms.py`  
This file will contain the implementations of the AI algorithms/agents used in your project.  
- Ensure your code is well-documented with comments explaining each algorithm.

### 2. `comparisons.py`  
This file will contain the code for performing comparisons between your selected algorithms.  
- The file should be able to perform **all comparisons** described in your report when executed.  
- **Recommended Feature:** Include a setting to run a subset of comparisons for testing purposes.  

### 3. `demo.py`  
This file will provide a brief demonstration of your project.

#### Submission Requirements:
- **Progress Report:** Demonstrate *random agents* attempting to solve each problem.  
- **Final Report:** Demonstrate *each algorithm* attempting to solve at least one problem.  

#### Guidelines for Demonstrations:
Keep the demonstrations concise but meaningful to highlight key behaviors. Some agent types (e.g., random agents) may struggle or fail to solve a problem. Some problems may take a long time to complete (e.g., a full game of chess). In such cases, you should cut off the demonstration after a representative sample of the agent's behavior and problem mechanics has been shown. 

### 4. `problems.py`  
This file will contain the implementation of the problems you are solving with your AI algorithms.  
- Ensure that the problems are clearly defined and modular, so the algorithms can be easily tested on each.  
- For the **progress report**, this file should be fully implemented and require no major edits afterward.

---

## Instructions for Students

### Step 0: Prepare Python Environment
These instructions will setup the evaluation environment we will use to evaluate your project. Use this environment (without addition or modification) to make sure your code will run the same on our machines.
- Download and install [Anaconda](https://www.anaconda.com/download)
- Open Terminal (or Anaconda prompt in Windows)
- `conda create --name evalenv python=3.9`
- `conda activate evalenv`
- `pip install --upgrade pip`
- `pip install -r requirements.txt`

### Step 1: Clone the Repository
Click the green "Use this template" button in the upper right, and create your own copy of the repository. Next, clone your new repository to your local machine:  
```
git clone <your_repo>
```
Test your repository/environment:  
- Open Terminal (or Anaconda prompt in Windows)
- `conda activate evalenv`
- Open project directory: `cd <your_directory>`
- `python demo.py`
  
### Step 2: Code Your Project
- Define your problems in [`problems.py`](./problems.py).
- Implement your algorithms in [`algorithms.py`](./algorithms.py).
- Write the comparison logic in [`comparisons.py`](./comparisons.py).
- Create the demonstrations in [`demo.py`](./demo.py).

For detailed instructions, refer to "Course Project Instructions" under "Content" on the D2L page.

### Step 3: Commit Regularly
- Ensure at least 10 commits are made BEFORE the progress report submission deadline.
- Ensure at least 10 commits are made AFTER the progress report submission deadline.
- Make detailed commit messages describing what was added or changed.
