# marenostrum-requirements

A package to install common ML/AI dependencies.

## Installation

### Using pip

Install directly from GitHub:

```bash
pip install git+https://github.com/lightonai/marenostrum-requirements.git
```

### Using uv

Install directly from GitHub:

```bash
uv pip install git+https://github.com/lightonai/marenostrum-requirements.git
```


## Notes
Flash Attention file used:
```
flash_attn-2.6.3+cu128torch2.8-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl
```

```
uv venv .venv
source .venv/bin/activate
uv sync
```

## Included Dependencies

- transformers
- vllm
- flash-attn
- trl
- lm-eval (lm-harness)
- ray

## Usage

```python
import open_requirements

# Check all dependencies
results = open_requirements.check_all()
print(results)

# Check individual packages
print(open_requirements.check_transformers())
print(open_requirements.check_vllm())
print(open_requirements.check_flash_attn())
print(open_requirements.check_trl())
print(open_requirements.check_lm_eval())
print(open_requirements.check_ray())
```

## License

MIT
