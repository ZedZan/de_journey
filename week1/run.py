import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import Config
from pipelines.pipeline_v4 import run_pipeline

if __name__ == "__main__":
    run_pipeline(Config())