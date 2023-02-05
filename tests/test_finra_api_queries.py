import json
import os
import requests
import pandas as pd
import re

my_access_token2 = '*AAJTSQACMDIABHR5cGUAA0pXVAACUzEAAjAx*eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.ZXlKMGVYQWlPaUpLVjFRaUxDSmxibU1pT2lKQk1USTRRMEpETFVoVE1qVTJJaXdpWVd4bklqb2laR2x5SW4wLi4xTk9PLTZEckhzNEljLWg1TDJCLU9nLkNEQWJPY2xQRHJEM1RnRmJjOUUtWjVVQVpieGpuc2QxVFFha3h2WmhlZFcydm5fblFVWmZsMmVLbWdHZVRQeHprVWFYT3hRenY5SE90cEhRTHY2U1FIRDJaME43bGtYMVp5Mm9US1J1eVI3MUdPZ2twZUVDM2xJOElMU2YwM3YxY0tOMHZXVnpsdDN3ei1Ua2lzXzhaNEZYVThzVFlaZEo2OXNpV3lWMDl3TWIyZXRTQndQM2tqVXhWdFNmeThadDl1cUdUY1lZX3F5TUVGdWVISnh2MnVDVXZtX0JOY1U4ckpSLW5ydnZDSFBqa0dyU1BrS0JCVVZ5TVNCUlluX0dWQjdvZFo5ZGRCQWs1NlFZRm9iZUg3WkgwdkVkMlY5bkJKT1dOaTUzWW1WX05hQ045WmtvY2pkU0dmVC1Wc194WHF1UWRkQl8zUk1STllqZ0E3c2l4eHVVUG00YXk3SDNkbndQMUwzTzFUUFV0b1pYZE81Z29FdXY0OGNTeDBYVlZRTTh5VTJoZGhKOG1PS2dYd1Y1ZHFLVkZocGxEUURSM0pzVmNkY05QTldveHk5XzdYeFRCMHd3cndKNzF5MVBjZEc0UmdnT0RnZ2Mzc3JkekUyeGIwOE5fMjhEYXhrQnI5MnVuV2t5b3RLNUxodlpxZzYxQlZDeDk2SmFNcjNuUjNWSW9WdVotY3A1VU9nNzdBS2RkSjZNb0dyOXBDUUt3SDJZR2tZdzJkRUlqZWVpcHpJSmh5MFJDMnRWMHhaU0ltOTV5T29RaUJLSjhJNFZtM2FNRTFQbWRWcTd3ekRSQ29HRkh6US05V2sxS0tRVmdCZ2JZcTg4bFZBOS1QOEJRLVE3am52Vjk4SU8wTzMyZjI0SEh0ajU5MWZtY2FxVTg0TFJxWUZaMHVWNlJ1OHBabm1JZU91TG1lYWE2b2NuSHYwbzU5N0JRTm9KN0g3anJFSF9aSTNLSGhqN3BnODd3eGRJa1FLQUxhU0pWU2o5ZU1LeldqeEpqRk4xeDZZWjBVSzFybG9GeGxQcUVCT0RwNm9hUm9xRlgwVkpMVEpic3FIWFR3d3RmOG0wcEdTRmRMZGxQM0ZVZ2xCNjcwRHl0MzdpbVZzSWZySmdOanpjY0l4RjVRcjBpZGtSQ2N2RDdqY3Npblo5Qkp2dTJCM2R6cGFpU3dJLU1PaGVZMlZKdHhuUkR6dF9KVkhJekVVMk5zcVZoRnQ4S05BTmNTUFJyYkVobGg1Rl9NdEF0TmNKTUFERndjVU9xZU8wOUR3ZmdORV8xVGQ5UDhUS1ZZbjV3MFdVNlE1MFotcS1XaUdqUkhlWVdPeUZjWUliaEpuSFVKZzJpbUxiWVI5NV9SSF83ZUZpRXo2NXNmMXp5UzdOVjNJbUNneVVWY2FGVXNaWkgzczB6bm0yYmd3SlVpekZIQ3d0VmJGczFQUlVhVHRXTnd3UTFIRXowQU1ZTEdoRUZjcTZRSm5PUWxYR3hhR1pxbHpDRVBqM0ZWWEtMazVZUTRNR1JsNmJLX3FoVk1XTFJ3dFVPMDNkWnptc1o3U010VlU0cjYtVDF5UnBRRVBXOEFjQnQtNEJXM2VxcW9pWVhxQ2NTcmJTc0E5MzMzOG42b1p5OXNjNDhWUWVlcHZ4aWVydlR4c183QktpOWVYQ2ptTng0cHNnZ1pIV05td0EtcTlKeXRCeVBhNGxwakFTYVpBWk1zWnBmb256LV9MYUZRalhENDBoazMtNHJ3RDNWaGtrLUYzc0t2X3hZZ01EcGRXNjVEWWxFNXhfN0JXWmJnSy1GOUdrRmxPUE5MclpUaHZ6b2dwV3dUV0dOLWxiYWRfbWZ3dUhGak5zam03bktLSGxXV1Bnek1zREdFaTlSSHBnOThfWHQwUVlHT3FvQU8zMHBQWmlxc1l4Q0FXaDFhS3dZc0t1T1ZTSHRBLUdiVGFzcWEtaEhNOUJtUl9lelQyaDNwOFo0enkxR3hGcjBnQnNRWDdPSmFyOFRIZU9fOWZhN3N2bGx0VjFLMzBBVjhoMk5pNWJSLWZfei1QVi4xTnBHMDQ4OUpGQmt5M1JReGNPdkN3.5dFd117uy2REl-Xo1gBSscA0cLuQDzw1keAPi8aKu-w'

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
        Optional. Filter the data set on one or more values; multiple column filters are possible, and you can also filter on values using
        simple quantifiers like >, <, <=, >=, ==, and !=.
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
    comp_symbol = 0 # make fake value for com_symbol for now

    if (filters != {}):
        for i, j in filters.items():
            # check that the value is only a length of one, because otherwise it is not a comparison filter
            if len(j) == 1:
                for l in j:
                    # check that the single entry includes a comparison
                    try:
                        match = re.search(r'^([>=!<]+)\s(\d+)', l)
                        comp_symbol = match.group(1)
                    except:
                        pass

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

