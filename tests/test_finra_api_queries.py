import json
import os
import requests
import pandas as pd
import re

my_access_token2 = '*AAJTSQACMDIABHR5cGUAA0pXVAACUzEAAjAx*eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.ZXlKMGVYQWlPaUpLVjFRaUxDSmxibU1pT2lKQk1USTRRMEpETFVoVE1qVTJJaXdpWVd4bklqb2laR2x5SW4wLi5TTjBJd3E5bG1yU1lXeGNESmdiTE9BLkNsbFZVdzJBZ1Y5TzR5LUtaeGdEYzE1UU9ZQVJ1OHpCTGJvWVFCQUY3bXZRTW5JVG5hVmktRE91c1RiVldSeHFrUkEzM3R6c25mSGpqU0tCTmF5UVRuUkFON3VfNmFXdjFKOUE3VGUwWWxYWWd4T0pxdTEybWVtYU9td1p5ZTJxb3VkTEtWNU5FSzJrZFllR1p4LVdYN3QwVmx2X1hfSll6YTVzb0ZoX1ZFcW5HYWdRMGxJVUs4RHJpY2s1anNDbzBVY2p0dThJLUE1UzMtaEttLWZNZU1lQzB6SkRMMmFiUFNSVHBoVjZnekMwVEtKdjJXUktDQXM0VWoxSVEwalZCY0dqal9nM1BvY3B1TDhMbVdrendRUmtJYVBCazdyYzdNX2R3UWpoVHpiMXRWbUFtMDFzUnFRaWkzTGdFbHZCeGUxYV9abGI1UHdaRjVmTFNnb1gyc3lXUVB6dW9UeFkwZFFONjQyN2w2WFhYcmNQbVlnZm0tS1RtSjAyOV9CT1RvRXMybGlQSDN5LU84UGVNVEhDQm43LTZ3S0cwNWctcFI3X1RXdnRLVi1lRkpUV0JoNEdiVG43aFRHVXNjMWZ6WUwzTktSRVIzaWJEX1pQdHlaQ0xHMXZsZU1hNWpITG80UnhjWWZvWUFzZDgzc2UzWXJLSF8zeUVyLTF4bE1JQjVYcG5Nc0NwUUlZUGhfeGVlWUJvSlBQUHdJa0xnSjh2ZmZoa0k3dkpaQV9SdVFTaDZIZi1ZcFlSM2dkTDR1RWR1S2hxYUZMN2dTbGJQc3BRYXFhMDl4V1B3S0U1QWR6RmxkNjFlcTVCYW14ZngwdDN3a0FEdGRHRDdYWlh6eG1xdVhBc0ItRWlFZWlvWGg5YmZsX3hxcGxDM0pzS1kxUTN1aVJzVWdHRXhKM0YwVDYyUlpES2tubHRpcHdHWXM5Q3BxNHBYZkRsZTNjQ05VN1Y3dUwzZlVwR2lwaTVZclB6VlRGRF9UVFNnYlBtVGdfWVlCQ3JiZHNXQmdoX3ZCVVpfX25zNVkzc2U4cWhDSW9MVzlYdl9vVkk2SmUxanBaWHhHb1ZFdE15VTRMZHB6MUNhM09UcHNpdG8tVjFpRUl1N04yRkprUjJRV19pTjRhcDRseno0bzVwQXNlaVk0bk0yY3BseEIzM1dkSVNBRDE1SC15M1hkWjhvc0ZHVkhEQ3NaT04wUVNVX3pqQjE1WV9rbmtYeVFaX0l6RGFieFFxclozaV9GYXNzZThhUDZJUFFtVXNYdk5EY1lYNnp5dUpEMU5UcmZLTmw3c0t2NFlJY25hT01YVzNrTk5TVDlsd3JDODN5N0c3RXBBdjBzZTRiYVBhUElyUUtpTkZMbkFmT085dnV6RDU0VVFXTjEtYUhJaS1DbzhYQXVXZGgxdGViSXpObDBhRDJSSzVJeE84NkpVSTAyVmpiSm5yaHRGOHNqRWFYUzVqXzUwMjNKYjBVeTZIelJmYnJPV1Y3X05zdWNLNVVzWXhpWml0YzlPYkNEb2ZrUkNWN0pqT29mLVBicU9uclJtUTR1ZVkzNXN4M0RmOW1vY0ZFVGZJVTNFREp1djlYSEhjZzJESTM0QzRVMkVWeFRXMTNaNmNDdnFXX0FvVER2MEczN19BZXo1azNNRGdQa3IwMmZtZ0NqeHFESV80aFRRdkVIalJiTFk2STBYRnRDNWY2dXVzbGU5QmNNU25lYmNzZnlYcW40STZBbmlfLUxYZ0NsLXJoX1RDMjdyM2hMN3FnMVhKRTBLdFhvb1R3X1NiOWt4aU1SSDhGRDVCRFlDSW0ybUdrRXR1TnV0bURyRU85UndYbGRIQ0Y0MzFZS1Uyd2hjaEJoUzlPbFREaXJTT2tkRTBha0h6N0ExUWFaMVhnbFFPYUZ4WE5jMVFtaDNLbUFwdFMwQkg1VnlSZi1sMklra2tkV0lVcmlNeVJEV28tNVdnVUk2YXcxeXRJNlBzelFGUUV0TUFwRjdnNXNGMEp5RTlpY3BvVDJxVFlGNzUxdWV0aXBneG5xNEp0Z3V5VFNocWR4TC5EQkhIdUNYVFJlTjhwYk92ckFwWmV3.lLzJzggzI6VIeaKgeo1yFh01eTyBa_Jd6jLsvcBeUfk'

