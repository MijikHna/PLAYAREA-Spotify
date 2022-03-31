from typing import Dict


class UrlQueryParams:
    def __init__(self, query_params: Dict) -> None:
        if type(query_params) is not dict:
            raise TypeError(
                f'query_params must be Dict ,recieved: {query_params}'
            )

        self._query_params = query_params

    def to_query_str(self):
        query: str = ''

        for i, (key, value) in enumerate(self._query_params.items()):
            query += f'{key}={value}'

            if i < (len(self._query_params) - 1):
                query += '&'

        return query