def filter_market_participant(participant_keyword: str,
                            my_access_token: str,
                            rows_returned: int = 2000,
                            filtered_columns = [],
                            filters: dict = {},
                            date_filter = [{}]):

    """
    Filter on the Weekly Summary data set by the market participant using a fuzzy keyword match.

    PARAMETERS
    ----------
    participant_keyword: str
        A keyword of the market participant that informs the filtering of the marketParticipantName column.
    
    my_access_token: str
        Access token generated from retrieve_api_token() function

    rows_returned: int
        Rows returned by the query. Defaults to 2000 rows, though you should be cognizant of your API data quota.

    filtered_columns: list
        Optional. List of the specific columns to return in the data frame.
        Run show_filterable_columns() based on the dataset name to see eligible columns for filtering.
    
    filters: dictionary
        Optional. Filter the data set on one or more values; multiple column filters are possible, and you can also filter on values using
        simple quantifiers like >, <, <=, >=, ==, and !=.
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
    >>> participant_keyword ='goldman'
    >>> my_access_token = '12345abcd'
    >>> output_1 = finra_api_queries.filter_market_participant(participant_keyword = participant_keyword, my_access_token = my_access_token)

    >>> ouptut_1.head(n = 3)
            totalWeeklyShareQuantity  issueSymbolIdentifier  lastUpdateDate      marketParticipantName
    1141    462977                    BBBY                   2018-06-11          GOLDMAN SACHS & CO. LLC
    1527    37848                     BBBY                   2018-05-25          GOLDMAN SACHS & CO. LLC
    """

    # check input
    assert len(participant_keyword) > 0, "You must input a participant_keyword to use this function"
    
    # alter the stock keyword to lower case
    participant_keyword = participant_keyword.upper()

    # retrieve data
    weekly_test = retrieve_dataset(dataset_name = 'weekly_summary',
                                   my_access_token = my_access_token,
                                   rows_returned = rows_returned,
                                   filters = filters,
                                   filtered_columns = filtered_columns,
                                   date_filter = date_filter)

    # create a subset where the market participant column is not null
    non_null_df = weekly_test[(weekly_test['marketParticipantName'].isnull() == False)]

    # check for keyword in both columns
    final_df = non_null_df[non_null_df['marketParticipantName'].str.upper().str.contains(participant_keyword)]

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
        Optional. Filter the data set on one or more values; multiple column filters are possible, and you can also filter on values using
        simple quantifiers like >, <, <=, >=, ==, and !=.
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

