# open-requirements

A package to install common ML/AI dependencies.

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/lighton/open-requirements.git
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