def retrieve_api_token(finra_api_key_input: str = "",
                        finra_api_secret_input: str = ""):
                
    """
    Load credentials to access FINRA API token.

    Parameters
    ----------
    finra_api_key_input: str
        API Key supplied by FINRA API.
        Create an account using: https://developer.finra.org/docs#getting_started-the_api_console
    
    finra_api_secret_input: str
        API Secret supplied by FINRA API.
        Generate the secret/password using: https://developer.finra.org/docs#getting_started-the_api_console

    Returns
    -------
    FINRA-API generated access token: str

    Example
    -------
    >>> finra_api_key = 'abcdj3478wh'
    >>> finra_api_secret = "th1s1smyp@ss"
    >>> retrieve_api_token(finra_api_key_input = finra_api_key, finra_api_secret_input = finra_api_secret)
    '*AAHDFKNBSDIGJ324u328947u32hnfkjhfiwhfe28r93u12io4j31lkj4kl123129msi327833'
    """

    try:
        load_dotenv()
        finra_api_key = os.getenv('FINRA_API_CLIENT')
        finra_api_secret = os.getenv('SECRET')
    
    except:
        finra_api_key = finra_api_key_input
        finra_api_secret = finra_api_secret_input
        
    my_token = requests.post('https://ews.fip.finra.org/fip/rest/ews/oauth2/access_token?grant_type=client_credentials',
                            auth = (finra_api_key, finra_api_secret))

    assert my_token.status_code == 200, "Access Token could not be generated"

    global my_access_token
    my_access_token = my_token.json()['access_token']

    return my_access_token

def show_filterable_columns(dataset_name: str,
                            my_access_token: str):
    
    """
    Retrieves the column names in the FINRA data set.  This helps identify columns for filtering using the retrieve_database() function.

    Parameters
    ----------
    dataset_name: str
        Choose a dataset name from the following list (official FINRA API Dataset name in parentheses):
        - blocks_summary (Blocks Summary)
        - otc_equity_shorts (Equity Short Interest)
        - otc_blocks_summary (OTC Block Summary)
        - regsho_ddaily_shorts_volume (Reg SHO Daily Short Sale VOlume)
        - threshold_list (Threshold List)
        - weekly_summary (Weekly Summary)
        - fixed_income_agencydebt_marketbreadth (Agency Debt Market Breadth)
        - fixed_income_agencydebt_marketsentiment (Agency Debt Market Sentiment)
        - fixed_income_rule144a_marketbreadth (Corporate 144A Debt Market Breadth)
        - fixed_income_rule144a_marketsentiment (Corporate 144A Debt Market Sentiment)
        - fixed_income_corp_agency_capped_volume (Corporate and Agency Capped Volume)
        - fixed_income_corpdebt_marketbreadth (Corporate Debt Market Breadth)
        - fixed_income_corpdebt_marketsentiment (Corporate Debt Market Sentiment)
        - fixed_income_securitized_capped_volume (Securitized Product Capped Volume)
        - fixed_income_treasury_weekly_agg (Treasury Weekly Aggregates)

    my_access_token: str
        Access token generated using the retrieve_api_token() function.

    Returns
    ------
    list
        List of columns that user can filter using the retrieve_dataset() function.

    Example
    -------
    >>> from finra_api_queries import show_filterable_columns
    >>> dataset_name = "threshold_list"
    >>> my_access_token = "ABCD1234"
    >>> ouput_1 = finra_api_queries.show_filterable_columns(dataset_name = dataset_name, my_access_token = my_access_token)

    >>> output_1.head(3)
    ['tradeDate', 'issueSymbolIdentifier', 'issueName', 'marketClassCode', 'thresholdListFlag', 'marketCategoryDescription', 'regShoThresholdFlag', 'rule4320Flag']

    """
    # define dictionaries to ensure that inputs are valid
    eligible_groups = {'blocks_summary': 'otcMarket',
                        'otc_equity_shorts': 'otcMarket',
                        'otc_blocks_summary': 'otcMarket',
                        'regsho_daily_shorts_volume': 'otcMarket',
                        'threshold_list': 'otcMarket',
                        'weekly_summary': 'otcMarket',
                        'finra_registered_firms': 'finra',
                        'fixed_income_agencydebt_marketbreadth': 'fixedIncomeMarket',
                        'fixed_income_agencydebt_marketsentiment': 'fixedIncomeMarket',
                        'fixed_income_rule144a_marketbreadth': 'fixedIncomeMarket',
                        'fixed_income_rule144a_marketsentiment': 'fixedIncomeMarket',
                        'fixed_income_corp_agency_capped_volume': 'fixedIncomeMarket',
                        'fixed_income_corpdebt_marketbreadth': 'fixedIncomeMarket',
                        'fixed_income_corpdebt_marketsentiment': 'fixedIncomeMarket',
                        'fixed_income_securitized_capped_volume': 'fixedIncomeMarket',
                        'fixed_income_treasury_weekly_agg': 'fixedIncomeMarket'
                        }

    eligible_datasets = {'blocks_summary': 'blocksSummary',
                        'otc_equity_shorts': 'equityShortInterestStandardized',
                        'otc_blocks_summary': 'otcBlocksSummary',
                        'regsho_daily_shorts_volume': 'regShoDaily',
                        'threshold_list': 'thresholdList',
                        'weekly_summary': 'weeklySummary',
                        'finra_registered_firms': 'industrySnapshotFirmsByRegistrationType',
                        'fixed_income_agencydebt_marketbreadth': 'agencyMarketBreadth',
                        'fixed_income_agencydebt_marketsentiment': 'agencyMarketSentiment',
                        'fixed_income_rule144a_marketbreadth': 'corporate144AMarketBreadth',
                        'fixed_income_rule144a_marketsentiment': 'corporate144AMarketSentiment',
                        'fixed_income_corp_agency_capped_volume': 'corporatesAndAgenciesCappedVolume',
                        'fixed_income_corpdebt_marketbreadth': 'corporateMarketBreadth',
                        'fixed_income_corpdebt_marketsentiment': 'corporateMarketSentiment',
                        'fixed_income_securitized_capped_volume': 'securitizedProductsCappedVolume',
                        'fixed_income_treasury_weekly_agg': 'treasuryWeeklyAggregates'
                        }

    ## CHECKS                    
    # check that the access token is valid
    assert len(my_access_token) > 1, "You must have a valid access token to retrieve data from the API. Run retrieve_api_token() before running this command."

    # check that the inputs are correct
    assert dataset_name in eligible_datasets.keys(), "Please check the name of the dataset"

    # MAKE API CALL
    response = requests.get(f'https://api.finra.org/metadata/group/{eligible_groups[dataset_name]}/name/{eligible_datasets[dataset_name]}')

    assert response.status_code == 200, "Invalid request"

    # convert to data frame
    columns_to_print = json.loads(response.content)

    column_list = []

    # print out list of column names
    for i in range(len(columns_to_print['fields'])):
        column_list.append(columns_to_print['fields'][i]['name'])
    
    return(column_list)