def generate_market_participant_summary(my_access_token: str,
                                        rows_returned: int = 2000,
                                        filtered_columns = [],
                                        filters: dict = {},
                                        date_filter = [{}],
                                        column_to_sort = 'avg_weeklyShares'):
    
    """
    Summarize market participant activity in the Weekly Summary dataset aggregated by average and total trade and share counts.
    It also provides information on the percentage (%) share of the market participants' activity compared to all participants in the defined
    filters.  This output is then sorted according to criteria laid out in the input variable 'column_to_sort'.

    PARAMETERS
    ----------
    my_access_token: str
        Access token generated from retrieve_api_token() function

    rows_returned: int
        Rows returned by the query. Defaults to 2000 rows, though you should be cognizant of your API data quota.

    filtered_columns: list
        Optional. List of the specific columns to return in the data frame.
        Run show_filterable_columns() based on the dataset name to see eligible columns for filtering.
    
    filters: dictionary
        Optional. Filter the data set on one or more values; multiple column filters are possible, and you can also filter on values using
        simple quantifiers like >, <, <=, >=, ==, and !=.
        The input is different from the API based on field name as the key and the list of filtered values as the dictionary values.
        Filter values must be an exact match since the filter is applied to the API query and is not filter that's applied subsequent the API call.

    date_filter: dictionary within a list
        Optional argument if dates should be filtered by a certain date range for a date-related column.  Input follows the API input convention.
        Follows the convention [{'startDate': 'YYYY-MM-DD', 'endDate': 'YYYY-MM-DD', 'fieldName': 'DATECOLUMN'}]

    column_to_sort: str
        Optional argument based on the column or the list of columns to sequentially sort the output table. Defaults to avg_weeklyShares.
        The eight (8) options are 'avg_weeklyShares', 'sum_weeklyShares', 'avg_weeklyTradeCount', 'sum_weeklyTradeCount', 'percent_avg_shares',
        'percent_total_shares', 'percent_avg_trades', and 'percent_total_trades'

    RETURNS
    -------
    pandas.DataFrame
        Data frame

    EXAMPLES
    --------
    >>> my_access_token = '12345abcd'
    >>> column_to_sort_input = ['avg_weeklyShares', 'sum_weeklyShares']
    >>> output_1 = finra_api_queries.generate_market_participant_summary(my_access_token = my_access_token,
                                                                         column_to_sort = column_to_sort_input)

    >>> output_1.head(n = 4)
        marketParticipantName                avg_weeklyShares    sum_weeklyShares    avg_weeklyTradeCount    sum_weeklyTradeCount   
    1   JANE STREET EXECUTION SERVICES, LLC  67820273            67820273            1043                    1043
    2   De Minimis Firms                     1246017             124601714           1829                    182989
    3   CITADEL SECURITIES LLC               979667              44085032            441                     199862

    >>>  output_1.head(n = 4) ..cont
        percent_avg_shares      percent_total_shares        percent_avg_trades      percent_total_trades
    1   88.71                   17.66                       2.72                    0.10
    2   1.63                    32.45                       4.76                    17.48
    3   1.28                    11.48                       11.56                   19.09
    """

    # check that the column_to_sort input contains valid entries
    sorting_options = ['avg_weeklyShares', 'sum_weeklyShares',
                        'avg_weeklyTradeCount', 'sum_weeklyTradeCount',
                        'percent_avg_shares', 'percent_total_shares',
                        'percent_avg_trades','percent_total_trades']

    if isinstance(column_to_sort, list) == False:
        assert column_to_sort in sorting_options, "Please check the column_to_sort input as it must match at least one of the eight valid columns"
    else:
        for i in column_to_sort:
            assert i in sorting_options, "Please check the column_to_sort input as it must match at least one of the eight valid columns"

    # retrieve data
    weekly_test = retrieve_dataset(dataset_name = 'weekly_summary',
                                   my_access_token = my_access_token,
                                   rows_returned = rows_returned,
                                   filters = filters,
                                   filtered_columns = filtered_columns,
                                   date_filter = date_filter)

    # group the information by market participant and create the four desired metrics
    grouped_weekly = weekly_test.groupby('marketParticipantName').agg({'totalWeeklyShareQuantity':['mean', 'sum'], 'totalWeeklyTradeCount': ['mean', 'sum']}).reset_index()

    # rename columns so there aren't two 
    grouped_weekly.columns = ['marketParticipantName', 'avg_weeklyShares', 'sum_weeklyShares', 'avg_weeklyTradeCount', 'sum_weeklyTradeCount']
    
    # convert all column values into integers
    grouped_weekly[['avg_weeklyShares', 'avg_weeklyTradeCount']] = grouped_weekly[['avg_weeklyShares', 'avg_weeklyTradeCount']].astype(int)

    # create new columns
    grouped_weekly['percent_avg_shares'] = round(grouped_weekly['avg_weeklyShares'] / grouped_weekly['avg_weeklyShares'].sum() * 100, 2)
    grouped_weekly['percent_total_shares'] = round(grouped_weekly['sum_weeklyShares'] / grouped_weekly['sum_weeklyShares'].sum() * 100, 2)
    grouped_weekly['percent_avg_trades'] = round(grouped_weekly['avg_weeklyTradeCount'] / grouped_weekly['avg_weeklyTradeCount'].sum() * 100, 2)
    grouped_weekly['percent_total_trades'] = round(grouped_weekly['sum_weeklyTradeCount'] / grouped_weekly['sum_weeklyTradeCount'].sum() * 100, 2)

    # sort the resulting data frame
    final_df = grouped_weekly.sort_values(column_to_sort, ascending = False).reset_index()

    # drop the excess index column
    final_df.drop('index', axis = 1, inplace = True)

    assert len(final_df) > 0, "The keyword search did not yield any results."

    return final_df
    
