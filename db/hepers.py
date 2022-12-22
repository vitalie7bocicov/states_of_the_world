def create_response(query_result):
    """
    Create a response string from the given query result.

    :param query_result: The result of a query to a MySQL database.
    :type query_result: list
    :returns: A string representation of the query result.
    :rtype: str
    """
    response = ""
    for result in query_result:
        for index,value in enumerate(result):
            response += f"{value}"
            if index < len(result) - 1:
                response += ","
            else:
                response += "\n"
    return response

def format_query_result(query_result):
    """
    Formats the query result so that countries that have multiple properties,
    appearing on multiple lines, are reduced to a single line with all properties.

    :param query_result: A list of tuples, where each tuple contains a country name
                         and a property.
    :return: A list oftuples, where each tuple contains a country name as the first
             element and a list of its properties.
    :rtype: list[tuple[str, list[str]]]
    """
    result = []
    countries = dict()
    for values in query_result:
        if values[0] not in countries.keys():
            countries[values[0]]=[values[1]]
        else:
            countries[values[0]].append(values[1])

    for country in countries.keys():
        country_list = [country]
        country_list.extend(countries[country])
        result.append(tuple(country_list))
    return result