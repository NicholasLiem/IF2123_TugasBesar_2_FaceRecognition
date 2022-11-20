# Face Recognition Using Eigenface
>Tugas ini merupakan salah satu tugas besar matakuliah IF2123 Aljabar Linier dan Geometri yang berfokus pada pengaplikasian PCA (Principal Component Analysis) untuk mencari Eigenface yang kemudian akan digunakan untuk menentukan kemiripan suatu gambar (dalam kasus ini kemiripan muka, face recognition).

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)


## General Information
- Tugas ini merupakan salah satu bentuk pengaplikasian PCA (Principal Component Analysis) dan Eigenface yang memerlukan pemahaman mendalam tentang nilai eigen, vektor eigen, dan ruang eigen. Objektif dari tugas ini adalah untuk menentukan gambar pada database mana yang paling cocok dengan gambar uji.


## Technologies Used
- Python - version 3.10.6


## Dependencies
- Tkinter - pip install tk
- NumPy   - pip install numpy
- OpenCV  - pip install opencv-python


## Features
- Pencarian wajah tercocok berdasarkan gambar uji
- Pengambilan wajah melalui webcam dan pencarian gambar tercocok (Bonus)


## Screenshots
![Example screenshot](./img/screenshot.png)


## Setup
What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?
Proceed to describe how to install / setup one's local environment / get started with the project.


## Usage
How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here`


## Project Status
Project is: _complete_


## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Menurunkan pemrosesan pencocokan wajah dengan optimisasi algoritma QR untuk mencari vektor eigen.


## Acknowledgements
Give credit here.
- This project was inspired by...
- This project was based on [this tutorial](https://www.example.com).
- Many thanks to...
