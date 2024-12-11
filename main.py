#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 04:48:37 2024

@author: kirill_falaleev
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Модели данных
class Car(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    price: float

# Хранилище автомобилей
cars_db = []

# Эндпоинт для создания автомобиля
@app.post("/cars", response_model=Car)
def create_car(car: Car):
    cars_db.append(car)
    return car

# Эндпоинт для получения списка всех автомобилей
@app.get("/cars", response_model=List[Car])
def get_cars():
    return cars_db

# Эндпоинт для получения информации о конкретном автомобиле
@app.get("/cars/{car_id}", response_model=Car)
def get_car(car_id: int):
    for car in cars_db:
        if car.id == car_id:
            return car
    raise HTTPException(status_code=404, detail="Car not found")

# Эндпоинт для обновления данных автомобиля
@app.put("/cars/{car_id}", response_model=Car)
def update_car(car_id: int, car: Car):
    for idx, existing_car in enumerate(cars_db):
        if existing_car.id == car_id:
            cars_db[idx] = car
            return car
    raise HTTPException(status_code=404, detail="Car not found")

# Эндпоинт для удаления автомобиля
@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    for idx, car in enumerate(cars_db):
        if car.id == car_id:
            del cars_db[idx]
            return {"detail": "Car deleted"}
    raise HTTPException(status_code=404, detail="Car not found")