def retrieve_dataset(dataset_name: str,
                    my_access_token: str,
                    rows_returned: int = 2000,
                    filtered_columns: list = [],
                    filters: dict = {},
                    date_filter = [{}]):
    
    """
    Simplifies the retrieval of publicly-accessible data sets from the FINRA API, allowing optional column subsetting, filtering, and date filtering.
    Does not further transform the data sets from the API output.

    Parameters
    ----------
    dataset_name: str
        Choose a dataset name from the following list (official FINRA API Dataset name in parentheses):
        - blocks_summary (Blocks Summary)
        - otc_equity_shorts (Equity Short Interest)
        - otc_blocks_summary (OTC Block Summary)
        - regsho_daily_shorts_volume (Reg SHO Daily Short Sale Volume)
        - threshold_list (Threshold List)
        - weekly_summary (Weekly Summary)
        - finra_registered_firms (Firm Registration Types)
        - fixed_income_agencydebt_marketbreadth (Agency Debt Market Breadth)
        - fixed_income_agencydebt_marketsentiment (Agency Debt Market Sentiment)
        - fixed_income_rule144a_marketbreadth (Corporate 144A Debt Market Breadth)
        - fixed_income_rule144a_marketsentiment (Corporate 144A Debt Market Sentiment)
        - fixed_income_corp_agency_capped_volume (Corporate and Agency Capped Volume)
        - fixed_income_corpdebt_marketbreadth (Corporate Debt Market Breadth)
        - fixed_income_corpdebt_marketsentiment (Corporate Debt Market Sentiment)
        - fixed_income_securitized_capped_volume (Securitized Product Capped Volume)
        - fixed_income_treasury_weekly_agg (Treasury Weekly Aggregates)

    my_access_token: str
        Access token previously generated

    rows_returned: int
        Rows returned by the query. Defaults to 2000 rows, though you should be cognizant of your API data quota.

    filtered_columns: list
        Optional. List of the specific columns to return in the data frame.
        Run show_filterable_columns() based on the dataset name to see eligible columns for filtering.
    
    filters: dictionary
        Optional. Filter the data set on one or more values; multiple column filters are possible.
        The input is different from the API based on field name as the key and a __list__ of filtered values as the dictionary values.
        Filter values must be an exact match since the filter is applied to the API query and is not filter that's applied subsequent the API call.

    date_filter: dictionary within a list
        Optional argument if dates should be filtered by a certain date range for a date-related column.  Input follows the API input convention.
        Follows the convention [{'startDate': 'YYYY-MM-DD', 'endDate': 'YYYY-MM-DD', 'fieldName': 'DATECOLUMN'}]

    Returns
    -------
    pandas.DataFrame

    Examples
    --------
    >>> from finra_api_queries import finra_api_queries
    >>> dataset_name = "otc_blocks_summary"
    >>> my_access_token = "ABCDFGH545645645645648797212630"
    >>> rows_returned = 200
    >>> filtered_columns_input = ['lastUpdateDate', 'averageTradeSize', 'crdFirmName']
    >>> filters_input = filters= {'crdFirmName': ['CITADEL SECURITIES LLC', 'SIDOTI & COMPANY, LLC'],
                                  'averageTradeSize': ['>= 20'],
                                  'averageTradeSizeRank': ['!= 100']}
    >>> date_filter_inputs = [{'startDate': '2020-04-01', 'endDate': '2021-03-01', 'fieldName': 'lastUpdateDate'}]
    >>> output_1 = finra_api_queries.retrieve_dataset(dataset_name, my_access_token, rows_returned,
                                            filtered_columns = filtered_columns_input,
                                            filters = filters_input,
                                            date_filter = date_filter_inputs) 
    
    >>> output_1.head(n = 3)
        crdFirmName             lastUpdateDate  averageTradeSize
    0   CITADEL SECURITIES LLC  2020-04-06      281
    1   SIDOTI & COMPANY, LLC   2020-04-06      28892
    2   CITADEL SECURITIES LLC  2020-04-06      281
    """

    # set up dictionaries of the groups and datasets in the FINRA API to call the correct API URL

    eligible_groups = {'blocks_summary': 'otcMarket',
                        'otc_equity_shorts': 'otcMarket',
                        'otc_blocks_summary': 'otcMarket',
                        'regsho_daily_shorts_volume': 'otcMarket',
                        'threshold_list': 'otcMarket',
                        'weekly_summary': 'otcMarket',
                        'finra_registered_firms': 'finra',
                        'fixed_income_agencydebt_marketbreadth': 'fixedIncomeMarket',
                        'fixed_income_agencydebt_marketsentiment': 'fixedIncomeMarket',
                        'fixed_income_rule144a_marketbreadth': 'fixedIncomeMarket',
                        'fixed_income_rule144a_marketsentiment': 'fixedIncomeMarket',
                        'fixed_income_corp_agency_capped_volume': 'fixedIncomeMarket',
                        'fixed_income_corpdebt_marketbreadth': 'fixedIncomeMarket',
                        'fixed_income_corpdebt_marketsentiment': 'fixedIncomeMarket',
                        'fixed_income_securitized_capped_volume': 'fixedIncomeMarket',
                        'fixed_income_treasury_weekly_agg': 'fixedIncomeMarket'
                        }

    eligible_datasets = {'blocks_summary': 'blocksSummary',
                        'otc_equity_shorts': 'equityShortInterestStandardized',
                        'otc_blocks_summary': 'otcBlocksSummary',
                        'regsho_daily_shorts_volume': 'regShoDaily',
                        'threshold_list': 'thresholdList',
                        'weekly_summary': 'weeklySummary',
                        'finra_registered_firms': 'industrySnapshotFirmsByRegistrationType',
                        'fixed_income_agencydebt_marketbreadth': 'agencyMarketBreadth',
                        'fixed_income_agencydebt_marketsentiment': 'agencyMarketSentiment',
                        'fixed_income_rule144a_marketbreadth': 'corporate144AMarketBreadth',
                        'fixed_income_rule144a_marketsentiment': 'corporate144AMarketSentiment',
                        'fixed_income_corp_agency_capped_volume': 'corporatesAndAgenciesCappedVolume',
                        'fixed_income_corpdebt_marketbreadth': 'corporateMarketBreadth',
                        'fixed_income_corpdebt_marketsentiment': 'corporateMarketSentiment',
                        'fixed_income_securitized_capped_volume': 'securitizedProductsCappedVolume',
                        'fixed_income_treasury_weekly_agg': 'treasuryWeeklyAggregates'
                        }

    qualifiers = {'>=': 'GTE',
                  '<=': 'LTE',
                  '==': 'EQUALS',
                  '=': 'EQUALS',
                  '!=': 'NOT_EQUAL',
                  '<>': 'NOT_EQUAL',
                  '<': 'LESSER',
                  '>': 'GREATER'}

    ## CHECKS                    
    # check that the access token is valid
    assert len(my_access_token) > 1, "You must have a valid access token to retrieve data from the API. Run retrieve_api_token() before running this command."
    
    # check that the inputs are correct
    assert dataset_name in eligible_datasets.keys(), "Please check the name of the dataset"

    # convert the filters input into the appropriate format for the API
    filters_list = [] # for exact matches
    comp_filters_list = [] # for comp values

    # if filters != {}:
    #     for i, j in filters.items():
    #         filters_list.append({'fieldName': i, 'values': j})

    if (filters != {}):
        for i, j in filters.items():
            # check that the value is only a length of one, because otherwise it is not a comparison filter
            if len(j) == 1:
                for l in j:
                    match = re.search(r'^([>=!<]+)\s(\d+)', l)
                    comp_symbol = match.group(1)
                if comp_symbol in qualifiers:
                    comp_filters_list.append({'fieldName': i,
                                            'fieldValue': match.group(2),
                                            'compareType': qualifiers[comp_symbol]})
                else:
                    filters_list.append({'fieldName': i, 'values': j}) # add entry to the filters_list
            else:
                filters_list.append({'fieldName': i, 'values': j}) # add entry to the filters_list

    # make the API call
    # if optional argument for columns has been entered
    if ((filtered_columns == []) & (filters == {}) & (date_filter == [{}])):
        # if no filters are deployed
        response = requests.post(f'https://api.finra.org/data/group/{eligible_groups[dataset_name]}/name/{eligible_datasets[dataset_name]}',
                            headers = {'Authorization': 'Bearer ' + my_access_token,
                                       'Accept': 'application/json'},
                            json = {'limit': rows_returned})
    
    elif ((filtered_columns != []) & (filters != {}) & (date_filter != [{}])):
        # if all filters are deployed

        # check if there are comp_filters
        if comp_filters_list == []:
            response = requests.post(f'https://api.finra.org/data/group/{eligible_groups[dataset_name]}/name/{eligible_datasets[dataset_name]}?limit={rows_returned}',
                                headers = {'Authorization': 'Bearer ' + my_access_token,
                                           'Accept': 'application/json'},
                                json = {'fields': filtered_columns,
                                        'limit': rows_returned,
                                          'domainFilters': filters_list,
                                          'dateRangeFilters': date_filter})
        
        else:
            response = requests.post(f'https://api.finra.org/data/group/{eligible_groups[dataset_name]}/name/{eligible_datasets[dataset_name]}?limit={rows_returned}',
                                headers = {'Authorization': 'Bearer ' + my_access_token,
                                           'Accept': 'application/json'},
                                json = {'fields': filtered_columns,
                                        'compareFilters': comp_filters_list,
                                        'limit': rows_returned,
                                          'domainFilters': filters_list,
                                          'dateRangeFilters': date_filter})

    elif ((filtered_columns != []) & (filters == {}) & (date_filter == [{}])):
        # if only column filter is dpeloyed
        response = requests.post(f'https://api.finra.org/data/group/{eligible_groups[dataset_name]}/name/{eligible_datasets[dataset_name]}?limit={rows_returned}',
                            headers = {'Authorization': 'Bearer ' + my_access_token,
                                       'Accept': 'application/json'},
                            json = {'fields': filtered_columns,
                                    'limit': rows_returned,})

    elif ((filtered_columns == []) & (filters != {}) & (date_filter == [{}])):
        # if only values filter is deployed

        # check if comp_filters exist
        if comp_filters_list == []:
            response = requests.post(f'https://api.finra.org/data/group/{eligible_groups[dataset_name]}/name/{eligible_datasets[dataset_name]}?limit={rows_returned}',
                                headers = {'Authorization': 'Bearer ' + my_access_token,
                                           'Accept': 'application/json'},
                                json = {'domainFilters': filters_list,
                                        'limit': rows_returned})
        else:
            response = requests.post(f'https://api.finra.org/data/group/{eligible_groups[dataset_name]}/name/{eligible_datasets[dataset_name]}?limit={rows_returned}',
                                headers = {'Authorization': 'Bearer ' + my_access_token,
                                           'Accept': 'application/json'},
                                json = {'domainFilters': filters_list,
                                        'compareFilters': comp_filters_list,
                                        'limit': rows_returned})

    elif ((filtered_columns == []) & (filters == {}) & (date_filter != [{}])):
        # if only the date filter is deployed
        response = requests.post(f'https://api.finra.org/data/group/{eligible_groups[dataset_name]}/name/{eligible_datasets[dataset_name]}?limit={rows_returned}',
                            headers = {'Authorization': 'Bearer ' + my_access_token,
                                       'Accept': 'application/json'},
                            json = {'dateRangeFilters': date_filter,
                                    'limit': rows_returned})
    
    elif ((filtered_columns != []) & (filters != {}) & (date_filter == [{}])):
        # if only the column and values filters are deployed

        # check if comp_filters are deployed
        if comp_filters_list == []:
            response = requests.post(f'https://api.finra.org/data/group/{eligible_groups[dataset_name]}/name/{eligible_datasets[dataset_name]}?limit={rows_returned}',
                                headers = {'Authorization': 'Bearer ' + my_access_token,
                                           'Accept': 'application/json'},
                                json = {'fields': filtered_columns,
                                          'domainFilters': filters_list,
                                          'limit': rows_returned})
        else:
            response = requests.post(f'https://api.finra.org/data/group/{eligible_groups[dataset_name]}/name/{eligible_datasets[dataset_name]}?limit={rows_returned}',
                                headers = {'Authorization': 'Bearer ' + my_access_token,
                                           'Accept': 'application/json'},
                                json = {'fields': filtered_columns,
                                        'compareFilters': comp_filters_list,
                                          'domainFilters': filters_list,
                                          'limit': rows_returned})

    elif ((filtered_columns != []) & (filters == {}) & (date_filter != [{}])):
        # if only the column and date filters are deployed

        response = requests.post(f'https://api.finra.org/data/group/{eligible_groups[dataset_name]}/name/{eligible_datasets[dataset_name]}?limit={rows_returned}',
                                headers = {'Authorization': 'Bearer ' + my_access_token,
                                           'Accept': 'application/json'},
                                json = {'fields': filtered_columns,
                                          'dateRangeFilters': date_filter,
                                          'limit': rows_returned})

    else:
        # if only the values and date filters are deployed

        # check if comp_filters exist
        if comp_filters_list == []:
            response = requests.post(f'https://api.finra.org/data/group/{eligible_groups[dataset_name]}/name/{eligible_datasets[dataset_name]}?limit={rows_returned}',
                                headers = {'Authorization': 'Bearer ' + my_access_token,
                                           'Accept': 'application/json'},
                                json = {'domainFilters': filters_list,
                                          'dateRangeFilters': date_filter,
                                          'limit': rows_returned})
        else:
            response = requests.post(f'https://api.finra.org/data/group/{eligible_groups[dataset_name]}/name/{eligible_datasets[dataset_name]}?limit={rows_returned}',
                                headers = {'Authorization': 'Bearer ' + my_access_token,
                                           'Accept': 'application/json'},
                                json = {'fields': filtered_columns,
                                        'compareFilters': comp_filters_list,
                                          'dateRangeFilters': date_filter,
                                          'limit': rows_returned})


    # convert to data frame
    response_df = pd.DataFrame(response.json())
    
    return(response_df)

