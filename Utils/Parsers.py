from __future__ import annotations

from typing     import List, Optional
################################################################################

__all__ = ("Parsers",)

################################################################################
class Parsers:

    @staticmethod
    def convert_db_list(data: Optional[str]) -> List[str]:

        if data is None or not data or data == "{}":
            return []

        base_list = [i for i in data.lstrip("{").rstrip("}").split(",")]

        return [i.strip("'").strip('"') for i in base_list]

################################################################################
    @staticmethod
    def parse_salary(salary: str) -> Optional[int]:

        # Remove commas and whitespace, and make lowercase
        salary = salary.lower().strip().replace(",", "")

        try:
            if salary.endswith("k"):
                return int(salary[:-1]) * 1000
            elif salary.endswith("m"):
                return int(salary[:-1]) * 1000000
            else:
                return int(salary)
        except ValueError:
            return

################################################################################
