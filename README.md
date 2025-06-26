# Smart Healthcare Appointment Scheduler (Optimized)

This project implements an **optimized appointment scheduler** for smart healthcare environments. It uses a **greedy approach** to assign patients to doctors, trying to reduce waiting times by always allocating the earliest available slot.

---

## ✅ Features
- Greedy logic: Assigns patients to earliest available time slot per doctor
- Simple and customizable Python code
- Extendable with advanced optimization (e.g. Genetic Algorithm, PSO)
- Prints a full schedule for patients and doctors

---

## 🧠 How it works
Each doctor has their own list of available time slots. The scheduler:
1. Iterates through patients
2. Finds the doctor with the most available time slots
3. Assigns the earliest slot to the patient
4. Removes that slot from the doctor’s availability

This simulates real-world scheduling logic while remaining simple.

---

## 🚀 How to Run

1. Clone or download the repository  
2. Run the script using Python:

```bash
python scheduler.py
```

---

## 🖥️ Example Output
```
Optimized Smart Healthcare Appointment Schedule:
Alice -> Dr. Smith at 09:00
Bob -> Dr. Lee at 09:00
Charlie -> Dr. Smith at 09:30
Diana -> Dr. Lee at 09:30
...
```

---

## 🔧 Future Improvements
- Replace greedy logic with Genetic Algorithm or Particle Swarm Optimization
- Add user interface (CLI or Web via Flask)
- Load patient data from real sources (CSV/DB)

---

## 📄 License
MIT License
