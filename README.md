# `nbdev` Template @tongyx361


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Adaptation Checklist

- [ ] [`nbs/index.ipynb`](nbs/index.ipynb)
- [ ] [`settings.ini`](settings.ini)
- [ ] [`environment.yml`](environment.yml)
- [ ] [`pkg_name` directory](pkg_name)
- [ ] Run `bash utils/prepare-commit.sh`

## Setup

We recommend:

- using [Conda](https://docs.conda.io/projects/miniconda) to set up the
  **basic Python environment** and install some **non-Python packages**
  like `git-lfs` when **without the root permission**;
- using [`pip`](https://pip.pypa.io/en/stable/#) to manage the **Python
  packages** because some packages are **only available via `pip`**.

Run the following commands to setup the **basic environment** and
**install most dependencies**:

``` shell
git clone https://github.com/tongyx361/nbdev-template-tongyx361.git
cd nbdev-template-tongyx361
conda env create -f environment.yml
conda activate myenv
pip install -r requirements.txt
```

For common users/developers, please just run the following command the
install the `pkg_name` package:

``` shell
pip install -e "."
```

For intended contributors, we recommend installing the package with the
`dev` extras and setting up the pre-commit hooks by running:

``` shell
pip install -e ".[dev]"
pre-commit install
conda install quarto # For nbdev
```

## Contribution Guidelines

### File Structure

    nbdev_template_tongyx361
    ├── data
    ├── utils # Repository utilities
    ├── pkg_name # Package code for common utilities
    ├── nbs # Notebooks and other files to run tests and generate documentation with https://nbdev.fast.ai
    ├── cfgs # Configurations
    ├── [pipelines] # Reusable (Python / Shell) scripts or notebooks
    └── [scripts] # One-time scripts

### Checklist Before Commit

Run the [`prepare-commit.sh`](utils/prepare-commit.sh) to clean the
notebooks and export scripts for pipeline notebooks, generate
documentation, run tests, render README if needed:

    bash utils/prepare-commit.sh
