from three_body_problem.parsing import parse_config
from three_body_problem.physics import Engine
from three_body_problem.visualizer import Visualizer


def main():
    config = parse_config("example.json")
    engine = Engine(config)
    engine.simulate()
    recording = engine.get_dataframe()
    visualizer = Visualizer(config, recording)
    visualizer.play_movie()
    print(config)


main()
