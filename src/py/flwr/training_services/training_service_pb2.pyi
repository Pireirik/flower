from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Error(_message.Message):
    __slots__ = ["code", "message"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class InstanceState(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class Scalar(_message.Message):
    __slots__ = ["float", "int", "bool", "str"]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    INT_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_NUMBER: _ClassVar[int]
    STR_FIELD_NUMBER: _ClassVar[int]
    float: float
    int: int
    bool: bool
    str: str
    def __init__(self, float: _Optional[float] = ..., int: _Optional[int] = ..., bool: bool = ..., str: _Optional[str] = ...) -> None: ...

class HubPort(_message.Message):
    __slots__ = ["port"]
    PORT_FIELD_NUMBER: _ClassVar[int]
    port: int
    def __init__(self, port: _Optional[int] = ...) -> None: ...

class TrainingParameters(_message.Message):
    __slots__ = ["names", "strategy", "command"]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    names: UserTrainingNames
    strategy: str
    command: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, names: _Optional[_Union[UserTrainingNames, _Mapping]] = ..., strategy: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ...) -> None: ...

class UserTrainingNames(_message.Message):
    __slots__ = ["username", "training_name"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    TRAINING_NAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    training_name: str
    def __init__(self, username: _Optional[str] = ..., training_name: _Optional[str] = ...) -> None: ...

class FlTrainingName(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ImageTar(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class StrategyParameters(_message.Message):
    __slots__ = ["accept_failure", "fraction_fit", "fraction_evaluate", "server_learning_rate", "server_momentum", "min_completion_rate_fit", "min_completion_rate_evaluate", "eta", "eta_l", "bate_1", "bate_2", "q_param", "qffl_learning_rate", "min_fint_clients", "min_evaluate_clients", "min_available_clients", "tau"]
    ACCEPT_FAILURE_FIELD_NUMBER: _ClassVar[int]
    FRACTION_FIT_FIELD_NUMBER: _ClassVar[int]
    FRACTION_EVALUATE_FIELD_NUMBER: _ClassVar[int]
    SERVER_LEARNING_RATE_FIELD_NUMBER: _ClassVar[int]
    SERVER_MOMENTUM_FIELD_NUMBER: _ClassVar[int]
    MIN_COMPLETION_RATE_FIT_FIELD_NUMBER: _ClassVar[int]
    MIN_COMPLETION_RATE_EVALUATE_FIELD_NUMBER: _ClassVar[int]
    ETA_FIELD_NUMBER: _ClassVar[int]
    ETA_L_FIELD_NUMBER: _ClassVar[int]
    BATE_1_FIELD_NUMBER: _ClassVar[int]
    BATE_2_FIELD_NUMBER: _ClassVar[int]
    Q_PARAM_FIELD_NUMBER: _ClassVar[int]
    QFFL_LEARNING_RATE_FIELD_NUMBER: _ClassVar[int]
    MIN_FINT_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    MIN_EVALUATE_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    MIN_AVAILABLE_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    TAU_FIELD_NUMBER: _ClassVar[int]
    accept_failure: bool
    fraction_fit: float
    fraction_evaluate: float
    server_learning_rate: float
    server_momentum: float
    min_completion_rate_fit: float
    min_completion_rate_evaluate: float
    eta: float
    eta_l: float
    bate_1: float
    bate_2: float
    q_param: float
    qffl_learning_rate: float
    min_fint_clients: int
    min_evaluate_clients: int
    min_available_clients: int
    tau: float
    def __init__(self, accept_failure: bool = ..., fraction_fit: _Optional[float] = ..., fraction_evaluate: _Optional[float] = ..., server_learning_rate: _Optional[float] = ..., server_momentum: _Optional[float] = ..., min_completion_rate_fit: _Optional[float] = ..., min_completion_rate_evaluate: _Optional[float] = ..., eta: _Optional[float] = ..., eta_l: _Optional[float] = ..., bate_1: _Optional[float] = ..., bate_2: _Optional[float] = ..., q_param: _Optional[float] = ..., qffl_learning_rate: _Optional[float] = ..., min_fint_clients: _Optional[int] = ..., min_evaluate_clients: _Optional[int] = ..., min_available_clients: _Optional[int] = ..., tau: _Optional[float] = ...) -> None: ...

class TrainingParameter(_message.Message):
    __slots__ = ["rounds", "strategy", "parameters"]
    ROUNDS_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    rounds: int
    strategy: str
    parameters: StrategyParameters
    def __init__(self, rounds: _Optional[int] = ..., strategy: _Optional[str] = ..., parameters: _Optional[_Union[StrategyParameters, _Mapping]] = ...) -> None: ...

class NewTraining(_message.Message):
    __slots__ = ["training_id", "names", "training_parameters", "training_server", "hub_server"]
    TRAINING_ID_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    TRAINING_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    TRAINING_SERVER_FIELD_NUMBER: _ClassVar[int]
    HUB_SERVER_FIELD_NUMBER: _ClassVar[int]
    training_id: str
    names: UserTrainingNames
    training_parameters: TrainingParameter
    training_server: ServerInfo
    hub_server: ServerInfo
    def __init__(self, training_id: _Optional[str] = ..., names: _Optional[_Union[UserTrainingNames, _Mapping]] = ..., training_parameters: _Optional[_Union[TrainingParameter, _Mapping]] = ..., training_server: _Optional[_Union[ServerInfo, _Mapping]] = ..., hub_server: _Optional[_Union[ServerInfo, _Mapping]] = ...) -> None: ...

class ServerInfo(_message.Message):
    __slots__ = ["port", "ip"]
    PORT_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    port: int
    ip: str
    def __init__(self, port: _Optional[int] = ..., ip: _Optional[str] = ...) -> None: ...

class TrainingID(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ClientSignature(_message.Message):
    __slots__ = ["id", "name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ModelUpdated(_message.Message):
    __slots__ = ["id", "model", "round"]
    ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    ROUND_FIELD_NUMBER: _ClassVar[int]
    id: str
    model: str
    round: int
    def __init__(self, id: _Optional[str] = ..., model: _Optional[str] = ..., round: _Optional[int] = ...) -> None: ...

class AllTrainings(_message.Message):
    __slots__ = ["trainings"]
    TRAININGS_FIELD_NUMBER: _ClassVar[int]
    trainings: _containers.RepeatedCompositeFieldContainer[TrainingResult]
    def __init__(self, trainings: _Optional[_Iterable[_Union[TrainingResult, _Mapping]]] = ...) -> None: ...

class TrainingResult(_message.Message):
    __slots__ = ["training_id", "names", "training_parameters"]
    TRAINING_ID_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    TRAINING_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    training_id: str
    names: UserTrainingNames
    training_parameters: TrainingParameter
    def __init__(self, training_id: _Optional[str] = ..., names: _Optional[_Union[UserTrainingNames, _Mapping]] = ..., training_parameters: _Optional[_Union[TrainingParameter, _Mapping]] = ...) -> None: ...

class Signed(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
