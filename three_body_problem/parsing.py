import pydantic


class Body(pydantic.BaseModel):
    x: float
    y: float
    mass: float
    v_x: float
    v_y: float
    color: str = "white"


class Configuration(pydantic.BaseModel):
    bodies: list[Body]
    delta_t: float
    video_length: int
    output_path: str
    width: int = 600
    height: int = 600


def parse_config(path: str):
    config = Configuration.parse_file(path)
    return config
