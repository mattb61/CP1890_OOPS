from dataclasses import dataclass

@dataclass
class Region:
    code: str
    name: str


@dataclass
class RegionsList:
    Region: list

    def add_regions(self, region):
        self.Region.append(region)


@dataclass
class DailySales:
    id: int
    amount: float
    salesDate: str

