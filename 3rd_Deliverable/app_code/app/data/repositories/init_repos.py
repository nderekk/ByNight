from app.data.repositories.reservation_respository import ReservationRepository
from app.data.repositories.user_repository import UserRepository
from app.data.repositories.club_repository import ClubRepository
from app.utils.container import Container

class InitRepos():
  def __init__(self):
    Container.register(UserRepository, UserRepository)
    Container.register(ReservationRepository, ReservationRepository)
    Container.register(ClubRepository, ClubRepository)