def filter_by_weekly_stock(stock_keyword: str,
                            my_access_token: str,
                            rows_returned: int = 2000,
                            filtered_columns = [],
                            filters: dict = {},
                            date_filter = [{}]):

    """
    Filter on the Weekly Summary data set by the stock ticker (like AAPL) or the full company name (Apple) using a fuzzy keyword match.

    PARAMETERS
    ----------
    stock_keyword: str
        A stock keyword such as the ticker name or a partial string of the company that informs the filtering of the issueSymbolIdentifier and issuerName columns.
    
    my_access_token: str
        Access token generated from retrieve_api_token() function

    rows_returned: int
        Rows returned by the query. Defaults to 2000 rows, though you should be cognizant of your API data quota.

    filtered_columns: list
        Optional. List of the specific columns to return in the data frame.
        Run show_filterable_columns() based on the dataset name to see eligible columns for filtering.
    
    filters: dictionary
        Optional. Filter the data set on one or more values; multiple column filters are possible.
        The input is different from the API based on field name as the key and the list of filtered values as the dictionary values.
        Filter values must be an exact match since the filter is applied to the API query and is not filter that's applied subsequent the API call.

    date_filter: dictionary within a list
        Optional argument if dates should be filtered by a certain date range for a date-related column.  Input follows the API input convention.
        Follows the convention [{'startDate': 'YYYY-MM-DD', 'endDate': 'YYYY-MM-DD', 'fieldName': 'DATECOLUMN'}]


    RETURNS
    -------
    pandas.DataFrame
        Data frame

    EXAMPLES
    --------
    >>> stock_keyword ='bed'
    >>> my_access_token = '12345abcd'
    >>> output_1 = finra_api_queries.filter_by_weekly_stock(stock_keyword = stock_keyword, my_access_token = my_access_token)

    >>> ouptut_1.head(n = 3)
            totalWeeklyShareQuantity    issueSymbolIdentifier   issueName                           lastUpdateDate      lastReportDate
    1141    45050                       BBBY                    Bed Bath & Beyond Inc. Common Stock 2018-06-11          2018-05-21
    1527    2199366                     BBBY                    Bed Bath & Beyond Inc. Common Stock 2018-06-11          2018-05-25
    """

    # check input
    assert len(stock_keyword) > 0, "You must input a stock_keyword to use this function"
    
    # alter the stock keyword to lower case
    stock_keyword = stock_keyword.lower()

    # retrieve data
    weekly_test = retrieve_dataset(dataset_name = 'weekly_summary', my_access_token = my_access_token, rows_returned = rows_returned, filters = filters, filtered_columns = filtered_columns, date_filter = date_filter)

    # create a subset where the two keyword columns are not null
    non_null_df = weekly_test[(weekly_test['issueName'].isnull() == False) & (weekly_test['issueSymbolIdentifier'].isnull() == False)]

    # check for keyword in both columns
    final_df = non_null_df[(non_null_df['issueSymbolIdentifier'].str.lower().str.contains(stock_keyword)) | (non_null_df['issueName'].str.lower().str.contains(stock_keyword))]

    assert len(final_df) > 0, "The keyword search did not yield any results."

    return final_df


