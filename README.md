ByNight

Το ByNight είναι μια εφαρμογή διαχείρισης και αναζήτησης κρατήσεων για νυχτερινά μαγαζιά, η οποία απευθύνεται τόσο στους πελάτες όσο και στους ιδιοκτήτες.

Βασικές Λειτουργίες

#Για πελάτες

-Αναζήτηση και φιλτράρισμα μαγαζιών με βάση τοποθεσία, μουσική και events.

-Online κράτηση με επιλογή τραπεζιού, αριθμού ατόμων και προτιμώμενων ποτών.

-Δυνατότητα τροποποίησης ή ακύρωσης κράτησης.

-Check-in μέσω QR Code για γρήγορη είσοδο.

-Αξιολόγηση μαγαζιών με σχόλια και βαθμολογία(αστεράκια).


#Για Ιδιοκτήτες

-Προσθήκη και διαχείριση πληροφοριών μαγαζιού όπως τοποθεσία, ωράριο, εκδηλώσεις, και τιμοκατάλογος.

-Παρακολούθηση κρατήσεων και στατιστικών.

-Προσθήκη και διαχείριση εκδηλώσεων.

Project Structure

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

## Getting Started

1. Navigate to the project directory:
   ```bash
   cd /app_code
   ```

2. Create a virtual environment (if you want):
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
# Test Users

# Managers
-email: papadopoulos@ceid.gr
-password: password

-email: georgiou@ceid.gr
-password: password

-email: ioannou@ceid.gr
-password: password

-email: toulas@ceid.gr
-password: slet

-email: sioufas@ceid.gr
-password: slet

# Customer
-email: papadopoulos@ceid.gr
-password: slet

-email: gavrilidis@ceid.gr
-password: slet

-email: farmakis@ceid.gr
-password: slet

# Staff
-email: giparis@ceid.gr
-password: slet

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
