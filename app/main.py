class Distance:
    def __init__(self, km: float):
        self.km = km

    def __str__(self):
        value = self.km
        if isinstance(value, float) and value.is_integer():
            value = int(value)
        return f"Distance: {value} kilometers."

    def __repr__(self):
        val = self.km
        if isinstance(val, float) and val.is_integer():
            val = int(val)
        return f"Distance(km={val})"

    def __add__(self, other):
        if isinstance(other, Distance):
            total_km = self.km + other.km
        elif isinstance(other, (int, float)):
            total_km = self.km + other
        else:
            return NotImplemented
        return Distance(total_km)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero")
            return Distance(round(self.km / other, 2))
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            return NotImplemented
