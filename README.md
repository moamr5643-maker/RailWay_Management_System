# RailWay_Management_System

This Railway Management System is a console-based Python application designed to manage trains, bookings, and seat availability efficiently. It simulates key functionalities of a real-world railway system, allowing users to add trains, book or cancel tickets, search trains by ID, and remove trains from the system.

---

## Features

**Train Management:**  
Easily add and organize trains using unique IDs, names, and seat counts. The system keeps track of booked and available seats to simplify train management.

**Search Functionality:**  
- **Search by ID:** Quickly locate a train using its unique identifier.  

**Booking & Cancellation:**  
- **Book a Ticket:** Users can book tickets based on train ID. The system ensures that no more tickets can be booked than available seats.  
- **Cancel a Ticket:** Users can cancel booked tickets, freeing up seats for future bookings.  

**Seat Availability Tracking:**  
Each train's seat availability is dynamically updated, making it easy to track which seats are booked and which are free.

---

## Technical Highlights

**Data Structures:**  
The system uses Python lists to manage multiple train objects efficiently.

**Object-Oriented Programming (OOP):**  
- **Encapsulation:** Each train is represented as an object containing its name, ID, total seats, and booked seats.  
- **Modularity:** Train and Railway System functionalities are separated into different classes (`Train` and `RailWayManagementSystem`) for maintainability and extensibility.  

**User Interaction:**  
A simple, interactive console menu allows users to navigate through functionalities like adding trains, viewing trains, booking, canceling, searching, and removing trains with ease.

---

## Future Improvements

- Add support for **saving and loading data** to files for persistence between program runs.  
- Integrate a **Graphical User Interface (GUI)** for a more interactive experience.  
- Implement **train categorization** by type, route, or time.  
- Add **user registration and authentication** for personalized booking experience.  
