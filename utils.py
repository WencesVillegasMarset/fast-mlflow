"""Utils module for MLflow experiment tracking."""
import logging
from functools import wraps
from pathlib import Path
from typing import Dict, Union

import mlflow

logger = logging.getLogger(__name__)

CONFIG = dict(mlflow_active=True)


def if_tracking_is_active(tracking_func):
    """
    Check if MLflow is activated.

    Notes:
        This can be helpful for having seamless code
        that can optionally log to mlflow without having
        to check.
        You are encouraged to adapt the config parameter
        management to what's best suited for your project.
    """

    @wraps(tracking_func)
    def wrapper(*args, **kwargs):
        if CONFIG["mlflow_active"]:
            result = tracking_func(*args, **kwargs)
            return result
        else:
            logger.info("MLflow tracking inactive, skipping.")

    return wrapper


@if_tracking_is_active
def start_tracking(
    tracking_uri: str = None,
    run_name: str = None,
    experiment_name: str = None,
    tags: Dict = None,
) -> mlflow.ActiveRun:
    """Create a run and start tracking context manager.

    Parameters
    ----------
    tracking_uri : str, optional
        tracking server uri, by default None
    run_name : str, optional
        run name, by default None
    experiment_name : str, optional
        experiment name, by default None
    tags : Dict, optional
        tags for the run, by default None

    Returns
    -------
    mlflow.ActiveRun
    """
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(experiment_name)
    return mlflow.start_run(run_name=run_name, tags=tags)


@if_tracking_is_active
def end_tracking():
    """End current Run tracking."""
    mlflow.end_run()


@if_tracking_is_active
def log_artifacts(local_dir: Union[str, Path], **kwargs):
    """Log all artifacts present in directory to current run.

    Parameters
    ----------
    local_dir : Union[str, Path]
        path to log artifacts from.
    """
    logger.info("Logging artifacts from %s", str(local_dir))
    mlflow.log_artifacts(local_dir, **kwargs)
