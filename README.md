# Gold and US Bond Yield Analysis

**Work in progress** python project analysing the relationship between gold prices and US bond yields (real and nominal)

## Current Analysis

The project currently includes:

- Cleaning of the bond yield and gold datasets
- Linear regression of gold prices against US 10 year bond yields
- Rolling linear regression representing the change in relationship between gold prices and bond yields (nominal and real yields are compared) over time
- Visualisation of these results (All found in /notebooks which contains the exploratory research notebooks)

## Structure

- `data/` — raw and processed datasets
- `notebooks/` — exploratory analysis
- `src/` — data processing script and reusable rolling regression function