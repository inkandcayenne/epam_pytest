# TODO: add documentation
def get_result_by_percentage(corrupted_records_amount: int, overall_records_amount: int, description: str) -> bool:
    # TODO: implement common function for all verifiers functions
    pass


# TODO: add documentation
def verify_completeness(records: list) -> bool:
    records_amount_with_empty_values = 0

    # TODO: implement

    return get_result_by_percentage(records_amount_with_empty_values, len(records), "Percentage of completed records")


# TODO: add documentation
def verify_max_length(records: list, max_length: int):
    records_amount_with_values_more_than_max_length = 0

    # TODO: implement

    return get_result_by_percentage(records_amount_with_values_more_than_max_length, len(records),
                                    f"Percentage of records with length less than {max_length}")


# TODO: add documentation
def verify_allowed_values(records: list, allowed_values: list):
    records_amount_with_not_allowed_values = 0

    # TODO: implement

    return get_result_by_percentage(records_amount_with_not_allowed_values, len(records),
                                    f"Percentage of records with allowed values ({allowed_values})")

# TODO: add at least 5 verifiers
