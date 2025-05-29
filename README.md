🌃 ByNight

Το ByNight είναι μια εφαρμογή για διαχείριση και αναζήτηση κρατήσεων σε νυχτερινά μαγαζιά.
Απευθύνεται τόσο σε  πελάτες όσο και σε  ιδιοκτήτες.

🙋‍♂️ Για Πελάτες

    🔎 Αναζήτηση και φιλτράρισμα μαγαζιών (📍 τοποθεσία, 🎵 μουσική, 🎫 events)

    🪑 Online κράτηση (τραπέζι, 👥 αριθμός ατόμων, 🍸 προτίμηση ποτών)

    ✏️ Τροποποίηση ή ❌ ακύρωση κράτησης

    📲 Check-in με QR Code για γρήγορη είσοδο

    ⭐ Αξιολόγηση μαγαζιών με σχόλια & βαθμολογία

🧑‍💼 Για Ιδιοκτήτες

    ➕ Προσθήκη & διαχείριση πληροφοριών (📍 τοποθεσία, ⏰ ωράριο, 🎤 εκδηλώσεις, 💰 τιμοκατάλογος)

    📊 Παρακολούθηση κρατήσεων & στατιστικών

    📅 Δημιουργία και διαχείριση εκδηλώσεων

## Project Structure

```
3rd_Deliverable/
└── app_code/
    ├── models/          # Data models and business objects
    ├── views/           # User interface components
    ├── controllers/     # Business logic and user input handling
    ├── services/        # Business services and operations
    ├── data/           # Data persistence and storage
    ├── utils/          # Utility functions and helpers
    ├── assets/         # Static resources (images, styles, etc.)
    └── main.py         # Application entry point
```

## Technology Stack

- **Language**: Python 3.x
- **GUI Framework**: PySide6
- **Database**: SQLite
- **Testing**: pytest

## Getting Started

1. Navigate to the project directory:
   ```bash
   cd 3rd_Deliverable/app_code
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

## Key Features

### For Customers
- Venue search and filtering by location, music, and events
- Online reservations with table selection and drink preferences
- Reservation modification and cancellation
- QR code check-in
- Venue ratings and reviews

### For Owners
- Venue information management (location, hours, events, menu)
- Reservation tracking and statistics
- Event management
