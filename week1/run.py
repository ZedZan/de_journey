import sys
import os
from config import Config
from pipelines.pipeline_v4 import run_pipeline

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
if __name__ == "__main__":
    run_pipeline(Config())
