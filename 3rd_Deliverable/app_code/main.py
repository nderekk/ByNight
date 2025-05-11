from app.controllers.view_res_controller import ViewReservationController
from app.views.customer_view_res import CustomerViewReservations
from datetime import datetime
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # vr_controller = ViewReservationController()
    # upcoming = vr_controller.get_upcoming_reservations_for_display(xx)

    upcoming = [
        ("Saint Club", datetime(2025, 5, 30, 0, 30), "123456789", "Kultura"),
    ]

    past = [
        ("Vibe Lounge", datetime(2025, 3, 20, 22, 0), "987654321", "Retro Night"),
        ("The Garden", datetime(2025, 2, 14, 20, 0), "456789123", "Valentine's Special"),
    ]

    window = CustomerViewReservations(upcoming, past)
    window.show()
    sys.exit(app.exec())