def summarize_trading_breadth(dataset_name: str,
                              my_access_token: str,
                              rows_returned: int = 2000,
                              date_filter = [{}]
                              ):
    """
    Summarize fixed income trading information (volume per trade, totals, proportions) by product category.

    Parameters
    ----------
    dataset_name: str
        Data set name for summarizing market breadth. Must be one of three datasets
        fixed_income_agencydebt_marketbreadth (Agency Debt Market Breadth)
        fixed_income_rule144a_marketbreadth (Corporate 144A Debt Market Breadth)
        fixed_income_corpdebt_marketbreadth (Corporate Debt Market Breadth)

    my_access_token: str
        Access token generated from retrieve_api_token() function

    rows_returned: int
        Rows returned by the query. Defaults to 2000 rows, though you should be cognizant of your API data quota.

    date_filter: dictionary within a list
        Optional argument if dates should be filtered by a certain date range for a date-related column.  Input follows the API input convention.
        Follows the convention [{'startDate': 'YYYY-MM-DD', 'endDate': 'YYYY-MM-DD', 'fieldName': 'DATECOLUMN'}]

    Returns
    -------
    pandas.DataFrame
        Output sorted by volume per trade in descending order.
        Shows lowest fiftyTwoWeekLow and highest fiftyTwoWeekHigh within the time frame selected
        Shows the total for all other metrics and includes a calculated field of volume per trade

    Examples
    --------
    >>> dataset_name = 'fixed_income_corpdebt_marketbreadth'
    >>> my_access_token = "abc123"
    >>> date_filter_inputs = [{'startDate': '2022-02-25', 'endDate': '2022-03-01', 'fieldName': 'tradeReportDate'}]
    >>> output_1 = finra_api_queries.summarize_trading_breadth(dataset_name = dataset_name, my_access_token = my_access_token, date_filter = date_filter_inputs)

    >>> output_1.head(n=2)
            productCategory fiftyTwoWeekLow fiftyTwoWeekHigh    declines    advances    unchanged   totalVolume totalTrades Volume_per_Trade
        0   convertibles     12             11                  246         395         11          3717.737109 675         5.507759
        1   investment grade 342            67                  4776        15490       64          75319.218227 20850      3.612433
        dtype: pd.DataFrame

    """

    eligible_dataset = ['fixed_income_agencydebt_marketbreadth',
                        'fixed_income_rule144a_marketbreadth',
                        'fixed_income_corpdebt_marketbreadth']
    
    # check that dataset_name matches the three possible market breadth data sets
    assert dataset_name in eligible_dataset, "Please check the data set name input."

    # retrieve data
    orig_df = retrieve_dataset(dataset_name, my_access_token, rows_returned = rows_returned, date_filter = date_filter)
    orig_df = orig_df.drop('tradeReportDate', axis = 1) # drop this column

    # aggregate the data first
    new_df = orig_df.groupby('productCategory').agg({'fiftyTwoWeekLow': 'min',
                                                    'fiftyTwoWeekHigh': 'max',
                                                    'declines': 'sum',
                                                    'advances': 'sum',
                                                    'unchanged': 'sum',
                                                    'totalVolume': 'sum',
                                                    'totalTrades': 'sum'}).reset_index()

    new_df['Volume_per_Trade'] = new_df['totalVolume'] / new_df['totalTrades'] # create new calculated field
    new_df = new_df.sort_values(by = 'Volume_per_Trade', ascending = False).reset_index() # sort data frame
    new_df = new_df.drop('index', axis = 1) # drop extra index column

    return new_df

