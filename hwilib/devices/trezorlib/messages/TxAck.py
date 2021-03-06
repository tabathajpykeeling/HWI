# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .TransactionType import TransactionType


class TxAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 22

    def __init__(
        self,
        tx: TransactionType = None,
    ) -> None:
        self.tx = tx

    @classmethod
    def get_fields(cls):
        return {
            1: ('tx', TransactionType, 0),
        }
