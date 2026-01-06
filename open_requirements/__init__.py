"""
Open Requirements - A package to install and verify common ML/AI dependencies.
"""

__version__ = "0.1.0"


def check_transformers():
    """Import transformers and perform a basic check."""
    import transformers

    return f"transformers version: {transformers.__version__}"


def check_vllm():
    """Import vllm and perform a basic check."""
    import vllm

    return f"vllm version: {vllm.__version__}"


def check_trl():
    """Import trl and perform a basic check."""
    import trl

    return f"trl version: {trl.__version__}"


def check_lm_eval():
    """Import lm_eval (lm-harness) and perform a basic check."""
    import lm_eval

    return f"lm-eval version: {lm_eval.__version__}"


def check_ray():
    """Import ray and perform a basic check."""
    import ray

    return f"ray version: {ray.__version__}"


def check_all():
    """Run all checks and return results."""
    checks = [
        ("transformers", check_transformers),
        ("vllm", check_vllm),
        ("trl", check_trl),
        ("lm-eval", check_lm_eval),
        ("ray", check_ray),
    ]

    results = {}
    for name, check_fn in checks:
        try:
            results[name] = {"status": "ok", "message": check_fn()}
        except ImportError as e:
            results[name] = {"status": "error", "message": str(e)}
        except Exception as e:
            results[name] = {"status": "error", "message": str(e)}

    return results