# def test_retrieve_api_token():
#     assert len(retrieve_api_token(finra_api_key, finra_api_secret)) > 1, "retrieve_api_token() function doesn't work correctly"

def test_show_filterable_columns():
    assert len(show_filterable_columns('finra_registered_firms', my_access_token = my_access_token2)) > 1, "show_filterable_columns() function doesn't work correctly"

def test_retrieve_dataset():
    assert len(retrieve_dataset('fixed_income_corpdebt_marketsentiment', my_access_token = my_access_token2, rows_returned = 5)) > 0, "retrieve_dataset() function doesn't work correctly"

def test_filter_market_participant():
    assert len(filter_market_participant('a', my_access_token = my_access_token2)) > 0, "filter_by_weekly_stock() function doesn't work"

def test_summarize_trading_breadth():
    assert len(summarize_trading_breadth('fixed_income_rule144a_marketbreadth', my_access_token = my_access_token2, rows_returned = 5)) > 0, "summarize_trading_breadth() function doesn't work"

def test_visualize_market_sentiment():
    assert len(visualize_market_sentiment('fixed_income_corpdebt_marketsentiment', my_access_token = my_access_token2, rows_returned = 50, x_axis = 'tradeType')) > 0, "visualize_market_sentiment() function doesn't work"

def test_generate_market_participant_summary():
    assert len(generate_market_participant_summary(my_access_token = my_access_token2)) > 0, "generate_market_participant_summary doesn't work"