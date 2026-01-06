# marenostrum-requirements

A package to install common ML/AI dependencies.

## Installation

### Using pip

Install directly from GitHub:

```bash
pip install git+https://github.com/lightonai/marenostrum-requirements.git
```

Install a specific branch:

```bash
pip install git+https://github.com/lightonai/marenostrum-requirements.git@main
```

Install a specific tag/version:

```bash
pip install git+https://github.com/lightonai/marenostrum-requirements.git@v0.1.0
```

### Using uv

Install directly from GitHub:

```bash
uv pip install git+https://github.com/lightonai/marenostrum-requirements.git
```

Install a specific branch:

```bash
uv pip install git+https://github.com/lightonai/marenostrum-requirements.git@main
```

Install a specific tag/version:

```bash
uv pip install git+https://github.com/lightonai/marenostrum-requirements.git@v0.1.0
```

Add to a uv project:

```bash
uv add git+https://github.com/lightonai/marenostrum-requirements.git
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
