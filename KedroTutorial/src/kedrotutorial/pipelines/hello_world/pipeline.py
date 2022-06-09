from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import hello_world


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=hello_world,
                inputs=None,
                outputs="output_msg",
                name="hello_world_node",
            )
        ],
        namespace="hello_world_pipeline",
        inputs=None,
        outputs="output_msg",
    )
