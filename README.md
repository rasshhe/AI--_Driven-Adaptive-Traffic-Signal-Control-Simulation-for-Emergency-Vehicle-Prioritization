
}
# AI-Driven Adaptive Traffic Signal Control for Emergency Vehicle Prioritization

## Overview
This project simulates an intelligent traffic signal control system that prioritizes emergency vehicles such as ambulances, fire trucks, and police vehicles. The system uses computer vision and a priority-based scheduling algorithm to dynamically decide which lane should receive the green signal.

The goal is to reduce emergency response delays while maintaining fairness among normal traffic lanes.

## Key Features
- Vehicle detection using YOLO
- Traffic density estimation per lane
- Emergency vehicle prioritization
- Dynamic traffic signal decision
- Modular system architecture

## System Architecture
Traffic Frame  
↓  
Vehicle Detection (YOLO)  
↓  
Lane Division  
↓  
Vehicle Count per Lane  
↓  
Density Calculation  
↓  
Emergency Vehicle Detection  
↓  
Priority Scheduling Algorithm  
↓  
Traffic Signal Decision

## Datasets
This project uses:
- UA-DETRAC traffic vehicle dataset
- Emergency vehicle detection dataset from Roboflow

Datasets are not stored in the repository and are downloaded dynamically using the Roboflow API.

## Technologies Used
- Python
- OpenCV
- Ultralytics YOLOv8
- Roboflow
- Google Colab

## Project Structure
modules/ – core system modules  
datasets/ – dataset loader and documentation  
notebooks/ – Colab notebook for demonstration  
main_pipeline.py – integrates all modules

## Future Improvements
- Real-time traffic camera integration
- Multi-intersection coordination
- Reinforcement learning based signal optimization
- Smart city deploymen