import seaborn as sns
import matplotlib.pyplot as plt 

def visualize_market_sentiment(dataset_name: str,
                                my_access_token: str,
                                x_axis: str,
                                grouping: str = '',
                                aggregate_method: str = 'sum',
                                rows_returned: int = 2000,
                                filters: dict = {},
                                date_filter=[{}]
                                 ):

    """
    Visualiize a Fixed Income-related market sentiment data set and returns a complementary table with aggregated data that was used in the visualization.

    PARAMETERS
    ----------
    dataset_name: str
        Data set name to generate visualization.  Can only choose between 3 data sets:
        fixed_income_agencydebt_marketsentiment (Agency Debt Market Sentiment)
        fixed_income_rule144a_marketsentiment (Corporate 144A Debt Market Sentiment)
        fixed_income_corpdebt_marketsentiment (Corporate Debt Market Sentiment)

    my_access_token: str
        API access token that was generated using retrieve_api_token()

    x_axis: str
        The column to use as an x-axis. If tradeReportDate is selected, the charts will be a line chart. Otherwise, it will be a bar chart. The three options are:
        tradeReportDate
        tradeType
        productCategory
    
    grouping: str
        Optional argument. Groups the lines or bars by one of two possible values.  If no grouping is selected, it will aggregate the data. The two options are:
        - productCategory
        - tradeType

    aggregate_method: str
        Optional argument. Defaults to sum.  Choose how data should be aggregated in the table by the x-axis variable and if applicable, the grouping variable based on the following options:
        sum
        mean
        count
        max
        min

    rows_returned: int
        Optional.  Number of rows to query from FINRA Query API. Defaults to 2000 rows.
    
    filters: dictionary
        Optional. Filter the data set on one or more values; multiple columns are possible.
        The input is different from the API based on field name as the key and the list of filtered values as the dictionary values.

    date_filter: dictionary within a list
        Optional argument if dates should be filtered by a certain date range for a date-related column.  Input follows the API input convention.
        Follows the convention [{'startDate': 'YYYY-MM-DD', 'endDate': 'YYYY-MM-DD', 'fieldName': 'DATECOLUMN'}]

    RETURNS
    -------
    pandas.DataFrame
        Returns a pandas data frame of the aggregated data that is used to generate the three Seaborn plots 
   
    seaborn.lineplot
    seaborn.barplot
        Returns three Seaborn-based plots.  The type of plot generated depends on the inputs.
    
    EXAMPLE
    -------
    >>> dataset_name = 'fixed_income_corpdebt_marketsentiment'
    >>> my_access_token = 'abcd1234'
    >>> x_axis = 'tradeReportDate'
    >>> grouping = 'productCategory'
    >>> aggregate_method = 'sum'
    >>> date_filter=[{'startDate': '2020-07-01', 'endDate': '2020-07-10', 'fieldName': 'tradeReportDate'}]
    >>> output_1 = finra_api_queries.visualize_market_sentiment(dataset_name = dataset_name,
                                my_access_token = my_access_token,
                                x_axis = x_axis,
                                grouping = grouping,
                                date_filter = date_filter)
    
    >>> output_1.head(n = 3)
        tradeReportDate productCategory totalVolume totalTransactions
    0   2020-07-01      affiliate buy   2163.19306  3228
    1   2020-07-01      affiliate sell  2283.10436  3452
    2   2020-07-01      all securities  51687.17489 113670

    [an image with three plots appears below]
    """

    # dictionaries to check inputs
    eligible_list = ['fixed_income_agencydebt_marketsentiment',
                     'fixed_income_rule144a_marketsentiment',
                     'fixed_income_corpdebt_marketsentiment']

    eligible_x_axes = ['tradeReportDate', 'tradeType', 'productCategory']

    eligible_groupings = ['productCategory', 'tradeType', '']

    eligible_aggregation_method = {'mean': 'Avg ',
                                    'sum': 'Total ',
                                    'max': 'Max ',
                                    'min': 'Min',
                                    'count': 'Count of '}

    # run checks on function inputs
    assert dataset_name in eligible_list, "Please check the name of the data set as only three data sets are eligible for this visualization."
    assert x_axis in eligible_x_axes, "Please check the x_axis variable selected. Must match one of three possible inputs"
    assert aggregate_method in eligible_aggregation_method.keys(), "Please check the aggregate method. Must match one of the five possible inputs."

    if ((x_axis == 'tradeReportDate') and (grouping == '')):
        raise Exception('grouping input cannot be blank if the x-axis is equal to tradeReportDate')

    assert grouping in eligible_groupings, 'Please check the grouping variable selected. Must match one of two inputs.'

    # retrieve data using the retrieve_dataset() function
    orig_df = retrieve_dataset(dataset_name, my_access_token, rows_returned = rows_returned, filters = filters, date_filter = date_filter)

    # generate plot
    fig, axs = plt.subplots(ncols=3, figsize = (12, 4))
    
    if (x_axis == 'tradeReportDate'):

        # group variables based on criteria
        orig_df = pd.DataFrame(orig_df.groupby([x_axis, grouping]).agg(aggregate_method)).reset_index()

        # create chart
        sns.lineplot(data = orig_df, x = x_axis, y = "totalVolume", hue = grouping, ax=axs[0]).set(ylabel=None, title = (eligible_aggregation_method[aggregate_method] + 'Volume'))
        sns.lineplot(data = orig_df, x = x_axis, y = "totalTransactions", hue = grouping,  ax=axs[1]).set(ylabel=None, title = (eligible_aggregation_method[aggregate_method] + 'Txns'))
        sns.lineplot(data = orig_df, x = x_axis, y = "totalTrades", hue = grouping,  ax=axs[2]).set(ylabel=None, title = (eligible_aggregation_method[aggregate_method] + 'Trades'))
        axs[0].tick_params(axis = "x", rotation = 45, labelsize = 8)
        axs[1].tick_params(axis = "x", rotation = 45, labelsize = 8)
        axs[2].tick_params(axis = "x", rotation = 45, labelsize = 8)

        axs[0].get_legend().remove()
        axs[1].get_legend().remove()
        axs[2].legend(bbox_to_anchor =(-0.8,-0.6), loc = "lower center", borderaxespad = 0, fontsize = 6)

    elif ((x_axis != 'tradeReportDate') & (grouping == '')):
        orig_df = pd.DataFrame(orig_df[[x_axis, 'totalTransactions', 'totalVolume', 'totalTrades']].groupby(x_axis).agg(aggregate_method)).reset_index()
            
        sns.barplot(data = orig_df, x = x_axis, y = "totalVolume", ax=axs[0]).set(ylabel=None, title = (eligible_aggregation_method[aggregate_method] + 'Volume'))
        sns.barplot(data = orig_df, x = x_axis, y = "totalTransactions", ax=axs[1]).set(ylabel=None, title = (eligible_aggregation_method[aggregate_method] + 'Total Txns'))
        sns.barplot(data = orig_df, x = x_axis, y = "totalTrades",  ax=axs[2]).set(ylabel=None, title = (eligible_aggregation_method[aggregate_method] + 'Trades'))
        axs[0].tick_params(axis = "x", labelsize = 8)
        axs[1].tick_params(axis = "x", labelsize = 8)
        axs[2].tick_params(axis = "x", labelsize = 8)
    
    else:
        orig_df = pd.DataFrame(orig_df.groupby([x_axis, grouping]).agg(aggregate_method)).reset_index()
            
        sns.barplot(data = orig_df,x = x_axis, y = "totalVolume", hue = grouping, ax = axs[0]).set(ylabel=None, title = (eligible_aggregation_method[aggregate_method] + 'Volume'))
        sns.barplot(data = orig_df, x = x_axis, y = "totalTransactions", hue = grouping, ax=axs[1]).set(ylabel=None, title = (eligible_aggregation_method[aggregate_method] + 'Total Txns'))
        sns.barplot(data = orig_df, x = x_axis, y = "totalTrades",  hue = grouping, ax=axs[2]).set(ylabel=None, title = (eligible_aggregation_method[aggregate_method] + 'Trades'))
        axs[0].tick_params(axis = "x", labelsize = 8)
        axs[1].tick_params(axis = "x", labelsize = 8)
        axs[2].tick_params(axis = "x", labelsize = 8)

        axs[0].get_legend().remove()
        axs[1].get_legend().remove()
        axs[2].legend(bbox_to_anchor =(-0.8,-0.6), loc = "lower center", borderaxespad = 0, fontsize = 6)

    # apply certain plot changes that are agnostic of plot type
    axs[0].tick_params(axis = "y", labelsize = 8)
    axs[1].tick_params(axis = "y", labelsize = 8)
    axs[2].tick_params(axis = "y", labelsize = 8)
    
    return orig_df, fig

