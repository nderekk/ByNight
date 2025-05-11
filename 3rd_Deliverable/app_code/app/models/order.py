class Order:
  def __init__(self, id: int, cost: float, delivered: bool, paid: bool):
    self.id = id
    self.cost = cost
    self.delivered = delivered
    self.paid = paid