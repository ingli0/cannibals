# cannibals
Assignment for the subject of Artificial Intelligence 
# Cannibals and Missionaries Problem Solver

This repository contains a Python program that solves the Cannibals and Missionaries problem using a breadth-first search algorithm.

## Problem Description

In this problem, there are three cannibals and three missionaries on one side of a river. They need to cross the river to the other side using a boat. However, there are certain rules that must be followed:

- The boat can carry either one or two individuals.
- The cannibals should never outnumber the missionaries on either side of the river, otherwise the cannibals will eat the missionaries.
- At all times, there should be an equal or greater number of missionaries than cannibals on both sides of the river.

The goal is to find a sequence of boat trips that allows all individuals to safely cross the river.

## Program Description

The program (`canibals.py`) implements a solution to the problem using a breadth-first search algorithm. It defines several functions to check the validity of states, generate valid moves, and find a solution through iterative search.

To use the program, you can run it with Python. The initial state is set to 3 cannibals and 3 missionaries on the starting bank. The program will print the sequence of moves needed to solve the problem if a solution is found, or it will indicate if no solution was found.

## output
![image](https://github.com/ingli0/cannibals/assets/76855285/e8636145-00b7-4da9-ae39-98cc4011f450)
![image](https://github.com/ingli0/cannibals/assets/76855285/2898f6c0-cfaf-4806-a2d2-8fed6d4e638f)
![image](https://github.com/ingli0/cannibals/assets/76855285/9ffb1099-71c7-411a-954a-a07c9ad130fe)
