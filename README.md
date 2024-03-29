# featureguards-python

Official Python SDK for FeatureGuards

## Installation

```sh
python3 -m pip install --upgrade featureguards
```

```python
from featureguards.feature_flags import feature_flags
from os import getenv

fg = feature_flags(api_key=getenv('FEATUREGUARDS_API_KEY'))

# Simple example checking is feature flag FOO is on
print(fg.is_on('FOO'))

# Passing user_id as an attribute.
print(fg.is_on('FOO', {'user_id': 123}))
```

## Documentation

For details on all the functionality in this library, see the [Python
documentation][pyref].

Below are a few simple examples:

### is_on

```python

# Create the featureguards class once.
fg = feature_flags(api_key=getenv('FEATUREGUARDS_API_KEY'))

# Call is_on multiple times.
fg.is_on('FOO')
fg.is_on('BAR')

```

### is_on with attributes

```python
# Create the featureguards class once.
fg = feature_flags(api_key=getenv('FEATUREGUARDS_API_KEY'))

# Call is_on multiple times.
fg.is_on('FOO', {'user_id': 123})
fg.is_on('BAR', {'user_id': 123, 'company_slug': 'acme'})
```

## Examples

See full [examples](examples)

[pyref]: https://pypi.org/project/featureguards/
[issues]: https://github.com/featureguards/featureguards-python/issues/new
[pulls]: https://github.com/featureguards/featureguards-python/pulls
[examples]: https://github.com/featureguards/featureguards-python/blob/main/examples/featureflags.py
[featureguards]: https://featureguards.com
