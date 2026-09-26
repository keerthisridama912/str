from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Restaurant Online Booking API")


# Restaurant details
class Restaurant(BaseModel):
    name: str
    location: str
    tables: int


# Booking details
class Booking(BaseModel):
    customer_name: str
    restaurant_name: str
    date: str
    time: str
    guests: int


restaurants = [
    {
        "name": "Paradise Restaurant",
        "location": "Hyderabad",
        "tables": 20
    },
    {
        "name": "Bawarchi",
        "location": "Hyderabad",
        "tables": 15
    }
]

bookings = []


@app.get("/")
def home():
    return {"message": "Restaurant Online Booking API is running"}


@app.get("/restaurants")
def get_restaurants():
    return restaurants


@app.post("/restaurants")
def add_restaurant(restaurant: Restaurant):
    restaurants.append(restaurant.dict())
    return {
        "message": "Restaurant added successfully",
        "restaurant": restaurant
    }


@app.post("/bookings")
def create_booking(booking: Booking):
    bookings.append(booking.dict())

    return {
        "message": "Table booked successfully",
        "booking": booking
    }


@app.get("/bookings")
def get_bookings():
    return bookings


@app.delete("/bookings/{customer_name}")
def cancel_booking(customer_name: str):

    for booking in bookings:
        if booking["customer_name"] == customer_name:
            bookings.remove(booking)

            return {
                "message": "Booking cancelled successfully"
            }

    return {
        "message": "Booking not found"
    }