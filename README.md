## Python env

Using **[uv](https://docs.astral.sh/uv/getting-started/installation/)** for portabililty

```sh
uv python install 3.11
uv venv scraperdevenv --python 3.11
source scraperdevenv/bin/activate
uv pip install -r pyproject.toml --all-extras
python --version # confirm a version match
```

## Sample usage

```

uv run fetcher.py fetch --lat 44.0582 --long -121.3153 --all

uv run fetcher.py fetch --lat 44.0582 --long -121.3153 --source prism

# Fetch data for a specific lat/long and process/save it for all sources
uv run fetcher.py fetch --lat 44.0582 --long -121.3153 --all

# Fetch data for a bounding box (all sources)
uv run fetcher.py fetch --bbox 40.0,50.0,-120.0,-110.0 --all

# Specify output directory for saving results
uv run fetcher.py fetch --lat 44.0582 --long -121.3153 --source prism --output /path/to/output/
```

## Data sources

| Data Source                                                                                           | Description                      | Status                          | Additional Info                                     |
| ----------------------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------- | --------------------------------------------------- |
| [SSURGO](https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo) | Soil information from NRCS       | Still figuring out data         | -                                                   |
| [PRISM](https://prism.oregonstate.edu/)                                                               | Climatology data                 | WiP                             | [PRISM R package](https://docs.ropensci.org/prism/) |
| [3D Elevation Program (DEP)](https://www.usgs.gov/3d-elevation-program)                               | Digital elevation models by USGS | -                               | S3 Bucket, named by lat/long of USGS quads          |
| [NASA GLC](https://gpm.nasa.gov/landslides/projects.html#GLC)                                         | Historical landslide data        | -                               | Possibly other sources too                          |
| [USGS Land Use Classification](https://www.mrlc.gov/)                                                 | Land use classification          | Blocker: Need to know which one | Download .zip, unpack, parse                        |
| [NOAA / NWS](https://www.weather.gov/)                                                                | Weather forecasts                | -                               | -                                                   |

### Model 1 Data Dependencies:

- **SSURGO**: Still figuring out data
- **MRLC Land Use Classification**: Blocker, need to know which one
- **PRISM**: Work in Progress ([PRISM R package](https://docs.ropensci.org/prism/))
