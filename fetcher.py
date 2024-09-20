import click
from abc import ABC, abstractmethod
import os

# Step 1: Base Class for Data Sources
class DataSourceBase(ABC):
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    @abstractmethod
    def fetch(self):
        """Fetch the raw data."""
        pass

    @abstractmethod
    def process(self, raw_data):
        """Process the fetched data."""
        pass

    @abstractmethod
    def save(self, processed_data, output_dir):
        """Save the processed data."""
        pass

    def run(self, output_dir):
        """Fetch, process, and save data."""
        print(f"Running fetch/process/save for {self.__class__.__name__} at {self.lat}, {self.long}")
        raw_data = self.fetch()
        processed_data = self.process(raw_data)
        self.save(processed_data, output_dir)

# Step 2: Example Fetcher Implementation (PRISM Stub)
class PrismFetcher(DataSourceBase):
    def fetch(self):
        print(f"Fetching PRISM data for lat: {self.lat}, long: {self.long}")
        return {"raw": "PRISM data"}

    def process(self, raw_data):
        print(f"Processing PRISM data: {raw_data}")
        return {"processed": "Processed PRISM data"}

    def save(self, processed_data, output_dir):
        print(f"Saving PRISM data to {output_dir}")
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, f"prism_data_{self.lat}_{self.long}.txt")
        with open(file_path, 'w') as f:
            f.write(str(processed_data))

# Step 3: Manager for Running Multiple Fetchers
class FetcherManager:
    def __init__(self, lat, long, output_dir):
        self.lat = lat
        self.long = long
        self.output_dir = output_dir
        self.fetchers = [PrismFetcher(lat, long)]  # Add more fetchers as needed

    def run_all(self):
        for fetcher in self.fetchers:
            fetcher.run(self.output_dir)

# Step 4: Click CLI
@click.group()
def cli():
    """CLI for fetching data from various sources."""
    pass

@click.command()
@click.option('--lat', type=float, required=True, help="Latitude of the location.")
@click.option('--long', type=float, required=True, help="Longitude of the location.")
@click.option('--source', type=click.Choice(['prism', 'ssurgo'], case_sensitive=False), help="Data source to fetch from.")
@click.option('--all', is_flag=True, help="Run for all data sources.")
@click.option('--output', type=click.Path(), default='./output', help="Directory to save results.")
def fetch(lat, long, source, all, output):
    """Fetch data for a specific lat/long or all sources."""
    
    if all:
        print("Fetching data from all sources...")
        manager = FetcherManager(lat, long, output)
        manager.run_all()
    elif source == 'prism':
        print("Fetching from PRISM...")
        fetcher = PrismFetcher(lat, long)
        fetcher.run(output)
    else:
        print(f"Fetching from source: {source} is not yet implemented.")
        
cli.add_command(fetch)

if __name__ == '__main__':
    cli()
