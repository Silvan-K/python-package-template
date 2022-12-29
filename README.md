# Python Package Template
A template repository for python packages. Lowering the barrier to creating properly packaged python libraries including tests and CI.

![CI status](https://github.com/Silvan-K/python-package-template/actions/workflows/ci.yaml/badge.svg)

## Installation

To install this package, please checkout the repository and install via pip:

```
git clone git@github.com:Silvan-K/python-package-template.git
cd python-package-template
pip install .
```

## Tests

To run tests (located in the [tests](https://github.com/Silvan-K/python-package-template/tree/main/tests) directory) please run

```
pytest
```

from within the repository's root directory.

## CI

The tests are configured to run as a [Github Action](https://github.com/features/actions) on every push to the repository, as configured in [ci.yaml](https://github.com/Silvan-K/python-package-template/blob/main/.github/workflows/ci.yaml)
