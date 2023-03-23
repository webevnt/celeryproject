from enum import IntEnum



class RenewalType(IntEnum):
    """Renewal Type"""
    ONETIME = 0
    MONTHLY = 1
    YEARLY = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class SubscriptionStatus(IntEnum):
    """Subscription Status"""
    IN_ACTIVE = 0
    ACTIVE = 1
    PENDING = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]