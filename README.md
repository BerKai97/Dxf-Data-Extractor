# Dxf Data Extractor 

Dxf Data Extractor for cost est.
Useful for modular drawings like prefabricated buildings.

## --- How to use ---
1. Select the DXF file you want to extract data from.
2. Select CSV file that contains the asset names and prices.

## --- How to use CSV file ---
1. The first row must be the column names.
2. The column names must be "Asset" and "Price".
3. The "Asset" column must contain the asset names. (The names must be the same as the object names in the DXF file)
4. The "Price" column must contain the asset prices.

## --- How to use DXF file ---
1. The DXF file must contain the asset names in the layer names.
2. The asset names must be the same as the names in the CSV file.

## --- OUTPUT ---
- A CSV file that contains the asset names and counts.
- A text file that contains the total cost and asset names that are not found in the prices CSV file.


## --- RoadMap ---

- Export names and counts of the assets for cost est.  (Done)
- Automatically read asset prices from DB or File that needed and calculate est. cost. (Done)
- Custom attributes export support.


## --- Support ---  
For support, message me on [Twitter](https://twitter.com/BerKai97)