def test_retrieve_api_token():
    assert len(retrieve_api_token(finra_api_key, finra_api_secret)) > 1, "retrieve_api_token() function doesn't work correctly"

def test_show_filterable_columns():
    assert len(show_filterable_columns('finra_registered_firms', my_access_token = my_access_token2)) > 1, "show_filterable_columns() function doesn't work correctly"

def test_retrieve_dataset():
    assert len(retrieve_dataset('fixed_income_corpdebt_marketsentiment', my_access_token = my_access_token2, rows_returned = 5)) > 0, "retrieve_dataset() function doesn't work correctly"

def test_filter_by_weekly_stock():
    assert len(filter_by_weekly_stock('a', my_access_token = my_access_token2)) > 0, "filter_by_weekly_stock() function doesn't work"

def test_summarize_trading_breadth():
    assert len(summarize_trading_breadth('fixed_income_rule144a_marketbreadth', my_access_token = my_access_token2, rows_returned = 5)) > 0, "summarize_trading_breadth() function doesn't work"

def test_visualize_market_sentiment():
    assert len(visualize_market_sentiment('fixed_income_corpdebt_marketsentiment', my_access_token = my_access_token2, rows_returned = 50, x_axis = 'tradeType')) > 0, "visualize_market_sentiment() function doesn't work"