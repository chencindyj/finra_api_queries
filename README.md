# finra_api_queries

FINRA is the Financial Industry Regulatory Authority, which oversees US brokerages and exchanges such as the NYSE and NASDAQ.  They ensure that brokers and dealers in US stock/debt markets are acting according to the laws and rules defined by the Securities and Exchange Commission (SEC) as well as by FINRA.  Their API contains information about historical market activity, such as fixed income market activity, statistics such as the size of trades that major institutional investors make, and over-the-counter (OTC) trading activity.  This information allows regulators as well as the public to understand market trading behavior.

The finra_api_queries package simplifies the querying of the FINRA Query API including more complex API calls. It also features functions that enable the time series data visualization of fixed income data, summarization of key market breadth data, and keyword filtering for stocks.

## Installation

```bash
$ pip install finra_api_queries
```

## How to Use

```bash
$ from finra_api_queries import finra_api_queries
```

## Usage

1. Obtain an API key and secret on the FINRA API website.
2. Input the key and secret using the retrieve_api_token() function to generate the time-limited access token necessary to retrieve data from the API.
3. Use the various functions to easily extract data sets from the FINRA Query API with a variety of parameters, visualize time series data, as well as filter and aggregate data in pandas data frames and Seaborn plots.
4. Use API to glean time series-related and aggregated insights about fixed income activity and trading block activity.

This package features the following 6 functions:

* retrieve_api_token
* show_filterable_columns
* retrieve_dataset
* filter_by_weekly_stock
* summarize_trading_breadth
* visualize_market_sentiment

#### readthedocs Package Documentation
https://readthedocs.org/projects/finra-api-queries/

#### Test PyPi Link
https://test.pypi.org/project/finra-api-queries/

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`finra_api_queries` was created by Cindy Chen. It is licensed under the terms of the MIT license.

## Credits

`finra_api_queries` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
