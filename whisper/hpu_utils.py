import warnings

import habana_frameworks.torch.hpu as hthpu
import torch


def load_default_hpu() -> str:
    """
    Load HPU if available, otherwise use CUDA or CPU.
    """

    if not hthpu.is_available():
        warnings.warn("HPU is not available; trying to use CUDA instead.")
        return "cuda" if torch.cuda.is_available() else "cpu"

    return "hpu"