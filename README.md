# Ticket Price Tracker – Architecture Comparison Project

CS 5319 – Software Architecture and Design  
Final Project Group 12– Victoria Valdez and Elizabeth Larez Diaz  
**Selected Architecture:** Client–Server  
**Unselected Architecture:** Event-Based (Pub/Sub)

---

## 1. Team & Roles

### **Victoria Valdez — Implementation & Demo Lead**  
Responsible for all executable and technical deliverables:
- Implemented Architecture Option 1 prototype (Client–Server)
- Implemented Architecture Option 2 prototype (Event-Based / Pub-Sub)
- Ensured both versions compiled and executed successfully
- Collected execution screenshots
- Created step-by-step demo sequence
- Recorded demo portion for presentation
- Organized GitHub repository structure

### **Elizabeth Larez Diaz — Architecture & Design Lead**  
Responsible for conceptual and documentation deliverables:
- System description & overview
- Architecture Option 1 diagrams (Client–Server)
- Architecture Option 2 diagrams (Event-Based)
- Component-to-class mapping tables
- Pros/Cons comparison
- Final rationale for selected architecture
- Risk analysis
- Full README documentation

---

## 2. Project Overview

The **Ticket Price Tracker** is a simple backend service that allows users to:

- View available concerts  
- Track concerts of interest  
- Simulate ticket price drops  
- Receive alerts when tracked concerts become cheaper  

The system is implemented twice using two architectural styles:

1. **Client–Server architecture** (Selected)  
2. **Event-Based Publish/Subscribe architecture** (Unselected)

This project compares these architectures, analyzes tradeoffs, and justifies the final choice.

---

## 3. Technology Stack & Platform Setup

### **3.1 Language & Frameworks**
- Python 3.10+ (tested on Python 3.13)
- FastAPI
- Uvicorn (ASGI server)
- macOS development environment (compatible with Windows & Linux)

### **3.2 Installing Python**
Download from:  
https://www.python.org/downloads/

Verify installation:

```
python3 --version
```

---

## 4. Environment Setup (Compilation Equivalent)

Python compiles at runtime, so setup = "compilation."

### **4.1 Create Virtual Environment**
```
python3 -m venv venv
```

### **4.2 Activate Environment**
macOS/Linux:
```
source venv/bin/activate
```
Windows:
```
venv\Scripts\activate
```

### **4.3 Install Dependencies**
```
pip install fastapi "uvicorn[standard]" pydantic
```

(Optional)
```
pip freeze > requirements.txt
```

---

## 5. Repository Structure

```
.
├── Selected/
│   └── client_server/
│       └── backend/
│           └── main.py
│
├── Unselected/
│   └── event_based/
│       ├── main.py
│       └── services/
│           ├── event_bus.py
│           ├── price_fetcher.py
│           └── notifier.py
│
└── README.md
```

- **Selected** contains code for the chosen architecture  
- **Unselected** contains the alternate prototype

---

## 6. How to Run Both Architectures (TA QUICK GUIDE)

### For Client–Server:

```
1. source venv/bin/activate
2. cd Selected/client_server/backend
3. uvicorn main:app --reload
4. Open http://127.0.0.1:8000/docs
5. Run:
   - GET /concerts
   - POST /track
   - GET /tracked
   - POST /simulate_price_drop/{concert_id}
```

---

### For Event-Based:

```
1. source venv/bin/activate
2. cd Unselected/event_based
3. uvicorn main:app --reload
4. Open http://127.0.0.1:8000/docs
5. Run:
   - GET /concerts
   - POST /price_change
   - GET /alerts
```

---

## 7. Architecture Designs – Differences & Analysis

### **7.1 Client–Server Architecture (Selected)**

**Characteristics**
- Request/response model
- All logic handled in a single server
- In-memory state stored in dictionaries
- Tight coupling between client and server
- Immediate synchronous responses

**Key Components**
- Server API (`main.py`)
- Routes: `/concerts`, `/track`, `/tracked`, `/simulate_price_drop`
- State: `CONCERTS`, `TRACKED`
- Logic in endpoint handlers

**Connector:** HTTP/REST  
**Control Flow:** Client → Server → Response

---

### **7.2 Event-Based Architecture (Unselected)**

**Characteristics**
- API Gateway receives user actions
- Price changes become **events**
- Events published to **EventBus**
- Subscribers (Notifier) handle events asynchronously
- Loosely coupled components

**Key Components**
- API Gateway (`main.py`)
- EventBus (`event_bus.py`)
- Publisher (`price_fetcher.py`)
- Subscriber (`notifier.py`)

**Connector:** Publish–Subscribe event bus  
**Control Flow:** Client → Gateway → EventBus → Subscribers

---

## 8. Side-by-Side Comparison

| Category | Client–Server (Selected) | Event-Based (Unselected) |
|---------|---------------------------|---------------------------|
| Communication | Request/Response | Publish–Subscribe |
| Coupling | Tight | Loose |
| Architecture Complexity | Low | Moderate |
| Scalability | Moderate | High |
| Components | Single server | Gateway, Bus, Publisher, Subscribers |
| Best Fit | Small synchronous apps | Distributed or asynchronous apps |

---

## 9. Component-to-Code Mapping

### **Client–Server Mapping**

| Component | Code |
|----------|------|
| Client (UI) | Swagger UI |
| Server | Selected/client_server/backend/main.py |
| Concert Repository | `CONCERTS` dict |
| Tracking Manager | `TRACKED` dict |
| Logic Layer | Endpoint handlers |

---

### **Event-Based Mapping**

| Component | Code |
|----------|------|
| API Gateway | Unselected/event_based/main.py |
| Event Bus | services/event_bus.py |
| Publisher | services/price_fetcher.py |
| Subscriber | services/notifier.py |

---

## 10. Rationale for Selected Architecture

We selected the **Client–Server architecture** because:

- It is the simplest architecture that satisfies all requirements  
- It aligns with synchronous user actions (price checking, tracking)  
- Lower overhead makes it ideal for academic demonstration  
- Easy to run, grade, and extend  
- No need for distributed event pipelines for the current scale  

The Event-Based model is more flexible but unnecessarily complex for this system.

---

## 11. Changes from Original Project Proposal

We **kept the same two candidate architectures**, but refined them:

- Clarified component roles after proposal feedback  
- Added clean separation for EventBus, publisher, subscriber modules  
- Improved mapping tables and diagrams  
- Ensured both architectures are runnable and consistent  

All changes have been documented in this README.

---

## 12. Additional Notes for the TA

- No external databases, brokers, or dependencies are required  
- Everything runs locally with Python + FastAPI + Uvicorn  
- All state is in-memory and resets on restart  
- Swagger documentation is automatically available at `/docs`  
- Both architectures have been tested end-to-end  

---

## 13. TA Quick-Run Summary

```
git clone <repo>
cd repo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Run Client–Server**
```
cd Selected/client_server/backend
uvicorn main:app --reload
```

**Run Event-Based**
```
cd Unselected/event_based
uvicorn api_gateway.main:app --reload
```

